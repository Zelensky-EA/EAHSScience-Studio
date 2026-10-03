from html.parser import HTMLParser
from pathlib import Path
import re,json
root=Path(__file__).parent
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.ids=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  for key in ['href','src']:
   if key in a:self.refs.append(a[key])
for name in ['index.html','data-tools.html',*[f'unit-{i}.html' for i in range(1,9)]]:
 p=Parser();p.feed((root/name).read_text());assert len(p.ids)==len(set(p.ids)),name+' duplicate ids'
 for ref in p.refs:
  if ref.startswith(('http:','https:','#','?')):continue
  assert (root/ref.split('#')[0].split('?')[0]).is_file(),(name,ref)
 if name!='index.html':
  script=(root/'app.js').read_text()
  static_ids=set(re.findall(r"\$\('([^']+)'\)",script))
  dynamic={'random-family','check-reading','new-reading','read-answer','reading-feedback','digest-to-gel'}
  assert static_ids-set(p.ids)-dynamic==set(),(name,static_ids-set(p.ids)-dynamic)
print('PASS: landing and nine workspaces have valid local asset/navigation references, unique IDs and all required static controls.')
