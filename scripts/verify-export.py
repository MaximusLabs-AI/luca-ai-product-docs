import json,os
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
root=Path(__file__).resolve().parent.parent;out=root/'out'
c=json.loads((root/'lib/content.json').read_text());pages=c['pages'];entries=c['parameters'];routes={p['url'] for p in pages}
origin=os.environ.get('NEXT_PUBLIC_SITE_URL','http://127.0.0.1:3000').rstrip('/');base=os.environ.get('NEXT_PUBLIC_BASE_PATH','').rstrip('/')
class D(HTMLParser):
 def __init__(s):super().__init__();s.ids=set();s.links=[];s.meta={};s.canon=None;s.text=[];s.skip=0;s.ld=[];s.buf=None;s.title=[];s.it=False
 def handle_starttag(s,t,a):
  a=dict(a)
  if t in('script','style'):s.skip+=1
  if t=='script' and a.get('type')=='application/ld+json':s.buf=[]
  if t=='title':s.it=True
  if 'id' in a:s.ids.add(a['id'])
  if t=='a' and a.get('href'):s.links.append(a['href'])
  if t=='meta':s.meta[a.get('name',a.get('property',''))]=a.get('content','')
  if t=='link' and a.get('rel')=='canonical':s.canon=a.get('href')
 def handle_endtag(s,t):
  if t=='script' and s.buf is not None:s.ld.append(json.loads(''.join(s.buf)));s.buf=None
  if t=='title':s.it=False
  if t in('script','style'):s.skip=max(0,s.skip-1)
 def handle_data(s,d):
  if s.buf is not None:s.buf.append(d)
  if s.it:s.title.append(d)
  if not s.skip:s.text.append(d)
n=lambda x:' '.join(x.split())
parsed={}
for p in pages:
 f=out/p['url'].strip('/')/'index.html' if p['url']!='/' else out/'index.html'
 assert f.exists(),('missing route',p['url'])
 d=D();d.feed(f.read_text());parsed[p['url']]=d
 assert 'noindex' in d.meta.get('robots',''),p['url']
 assert d.canon==origin+p['url'],('canonical',p['url'],d.canon)
 assert ''.join(d.title)==p['seoTitle'],('title',p['url'])
 assert len(d.ld)==1 and d.ld[0]==p['schema'],('schema',p['url'])
 t=n(' '.join(d.text))
 for e in p['parameters']:
  assert e['anchor'] in d.ids,('anchor',e['id'])
  for a in e['answers']:
   for para in a['paragraphs']:assert n(para) in t,('text missing without JS',e['id'])
  if e['scope']:assert n(e['scope']) in t,('scope missing',e['id'])
for path,d in parsed.items():
 for h in d.links:
  u=urlsplit(h)
  if u.scheme or u.netloc:continue
  tg=u.path or base+path
  if not tg.startswith('/'):continue
  if base:
   assert tg==base or tg.startswith(base+'/'),('prefix',path,h);tg=tg[len(base):] or '/'
  if '.' in tg.split('/')[-1]:
   assert (out/unquote(tg.lstrip('/'))).exists(),('asset',tg);continue
  tg='/' if tg=='/' else tg.rstrip('/')+'/'
  assert tg in routes,('broken link',path,h)
  if u.fragment:assert unquote(u.fragment) in parsed[tg].ids,('broken anchor',path,h)
assert len({''.join(d.title) for d in parsed.values()})==len(pages)
r=dict(result='passed',pages=len(pages),capabilities=len(entries),statusCounts=c['stats']['statusCounts'],origin=origin,basePath=base)
(root/'verification.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
