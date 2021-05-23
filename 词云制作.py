# import wordcloud
# w = wordcloud.WordCloud()
# w.generate('and that government of the people, by the people, for the people, shall not perish from the earth.')
# w.to_file('C:\\Users\\Administrator\\Desktop\\output1.png')




import wordcloud

# 从外部.txt文件中读取大段文本，存入变量txt中
f = open('C:\\Users\\Administrator\\Desktop\\novel\\第一章 身死 上.txt')
txt = f.read()

# 构建词云对象w，设置词云图片宽、高、字体、背景颜色等参数
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc')

# 将txt变量传入w的generate()方法，给词云输入文字
w.generate(txt)

# 将词云图片导出到当前文件夹
w.to_file('C:\\Users\\Administrator\\Desktop\\output2.png')