from tool.operation_excle import OperationExcle
from operation_data.get_data import GetData
import xlsxwriter
import pandas
import codecs
import time

class Write_testReport_excle():
    global workbook,worksheet,chart,formatter,title_formatter,ave_formatter,now,filename
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    workbook=xlsxwriter.Workbook("../report/excle_report/" + now + '_test_report.xls')
    filename='../report/excle_report/' + now + '_test_report.xls'
    worksheet = workbook.add_worksheet("测试报告")
    # 创建一个图表对象,column:柱形图
    chart = workbook.add_chart({'type': 'column'})

    # # 定义平均值栏数据格式对象：边框加粗1像素，数字按2位小数显示
    # ave_formatter = workbook.add_format()
    # ave_formatter.set_border(1)
    # ave_formatter.set_num_format('0.00')
    def __init__(self):
        # self.Ope=OperationExcle()
        self.data=GetData()
        # self.workbook=workbook
        # self.worksheet=worksheet
    def create_TestReport(self):
        worksheet.set_column("A:ZZ",20)
        # bold = workbook.add_format({"bold": True})
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
        #添加柱形图
        list1=('B','C','D')
        for row_num in list1:
            chart.add_series({
            "name":"=测试报告!$B$1",
            "categories":"=测试报告!$A$2:$A$6",
            "values":"=测试报告!${}$2:${}$6".format(row_num,row_num)
            })
        # 添加柱状图标题
        chart.set_title({"name": "各个系统接口测试报告"})
        # Y轴名称
        chart.set_y_axis({"name": "接口数量明细"})
        # X轴名称
        chart.set_x_axis({"name": "系统名称"})
        # 图表样式
        chart.set_style(10)
        #设置图表大小
        chart.set_size({'width': 600, 'height': 400})
        # 插入图表带偏移
        worksheet.insert_chart('G2', chart, {'x_offset': 25, 'y_offset': 10})
        # 定义标题栏格式对象：边框加粗1像素，背景色为灰色，单元格内容居中、加粗,自动换行
        formatter = workbook.add_format()
        formatter.set_border(1)
        formatter.set_text_wrap()
        # 写入第2到第6行的数据，并将第2~6行数据加入图表系列
        for i in range(2,7):
            worksheet.write_row('B{}'.format(i), data[i - 2],formatter)
        self.create_TestReport()
        self.write_faild_to_excle()
        # workbook.close()
    def write_faild_to_excle(self):
        rows_count=self.data.get_case_line()
        #定义标题栏格式对象：边框加粗1像素，背景色为灰色，单元格内容居中、加粗,自动换行
        formatter = workbook.add_format()
        formatter.set_border(1)
        formatter.set_font_color('red')
        formatter.set_text_wrap()
        # for i in range(1,rows_count):
        #     #将失败的用例写入测试报告中
        #     if not self.data.get_result(i)=='pass':
        #         # print(self.Ope.get_row_values(i))
        #         # print(self.data.get_result(i))
        #         worksheet.write_row('A{}'.format(i+8), self.Ope.get_row_values(i),formatter)
        #     else:
        #         pass
        #         # worksheet.write_row('A{}'.format(i+8+rows_count), self.Ope.get_row_values(i),formatter)
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
    # wte.excle_to_html()
    wte.write_faild_to_excle()