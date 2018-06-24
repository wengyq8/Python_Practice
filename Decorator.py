# -*- coding: utf-8 -*-
'''
装饰模式，顾名思义，就是在调用目标函数之前，对这个函数对象进行装饰。比如一个对数据库操作的方法，
我们在查询数据之前，需要连接一下数据库，当查询结束之后，需要再把连接断开关闭。正常的逻辑如下：
'''
def Connect_db():
    print 'Connect db'

def Close_db():
    print 'Close db'

def query_db():
    Connect_db()
    print 'query the user'
    Close_db()

query_db()

'''
我们把 连接数据库(connect_db) 和 关闭连接 (close_db)都封装成了函数。 
query_data 方法执行我们查询的具体逻辑。这样需要不同的查询方法，只需要把查询的逻辑也封装成一个方法
'''

def query_user():
    print 'query some user'
def query_data(query):
    Connect_db()
    query()
    Close_db()
query_data(query_user)



def query_user():
    print 'query some user'
def query_data(query):
    """ 定义装饰器，返回一个函数，对query进行wrapper包装 """
    def wrapper():
        Connect_db()
        query()
        Close_db()
    return wrapper
# 这里调用query_data进行实际装饰（注意装饰是动词）
query_user = query_data(query_user)
# 调用被装饰后的函数query_user
query_user()



def query_data(query):
    def wrapper():
        Connect_db()
        query()
        Close_db()
    return wrapper
# 使用@调用装饰器进行装饰
@query_data
def query_user():
    print 'query some user'
query_user()