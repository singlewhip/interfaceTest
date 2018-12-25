import sys
import json
import os
sys.path.append("../../interfacetest_diy")
from tool.operation_excle import OperationExcle
from tool.operation_json import OperationJson
from base.runmethod import RunMethod
from operation_data.get_data import GetData
from jsonpath_rw import jsonpath,parse
#jsonpath_rw：接口自动化测试中，存在依赖情况：test_02的某个请求参数的值，需要依赖test_01返回结果中某个字段的数据，
# 所以就先需要拿到返回数据中特定字段的值

class DependentData:
    def __init__(self,case_id):
        self.case_id=case_id
        self.opera_excle=OperationExcle()
        self.data=GetData()
    #通过case_id去获取该case_id的整行数据
    def get_case_line_data(self):
        rows_data=self.opera_excle.get_rows_data(self.case_id)
        return rows_data
    #执行依赖测试，获取结果
    def run_dependent(self):
        run_method=RunMethod()
        row_num=self.opera_excle.get_row_num(self.case_id)
        # request_data=self.data.get_data_for_json(row_num)
        request_data = self.data.get_request_data(row_num)
        header=self.data.get_is_header(row_num)
        method=self.data.get_request_method(row_num)
        url=self.data.get_url(row_num)
        res=run_method.run_main(method,url,request_data,header)
        return json.loads(res)
    #根据依赖key去获取执行依赖测试case的响应，然后返回
    def get_data_for_key(self,row):
        depend_data=self.get_data_for_key(row)
        #response_data为依赖测试的执行结果
        response_data=self.run_dependent()
        #定义要获取的key
        json_exe=parse(depend_data)
        #定义响应数据,key从响应数据里获取
        madle=json_exe.find(response_data)
        #math.value返回的是一个list，可以使用索引访问特定的值jsonpath_rw的作用就相当于从json里面提取响应的字段值
        return [math.value for math in madle][0]
if __name__=='__main__':
    order = {"data":{"ser":"666","bn":"erre"}}
    #可以定义多个对象data.(_input_charset,subject),
    res = "data.(ser)"
    json_exe = parse(res)
    madle = json_exe.find(order)
    print([math.value for math in madle][::])