(async function () {

    const mediaList = await listMedia();
    console.table(mediaList);

        async function listMedia() {
        
        var mediaList = [];
        const limit = 100;
        var skip = 100;
        var url = '/api/v1/media?take=' + limit ;
        
        while (url) {
            
            const r = await fetch (url, {method: 'get'});
            const res = await r.json();
            
            const pageInfo = res.pageInfo;
            const page = pageInfo.page;
            const pages = pageInfo.pages;

            if (page < pages) {
            
                skip += 100;
                var url = '/api/v1/media?take=' + limit + '&skip=' + skip ;
                const r = await fetch (url, {method: 'get'});
                const res = await r.json();
                var results = res.results;
                mediaList = mediaList.concat(results);

            }
            else { 
            
                console.table(mediaList);
                return mediaList; 
                
            }
    }

}
}
)();