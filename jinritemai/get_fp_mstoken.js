function get_fp_mstoken () {
        let web = window['localStorage']['getItem']('__tea_cache_tokens_2018')
        web = JSON.parse(web)
        let result = {}
        result.fp = web?.user_unique_id
        result.msToken = window['localStorage']['getItem']('xmst')
        result._lid = "".concat(String(Date.now()).slice(5)).concat(String(Math.random()).slice(2, 6))
    return result;
}