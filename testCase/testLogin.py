#Author:Mr.Qin
from operation_data.get_data import GetData
from tool.operation_excle import OperationExcle
from tool.common_util import CommonUtil
from base.runmethod import RunMethod

class login():
    def __init__(self):
        self.Opexl=OperationExcle('../dataCase/login.xls',0)
        self.data=GetData()
        self.com_util = CommonUtil()
        self.run_method = RunMethod()
    def test_Login(self):
        rownums=self.data.get_case_line()
        for i in range(1,rownums):
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
                res = self.run_method.run_main(method, url, request_data, header)
                if except_str is False:
                    if self.com_util.is_contain(expect, res) == True:
                        self.data.write_result(i, 'pass')
                        print("测试通过")
                    else:
                        self.data.write_result(i, 'Filed')
                        print('测试失败')
                # print(res)

                if except_str is True:
                    if self.com_util.is_equal_dict(expect, res) == True:  # 判断字典是否相等
                        self.data.write_result(i, 'pass')
                        print('测试通过')
                    else:
                        self.data.write_result(i, res)
                        print('测试失败')
                print(res)
            else:
                pass

            # print(self.com_util.is_contain(expect,res)==True)

if __name__=='__main__':

    login_test=login()
    login_test.test_Login()
    # print(login_test.test_Login())
