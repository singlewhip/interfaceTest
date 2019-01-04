import sys
sys.path.append('../')
from tool.common_util import CommonUtil

class TypeChange:
    def __init__(self):
        self.Cu=CommonUtil()
    def data_change(self,data):
        datas=self.Cu.is_contain("{",data)
        if datas==True:
            return eval(data)
        else:
            return data

if __name__=="__main__":
    op=TypeChange()
    str1='{"nihao":555}'
    print(type(str1))
    data=op.data_change(str1)
    print(type(data))