const assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
process.chdir(__dirname);
const M=require('./models.js');const ctx=vm.createContext({Models:M,document:{getElementById:()=>({})},console});
vm.runInContext(fs.readFileSync('extra.js','utf8'),ctx);
vm.runInContext(fs.readFileSync('app.js','utf8').split("$('tools').innerHTML=")[0],ctx);
const run=x=>vm.runInContext(x,ctx),near=(a,b,t=1e-8)=>assert.ok(Math.abs(a-b)<t,`${a} != ${b}`);
near(run('potential({temperature:25,ia:1,ib:1,ca:.2,cb:.4,pa:0,pb:0}).a'),-.49576382);
assert.equal(run('revcomp("ATGC")'),'GCAT');assert.equal(run('translate("AUGGCUUUUGAAUGA").protein'),'MAFE');assert.equal(run('translate("UGA").protein'),'');
assert.deepEqual(JSON.parse(run('JSON.stringify(digest("AAAAGAATTCTTT","EcoRI",false).sizes)')),[5,8]);
for(const circle of [true,false])assert.equal(run(`digest("ATGGAATTCCCGGATCCAAAGAATTCTTT","EcoRI",${circle}).sizes.reduce((a,b)=>a+b,0)`),29);
near(run('pcr(1,1,10)'),1024);near(run('alleleSelection(.5,1,1,1).p'),.5);near(run('chiSquare([90,30,30,10],[9,3,3,1]).value'),0);
const params='{substrate:10,enzyme:1,kcat:100,ph:7,optimum:7,temperature:25,inhibitor:2,km:2,ki:2,inhibition:"none"}';
let base=run(`enzymeRate(${params})`),competitive=run(`enzymeRate({...${params},inhibition:'competitive'})`);assert.ok(competitive<base);
near(run(`enzymeRate({...${params},inhibition:'competitive'},1e9)`),run(`enzymeRate({...${params},inhibition:'none'},1e9)`),1e-5);
const keys=run('Object.keys(tools)');fs.mkdirSync('qa-figures',{recursive:true});
let count=0;for(const key of keys){let out;try{out=run(`current=${JSON.stringify(key)};data=[];validate();renderers[current](states[current])`);}catch(e){throw Error(key+': '+e.message)}assert.ok(out.figure.includes('<svg'));assert.ok(!out.figure.includes('NaN')&&!out.figure.includes('undefined'),key);fs.writeFileSync(`qa-figures/${key}.svg`,out.figure);count++;}
// Every select option and each tool's declared numeric minimum/maximum must produce a result or a clear validation error, never a code error.
let scenarios=0,expectedErrors=0;for(const key of keys){const fields=run(`tools[${JSON.stringify(key)}].fields`);for(const f of fields){const values=f.type==='select'?f.options.map(x=>x[0]):f.type==='number'?[f.min,f.max]:[];for(const value of values){try{run(`current=${JSON.stringify(key)};states[current]=initial(current);states[current][${JSON.stringify(f.key)}]=${JSON.stringify(value)};data=[];validate();renderers[current](states[current])`);}catch(e){if(e.name==='ReferenceError'||e.name==='TypeError'||e.name==='SyntaxError')throw Error(`${key}/${f.key}/${value}: ${e.message}`);expectedErrors++;}scenarios++;}}}
for(const key of keys){run(`current=${JSON.stringify(key)};states[current]=initial(current);states[current].mono=true;states[current].answers=false;data=[]`);let out=run('renderers[current](states[current])');fs.writeFileSync(`qa-figures/${key}-mono.svg`,out.figure);}
const catalog=run('Object.entries(tools).map(([id,t])=>({id,unit:t.unit,title:t.title,topics:t.topics,assumptions:t.assumptions,fields:t.fields.map(f=>({key:f.key,label:f.label,type:f.type}))}))');fs.writeFileSync('model-catalog.json',JSON.stringify(catalog,null,2));
console.log(`PASS: ${count} default model renderers, ${count} grayscale/result-hidden variants, ${scenarios} parameter scenarios (${expectedErrors} expected constraint errors), and quantitative invariants.`);
