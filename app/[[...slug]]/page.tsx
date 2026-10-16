import { DocsPage,DocsBody,DocsTitle,DocsDescription } from 'fumadocs-ui/layouts/docs/page';
import { notFound } from 'next/navigation';
import Link from 'next/link';
import { pages,getPage } from '@/lib/source';
import { origin, withBasePath } from '@/lib/config';
import { getSchema } from '@/lib/schema';
import { PageControls } from '@/components/controls';
export const dynamicParams=false;
export function generateStaticParams(){return pages.map(p=>({slug:p.url.split('/').filter(Boolean)}));}
export async function generateMetadata({params}:{params:Promise<{slug?:string[]}>}){const p=getPage((await params).slug);if(!p)return{};return{title:{absolute:p.seoTitle},description:p.metaDescription,alternates:{canonical:origin+p.url},openGraph:{title:p.seoTitle,description:p.metaDescription,url:origin+p.url,type:'article'},twitter:{card:'summary',title:p.seoTitle,description:p.metaDescription}}}
export default async function Page({params}:{params:Promise<{slug?:string[]}>}){const p=getPage((await params).slug);if(!p)notFound();
const toc=[{title:'Overview',url:'#overview',depth:2},...p.sections.map(s=>({title:s.title,url:'#'+s.id,depth:2})),...p.parameters.map(x=>({title:x.name,url:'#'+x.anchor,depth:3}))];
const breadcrumbs=p.url.split('/').filter(Boolean).map((seg,i,a)=>({name:seg.replaceAll('-',' '),url:'/'+a.slice(0,i+1).join('/')+'/'}));
return <DocsPage toc={toc} full={false}><div className="page-topline">LUCA AI PRODUCT DOCUMENTATION <span>Version 1.0 · 16 October 2026</span></div><DocsTitle>{p.title}</DocsTitle><DocsDescription>{p.metaDescription}</DocsDescription><PageControls title={p.title} url={p.url}/><DocsBody>
<nav className="url-trail" aria-label="URL hierarchy"><Link href="/">Home</Link>{breadcrumbs.map(b=><span key={b.url}> / <Link href={b.url}>{b.name}</Link></span>)}</nav>
<section id="overview"><h2>Overview</h2>{p.intro.map((v,i)=><p key={i}>{v}</p>)}</section>
{p.sections.map(s=><section id={s.id} key={s.id}><h2>{s.title}</h2>{s.paragraphs.map((v,i)=><p key={i}>{v}</p>)}{s.links?.length>0&&<ul>{s.links.map(l=><li key={l.url}>{l.url.startsWith('/downloads/')?<a href={withBasePath(l.url)} download>{l.title}</a>:<Link href={l.url}>{l.title}</Link>}</li>)}</ul>}</section>)}
{p.parameters.length>0&&<><h2>Capabilities on this page</h2><p className="muted">Each entry explains what the capability is, how it works in Luca, why it matters and its limits. Expand an entry to read it in full.</p></>}
{p.parameters.map(x=><details className="micro-feature" key={x.id} id={x.anchor}><summary><span className={'status status-'+x.statusKey}>{x.status}</span><strong>{x.name}</strong><span className="parameter-id">{x.id}</span></summary><div className="micro-body">
<p className="definition">{x.definition}</p>
{x.scope&&<p className="scope-note"><strong>Scope:</strong> {x.scope}</p>}
{x.answers.map((a,i)=><section key={i}><h3>{a.question}</h3>{a.paragraphs.map((v,j)=><p key={j}>{v}</p>)}</section>)}
<section><h3>How to check it during setup or a trial</h3><p>{x.example}</p></section>
<section><h3>Limits and boundaries</h3><p>{x.boundary}</p></section>
<section className="review-note"><h3>Evidence</h3><ul>{x.evidence.map((e,i)=><li key={i}>{e.fact} <em>Source: {e.source}.</em></li>)}</ul><p><strong>To confirm with Luca before publication:</strong> {x.review}</p><dl><dt>Status</dt><dd>{x.statusDetail}</dd><dt>Buyer importance</dt><dd>{x.weightLabel}</dd><dt>Inventory reference</dt><dd>{x.section}</dd></dl></section>
{x.related?.length>0&&<section><h3>Related documentation</h3><ul>{x.related.map(l=><li key={l.url}><Link href={l.url}>{l.title}</Link></li>)}</ul></section>}
<a className="anchor-link" href={'#'+x.anchor}>Permanent link to {x.id}</a></div></details>)}
{p.children.length>0&&<section id="explore"><h2>In this section</h2><div className="child-grid">{p.children.map(c=><Link className="child-card" href={c.url} key={c.url}><strong>{c.title}</strong><small>{c.description}</small><span>{c.url}</span></Link>)}</div></section>}
<footer className="document-footer"><p>Version 1 documents only capabilities MaximusLabs has confirmed from Luca&apos;s product, founder statements and published policies, each dated. Anything not yet confirmed is out of this version and listed for Luca&apos;s team to confirm. Benefits describe why a capability matters; they are not performance guarantees.</p><Link href="/review/">Coverage and open questions →</Link></footer>
</DocsBody><script type="application/ld+json" dangerouslySetInnerHTML={{__html:JSON.stringify(getSchema(p)).replace(/</g,'\\u003c')}}/></DocsPage>}
