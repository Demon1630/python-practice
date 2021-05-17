from tkinter import INSERT

import requests
import execjs
import tkinter
from fake_useragent import UserAgent


class Translate:
    # def __init__(self):
    #     self.q=''
    def get_result(self,to_trans):
        self.headers = {'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BAIDUID=779675DE60B7773D2B5ABC77906B7546:FG=1; BAIDUID_BFESS=779675DE60B7773D2B5ABC77906B7546:FG=1; BIDUPSID=779675DE60B7773D2B5ABC77906B7546; PSTM=1615268644; BDUSS=ld3RkJWaWt-UDFUSURtYzVoS1pYU1QtdWgyWDh3TWFWVXYxMnd5dEZsTHNoWDlnSVFBQUFBJCQAAAAAAAAAAAEAAADSm7VOZmZqZmdmZ2trAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOz4V2Ds-FdgU; BDUSS_BFESS=ld3RkJWaWt-UDFUSURtYzVoS1pYU1QtdWgyWDh3TWFWVXYxMnd5dEZsTHNoWDlnSVFBQUFBJCQAAAAAAAAAAAEAAADSm7VOZmZqZmdmZ2trAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOz4V2Ds-FdgU; __yjs_duid=1_dce50a1623bd207e0ed2c3170cf11d471620617963740; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1621089807,1621158773; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1621158773; __yjs_st=2_MDZmZWQyODMyOTAwMTk0NWVmYjQ2ZjVhNmU5MGJiOTlkMmNlMTdiNGFjMWMxNjg0YTdiYWU5ZjZmOGViYjU5NjY0ZWE4ODgzOTE4ZjY4MDE2OGJjMWU2ODRjYzZiMTBkOTlkZWZiOGM3MjBlZDA2YzRlNDNlZjhiNzVlOWI4NzQzNDBiYWNiOGQ2YjhkNjQ3YzljMmNmYTYxNWI3OWQ1OWIwOGFjOTFiNzExY2UxZjdjMDJmN2U3NmY4YTc1YzM2OGEyZTQ0ZmYzNGU4ZjIxNDI2NDQ1ODJkOWMyN2ZiNTZjZDkwNTc2NzliYzJjZDRkNzhjMDRlYjExMmEyMmQxYV83XzYzZDBiY2E4',
    'User-Agent':UserAgent().random,
        }


        self.js = '''
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

        self.url = 'https://fanyi.baidu.com/v2transapi'

        self.From = 'zh'
        self.To = 'en'
        self.token= '1cd6523421d1875e890a2aed45029ce2'
        self.q = to_trans

        # q = input('翻译：')
        self.sign = execjs.compile(self.js).call("e",self.q)
        self.data = {'from':self.From,
        'to':self.To,
        'query':self.q,
        'sign':self.sign,
        'token':self.token}

        self.text = requests.post(self.url,headers=self.headers,data=self.data).json()['trans_result']['data'][0]['dst']
        # print(self.text)
        return self.text


# trans = Translate().get_result('天气')
# # print(trans.get_result('天气'))
# print(trans)

class Trans_GUI:
    def __init__(self):

        #创建主窗口
        self.main_window = tkinter.Tk()

        #修改标题与窗口大小
        self.main_window.title('翻译')
        self.main_window.geometry('1000x400')

        #创建三个frame模块
        # self.top_frame = tkinter.Frame(self.main_window)
        self.mid_f_frame = tkinter.Frame(self.main_window) #放输入文本
        self.mid_r_frame = tkinter.Frame(self.main_window) #显示翻译后文本，左右放置
        # self.button_frame = tkinter.Frame(self.main_window)

        #定义提示输入标签
        self.show_label = tkinter.Label(self.mid_f_frame,text = '翻译内容（中文）',bg = 'green',font = ('Arial',12),width = 20 ,height = 1)

        #定义用于显示结果的标签
        # self.mid_label = tkinter.Label(self.mid_r_frame,text =' 百度翻译结果：')
        self.m1 = tkinter.Label(self.mid_r_frame, text='百度翻译结果：')   #使用Message，可以自动换行，用于显示多行文本

        #使用StringVar创建一个对象
        # self.value = tkinter.StringVar()

        #定义一个标签来接收计算后结果
        # self.K_label = tkinter.Message(self.mid_r_frame,textvariable = self.value)
        self.K_label = tkinter.Text(self.mid_r_frame,width=70,height=15,wrap='word')

        # self.K_label['state'] = 'disabled'

        #定义输入窗格
        self.input_window = tkinter.Text(self.mid_f_frame,width=70,height=15)   #使用Text函数，可以自动换行，用于输入多行文本
        # self.input_window.place(x=50,y=20,width=40,height = 10)

        #定义按钮
        self.calc_button = tkinter.Button(self.main_window,text = 'Convert',command = self.calculate,width = 10)
        self.quit_button = tkinter.Button(self.main_window,text = 'quit',command = self.main_window.destroy,width = 10,bg= 'red')


        #放置按钮
        # self.calc_button.pack(side = 'left')
        self.calc_button.place(x=200,y=350,width=100)
        # self.quit_button.pack(side = 'right')
        self.quit_button.place(x=600,y=350,width=100)

        #放置输入窗格与提示标签
        self.show_label.pack(side = 'top')
        self.input_window.pack(side = 'top')

        #放置中间显示结果的标签
        # self.mid_label.pack(side='left')
        self.m1.pack(side='top')
        self.K_label.pack(side = 'top')


        #放置frame
        # self.top_frame.pack(side = 'top')
        self.mid_f_frame.pack(side = 'left')
        self.mid_r_frame.pack(side = 'right')
        # self.button_frame.pack(side = 'bottom')

        tkinter.mainloop()

        #定义转换函数
    def calculate(self):
        t = self.input_window.get(0.0,'end')  #get函数中，第一个参数0.0表示从第0行0列开始读取，end表示读取到最后字符串
        print(t)
        trans = Translate().get_result(t)

        # T = t + 273.15

        self.K_label.insert(INSERT,trans)
        # self.value.set(trans)
        # self.value =T   #必须用set函数赋值

        # tkinter.messagebox.showinfo('Response', f'{t}摄氏度是{T}开尔文')  # 显示信息 surprise

temperature_gui = Trans_GUI()
