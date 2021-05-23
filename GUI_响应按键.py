import tkinter

win = tkinter.Tk()
win.title("xinghaohan")
win.geometry("400x400+200+20")

label = tkinter.Label(win, text="good good study", bg="red")
# 设置焦点
label.focus_set()
label.pack()


def func(event):
    print("event.char =", event.char)
    print("event.keycode =", event.keycode)


# <Shift_L> 左shift
# <Shift_R> 左shift
# <F5>
# <Return    回车
# <BackSpace>退格
label.bind("<Shift_L>", func)

win.mainloop()
