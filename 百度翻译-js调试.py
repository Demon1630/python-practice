# -*- coding: UTF-8 ...

import requests
import execjs
import tkinter
from fake_useragent import UserAgent


headers={
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BAIDUID=779675DE60B7773D2B5ABC77906B7546:FG=1; BAIDUID_BFESS=779675DE60B7773D2B5ABC77906B7546:FG=1; BIDUPSID=779675DE60B7773D2B5ABC77906B7546; PSTM=1615268644; BDUSS=ld3RkJWaWt-UDFUSURtYzVoS1pYU1QtdWgyWDh3TWFWVXYxMnd5dEZsTHNoWDlnSVFBQUFBJCQAAAAAAAAAAAEAAADSm7VOZmZqZmdmZ2trAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOz4V2Ds-FdgU; BDUSS_BFESS=ld3RkJWaWt-UDFUSURtYzVoS1pYU1QtdWgyWDh3TWFWVXYxMnd5dEZsTHNoWDlnSVFBQUFBJCQAAAAAAAAAAAEAAADSm7VOZmZqZmdmZ2trAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOz4V2Ds-FdgU; __yjs_duid=1_dce50a1623bd207e0ed2c3170cf11d471620617963740; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1621089807,1621158773; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1621158773; __yjs_st=2_MDZmZWQyODMyOTAwMTk0NWVmYjQ2ZjVhNmU5MGJiOTlkMmNlMTdiNGFjMWMxNjg0YTdiYWU5ZjZmOGViYjU5NjY0ZWE4ODgzOTE4ZjY4MDE2OGJjMWU2ODRjYzZiMTBkOTlkZWZiOGM3MjBlZDA2YzRlNDNlZjhiNzVlOWI4NzQzNDBiYWNiOGQ2YjhkNjQ3YzljMmNmYTYxNWI3OWQ1OWIwOGFjOTFiNzExY2UxZjdjMDJmN2U3NmY4YTc1YzM2OGEyZTQ0ZmYzNGU4ZjIxNDI2NDQ1ODJkOWMyN2ZiNTZjZDkwNTc2NzliYzJjZDRkNzhjMDRlYjExMmEyMmQxYV83XzYzZDBiY2E4',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
}


js = '''
    function a(r) {
        if (Array.isArray(r)) {
            for (var o = 0, t = Array(r.length); o < r.length; o++)
                t[o] = r[o];
            return t
        }
        return Array.from(r)
    }
    
    function n(r, o) {
        for (var t = 0; t < o.length - 2; t += 3) {
            var a = o.charAt(t + 2);
            a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a),
                a = "+" === o.charAt(t + 1) ? r >>> a : r << a,
                r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
        }
        return r
    }
    
    function e(r) {
        var o = r.match(/[\\uD800-\\uDBFF][\\uDC00-\\uDFFF]/g);
        if (null === o) {
            var t = r.length;
            t > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(t / 2) - 5, 10) + r.substr(-10, 10))
        } else {
            for (var e = r.split(/[\\uD800-\\uDBFF][\\uDC00-\\uDFFF]/), C = 0, h = e.length, f = []; h > C; C++)
                "" !== e[C] && f.push.apply(f, a(e[C].split(""))),
                C !== h - 1 && f.push(o[C]);
            var g = f.length;
            g > 30 && (r = f.slice(0, 10).join("") + f.slice(Math.floor(g / 2) - 5, Math.floor(g / 2) + 5).join("") + f.slice(-10).join(""))
        }
    //        var u = void 0
    //          , l = "" + String.fromCharCode(103) + String.fromCharCode(116) + String.fromCharCode(107);
    //        u = null !== i ? i : (i = window[l] || "") || "";
    
    
    //# u = null !== i ? i : (i = window[l] || "") || "";下面定义了var i=null;
    // # null !== i 为假，执行(i = window[l] || "")，结果为320305.131321201
    // # 这里多次运行发现window[1]是一个固定值：320305.131321201,(直接替换，调用js就可以得到结果了)，
    // #  简化成u= false ? : null : 320305.131321201 || "",最后u=320305.131321201是一个固定值
    
        var u = '320305.131321201';
        for (var d = u.split("."), m = Number(d[0]) || 0, s = Number(d[1]) || 0, S = [], c = 0, v = 0; v < r.length; v++) {
            var A = r.charCodeAt(v);
            128 > A ? S[c++] = A : (2048 > A ? S[c++] = A >> 6 | 192 : (55296 === (64512 & A) && v + 1 < r.length && 56320 === (64512 & r.charCodeAt(v + 1)) ? (A = 65536 + ((1023 & A) << 10) + (1023 & r.charCodeAt(++v)),
                S[c++] = A >> 18 | 240,
                S[c++] = A >> 12 & 63 | 128) : S[c++] = A >> 12 | 224,
                S[c++] = A >> 6 & 63 | 128),
                S[c++] = 63 & A | 128)
        }
        for (var p = m, F = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(97) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(54)), D = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(51) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(98)) + ("" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(102)), b = 0; b < S.length; b++)
            p += S[b],
                p = n(p, F);
        return p = n(p, D),
            p ^= s,
        0 > p && (p = (2147483647 & p) + 2147483648),
            p %= 1e6,
        p.toString() + "." + (p ^ m)
    }
    
    var i = null;
    '''


q = input('翻译:')
sign = execjs.compile(js).call("e",q)
print(sign)

token= '1cd6523421d1875e890a2aed45029ce2'

url = 'https://fanyi.baidu.com/v2transapi'

key ={
    'from': 'zh',
    'to': 'en',
    'query': q,
    'transtype': 'translang',
    'simple_means_flag': '3',
    'sign': sign,
    'token': token,
    'domain': 'common',
}

respons = requests.post(url = url,headers=headers,data=key).json()['trans_result']['data'][0]['dst']

print(type(respons))
print(respons)

