import sys
sys.path.append('../')
from tool.operation_excle import OperationExcle
from tool.operation_json import OperationJson
from operation_data import data_config
from tool.data_type_change import TypeChange
import json
from tool.Mysql_connect import Mysql_operation
import os

class GetData():
    def __init__(self):
        # path='../dataCase'
        # for test_list in os.listdir(path):
        #     # print(test_list)
        #     file_address = path + '/' + test_list
        #     sheet_id=0
        #     # self.file_address = file_address
        #     # self.sheet_id = sheet_id
        #     self.opera_excle=OperationExcle(file_address,sheet_id)
        self.opera_excle=OperationExcle()
    #获取excle行数，就是用例数
    def get_case_line(self):
       return self.opera_excle.get_lines()

    #获取是否执行
    def get_is_run(self, row: object) -> object:
        flag=None
        col=int(data_config.get_run())
        run_model=self.opera_excle.get_cell_value(row,col)
        # print(run_model)
        if run_model=='yes':
            flag=True
        elif run_model=='是否执行':
            pass
        else:
            flag=False
        return flag
    #是否携带header
    def is_header(self,row):
        col=int(data_config.get_header())
        header=self.opera_excle.get_cell_value(row,col)
        if header=='NoToken' or header=='':
            return data_config.get_header_no_token()
        elif header=='appToken':
            return data_config.get_header_value_token()
        else:
            return "header填写错误"

    #改变header数据类型，xlsxwriter模块写入数据是需要将数据类型为str
    def get_str_header(self,row):
        col=int(data_config.get_header())
        header=self.opera_excle.get_cell_value(row,col)
        return str(header)
    #获取请求url名称
    def get_request_name(self,row):
        col=int(data_config.get_request_name())
        request_name=self.opera_excle.get_cell_value(row,col)
        if request_name!='':
            print('请求url:'+request_name)
        else:
            return None
        return request_name
    #获取请求方式
    def get_request_method(self,row):
        col = int(data_config.get_request_method())
        request_method = self.opera_excle.get_cell_value(row, col)
        return request_method
    #获取URL
    def get_url(self,row):
        col = int(data_config.get_url())
        url = self.opera_excle.get_cell_value(row,col)
        return url
    #获取请求数据
    def get_request_data(self,row):
        col = int(data_config.get_data())
        data = self.opera_excle.get_cell_value(row, col)
        # if data == "":
        #     return None
        return data
    #更改请求数据类型
    def request_data_type_change(self,row):
        ty_ch=TypeChange()
        ch_data=ty_ch.data_change(self.get_request_data(row))
        interface_fabuhui_address="http://127.0.0.1:8000"
        if interface_fabuhui_address in self.get_url(row):
            return ch_data
        else:
            return json.dumps(ch_data)
    # #通过获取关键字拿到data数据
    # def get_data_for_json(self,row):
    #     opear_json=OperationJson()
    #     request_data=opear_json.get_data(self.get_request_data(row))
    #     return request_data
    #获取预期结果
    def get_expect_data(self,row):
        col=int(data_config.get_expect())
        expect=self.opera_excle.get_cell_value(row,col)
        # if expect=='':
        #     return None
        return expect

    #根据sql获取预期结果
    def get_sql_expect_data(self,row):
        sql=int(data_config.get_expect(row))
        My_op=Mysql_operation()
        sql_except=My_op.sql_select(sql)[0]
        return sql_except

    #写入实际结果
    def write_result(self, row, value):
        col=int(data_config.get_result())
        # result=self.opera_excle.write_value(row,col,value)
        self.opera_excle.write_value(row, col, value)

    #获取实际结果
    def get_result(self, row):
        col=int(data_config.get_result())
        result=self.opera_excle.get_cell_value(row,col)
        return result
    
    
    #获取依赖数据的key
    def get_depent_key(self,row):
        col=int(data_config.get_data_depend())
        depent_key=self.opera_excle.get_cell_value(row,col)
        if depent_key=='':
            return None
        else:
            return depent_key
    #判断是否有case的依赖
    def is_depend(self,row):
        col=int(data_config.get_case_dapend())
        depend_case_id=self.opera_excle.get_cell_value(row,col)
        if depend_case_id=='':
            return None
        else:
            return depend_case_id
    #获取数据依赖字段
    def get_depend_field(self,row):
        col=int(data_config.get_field_depend())
        data=self.opera_excle.get_cell_value(row,col)
        if data=='':
            return None
        else:
            return data

if __name__=='__main__':
    Gd=GetData()
    lins=Gd.get_case_line()
    for a in range(1,lins):
        print(Gd.get_is_run(a))
