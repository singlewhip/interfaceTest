import sys
sys.path.append('../')
from base.runmethod import RunMethod
from operation_data.get_data import GetData
from tool.common_util import CommonUtil
from operation_data.dependent import DependentData
from tool.send_email import SendEmail
from tool.operation_header import OperationHeader
from tool.operation_json import OperationJson
from tool.operation_excle import OperationExcle
from base import HTMLTestRunner
import time
from tool.operation_testReport_excle import Write_testReport_excle
import os

class RunTest:
    def __init__(self):
        path = '../dataCase'
        for test_list in os.listdir(path):
            # print(test_list)
            file_address = path + '/' + test_list
            sheet_id = 0
            self.ope=OperationExcle(file_address,sheet_id)
        # self.ope=OperationExcle()
        self.run_method=RunMethod()
        self.data=GetData()
        self.com_util=CommonUtil()
        self.send_mail=SendEmail()
        self.op_testReport=Write_testReport_excle()
    #程序执行
    def go_on_run(self):
        global pass_count,fail_count
        res=None
        pass_count=[]
        fail_count=[]
        rows_count=self.data.get_case_line()
        for i in range(1,rows_count):
            is_run=self.data.get_is_run(i)
            # print(is_run)
            if is_run:
                url=self.data.get_url(i)
                method=self.data.get_request_method(i)
                request_data=self.data.request_data_type_change(i)
                # print(request_data)
                expect=self.data.get_expect_data(i)
                # print(type(expect))
                header=self.data.is_header(i)
                # print(header)
                depent_case=self.data.is_depend(i)
                # print(str(url)+str(method)+str(request_data)+str(expect)+str(header))
                # if depent_case!=None:
                #     self.depent_data=DependentData(depent_case)
                #     #获取依赖响应数据
                #     depent_resonse_data=self.depent_data.get_data_for_key(i)
                #     #获取依赖key
                #     depent_key=self.data.get_depend_field(i)
                # if header=='wrire':
                #     res=self.run_method.run.main(method,url,request_data)
                #     op_header=OperationHeader(res)
                #     op_header.get_header()
                #
                # elif header=='yes':
                #     op_json=OperationJson('../dataconfig/test.json')
                #     cookie=op_json.get_data('Add_guest_one')
                #     cookies={'Add_guest_one':cookie}
                #     res=self.run_method.run_main(method,url,request_data)
                # else:
                res=self.run_method.run_main(method,url,request_data,header)
                if self.com_util.is_contain(expect,res)==True:
                    self.data.write_result(i,'pass')
                    print("测试通过")
                    pass_count.append(i)
                else:
                    self.data.write_result(i,'faild')
                    fail_count.append(i)
                    print("测试失败")
                # print(self.com_util.is_contain(expect,res)==True)
                print(res)
    #发送邮件、生成测试报告
    def create_test_report(self):
        self.op_testReport.write_TestReport(pass_count,fail_count) #生成excel表格测试报告
        self.op_testReport.excle_to_html() #将测试报告转换为html输出
        self.send_mail.send_main(pass_count,fail_count) #发送测试报告邮件

if __name__=='__main__':
    run=RunTest()
    run.go_on_run()
    run.create_test_report()

    # now=time.strftime("%Y-%m-%d %H-%M-%S") #获取当前时间
    # file_path='../report/'+now+'result.html'
    # fp=open(file_path,'wb')
    # runner=HTMLTestRunner.HTMLTestRunner(stream=fp, title='Testresult')  # 定义运行方法（定义变量与unittest结合）
    # fp.close()




