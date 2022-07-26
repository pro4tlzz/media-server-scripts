(async function () {

    const mediaList = await listMedia();
    console.table(mediaList);

        async function listMedia() {
        
            var mediaList = [];
            const limit = 25;
            var skip = 25;
            var url = '/api/v1/media?filter=all&take=' + limit ;
            
            while (url) {
                
                const r = await fetch (url, {method: 'get'});
                const res = await r.json();
                var results = res.results;
                mediaList = mediaList.concat(results);
                const pageInfo = res.pageInfo;
                const page = pageInfo.page;
                const pages = pageInfo.pages;
    
                if (page < pages) {
                
                    skip += 25;
                    var url = '/api/v1/media?filter=all&take=' + limit + '&skip=' + skip;
    
                }
                else { 
    
                    mediaList = mediaList.concat(results);
                    console.table(mediaList);
                    return mediaList; 
                    
                }
        
            }
            
            return mediaList;

}
}
)();