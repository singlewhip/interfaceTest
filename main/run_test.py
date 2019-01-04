import sys
sys.path.append('../')

from base.runmethod import RunMethod
from operation_data.get_data import GetData
from tool.common_util import CommonUtil
from operation_data.dependent import DependentData
from tool.send_email import SendEmail
from tool.operation_testReport_excle import Write_testReport_excle
import os


class RunTest:
    def __init__(self):
        # self.ope=OperationExcle()
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.send_mail = SendEmail()
        self.op_testReport = Write_testReport_excle()

    # 程序执行
    def go_on_run(self):
        global pass_count, fail_count
        res = None
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_line()
        # print(rows_count)
        for i in range(1, rows_count):
            is_run = self.data.get_is_run(i)
            # print(is_run)
            url = self.data.get_url(i)
            # print(url)
            method = self.data.get_request_method(i)
            request_data = self.data.request_data_type_change(i)
            # print(request_data)
            expect = self.data.get_expect_data(i)
            # print(expect)
            header = self.data.is_header(i)
            select_str = 'select'
            insert_str = 'INSERT'
            update_str = 'UPDATE'
            delete_str = 'DELETE'
            for except_num in select_str, insert_str, update_str, delete_str:
                except_str = self.com_util.is_contain(except_num, expect)
                if except_str is True:
                    expect = self.data.get_sql_expect_data(i)
                else:
                    expect = self.data.get_expect_data(i)
            # print(expect)

            if is_run is True:
                res = self.run_method.run_main(
                    method, url, request_data, header)
                if except_str is False:
                    if self.com_util.is_contain(expect, res) == True:
                        self.data.write_result(i, 'pass')
                        print("测试通过")
                        pass_count.append(i)
                    else:
                        self.data.write_result(i, 'Filed')
                        print('测试失败')
                        fail_count.append(i)
                # print(res)

                if except_str is True:
                    if self.com_util.is_equal_dict(expect, res) == True:  # 判断字典是否相等
                        self.data.write_result(i, 'pass')
                        pass_count.append(i)
                        print('测试通过')
                    else:
                        self.data.write_result(i, res)
                        print('测试失败')
                        fail_count.append(i)

            else:
                pass
            print(res)
            # print(self.com_util.is_contain(expect,res)==True)

    # 发送邮件、生成测试报告
    def create_test_report(self):
        self.op_testReport.write_TestReport(pass_count, fail_count)  # 生成excel表格测试报告
        self.op_testReport.excle_to_html()  # 将测试报告转换为html输出
        self.send_mail.send_main(pass_count, fail_count)  # 发送测试报告邮件


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()
    run.create_test_report()

    # now=time.strftime("%Y-%m-%d %H-%M-%S") #获取当前时间
    # file_path='../report/'+now+'result.html'
    # fp=open(file_path,'wb')
    # runner=HTMLTestRunner.HTMLTestRunner(stream=fp, title='Testresult')  # 定义运行方法（定义变量与unittest结合）
    # fp.close()
