from tool.operation_excle import OperationExcle

class test1:
    def setUp(self):
        self.file_address='../dataCase/test_app1.xls'
        self.sheet_id=0
    def test_a(self):
        ore=OperationExcle()
        file_address=self.file_address
        sheet_id=self.sheet_id
        ore.__init__(file_address,sheet_id)




if  __name__=="__main__":
    ts=test1()
    a=ts.setUp()
    b=ts.test_a()