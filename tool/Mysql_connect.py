import pymysql
import json

class Mysql_operation(object):
    def __init__(self):
        self.Mysql_operation=pymysql.connect(host='127.0.0.1',port=3306,  user='root', passwd='123456', db='guest',
                                            charset="utf8", cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.Mysql_operation.cursor() #创建操作游标

    def sql_select(self,sql_select):
        self.sql=sql_select
        # sql='select id,name,status,address from sign_event order by create_time limit 3'
        self.cursor.execute(sql_select) #执行sql
        result=self.cursor.fetchall()#获取全部查询结果
        return result

    def sql_insert(self,sql_insert):
        self.sql_insert=sql_insert
        self.cursor.execute(sql_insert)
        self.Mysql_operation.commit()  # 执行提交操作
        result=self.cursor.fetchall()
        return result

    def sql_update(self,sql_update):
        self.sql_update=sql_update
        self.cursor.execute(sql_update)
        self.Mysql_operation.commit()  # 执行提交操作
        result=self.cursor.fetchall()
        return result

    def sql_delete(self,sql_delete):
        self.sql_delete=sql_delete
        self.cursor.execute(sql_delete)
        self.Mysql_operation.commit()  # 执行提交操作
        result=self.cursor.fetchall()
        return result

    def close_db(self):
        self.Mysql_operation.close() #关闭数据库连接

if __name__=='__main__':
    Mst=Mysql_operation()
    sql_select=''' select id,name,status,address from sign_event  order by create_time limit 3'''
    sql_update = ''' UPDATE `guest`.`sign_event` SET `id`='1', `name`='发布会22', `limit`='500', `status`='0', `address`='成都玉林', `start_time`='2017-08-06 00:00:00', `create_time`='2018-11-22 22:15:55' WHERE (`id`='1');'''
    sql_insert=''' INSERT INTO `guest`.`sign_event` (`id`, `name`, `limit`, `status`, `address`, `start_time`, `create_time`) VALUES ('22', '发布会', '500', '0', '成都玉林', '2017-08-06 00:00:00', '2018-11-22 22:15:55')'''
    sql_delete=''' DELETE from sign_event where id='22' '''
    a=Mst.sql_select(sql_select)[0]
    print(type(a))

    # print(Mst.sql_insert(sql_insert))
    # print(Mst.sql_update(sql_update))
    # print(Mst.sql_delete(sql_delete))
    Mst.close_db()
