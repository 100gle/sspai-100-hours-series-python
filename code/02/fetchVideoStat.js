(function () {
    let api = window.__INITIAL_STATE__;
    let stat = undefined;
    try {
        stat = api.videoData.stat;
    } catch (e) {}

    const cols = ["rank", "like", "coin", "collect", "share"];

    let blankStat = {};
    for (const col of cols) {
        blankStat[col] = "";
    }

    if (stat === undefined) {
        return blankStat;
    }
    return {
        rank: stat.his_rank,
        like: stat.like,
        coin: stat.coin,
        collect: stat.favorite,
        share: stat.share,
    };
})();
