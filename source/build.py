"""Assemble lib/content.json + review downloads from spec.py, the writers' prose and the inventory."""
import csv, json, re, sys, collections, pathlib, shutil
ROOT = pathlib.Path('/Users/krishnakaanth/luca-ai-product-docs'); sys.path.insert(0, str(ROOT/'source'))
import spec
PROSE = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT/'source'/'prose'
INV = '/Users/krishnakaanth/Maximus Work/clients/luca-ai/strategy/2026-10-16_luca-ai_strategy_buyer-and-ai-evaluation-parameters.csv'
inv = {r['id']: r for r in csv.DictReader(open(INV))}
pages_out, params_out = {}, {}
for f in sorted(PROSE.glob('out-*.json')):
    d = json.load(open(f))
    for p in d['pages']: pages_out[p['url']] = p
    for x in d['parameters']: params_out[x['id']] = x

BANNED = [r'\bSOC ?2\b', r'\bISO ?27001', r'data residency', r'autonomous', r'autonomously', r'autonomy', r'anomal', r'forecast', r'scenario', r'\bmemory\b', r'proactive', r'push insight', r'\blender\b(?! of)', r'financing company', r'[€$£]\s?\d', r'\d+\s?%', r'\b\d+\s?(days?|weeks?)\b', r'[–—]', r'!', r'seamless', r'powerful', r'revolutionary', r'20\+']
ALLOW = {  # sentences where the banned token is a negation or a fact from the spec
 r'\blender\b(?! of)': ['not a lender', 'is not a lender', 'not a financing company', 'lending partners'],
 r'financing company': ['not a financing company'],
 r'[€$£]\s?\d': ['$72,000'], r'\b\d+\s?(days?|weeks?)\b': ['30 days', 'three weeks', 'couple of days'],
}
issues = []
def scan(where, text):
    for pat in BANNED:
        for m in re.finditer(pat, text, re.I):
            s = text[max(0, m.start()-60): m.end()+60]
            if any(a.lower() in s.lower() for a in ALLOW.get(pat, [])): continue
            if pat in (r'autonomous', r'autonomously', r'autonomy', r'proactive', r'\bmemory\b', r'forecast', r'scenario', r'anomal') and re.search(r"\b(not|no|never|doesn't|does not|isn't|without|cannot|can't|outside)\b", s, re.I): continue
            issues.append((where, pat, s.replace('\n', ' ')))

STATUS = {'available': ('Available', 'Confirmed from Luca product evidence, founder statements or published policy, as cited below. Not a fresh product test.'),
          'scoped': ('Available · limited scope', 'Confirmed to exist, in the narrower form stated in the scope note. Wider availability is listed for Luca to confirm.')}
WL = {'H': 'High', 'M': 'Medium', 'L': 'Low'}
page_by_url = {p['url']: p for p in spec.PAGES}
anchor = lambda i, n: (i + '-' + re.sub(r'[^a-z0-9]+', '-', n.lower())).strip('-')[:70]
params = []
for x in spec.P:
    w = params_out.get(x['id']); r = inv.get(x['id'], {})
    if not w: issues.append((x['id'], 'missing prose', '')); continue
    name = w.get('name') or x['name'] or r.get('parameter') or x['id']
    sk = x['status']; label, detail = STATUS[sk]
    rel = [dict(url=u, title=page_by_url[u]['title']) for u in x['related'] if u in page_by_url]
    e = dict(id=x['id'], name=name, parameter=name, section=(r.get('subsection') or 'Luca microfeature (outside the inventory)'), weight=r.get('weight_or_type') or 'M',
             weightLabel=WL.get(r.get('weight_or_type') or 'M', 'Medium'), have=r.get('have_or_status', '✅'), claimed=r.get('claimed', ''), ai=r.get('ai', ''),
             destination=x['dest'], anchor=anchor(x['id'], name), statusKey=sk, status=label, statusDetail=detail, scope=x['scope'] or '',
             definition=w['definition'], answers=w['answers'], example=w['example'], boundary=w['boundary'], review=w['review'], related=rel,
             evidence=[dict(fact=f, source=spec.SRC[s]) for f, s in x['facts']])
    blob = ' '.join([e['definition'], e['example'], e['boundary'], *[p for a in e['answers'] for p in a['paragraphs']]])
    scan(x['id'], blob)
    if x['scope'] and x['scope'][:40].lower() not in (blob + e['review']).lower(): issues.append((x['id'], 'scope sentence not in text', x['scope']))
    params.append(e)

pages = []
for sp in spec.PAGES:
    w = pages_out.get(sp['url'])
    if sp['url'] == '/review/':
        w = None
    if not w and sp['url'] != '/review/': issues.append((sp['url'], 'missing page prose', '')); w = dict(intro=[sp['title']], sections=[])
    depth = len(sp['url'].strip('/').split('/')) if sp['url'] != '/' else 0
    parent = '/' if depth <= 1 else '/' + '/'.join(sp['url'].strip('/').split('/')[:-1]) + '/'
    pg = dict(url=sp['url'], title=sp['title'], navTitle=sp['nav'], page_type=sp['type'], parent=parent if sp['url'] != '/' else '', depth=depth,
              intro=(w or {}).get('intro', []), sections=(w or {}).get('sections', []), parameters=[e for e in params if e['destination'] == sp['url']], children=[])
    for s in pg['sections']: s.setdefault('links', []); scan(sp['url'], ' '.join(s['paragraphs']))
    scan(sp['url'], ' '.join(pg['intro']))
    pg['parameter_ids'] = [e['id'] for e in pg['parameters']]
    pages.append(pg)
by = {p['url']: p for p in pages}
for p in pages:
    if p['url'] != '/' and p['parent'] in by: by[p['parent']]['children'].append(dict(url=p['url'], title=p['title'], description=''))
# Home lists the top areas; children of '/' already include all depth-1 pages.

# Review page (written here, from the worksheet facts).
wb_rows = 379
counts = collections.Counter(e['statusKey'] for e in params)
rv = by['/review/']
rv['intro'] = [f"This version documents {len(params)} capabilities: {counts['available']} confirmed as available and {counts['scoped']} confirmed in a limited form, each with its scope stated. They come from a 612-parameter evaluation of what e-commerce buyers and AI engines look for in an AI analyst agent.",
               "Everything MaximusLabs could not confirm is left out of this version on purpose. It is listed in a worksheet for Luca's team, together with the places where Luca's website currently describes the same thing in different ways."]
rv['sections'] = [
 dict(id='method', title='How capabilities were confirmed', paragraphs=['A capability is documented only when it appears in Luca\'s product (a product screenshot or a live demonstration), in a statement by Luca\'s founder on a recorded call, or in a policy Luca publishes. Each entry lists its evidence and date.', 'Capabilities that appear only in specifications, roadmaps or website copy we could not match to the product are not documented here, even where the website states them.'], links=[]),
 dict(id='open-questions', title='What Luca\'s team is asked to confirm', paragraphs=[f'The worksheet holds {wb_rows} parameters to confirm, 19 website contradictions to resolve and 23 product questions. Answers move items into version 2.'], links=[dict(url='/downloads/luca-ai-product-parameters-to-confirm.xlsx', title='Worksheet for Luca (Excel)'), dict(url='/downloads/luca-ai-documentation-review.csv', title='Documented capabilities (CSV)'), dict(url='/downloads/luca-ai-documentation-urls-v1.csv', title='URL map (CSV)'), dict(url='/downloads/luca-ai-product-documentation-v1.md', title='Full documentation (Markdown)')]),
 dict(id='not-documented', title='Areas deliberately not documented in version 1', paragraphs=['Actions Luca takes in connected systems on its own, automatic alerts and daily insights, memory across conversations, forecasting and scenario modelling, capital availability and terms, prices, certifications, data residency and the full connector list. Each is in the worksheet.'], links=[]),
]

stats = dict(pageCount=len(pages), parameterCount=len(params), statusCounts=dict(counts), inventoryParameters=612, toConfirm=wb_rows)
(ROOT/'lib'/'content.json').write_text(json.dumps(dict(pages=pages, parameters=params, stats=stats), ensure_ascii=False, indent=1))

# Downloads
dl = ROOT/'public'/'downloads'; dl.mkdir(parents=True, exist_ok=True)
with open(dl/'luca-ai-documentation-review.csv', 'w', newline='') as f:
    wr = csv.writer(f); wr.writerow(['ID', 'Capability', 'Status', 'Scope', 'Page', 'Anchor', 'Evidence', 'To confirm'])
    for e in params: wr.writerow([e['id'], e['name'], e['status'], e['scope'], e['destination'], e['anchor'], ' | '.join(f"{v['fact']} ({v['source']})" for v in e['evidence']), e['review']])
with open(dl/'luca-ai-documentation-urls-v1.csv', 'w', newline='') as f:
    wr = csv.writer(f); wr.writerow(['URL', 'Title', 'Type', 'Depth', 'Capabilities'])
    for p in pages: wr.writerow([p['url'], p['title'], p['page_type'], p['depth'], ' '.join(p['parameter_ids'])])
md = ['# Luca AI product documentation · Version 1', '', 'Review draft, 16 October 2026. Documents confirmed capabilities only.', '']
for p in pages:
    md += [f"## {p['title']}", f"`{p['url']}`", ''] + [x + '\n' for x in p['intro']]
    for s in p['sections']: md += [f"### {s['title']}", ''] + [x + '\n' for x in s['paragraphs']]
    for e in p['parameters']:
        md += [f"### {e['id']} · {e['name']} ({e['status']})", '', e['definition'], '']
        if e['scope']: md += [f"**Scope:** {e['scope']}", '']
        for a in e['answers']: md += [f"**{a['question']}**", ''] + [x + '\n' for x in a['paragraphs']]
        md += ['**How to check it:** ' + e['example'], '', '**Limits:** ' + e['boundary'], '', '**Evidence:**'] + [f"- {v['fact']} ({v['source']})" for v in e['evidence']] + ['', '**To confirm:** ' + e['review'], '']
(dl/'luca-ai-product-documentation-v1.md').write_text('\n'.join(md))
wbsrc = pathlib.Path('/Users/krishnakaanth/Maximus Work/clients/luca-ai/deliverables/product-documentation-v1/2026-10-16_luca-ai_deliverable_product-parameters-to-confirm.xlsx')
if wbsrc.exists(): shutil.copy(wbsrc, dl/'luca-ai-product-parameters-to-confirm.xlsx')
print(json.dumps(stats))
print(f'{len(issues)} issues')
for i in issues: print(' ', i)
