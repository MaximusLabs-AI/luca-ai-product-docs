import catalog from './content.json';
import type { Root, Node } from 'fumadocs-core/page-tree';
export const pages = catalog.pages;
export const parameters = catalog.parameters;
export const stats = catalog.stats;
export { origin } from './config';
export function getPage(slug?: string[]) {return pages.find(p=>p.url==='/' +(slug??[]).join('/') + ((slug??[]).length?'/':''));}
const roots=['products','integrations','solutions','pricing','security','support','review'];
const uiUrl=(url:string)=>url==='/'?'/':url.replace(/\/$/,'');
function nodes(prefix:string):Node[]{
 const level=prefix.split('/').filter(Boolean).length;
 return pages.filter(p=>p.url!==prefix&&p.url.startsWith(prefix)&&p.url.split('/').filter(Boolean).length===level+1).map(p=>{
 const children=nodes(p.url);
 return children.length?{type:'folder',name:p.navTitle??p.title,index:{type:'page',name:p.navTitle??p.title,url:uiUrl(p.url)},children}:{type:'page',name:p.navTitle??p.title,url:uiUrl(p.url)};
 });
}
const top=nodes('/');
export const tree:Root={name:'Luca AI',children:[{type:'page',name:'Start here',url:'/'},...roots.flatMap(r=>top.filter(n=>(n.type==='folder'?n.index?.url:(n as any).url)===`/${r}`)),...top.filter(n=>n.type==='page'&&!roots.includes(((n as any).url as string).split('/')[1]))]};
