import json
import requests

class RunMethod:
    def post_main(self,url,data,header=None):
        res=None
        if header!=None:
            res=requests.post(url=url,data=data,headers=header)
        else:
            res=requests.post(url=url,data=data)
        print(res.status_code)
        return res.json()
    def get_main(self,url,data=None,header=None):
        res=None
        if header!=None:
            #verify:验证——（可选）要么是布尔型，在这种情况下，它控制我们是否验证服务器的TLS证书或字符串，在这种情况下，它必须是通往CA捆绑包的路径。默认值为True
            # res=requests.get(url=url,params=data,headers=header,verify=false)
            res = requests.get(url=url, params=data, headers=header)
        else:
            # res=requests.get(url=url,params=data,verify=false)
            res = requests.get(url=url, params=data)
        print(res.status_code)
        return res.json()
    # def run_main(self,url=url,method=None,data=None,header=None):
    def run_main(self, method: object, url: object, data: object = None, header: object = None) -> object:
        res=None
        if method=='post':
            res=self.post_main(url,data,header)
        else:
            # res=self.get_main(url,data,header,verify=false)
            res = self.get_main(url, data, header)
            #dumps方法:
            # sort_keys是告诉编码器按照字典排序(a到z)输出,indent参数根据数据格式缩进显示，读起来更加清晰:
            # separators参数的作用是去掉,,:后面的空格,skipkeys可以跳过那些非string对象当作key的处理,输出真正的中文需要指定ensure_ascii=False
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=3)

