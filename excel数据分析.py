import  pandas

#sheet_name表示工作表名称
data = pandas.read_excel('E:\牧原\牧原\项目方案\智能冷冻冷藏项目-3代厂\立体库三代方案\效率需求测算\\2021.12.1内乡厂冻品库库存V1 - 副本.xlsx',sheet_name=0,header=1)
# print(type(data))

#输出前几行，为空默认为5行
print(data.head(3))

# 输出某一个单元格内容 第一个表示行，第二个表示列
# print(data.iloc[3][5])

#把某一行输出出来
# for i in data.iloc[0]:
#     print(i)

#根据行标签输出该行内容
# print(data.loc[0])

#输出多行数据
# print(data.loc[[0,1]])

#根据列标签输出该列内容
# print(data[0])

#根据列标签输出两列内容
# print(data[[0,5]])


# a = data['数量']<2
# print(data[a]['数量'])