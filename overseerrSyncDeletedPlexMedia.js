async function  getMe() {
    const url = '/api/v1/auth/me';
    const r = await fetch (url, {method: 'get'});
    const res = await r.json();
    console.log(res);
}

async function listMedia(mediaList) {
    const limit = 20;
    var skip = 20;
    const url = '/api/v1/media?take=' + limit ;
    const r = await fetch (url, {method: 'get'});
    const res = await r.json();
    console.log(res);
    var results = res.results;
    mediaList.push(results);
    console.table(results);
    const pageInfo = res.pageInfo;
    const page = pageInfo.page;
    const pages = pageInfo.pages;

    if (page != pages) {
        skip += 20;
        const url = '/api/v1/media?take=' + limit + '&skip=' + skip ;
        console.log(url);
        const r = await fetch (url, {method: 'get'});
        const res = await r.json();
        console.log(res);
    }

}

var mediaList = [];
await getMe();
await listMedia(mediaList);