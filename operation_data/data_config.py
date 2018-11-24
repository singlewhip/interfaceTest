class global_val:
    #case_id
    Id='0'
    request_name='1'
    url='2'
    run='3'
    request_method='4'
    header='5'
    case_dapend='6'
    data_depend='7'
    field_depend='8'
    data='9'
    expect='10'
    result='11'
    #获取case_id及每列的数据
def get_case_id():
    return global_val.Id

def get_request_name():
    return global_val.request_name

def get_url():
    return global_val.url

def get_run():
    return global_val.run
#获取请求方式
def get_request_method():
    return global_val.request_method

def get_header():
    return global_val.header

#获取header值
def get_header_value():
    header={"Content-Type": "application/json"}

def get_case_dapend():
    return global_val.case_dapend

def get_data_depend():
    return global_val.data_depend

def get_field_depend():
    return global_val.field_depend

def get_data():
    return global_val.data

def get_expect():
    return global_val.expect

def get_result():
    return global_val.result