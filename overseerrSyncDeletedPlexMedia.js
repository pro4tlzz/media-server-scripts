async function  getMe() {
    const url = '/api/v1/auth/me';
    const r = await fetch (url, {method: 'get'});
    const res = await r.json();
    console.log(res);
}

async function listMedia() {
    const url = '/api/v1/media';
    const r = await fetch (url, {method: 'get'});
    const res = await r.json();
    console.log(res);
}

await getMe();
await listMedia();