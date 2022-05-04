import pandas
muyuan = pandas.read_csv('E:\python学习\零基础学python爬虫、数据分析\数据处理练习\效率需求测算\muyuan.csv',index_col='date',parse_dates=['date'])
#将data列作为行标签，并将该列数据转换为date（日期）类型
print(muyuan)