import fs from 'node:fs';
const file='lib/content.json';const catalog=JSON.parse(fs.readFileSync(file,'utf8'));
const origin=(process.env.NEXT_PUBLIC_SITE_URL??'http://127.0.0.1:3000').replace(/\/$/,'');
const DATE='2026-10-16';
const shorten=(text,n)=>{if(text.length<=n)return text;const cut=text.slice(0,n);const end=Math.max(cut.lastIndexOf('. '),cut.endsWith('.')?cut.length-1:-1);return end>60?cut.slice(0,end+1):cut.slice(0,n-1).replace(/\s+\S*$/,'').replace(/[.,;: ]+$/,'')+'…';};
const counts=new Map();for(const p of catalog.pages)counts.set(p.title,(counts.get(p.title)??0)+1);
for(const p of catalog.pages){
 const title=counts.get(p.title)>1?p.title+' · '+p.url.split('/').filter(Boolean).slice(0,-1).join(' / ').replaceAll('-',' '):p.title;
 p.seoTitle=p.url==='/'?'Luca AI Product Documentation':title+' | Luca AI Docs';
 let description;
 if(p.url==='/')description='Luca AI product documentation: the AI analyst for e-commerce brands. Confirmed capabilities, integrations, security, pricing model and onboarding.';
 else if(p.parameters.length){const def=p.parameters[0].definition;const first=def.split(/(?<=\.)\s/)[0];const a=p.title+'. '+def,b=p.title+'. '+first;description=a.length<=158?a:b.length<=158?b:first;}
 else description=p.title+'. '+(p.intro[0]??'');
 p.metaDescription=shorten(description.replace(/\s+/g,' '),158);
 const pageUrl=origin+p.url;const segs=p.url.split('/').filter(Boolean);const breadcrumb=[{'@type':'ListItem',position:1,name:'Documentation',item:origin+'/'}];
 segs.forEach((name,i)=>breadcrumb.push({'@type':'ListItem',position:i+2,name:name.replaceAll('-',' '),item:origin+'/'+segs.slice(0,i+1).join('/')+'/'}));
 const kind=p.children.length?'CollectionPage':p.url.startsWith('/review/')||p.url==='/'?'WebPage':'TechArticle';p.schemaType=kind;
 const page={'@type':kind,'@id':pageUrl+'#document',url:pageUrl,name:p.title,...(kind==='TechArticle'?{headline:p.title}:{}),description:p.metaDescription,inLanguage:'en-GB',dateModified:DATE,creativeWorkStatus:'Draft',isPartOf:{'@id':origin+'/#website'},publisher:{'@id':origin+'/#publisher'},about:{'@id':origin+'/#product'},breadcrumb:{'@id':pageUrl+'#breadcrumb'},...(p.parameters.length?{mentions:p.parameters.map(e=>({'@type':'DefinedTerm','@id':pageUrl+'#'+e.anchor,name:e.name,description:e.definition}))}:{}),...(p.children.length?{hasPart:p.children.map(c=>({'@type':'WebPage',name:c.title,url:origin+c.url}))}:{})};
 p.schema={'@context':'https://schema.org','@graph':[{'@type':'Organization','@id':origin+'/#publisher',name:'Luca AI',url:'https://ask-luca.com',logo:origin+'/luca-logo.svg'},{'@type':'SoftwareApplication','@id':origin+'/#product',name:'Luca AI',applicationCategory:'BusinessApplication',operatingSystem:'Web',url:'https://ask-luca.com',publisher:{'@id':origin+'/#publisher'}},{'@type':'WebSite','@id':origin+'/#website',name:'Luca AI Product Documentation',url:origin+'/',inLanguage:'en-GB',publisher:{'@id':origin+'/#publisher'}},page,{'@type':'BreadcrumbList','@id':pageUrl+'#breadcrumb',itemListElement:breadcrumb}]};
}
for(const p of catalog.pages)for(const child of p.children){const t=catalog.pages.find(x=>x.url===child.url);if(t){child.title=t.title;child.description=t.metaDescription;}}
if(new Set(catalog.pages.map(p=>p.seoTitle)).size!==catalog.pages.length)throw Error('Duplicate SEO title');
if(new Set(catalog.pages.map(p=>p.metaDescription)).size!==catalog.pages.length)throw Error('Duplicate meta description');
fs.writeFileSync(file,JSON.stringify(catalog,null,1));
const q=s=>'"'+String(s).replaceAll('"','""')+'"';
fs.writeFileSync('public/downloads/luca-ai-page-metadata-v1.csv',[['URL','Page Title','Meta Description','Canonical URL','Depth','Schema Type','Robots'],...catalog.pages.map(p=>[p.url,p.seoTitle,p.metaDescription,origin+p.url,p.depth,p.schemaType,'noindex,nofollow'])].map(r=>r.map(q).join(',')).join('\n')+'\n');
fs.writeFileSync('public/downloads/luca-ai-schema-by-url.json',JSON.stringify(Object.fromEntries(catalog.pages.map(p=>[p.url,p.schema])),null,1));
fs.writeFileSync('public/sitemap.xml','<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+catalog.pages.map(p=>'<url><loc>'+origin+p.url+'</loc><lastmod>'+DATE+'</lastmod></url>').join('')+'</urlset>');
fs.writeFileSync('public/search-index.json',JSON.stringify([...catalog.pages.map(p=>({title:p.title,url:p.url,text:p.intro.join(' ')})),...catalog.parameters.map(e=>({title:e.id+' · '+e.name,url:e.destination+'#'+e.anchor,text:e.definition+' '+e.status}))]));
fs.writeFileSync('public/llms.txt','# Luca AI Product Documentation · Version 1 review draft\n\n> Documents confirmed capabilities of Luca AI, the AI analyst for e-commerce brands. Review draft; noindex.\n\n'+catalog.pages.map(p=>'- ['+p.title+']('+origin+p.url+'): '+p.metaDescription).join('\n')+'\n');
fs.writeFileSync('public/robots.txt','User-agent: *\nDisallow: /\n');
console.log('Prepared '+catalog.pages.length+' pages and '+catalog.parameters.length+' capabilities for '+origin);
