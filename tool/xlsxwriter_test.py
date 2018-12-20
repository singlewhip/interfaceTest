from operation_data.get_data import GetData
import xlsxwriter
import time
import pandas
import codecs
import time

class Write_testReport_excle():
    global workbook,worksheet,chart,formatter,title_formatter,ave_formatter,now,filename
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    workbook=xlsxwriter.Workbook("../report/excle_report/" + now + '_test_report.xlsx')
    filename='../report/excle_report/' + now + '_test_report.xlsx'
    worksheet = workbook.add_worksheet("测试报告")
    # 创建一个图表对象,column:柱形图
    chart = workbook.add_chart({'type': 'column'})

    def __init__(self):
        self.data=GetData()
    def create_TestReport(self):
        #设置列宽为20
        worksheet.set_column("A:ZZ",20)
        # 定义标题栏格式对象：边框加粗1像素，背景色为灰色，单元格内容居中、加粗，自动换行
        formatter = workbook.add_format()
        formatter.set_border(1)
        formatter.set_text_wrap()
        title_formatter = workbook.add_format()
        title_formatter.set_border(1)
        title_formatter.set_bg_color('#cccccc')
        title_formatter.set_align('center')
        title_formatter.set_bold()
        title_formatter.set_text_wrap()
        title = ['系统名称', '通过接口个数', '失败接口个数', '全部接口个数', '测试通过率', '测试失败率']
        buname = ['SCM3.0', '居家小二app', '发货宝', '运营后台系统', '直营oms系统']
        worksheet.write_row("A1",title,title_formatter)
        worksheet.write_column("A2", buname, formatter)
    def write_TestReport(self,pass_list,fail_list):
        pass_num=float(len(pass_list))
        fail_num=float(len(fail_list))
        all_num=pass_num+fail_num
        pass_result = "%.2f%%" % (pass_num / all_num * 100)
        fail_result = "%.2f%%" % (fail_num / all_num * 100)
        data = [[pass_num, fail_num, all_num, pass_result, fail_result],
                [pass_num, fail_num, all_num, pass_result, fail_result],
                [pass_num, fail_num, all_num, pass_result, fail_result],
                [pass_num, fail_num, all_num, pass_result, fail_result],
                [pass_num, fail_num, all_num, pass_result, fail_result]
                ]
        # 定义标题栏格式对象：边框加粗1像素，背景色为灰色，单元格内容居中、加粗,自动换行
        formatter = workbook.add_format()
        formatter.set_border(1)
        formatter.set_text_wrap()
        # 写入第2到第6行的数据，并将第2~6行数据加入图表系列
        for i in range(2, 7):
            worksheet.write_row('B{}'.format(i), data[i - 2],formatter)
        self.create_TestReport()
        workbook.close()
    def excle_to_html(self):
        # 注意这里不能直接使用workbook,因为直接引用workbook返回的对象不是一个文件路径，而是:<class 'xlsxwriter.workbook.Workbook'>
        fp=pandas.ExcelFile(filename)
        df=fp.parse()
        with codecs.open('../report/html_report/'+now+'_test_report.html', 'w', 'utf-8') as html_file:
            html_file.write(df.to_html(header=True, index=False))

if __name__=="__main__":
    wte=Write_testReport_excle()
    wte.write_TestReport([1,2,3],[2,3,4,5])
    wte.excle_to_html()