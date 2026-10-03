from pathlib import Path
import json,re
root=Path(__file__).parent
units=[
 ('Chemistry of Life','Water, macromolecules & molecular structure','Water & bonding · atom accounting','Polymers, carbohydrates & lipids','Nucleic acids, proteins & pH'),
 ('Cells','Structure, membranes & transport','Cell size, trafficking & permeability','Diffusion, water potential & osmosis','Pumps, compartments & endosymbiosis'),
 ('Cellular Energetics','Enzymes, photosynthesis & respiration','Enzyme kinetics & energy diagrams','Photosynthesis & light response','Respiration, fermentation & respirometry'),
 ('Cell Communication & Cell Cycle','Signals, feedback & regulated division','Receptors & signal transduction','Feedback & homeostasis','Cell cycle, mitotic index & checkpoints'),
 ('Heredity','Chromosomes, crosses & phenotype','Meiosis, nondisjunction & linkage','Punnett squares, pedigrees & epistasis','Polygenic traits & reaction norms'),
 ('Gene Expression & Regulation','From DNA sequence to cellular function','Replication, transcription & translation','Regulation, specialization & mutations','PCR, restriction digest, transformation & gels'),
 ('Natural Selection','Population change & evolutionary evidence','Selection, drift, gene flow & equilibrium','Trait distributions & artificial selection','Sequence evidence, phylogeny & speciation'),
 ('Ecology','Organisms, populations & ecosystems','Behavior, productivity & matter cycles','Populations, sampling & competition','Food webs, biodiversity & disruption')]
base=(root/'build'/'page-template.html').read_text()
base=base.replace('href="#"','href="index.html"',1)
base=base.replace('<span class="header-note">Explore · Create · Teach</span>','<a class="header-note home-link" href="index.html">← All units</a>')
base=base.replace('THE TOOL COLLECTION','UNIT TOOLS')
base=base.replace('<button id="about">About & scientific references</button>','<a href="data-tools.html">Data & investigation tools ↗</a><p><a href="index.html">← All units</a></p><button id="about">About & scientific references</button>')
base=base.replace('Show answers & annotations','Show results & annotations')
base=base.replace('<script src="models.js"></script>','<script>const UNIT_NUMBER=UNIT_VALUE;</script><script src="models.js"></script><script src="extra.js"></script>')
for i,u in enumerate(units,1):
 html=base.replace('<main id="workspace">',f'<main id="workspace"><p class="unit-context">Unit {i} · {u[0]}</p>').replace('UNIT_VALUE',str(i)).replace('<title>EAHS Science • Figure & Model Studio</title>',f'<title>Unit {i}: {u[0]} · EAHS Science</title>')
 (root/f'unit-{i}.html').write_text(html)
(root/'data-tools.html').write_text(base.replace('UNIT_VALUE','0').replace('<title>EAHS Science • Figure & Model Studio</title>','<title>Data & Investigation Tools · EAHS Science</title>'))
head='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="EAHS Science models and investigations organized by the eight AP Biology units."><title>EAHS Science · AP Biology Model Studio</title><link rel="stylesheet" href="styles.css"></head><body><header><a class="brand" href="index.html"><span class="mark">EA</span><span>EAHS <b>SCIENCE</b><small>FIGURE & MODEL STUDIO</small></span></a><a class="header-note home-link" href="data-tools.html">Data & investigation tools ↗</a></header><main class="landing"><div class="landing-intro"><p class="eyebrow">AP BIOLOGY · INTRODUCTORY COLLEGE</p><h1>Explore biology.<br><span>One model at a time.</span></h1><p>Choose a unit. Change a condition, investigate a mechanism, and create a figure for your lesson.</p></div><div class="unit-grid">'''
body=''
for i,(title,sub,*parts) in enumerate(units,1):
 body+=f'<a class="unit-card" href="unit-{i}.html"><div class="unit-card-top"><span class="unit-label">UNIT {i}</span><span class="unit-arrow">↗</span></div><h2>{title}</h2><p>{sub}</p><ul>'+''.join(f'<li>{p}</li>' for p in parts)+'</ul><span class="unit-open">Explore unit →</span></a>'
end='''</div><a class="data-card" href="data-tools.html"><div><p class="eyebrow">ACROSS ALL UNITS</p><h2>Data & investigation tools</h2><p>Graphing · SD & SE · chi-square · experimental design · micropipette practice</p></div><span>Explore tools →</span></a><div class="landing-notes"><p><strong>Built for reasoning.</strong> Quantitative models, schematic mechanisms and evidence explorers identify their assumptions. College extensions are identified in the notes.</p><p><strong>Take the figure with you.</strong> Download PNG or SVG, print the figure, export data, and share settings. No account or paid API required.</p><p>Aligned to AP Biology topic organization effective Fall 2025. Independent resource; not endorsed by College Board. <a href="https://apcentral.collegeboard.org/media/pdf/ap-biology-course-and-exam-description.pdf" target="_blank" rel="noopener">Course framework ↗</a></p></div><footer>Everett Alvarez High School · Science Department <span>AP Biology Model Studio · Unit edition</span></footer></main></body></html>'''
(root/'index.html').write_text(head+body+end)
# Offline all-in-one edition: same actual pages encoded as text, with inlined assets.
# Navigation uses a local URL query key and reloads into the chosen page.
pages={}
page_paths=[root/'index.html',*[root/f'unit-{i}.html' for i in range(1,9)],root/'data-tools.html']
for p in page_paths:
 html=p.read_text()
 for asset in ['styles.css','models.js','extra.js','app.js']:
  html=html.replace(f'"{asset}"',f'"{asset}?v=unit-edition-2"')
 p.write_text(html)
for p in [root/'index.html',*[root/f'unit-{i}.html' for i in range(1,9)],root/'data-tools.html']:
 html=p.read_text().replace('<link rel="stylesheet" href="styles.css?v=unit-edition-2">','<style>'+(root/'styles.css').read_text()+'</style>')
 for js in ['models.js','extra.js','app.js']:
  html=html.replace(f'<script src="{js}?v=unit-edition-2"></script>','<script>'+(root/js).read_text()+'</script>')
 for name in ['index.html',*[f'unit-{i}.html' for i in range(1,9)],'data-tools.html']:
  html=html.replace(f'href="{name}"',f'href="?page={name}"')
 pages[p.name]=html
payload=json.dumps(pages,ensure_ascii=False).replace('</script','<\\/script')
wrapper='<!doctype html><html><head><meta charset="utf-8"><title>EAHS Science Studio</title></head><body><script>const pages='+payload+';const p=new URLSearchParams(location.search).get("page")||"index.html";document.open();document.write(pages[p]||pages["index.html"]);document.close();</script></body></html>'
(root/'EAHS-Science-Studio.html').write_text(wrapper)
print('Built index, eight unit pages, shared data page and offline standalone edition.')
