#Author:Mr.Qin
import xlrd
from xlutils.copy import copy
# -*- coding: utf8 -*-
#读取testcase excel文件，获取测试数据，调用interfaceTest方法，将结果保存至errorCase列表中。
import xlrd
from xlutils.copy import copy

from common.interfaceTest import *


def loadDatas(self, file_address, sheetid):
      #testCaseFile = os.path.join(os.getcwd(),testCaseFile)
      if not file_address:
          print ('测试用例文件不存在！')
          #sys.exit()
      testCase = xlrd.open_workbook(file_address)    #打开excel
      table = testCase.sheet_by_name(sheetid)    #通过名称定位excel的表格
      # errorCase = []                #用于保存接口返回的内容和HTTP状态码
      wb = copy(testCase)
      wtable = wb.get_sheet(sheetid)
      results = []
      s = None
      for i in range(1,table.nrows):
            # a = []   #用来存一条测试用例
            if table.cell(i, 10).value.replace('\n','').replace('\r','') != 'Yes':
                continue
            num = str(int(table.cell(i, 0).value)).replace('\n','').replace('\r','')
            api_purpose = table.cell(i, 1).value.replace('\n','').replace('\r','')
            api_host = table.cell(i, 2).value.replace('\n','').replace('\r','')
            request_url = table.cell(i, 3).value.replace('\n','').replace('\r','')
            request_method = table.cell(i, 4).value.replace('\n','').replace('\r','')
            request_data_type = table.cell(i, 5).value.replace('\n','').replace('\r','')
            header_data = table.cell(i, 6).value.replace('\n','').replace('\r','')
            #header_data = str(table.cell(i, 6).value)
            request_data = table.cell(i, 7).value.replace('\n','').replace('\r','')
            encryption = table.cell(i, 8).value.replace('\n','').replace('\r','')
            check_point = table.cell(i, 9).value

            print ('\n' + num + ' ' + api_purpose + '\n')   # 打印用例标题
            #print (header_data)
            # print("传入的参数：")
            # print(num, api_purpose, api_host, request_url, request_method,request_data_type,header_data,request_data, encryption, check_point)
            # print(header_data)
            '''
            if encryption == 'MD5':              #如果数据采用md5加密，便先将数据加密
                request_data = json.loads(request_data)
                request_data['pwd'] = md5Encode(request_data['pwd'])
            '''
            status, resp, s, result = interfaceTest(num, api_purpose, api_host,request_url, request_method,request_data_type, header_data,request_data,encryption,check_point, s)
            #if status != 200 or check_point not in resp:            #如果状态码不为200或者返回值中没有检查点的内容，那么证明接口产生错误，保存错误信息。
                #errorCase.append(num + ' ' + api_purpose +  str(status) + 'http://'+api_host+request_url +  resp)

            with self.subTest(data=result):   # 注意subTest的用法 多条数据会分成多条运行结果
                  self.assertEqual(result, "pass")

            if result == "fail":   #如果失败，把结果写回excel
                  wtable.write(i, 11, "fail!" + ' ' + str(status) + "返回数据：" + resp)
                  wb.save(file_address)
            else:
                  wtable.write(i, 11, "pass!")
                  wb.save(file_address)

            results.append(result)
      return results    #返回结果