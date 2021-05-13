import requests
import execjs
import tkinter
from fake_useragent import UserAgent


class Translate:
    # def __init__(self):
    #     self.q=''
    def get_result(self,to_trans):
        self.headers = {'Cookie':'BAIDUID_BFESS=8A3A527F66D6DCD09ACA098B175B35D5:FG=1; MCITY=-179%3A; BIDUPSID=8A3A527F66D6DCD09ACA098B175B35D5; PSTM=1618113573; BAIDUID=38A1A5BDCFFAAAE2E8BCEE691D62CF43:FG=1; __yjs_duid=1_432ccb0c27473d07b901d45aedfa1f271619615500759; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BDRCVFR[Q5XHKaSBNfR]=mk3SLVN4HKm; BDUSS=9UcExGRH5OUGROcEVuSldzMDdTVEctZGZ5a2R-Rn5EbnJtS1JObjZhUmNYc05nSVFBQUFBJCQAAAAAAAAAAAEAAACGgrBZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFzRm2Bc0Ztga0; BDUSS_BFESS=9UcExGRH5OUGROcEVuSldzMDdTVEctZGZ5a2R-Rn5EbnJtS1JObjZhUmNYc05nSVFBQUFBJCQAAAAAAAAAAAEAAACGgrBZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFzRm2Bc0Ztga0; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; ab_sr=1.0.0_YzkwYTdkYjhlMDM4OGMzYTQ3MjFjZGFmZmMyNWRhNzZhYmEzYTE0OWVjYmI0YjNlYzU4ZTE1ZWIzZWQ1NGMyZTIyOWU2NzFmMTEwNTIyYjljNzBiMmUyYTMzZjBkMzkxMjUwZDBjM2M3MTEzODU0YjRlMDVhMTA2OTg2NGUwYTk=; __yjs_st=2_ZjkwMzFmNDBkYTE4ZWFiODlhNzE2MjQ2ZjZjMGE0MDQzYWI0ZDI1ZDIwNDYzMWFkNjExMmY3OThjYjMwYTJkNTRhMzYzM2VlMWYyZjIzZThmODA3ZGUzNWE0MDRmNGE0YTBlM2ZhZjc0NWY0OWIxZjllNzM3N2JlNzg5MWEyYzU0MmVlYzJjYjA5NzZkZDVkYzQyMmVkMTQwYzgxOTdjOTQ3MmE0ZGIyYzhkNmNmZGFjZjk3ZTE3OWFlOTM0NjcyYTFkNjIxZjFiN2JiOGY5MDhlZTg5NzgyODI1YTIxNzYwZDZlY2UwZGQ0ZDU2ODdlMWMyYzZkNjllMjExZDg1ZmZhOWRhNjI3NjYwMjRiNTZhZWJkZDRjNmYwZTY2MzYxXzdfNDkxNTBiZDU=',
                   'User-Agent':UserAgent().random,
        }


        self.js = '''var i = "320305.131321201"
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

        self.url = 'https://fanyi.baidu.com/v2transapi'

        self.From = 'zh'
        self.To = 'en'
        self.token = '76444dbf57188eabcd7d8cb0542eb47c'
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
        self.main_window.geometry('800x300')

        #创建三个frame模块
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        #定义提示输入标签
        self.show_label = tkinter.Label(self.top_frame,text = '翻译内容（中文）',bg = 'green',font = ('Arial',12),width = 10 ,height = 1)

        #定义用于显示结果的标签
        self.mid_label = tkinter.Label(self.mid_frame,text =' 百度翻译结果：')

        #使用StringVar创建一个对象
        self.value = tkinter.StringVar()

        #定义一个标签来接收计算后结果
        self.K_label = tkinter.Label(self.mid_frame,textvariable = self.value)

        #定义输入窗格
        self.input_window = tkinter.Entry(self.top_frame,width = 80)

        #定义按钮
        self.calc_button = tkinter.Button(self.button_frame,text = 'Convert',command = self.calculate,width = 10)
        self.quit_button = tkinter.Button(self.button_frame,text = 'quit',command = self.main_window.destroy,width = 10,bg= 'red')


        #放置按钮
        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side = 'right')

        #放置输入窗格与提示标签
        self.show_label.pack(side = 'left')
        self.input_window.pack(side = 'right')

        #放置中间显示结果的标签
        self.mid_label.pack(side='left')
        self.K_label.pack(side = 'left')


        #放置frame
        self.top_frame.pack(side = 'top')
        self.mid_frame.pack(side = 'top')
        self.button_frame.pack(side = 'bottom')

        tkinter.mainloop()

        #定义转换函数
    def calculate(self):
        t = self.input_window.get()
        trans = Translate().get_result(t)

        # T = t + 273.15

        self.value.set(trans)
        # self.value =T   #必须用set函数赋值

        # tkinter.messagebox.showinfo('Response', f'{t}摄氏度是{T}开尔文')  # 显示信息 surprise

temperature_gui = Trans_GUI()
