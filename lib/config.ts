export const basePath=(process.env.NEXT_PUBLIC_BASE_PATH??'').replace(/\/$/,'');
export const origin=(process.env.NEXT_PUBLIC_SITE_URL??'http://127.0.0.1:3000').replace(/\/$/,'');
export const withBasePath=(path:string)=>basePath+path;
