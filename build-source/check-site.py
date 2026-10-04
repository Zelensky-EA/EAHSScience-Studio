from pathlib import Path
from html.parser import HTMLParser
import json,re
root=Path(__file__).parent/'site'
class P(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.refs=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  for k in ['src','href']:
   if k in a:self.refs.append(a[k])
count=0
for file in root.rglob('*.html'):
 if file.name.startswith('EAHS-'):continue
 p=P();p.feed(file.read_text());assert len(p.ids)==len(set(p.ids)),file
 for link in p.refs:
  if link.startswith(('http:','https:','#','?','data:')):continue
  path=file.parent/link.split('?')[0].split('#')[0]
  assert path.is_file(),(file,link)
 count+=1
for code in ['ap-chemistry','anatomy-physiology','ap-calculus-ab','ap-calculus-bc']:
 d=root/code;catalog=json.loads((d/'model-catalog.json').read_text())
 assert len(catalog['activities'])==len({a['id'] for a in catalog['activities']})
 for unit in range(1,len(catalog['units'])+1):
  assert any(a['unit']==unit for a in catalog['activities']), (code,unit)
  for teacher in [False,True]:
   f=d/f'{"teacher-" if teacher else ""}unit-{unit}.html'
   cfg=json.loads(re.search(r'window.PORTAL=(.*?);',f.read_text())[1]);assert cfg=={'course':code,'unit':unit,'teacher':teacher}
 for target in ['index.html','teacher.html',*[f'unit-{i}.html' for i in range(1,len(catalog['units'])+1)],*[f'teacher-unit-{i}.html' for i in range(1,len(catalog['units'])+1)]]:assert (d/target).is_file()
 standalone=(d/('EAHS-'+code+'-Portal.html')).read_text();assert 'window.OFFLINE=true' in standalone;assert '<script src=' not in standalone;assert '<link rel="stylesheet"' not in standalone
print(f'PASS: {count} static pages, local assets, unit routes, unique activity IDs and four portable editions.')
