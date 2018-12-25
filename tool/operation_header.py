import json
import requests
import sys
sys.path.append('../')
from tool import operation_json

class OperationHeader:
    #获取token
    def get_header(self):
        host='test.v1-beta.api.jjtvip.com'
        url='http://'+host+'/ms-user-info/user/appFhbLogin'
        data={"phone": "18599937985", "core": "896522"}
        headerNotlogin = {"Content-Type": "application/json"}
        res=requests.post(url=url,data=json.dumps(data),headers=headerNotlogin)
        response=res.json()
        print(response)
        token=response['data']['token']
        # print(token)
        headerLogin={"Content-Type": "application/json","token":token}
        return headerLogin

if __name__=='__main__':
    op_header=OperationHeader()
    host = 'test.v1-beta.api.jjtvip.com'
    data='type=2&state=1'
    url='http://'+host+'/ms-fahuobao-user/fhbAnnouncement/fhb-announcement-list-worker'
    header=op_header.get_header()
    #get请求传参时使用params参数，post请求使用data传参
    res=requests.get(url=url,params=data,headers=header)
    response=res.json()
    print(response)
