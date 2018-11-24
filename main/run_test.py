import sys
sys.path.append('../')
from base.runmethod import RunMethod
from operation_data.get_data import GetData
from tool.common_util import CommonUtil
from operation_data.dependent import DependentData
from tool.send_email import SendEmail
from tool.operation_header import OperationHeader
from tool.operation_json import OperationJson
from base import HTMLTestRunner
import time

class RunTest:
    def __init__(self) :
        self.run_method=RunMethod()
        self.data=GetData()
        self.com_util=CommonUtil()
        self.send_mail=SendEmail()
    #程序执行
    def go_on_run(self):
        global res
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
                request_data=self.data.get_data_for_json(i)
                expect=self.data.get_expect_data(i)
                print(expect)
                header=self.data.is_header(i)
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
                if self.com_util.is_contain(expect,res)==0:
                    self.data.write_result(i,'pass')
                    print("测试通过")
                    pass_count.append(i)
                else:
                    self.data.write_result(i,'faild')
                    fail_count.append(i)
                    print("测试失败")
                print(res)
        # self.send_mail.send_main(pass_count,fail_count)
if __name__=='__main__':
    run=RunTest()
    run.go_on_run()

    # now=time.strftime("%Y-%m-%d %H-%M-%S") #获取当前时间
    # file_path='../report/'+now+'result.html'
    # fp=open(file_path,'wb')
    # runner=HTMLTestRunner.HTMLTestRunner(stream=fp, title='Testresult')  # 定义运行方法（定义变量与unittest结合）
    # fp.close()




