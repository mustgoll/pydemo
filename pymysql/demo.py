import pymysql

conn=pymysql.connect(host='localhost',port=3306,user='helin',passwd='abcd1234',db='helin')
cursor=conn.cursor()
row=cursor.execute('select * from stu')
print(cursor.fetchmany(3))