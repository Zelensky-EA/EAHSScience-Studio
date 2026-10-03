const assert=require('node:assert/strict'),M=require('./models.js');
function near(a,b,t=1e-9){assert.ok(Math.abs(a-b)<t,`${a} != ${b}`)}
let p=M.punnett({cross:'complete',parent1:'AaBb',parent2:'AaBb'});assert.deepEqual(p.phenotypes.map(x=>x[1]).sort((a,b)=>a-b),[1/16,3/16,3/16,9/16]);near(p.genotypes.reduce((a,x)=>a+x[1],0),1);
p=M.punnett({cross:'incomplete',parent1:'Aa',parent2:'Aa'});near(p.phenotypes.find(x=>x[0]==='Intermediate heterozygote')[1],.5);
p=M.punnett({cross:'x',parent1:'Aa',parent2:'aY'});near(p.phenotypes.find(x=>x[0]==='Affected male')[1],.25);near(p.phenotypes.find(x=>x[0]==='Affected female')[1],.25);
assert.throws(()=>M.punnett({cross:'complete',parent1:'AB',parent2:'aa'}));
let g=M.growth({model:'exponential',n0:100,r:Math.log(2),time:1});near(g.at(-1)[1],200);
g=M.growth({model:'logistic',n0:500,r:.3,k:1000,time:1});near(g[0][2],75);g=M.growth({model:'logistic',n0:1200,r:.3,k:1000,time:20});assert.ok(g[0][2]<0);assert.ok(g.at(-1)[1]>1000&&g.at(-1)[1]<1200);
let s={model:'classic',alpha:.6,beta:.02,gamma:.4,delta:.01,prey0:40,pred0:30,time:45};let pr=M.prey(s);pr.forEach(r=>{near(r[1],40,1e-6);near(r[2],30,1e-6)});
s.pred0=9;pr=M.prey(s);const invariant=r=>s.delta*r[1]-s.gamma*Math.log(r[1])+s.beta*r[2]-s.alpha*Math.log(r[2]);near(invariant(pr[0]),invariant(pr.at(-1)),1e-7);let finer=M.prey(s,24000);near(pr.at(-1)[1],finer.at(-1)[1],1e-5);near(pr.at(-1)[2],finer.at(-1)[2],1e-5);
// AR unaffected parents with an affected child force Aa × Aa; unaffected sibling has 2/3 carrier risk.
let status=['unaffected','unaffected','unaffected','affected',...Array(6).fill('unknown')];let ped=M.pedigree('AR',status);assert.deepEqual(ped.possible[0],['Aa']);near(ped.probabilities[2].Aa,2/3);assert.equal(M.pedigree('AD',status).count,0);
status=Array(10).fill('unknown');status[0]='unaffected';status[2]='affected';assert.equal(M.pedigree('XLR',status).count,0);
status=Array(10).fill('unknown');status[0]='affected';status[2]='unaffected';assert.equal(M.pedigree('XLD',status).count,0);
status=Array(10).fill('unknown');status[2]='affected';assert.equal(M.pedigree('Y',status).count,0);
for(const mode of M.modes)for(let i=0;i<10;i++)assert.ok(M.pedigree(mode,M.randomPedigree(mode)).count>0);
assert.equal(M.pipette({instrument:'P20',volume:12.5}).digits,'125');assert.equal(M.pipette({instrument:'P200',volume:125}).digits,'125');assert.equal(M.pipette({instrument:'P1000',volume:1000}).digits,'100');assert.throws(()=>M.pipette({instrument:'P200',volume:12.5}));
let stats=M.measurement('10, 10, 10',12.5);near(stats.sd,0);near(stats.bias,-20);
near(M.ph({method:'direct',ph:7,reference:8}).ratio,10);near(M.ph({method:'strong',conc:.1,reference:7}).ph,1,1e-9);near(M.ph({method:'weak',conc:.1,ka:1.8e-5,reference:7}).ph,2.875,1e-3);near(M.ph({method:'strong',conc:1e-10,reference:7}).ph,7,1e-3);near(M.ph({method:'buffer',pka:4.76,base:.1,acid:.1,reference:7}).ph,4.76);
assert.ok(M.migration(100,75)>M.migration(10000,75));assert.throws(()=>M.fragments({ladder:'0',lanes:'Test: 1000'}));
console.log('PASS: genetic probabilities, full-family pedigree constraints, conditional carrier risk, population solutions, RK4 equilibrium/invariant/convergence, pipette limits, statistics, pH equilibria and gel size direction.');
