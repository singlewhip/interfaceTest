from operation_data.get_data import GetData
import xlsxwriter
import time
import pandas
import codecs
import time

class Write_testReport_excle():
    global workbook,worksheet,chart,chart1,formatter,title_formatter,ave_formatter,now,filename
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    workbook=xlsxwriter.Workbook("../dataconfig/" + now + '_test_report.xlsx')
    filename='../dataconfig/' + now + '_test_report.xlsx'
    worksheet = workbook.add_worksheet("测试报告")
    # 创建一个图表对象,column:柱形图,饼图
    chart = workbook.add_chart({'type': 'column'})
    chart1 = workbook.add_chart({'type': 'pie'})

    # def __init__(self):
    #     self.data=GetData()
        # self.workbook=workbook
        # self.worksheet=worksheet
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
        #添加饼图
        col_num=2
        while col_num<7:
            chart1.add_series({
            "name":"=测试报告!$A${}".format(col_num),
            "categories":"=测试报告!$B$1:$D$1",
            "values":"=(测试报告!$B${}:$D${})".format(col_num,col_num)
            })
            i=0
            while i<5:
                value = 2
                value1 = value
                value1 =17 * i
                i+=1
                # worksheet.insert_chart('G{}'.format(value), chart1, {'x_offset': 25, 'y_offset': 10})
            col_num += 1
        #插入图表带偏移
        worksheet.insert_chart('A8', chart, {'x_offset': 25, 'y_offset': 10})
        # worksheet.insert_chart('G{}'.format(value), chart1, {'x_offset': 25, 'y_offset': 10})
        # 定义标题栏格式对象：边框加粗1像素，背景色为灰色，单元格内容居中、加粗,自动换行
        formatter = workbook.add_format()
        formatter.set_border(1)
        formatter.set_text_wrap()
        # 写入第2到第6行的数据，并将第2~6行数据加入图表系列
        for i in range(0 ,len(data)):
            worksheet.write_row('B{}'.format(i+2), data[i],formatter)
        self.create_TestReport()
        workbook.close()
    # def excle_to_html(self):
    #     # 注意这里不能直接使用workbook,因为直接引用workbook返回的对象不是一个文件路径，而是:<class 'xlsxwriter.workbook.Workbook'>
    #     fp=pandas.ExcelFile(filename)
    #     df=fp.parse()
    #     with codecs.open('../report/'+now+'_test_report.html', 'w', 'utf-8') as html_file:
    #         html_file.write(df.to_html(header=True, index=False))

if __name__=="__main__":
    wte=Write_testReport_excle()
    wte.write_TestReport([1,2,3],[2,3,4,5])
    # wte.excle_to_html()