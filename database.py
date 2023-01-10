import pymysql


class dataBase:

    def __init__(self, host='localhost', port=3306, user='root', passwd='mysql', db='campuscat', charset='utf8'):
        self._conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
        self._cur = self._conn.cursor()
        self._cur.execute("SELECT VERSION()")

        # 使用 fetchone() 方法获取单条数据.
        data = self._cur.fetchone()
        print(data)
        print("数据库连接成功！")

    def update(self):
        self._conn.commit()

    def select(self, table, column, condition):
        """
        select * from {table} where {column} = '{condition}'
        """
        sql = "select * from {} where {} = '{}'".format(table, column, condition)
        count = self._cur.execute(sql)
        res = self._cur.fetchall()
        return count, res

    def selectAll(self, table):
        """
        select * from {table}
        """
        sql = "select * from {} ".format(table)
        count = self._cur.execute(sql)
        res = self._cur.fetchall()
        return count, res

    # 用于注册
    def addUser(self, userRegInfo):
        sql = "insert into userinfo (userName, userPassword, userState) values (%s, %s, 0)"  # 默认注册普通用户
        self._cur.execute(sql, userRegInfo)
