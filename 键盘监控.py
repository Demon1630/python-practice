import keyboard  #监听键盘

def test_a():
    print('aaa')

def test(x):
    print(x)

if __name__ == '__main__':
    keyboard.add_hotkey('f1', test_a)
    #按f1输出aaa
    keyboard.add_hotkey('ctrl+alt', test, args=('b',))
    #按ctrl+alt输出b
    keyboard.wait('~')
    #wait里也可以设置按键，说明当按到该键时结束

