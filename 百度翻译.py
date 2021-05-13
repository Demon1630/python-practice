
import requests

import execjs  #反爬虫，获取 sign参数




token = '76444dbf57188eabcd7d8cb0542eb47c'


headers = {'Cookie':'BAIDUID_BFESS=8A3A527F66D6DCD09ACA098B175B35D5:FG=1; MCITY=-179%3A; BIDUPSID=8A3A527F66D6DCD09ACA098B175B35D5; PSTM=1618113573; BAIDUID=38A1A5BDCFFAAAE2E8BCEE691D62CF43:FG=1; __yjs_duid=1_432ccb0c27473d07b901d45aedfa1f271619615500759; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BDRCVFR[Q5XHKaSBNfR]=mk3SLVN4HKm; BDUSS=9UcExGRH5OUGROcEVuSldzMDdTVEctZGZ5a2R-Rn5EbnJtS1JObjZhUmNYc05nSVFBQUFBJCQAAAAAAAAAAAEAAACGgrBZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFzRm2Bc0Ztga0; BDUSS_BFESS=9UcExGRH5OUGROcEVuSldzMDdTVEctZGZ5a2R-Rn5EbnJtS1JObjZhUmNYc05nSVFBQUFBJCQAAAAAAAAAAAEAAACGgrBZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFzRm2Bc0Ztga0; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; ab_sr=1.0.0_YzkwYTdkYjhlMDM4OGMzYTQ3MjFjZGFmZmMyNWRhNzZhYmEzYTE0OWVjYmI0YjNlYzU4ZTE1ZWIzZWQ1NGMyZTIyOWU2NzFmMTEwNTIyYjljNzBiMmUyYTMzZjBkMzkxMjUwZDBjM2M3MTEzODU0YjRlMDVhMTA2OTg2NGUwYTk=; __yjs_st=2_ZjkwMzFmNDBkYTE4ZWFiODlhNzE2MjQ2ZjZjMGE0MDQzYWI0ZDI1ZDIwNDYzMWFkNjExMmY3OThjYjMwYTJkNTRhMzYzM2VlMWYyZjIzZThmODA3ZGUzNWE0MDRmNGE0YTBlM2ZhZjc0NWY0OWIxZjllNzM3N2JlNzg5MWEyYzU0MmVlYzJjYjA5NzZkZDVkYzQyMmVkMTQwYzgxOTdjOTQ3MmE0ZGIyYzhkNmNmZGFjZjk3ZTE3OWFlOTM0NjcyYTFkNjIxZjFiN2JiOGY5MDhlZTg5NzgyODI1YTIxNzYwZDZlY2UwZGQ0ZDU2ODdlMWMyYzZkNjllMjExZDg1ZmZhOWRhNjI3NjYwMjRiNTZhZWJkZDRjNmYwZTY2MzYxXzdfNDkxNTBiZDU=',
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
}

q = input('翻译：')

js = '''var i = "320305.131321201"
function n(r, o) {
    for (var t = 0; t < o.length - 2; t += 3) {
        var a = o.charAt(t + 2);
        a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a), a = "+" === o.charAt(t + 1) ? r >>> a : r << a, r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
    }
    return r
}


function e(r) {
    var o = r.match(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g);
    if (null === o) {
        var t = r.length;
        t > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(t / 2) - 5, 10) + r.substr(-10, 10))
    } else {
        for (var e = r.split(/[\uD800-\uDBFF][\uDC00-\uDFFF]/), C = 0, h = e.length, f = []; h > C; C++) "" !== e[C] && f.push.apply(f, a(e[C].split(""))), C !== h - 1 && f.push(o[C]);
        var g = f.length;
        g > 30 && (r = f.slice(0, 10).join("") + f.slice(Math.floor(g / 2) - 5, Math.floor(g / 2) + 5).join("") + f.slice(-10).join(""))
    }
    var u = void 0, l = "" + String.fromCharCode(103) + String.fromCharCode(116) + String.fromCharCode(107);
    u = null !== i ? i : (i = window[l] || "") || "";
    for (var d = u.split("."), m = Number(d[0]) || 0, s = Number(d[1]) || 0, S = [], c = 0, v = 0; v < r.length; v++) {
        var A = r.charCodeAt(v);
        128 > A ? S[c++] = A : (2048 > A ? S[c++] = A >> 6 | 192 : (55296 === (64512 & A) && v + 1 < r.length && 56320 === (64512 & r.charCodeAt(v + 1)) ? (A = 65536 + ((1023 & A) << 10) + (1023 & r.charCodeAt(++v)), S[c++] = A >> 18 | 240, S[c++] = A >> 12 & 63 | 128) : S[c++] = A >> 12 | 224, S[c++] = A >> 6 & 63 | 128), S[c++] = 63 & A | 128)
    }
    for (var p = m, F = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(97) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(54)), D = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(51) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(98)) + ("" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(102)), b = 0; b < S.length; b++) p += S[b], p = n(p, F);
    return p = n(p, D), p ^= s, 0 > p && (p = (2147483647 & p) + 2147483648), p %= 1e6, p.toString() + "." + (p ^ m)
}
'''
sign = execjs.compile(js).call("e",q)

From = 'zh'
to = 'en'


key = {
'from': From,
'to': to,
'query': q,
'transtype': 'realtime',
'simple_means_flag': '3',
'sign': sign,
'token': '76444dbf57188eabcd7d8cb0542eb47c',
# 'domain': 'common',
}



url = 'https://fanyi.baidu.com/v2transapi'

response = requests.post(url=url,headers=headers,data=key).json()['trans_result']['data'][0]['dst']      #['dict_result']['synthesize_means']['symbols'][0]['cys'][0]['means'][0]['word_mean']

# print(type(response))
# print(len(response))

# trans = response[0]#.find('word_mean')
# print(trans)



# for item in response.items():
#     print(item)


print(response)


