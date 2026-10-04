from pathlib import Path
import json,shutil,subprocess,re
root=Path(__file__).parent
source=root/'source'
meta=json.loads(subprocess.check_output(['node','-e',"const M=require("+json.dumps(str((source/'models.js').resolve()))+");console.log(JSON.stringify(Object.fromEntries(Object.entries(M.courses).map(([id,c])=>[id,{...c,activities:M.forCourse(id).map(a=>({id:a.id,title:a.title,unit:a.unit,description:a.description,equation:a.equation,limits:a.limits,goal:a.goal,fields:a.fields}))}]))))"],text=True))
site=root/'site';site.mkdir(exist_ok=True)
assets=['models.js','render.js','app.js','styles.css']
def page(code,unit=0,teacher=False,offline=False):
 cfg={'course':code,'unit':unit,'teacher':teacher}
 title=meta[code]['title']
 css='<style>'+ (source/'styles.css').read_text()+'</style>' if offline else '<link rel="stylesheet" href="styles.css?v=campus-1">'
 scripts=''.join('<script>'+ (source/js).read_text()+'</script>' if offline else f'<script src="{js}?v=campus-1"></script>' for js in assets if js.endswith('.js'))
 return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="EAHS '+title+' interactive models and student investigations."><title>'+title+' · EAHS Learning Portal</title>'+css+'</head><body><a class="skip" href="#site">Skip to workspace</a><div id="site"></div><script>window.PORTAL='+json.dumps(cfg)+';window.OFFLINE='+str(offline).lower()+';</script>'+scripts+'</body></html>'
for code,c in meta.items():
 d=site/code;d.mkdir(exist_ok=True)
 for asset in assets:shutil.copyfile(source/asset,d/asset)
 (d/'index.html').write_text(page(code));(d/'teacher.html').write_text(page(code,teacher=True))
 for unit in range(1,len(c['units'])+1):
  (d/f'unit-{unit}.html').write_text(page(code,unit))
  (d/f'teacher-unit-{unit}.html').write_text(page(code,unit,True))
 (d/'model-catalog.json').write_text(json.dumps(c,indent=2))
 (d/('EAHS-'+code+'-Portal.html')).write_text(page(code,offline=True))
# Retain the existing biology portal as a fifth course.
bio=Path('eahs-science-learning')
if not bio.exists():bio=root.parent/'ap-biology'
if bio.exists():
 dest=site/'ap-biology';dest.mkdir(exist_ok=True)
 for p in bio.iterdir():
  if p.is_file() and p.suffix in ['.html','.js','.css','.json']:shutil.copyfile(p,dest/p.name)
css=(source/'styles.css').read_text()
(site/'campus.css').write_text(css)
cards=''
entries=[('ap-biology','AP Biology','82 investigations · 8 units','Cells, energetics, heredity, evolution & ecology'),*[(code,c['title'],str(len(c['activities']))+' investigations · '+str(len(c['units']))+' units',('Body systems, structures, regulation & integrated physiology' if code=='anatomy-physiology' else 'Particle models, reactions, energetics & equilibrium' if code=='ap-chemistry' else 'Limits, derivatives, integrals & mathematical reasoning' if code=='ap-calculus-ab' else 'The AB collection plus BC methods, parametric & polar curves, and series')) for code,c in meta.items()]]
for code,title,count,desc in entries:cards+=f'<a class="unit-card" href="{code}/index.html"><span class="eyebrow">{count}</span><h2>{title}</h2><p style="font-size:16px">{desc}</p><strong>Open learning portal →</strong></a>'
(site/'index.html').write_text('''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>EAHS Science + Math Learning Campus</title><link rel="stylesheet" href="campus.css?v=campus-1"></head><body><header><a class="brand" href="index.html"><span class="mark">EA</span><span>EAHS <b>SCIENCE + MATH</b><small>STUDENT LEARNING CAMPUS</small></span></a><span class="micro">Everett Alvarez High School</span></header><main class="landing"><p class="eyebrow">FIVE COURSES · ONE PLACE TO INVESTIGATE</p><h1>Make a prediction.<br><span>Find the evidence.</span></h1><p class="lead">Choose a course, explore a unit, and build understanding through interactive models. Predict, manipulate, record observations and explain your reasoning.</p><div class="unit-grid">'''+cards+'''</div><div class="workflow"><div><strong>Predict</strong><p>Estimate before you reveal the model.</p></div><div><strong>Investigate</strong><p>Change conditions and collect evidence.</p></div><div><strong>Explain</strong><p>Connect observations to a mechanism or mathematical argument.</p></div><div><strong>Review</strong><p>Use feedback and download your learning journal.</p></div></div><div class="landing-notes"><p>Each course has a student portal and a separate teacher figure studio. Progress stays in the browser; journals can be submitted through your usual classroom workflow. No accounts or shared gradebook are included.</p><p>Calculations, qualitative mechanisms and illustrative structures identify their assumptions. These investigations support instruction and do not replace a complete course curriculum. AP resources are independent and not endorsed by College Board.</p></div><footer>Everett Alvarez High School · Science & Math <span>Learn by figuring it out.</span></footer></main></body></html>''')
(root/'catalog.json').write_text(json.dumps(meta,indent=2))
print('Built five-course campus and four independent student/teacher portals.')
