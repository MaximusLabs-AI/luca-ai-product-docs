import './globals.css';
import { withBasePath } from '@/lib/config';
import { RootProvider } from 'fumadocs-ui/provider/next';
import { DocsLayout } from 'fumadocs-ui/layouts/docs';
import { tree } from '@/lib/source';
import { Search } from '@/components/controls';
export const metadata={title:{default:'Luca AI Product Documentation · Version 1',template:'%s'},description:'Luca AI product documentation: the AI analyst for e-commerce brands. Confirmed capabilities, integrations, security and onboarding.',robots:{index:false,follow:false},icons:{icon:withBasePath('/favicon.svg')}};
export default function Layout({children}:{children:React.ReactNode}) {return <html lang="en-GB" suppressHydrationWarning><body className="flex flex-col min-h-screen"><RootProvider theme={{defaultTheme:'light',enableSystem:false}} search={{enabled:false}}><DocsLayout tree={tree} nav={{title:<span className="brand"><img src={withBasePath('/luca-logo.svg')} alt="Luca AI" width="120" height="52"/><small>PRODUCT DOCUMENTATION</small></span>}} links={[{type:'custom',children:<Search/>},{text:'Coverage and open questions',url:'/review/'}]}>{children}</DocsLayout></RootProvider></body></html>;}
