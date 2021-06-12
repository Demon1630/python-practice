from tkinter import INSERT
import requests
import execjs
import tkinter
from fake_useragent import UserAgent
import keyboard

#定义翻译函数
class Translate:
    def get_result(self,to_trans,From,To):
        self.headers = {'Connection': 'keep-alive',
                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'Cookie': 'BAIDUID_BFESS=8A3A527F66D6DCD09ACA098B175B35D5:FG=1; MCITY=-179%3A; BIDUPSID=8A3A527F66D6DCD09ACA098B175B35D5; PSTM=1618113573; BAIDUID=38A1A5BDCFFAAAE2E8BCEE691D62CF43:FG=1; __yjs_duid=1_432ccb0c27473d07b901d45aedfa1f271619615500759; BDUSS=9UcExGRH5OUGROcEVuSldzMDdTVEctZGZ5a2R-Rn5EbnJtS1JObjZhUmNYc05nSVFBQUFBJCQAAAAAAAAAAAEAAACGgrBZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFzRm2Bc0Ztga0; BDUSS_BFESS=9UcExGRH5OUGROcEVuSldzMDdTVEctZGZ5a2R-Rn5EbnJtS1JObjZhUmNYc05nSVFBQUFBJCQAAAAAAAAAAAEAAACGgrBZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFzRm2Bc0Ztga0; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_PREFER_SWITCH=1; SOUND_SPD_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1621513227,1621513236; ab_sr=1.0.0_MDY1YzM4ZDc5NWMxZGY5ZjQzZmM3ZGNlNzhkNTNiM2FiYTk1MDM0ODUzNjVhMjI3YWU0NjUwMzkwNGZmM2M0NTQ3M2VmNGViYjAyZTFjMDllNzhlNjQ1MjdkOGQ5NDU4NjA1ZTczYzMwNjczNGU3MGMyNDMxZWE2NDY3MWZlYTI=; __yjs_st=2_ZjkwMzFmNDBkYTE4ZWFiODlhNzE2MjQ2ZjZjMGE0MDQwZDAzZmIyM2MzZmQ2NjIyYzE2MGZkMzE1Zjg3ZDQ2NTkyOTIxYmZkZmRmZTExMWEwM2FjMzM0ZTMzODNkNGJhMzNlN2JhNTdkZDBiYjcwNTFmY2Y3ZDk4MDZlMTZkZjZkNmVmNzljZGY1MGUwMWNiNGFmNjQxZmIzODIxYTAxOWM0ZDM5NmUwYWQxNTYyOWJkNzhkZGUwZDQ4MjRhYjBkMzRhNzA1ZDhkN2E3NDg5ODYyZDE5ZmY1YzdkYzI1NGQxNWRmOGVkZDc0NzhkODYxNjZjZjZlMWE2ZDM5Nzg4NDBlZGVlNWQ4OGVmNDViZTNlZGUyZWRkN2JlMTk4ZTIyXzdfYmU1MDQwMTM=',
                        'User-Agent':UserAgent().random,
        }

#定义sign计算过程
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
    

    '''

        self.url = 'https://fanyi.baidu.com/v2transapi'

        self.From = From
        self.To = To
        self.token= '76444dbf57188eabcd7d8cb0542eb47c'
        self.q = to_trans

        # q = input('翻译：')
        self.sign = execjs.compile(self.js).call("e",self.q)
        self.data = {'from':self.From,
        'to':self.To,
        'query':self.q,
        'sign':self.sign,

        'token':self.token}

        self.text = requests.post(self.url,headers=self.headers,data=self.data).json()#['trans_result']['data'][0]['dst']
        # print(self.text)
        print(self.sign)
        return self.text



class Trans_GUI:
    def __init__(self):

        #创建主窗口
        self.main_window = tkinter.Tk()

        #修改标题与窗口大小
        self.main_window.title('翻译')
        self.main_window.geometry('1000x400')

        #创建两个frame模块
        self.mid_f_frame = tkinter.Frame(self.main_window) #放输入文本
        self.mid_r_frame = tkinter.Frame(self.main_window) #显示翻译后文本，左右放置

        #定义提示输入标签
        self.show_label = tkinter.Label(self.mid_f_frame,text = '待翻译内容',bg = 'green')

        #定义用于显示结果的标签
        self.m1 = tkinter.Label(self.mid_r_frame, text='百度翻译结果：')


        #定义一个标签来接收计算后结果
        self.K_label = tkinter.Text(self.mid_r_frame,width=70,height=20,wrap='word')  #采用Text窗格显示结果，和输入一样，可以自动换行 使用wrap = ’word‘，可以使单词不被换行

        #定义输入窗格
        self.input_window = tkinter.Text(self.mid_f_frame,width=70,height=20)   #使用Text函数，可以自动换行，用于输入多行文本

        #定义按钮
        # self.calc_button = tkinter.Button(self.main_window,text = 'Convert',command = self.calculate,width = 10)
        self.quit_button = tkinter.Button(self.main_window,text = 'quit',command = self.main_window.destroy,width = 10,bg= 'red')  #退出窗口
        self.zh_en_button = tkinter.Button(self.main_window,text = '中——》英',command = self.zh_en,width = 10) # 中文转英文
        self.en_zh_button = tkinter.Button(self.main_window,text='英——》中',command = self.en_zh,width = 10)  #英文转中文
        self.clear_button = tkinter.Button(self.main_window,text='clear',command = self.clear,width = 10)  #英文转中文

        #放置按钮
        # self.calc_button.place(x=200,y=365,width=100)   #使用place放置，采用绝对位置，但必须放置在主窗格中，不能放到frame，因为frame大小不固定
        self.quit_button.place(x=800,y=365,width=100)
        self.zh_en_button.place(x=200,y=365,width=100)
        self.en_zh_button.place(x=400,y=365,width=100)
        self.clear_button.place(x=600,y=365,width=100)

        #放置输入窗格与提示标签
        self.show_label.pack(side = 'top')
        self.input_window.pack(side = 'top')

        #放置中间显示结果的标签
        self.m1.pack(side='top')
        self.K_label.pack(side = 'top')


        #放置frame
        self.mid_f_frame.pack(side = 'left')
        self.mid_r_frame.pack(side = 'right')

        # self.main_window.bind("<Shift_L>", self.zh_en())

        tkinter.mainloop()
        # keyboard.add_hotkey('ctrl+enter', self.zh_en)
        # keyboard.add_hotkey('ctrl+enter', self.zh_en())
        # keyboard.wait('')



    def zh_en(self):
        self.From = 'zh'
        self.To = 'en'
        t = self.input_window.get(0.0,'end')  #get函数中，第一个参数0.0表示从第0行0列开始读取，end表示读取到最后字符串
        trans = Translate().get_result(t,self.From,self.To)
        self.K_label.delete('1.0','end')   #解决翻译内容添加问题，先清空
        self.K_label.insert(INSERT,trans)


    def en_zh(self):
        self.From = 'en'
        self.To = 'zh'
        t = self.input_window.get(0.0,'end')  #get函数中，第一个参数0.0表示从第0行0列开始读取，end表示读取到最后字符串
        trans = Translate().get_result(t,self.From,self.To)
        self.K_label.delete('1.0','end')   #解决翻译内容添加问题，先清空
        self.K_label.insert(INSERT,trans)

    def clear(self):
        self.K_label.delete('1.0','end')
        self.input_window.delete('1.0','end')


    #     #定义转换函数
    # def calculate(self):
    #     t = self.input_window.get(0.0,'end')  #get函数中，第一个参数0.0表示从第0行0列开始读取，end表示读取到最后字符串
    #     trans = Translate().get_result(t)
    #     self.K_label.delete('1.0','end')   #解决翻译内容添加问题，先清空
    #     self.K_label.insert(INSERT,trans)


temperature_gui = Trans_GUI()
