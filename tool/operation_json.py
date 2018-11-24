import json

class OperationJson:
    #初始化文件
    def __init__(self,file_path=None):
        if file_path==None:
             self.file_path='../dataconfig/test.json'
        else:
             self.file_path=file_path
        self.data=self.read_data()
    def read_data(self):
        #with 语句适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作，释放资源，
        # 比如文件使用后自动关闭／线程中锁的自动获取和释放
        #读取json文件
        with open(self.file_path,encoding='utf-8') as fp:
            data=json.load(fp)
            return data
        #根据关键字获取数据
    def get_data(self,id=None):
        if id!=None:
            return self.data[id]
        else:
            return print('id不存在，请检查id是否填写正确')
        #写入json
    def write_data(self,data):
        with open('../dataconfig/test.json','w') as fp:
            fp.write(json.dumps(data))

if __name__ == '__main__':
    opjson=OperationJson()
    print(opjson.get_data('Add_guest_one'))
