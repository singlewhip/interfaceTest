import json
#判断字符串是否包含，判断字典是否相等
class CommonUtil:
    def is_contain(self,str_one,str_two):
        '''判断字符串是否在另一个字符串中
        str_one:查找的字符串
        str_two:被查找的字符串
        '''
        flag=None
        '''
        if isinstance(str_one,unicode):
            str_one = str_one.encode('unicode-escape').decode('string_escape')
        return cmp(str_one,str_two)
        '''
        if str_one in str_two :
            flag=True
        else:
            flag=False
        return flag
    def is_equal_dict(self,dict_one,dict_two):
        '''判断两个字典是否相等'''
        flag=None
        #json.dumps()用于将dict类型的数据转成str,json.loads()用于将str类型的数据转成dict
        if isinstance(dict_one,str):
            dict_one=json.loads(dict_one)
        if isinstance(dict_two,str):
            dict_two=json.loads(dict_two)
        flag=None
        if dict_one in dict_two:
            flag=True
        else:
            flag=False
        return flag