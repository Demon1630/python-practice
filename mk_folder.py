import os


class Mk_folder():
    def __init__(self,folder_name):
        self.folder_name = 'C:/Users/Administrator/Desktop/'+folder_name

        #使用 exists 函数判断文件夹是否存在，如果存在则在后面加上两位数字
        i = 1

        #使用循环进行判断，如果加上数字后还存在，则重新加新数字，直到可以创建为止
        while os.path.exists(self.folder_name):
            self.folder_name = self.folder_name+str(i).zfill(2)
            i += 1

            if os.path.exists(self.folder_name):
                self.folder_name = self.folder_name[:-2]


        os.mkdir(self.folder_name)

# folder=Mk_folder('图片')
