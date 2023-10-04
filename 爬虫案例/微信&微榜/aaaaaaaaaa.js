
var l = Math.random().toString(16).slice(-9);
console.log(l)
//fa24f5ded
//e5aede09b
var _xl;
a1 = '/xdnphb/indexNew/getAdvertBannerImage'
e1 = {}


g = function(a, e) {
    var f = [];
    b.each(e, function(a, c) {
        f.push(b.trim(a))
    }),
    f.sort();
    var g = {}
      , h = "";
    0 == a.indexOf("http://") ? h += a.slice(a.indexOf("/", 7)) + "?AppKey=" + c.AppKey : 0 == a.indexOf("https://") ? h += a.slice(a.indexOf("/", 8)) + "?AppKey=" + c.AppKey : h = a + "?AppKey=" + c.AppKey,
    b(f).each(function() {
        var a = this;
        g[a] = e[a],
        h += "&" + a + "=" + e[a]
    });
    var i = j();
    return g.nonce = i,
    h += "&nonce=" + i,
    g.xyz = d(h),
    {
        objParameter: g
    }
}
// console.log(g(a1,e1))

//'/xdnphb/main/v1/weibo_day/rank'
//{rank_name_group: '', rank_name: '个人认证', start: '2022-09-01', end: '2022-09-01'}