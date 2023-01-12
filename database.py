import pymysql


class dataBase:

    def __init__(self, host='localhost', port=3306, user='root', passwd='mysql', db='campuscat', charset='utf8'):
        self._conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
        self._cur = self._conn.cursor()
        self._cur.execute("SELECT VERSION()")

        # 使用 fetchone() 方法获取单条数据.
        data = self._cur.fetchone()
        print('mysql版本：')
        print(data)
        print("连接数据库正常")

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

    def addRace(self, name):
        sql = "insert into catrace (raceName) values ('{}')".format(name)
        self._cur.execute(sql)


    # 用于注册
    def addUser(self, userRegInfo):
        sql = "insert into userinfo (userName, userPassword, userState) values (%s, %s, 0)"  # 默认注册普通用户
        self._cur.execute(sql, userRegInfo)

    def addAdmin(self, newAdminName):
        sql = "UPDATE `campuscat`.`userinfo` SET `userState` = '1' WHERE (`userName` = '{}');".format(newAdminName)
        self._cur.execute(sql)

    def getCatView(self):
        sql = "select * from catviewinfo"
        count = self._cur.execute(sql)
        res = self._cur.fetchall()
        return count, res

    def getFeedView(self):
        sql = "select * from feedview"
        count = self._cur.execute(sql)
        res = self._cur.fetchall()
        return count, res

    def getWitView(self):
        sql = "select * from witnessinfo"
        count = self._cur.execute(sql)
        res = self._cur.fetchall()
        return count, res

    def getVacNum(self, name):
        sql = "select vacNum from vacinfo where vacState = '{}'".format(name)
        self._cur.execute(sql)
        res = self._cur.fetchall()
        return res[0][0]

    def getRaceNum(self, name):
        sql = "select raceNum from catrace where raceName = '{}'".format(name)
        self._cur.execute(sql)
        res = self._cur.fetchall()
        return res[0][0]

    def getLocNum(self, name):
        sql = "select locNum from location where locName = '{}'".format(name)
        self._cur.execute(sql)
        res = self._cur.fetchall()
        return res[0][0]

    def getUserNum(self, name):
        sql = "select userNum from userinfo where userName = '{}'".format(name)
        self._cur.execute(sql)
        res = self._cur.fetchall()
        return res[0][0]

    def getCatNum(self, name):
        sql = "select catNum from cat where catName = '{}'".format(name)
        self._cur.execute(sql)
        res = self._cur.fetchall()
        return res[0][0]

    def getFoodNum(self, name):
        sql = "select foodNum from food where foodName = '{}'".format(name)
        self._cur.execute(sql)
        res = self._cur.fetchall()
        return res[0][0]

    def addCat(self, vacNum, raceNum, locNum, catName, catGender, catOther):
        sql = "insert into cat (vacNum, raceNum, locNum, catName, catGender, catOther) " \
              "values ({}, {}, {}, '{}', '{}','{}')" \
            .format(vacNum, raceNum, locNum, catName, catGender, catOther)
        self._cur.execute(sql)

    def addFeed(self, foodNum, catNum, locNum, userNum):
        sql = "insert into feedinfo (foodNum, catNum, locNum, userNum) " \
              "values ({}, {}, {}, {})" \
            .format(foodNum, catNum, locNum, userNum)
        self._cur.execute(sql)

    def addWitness(self, userNum, locNum, catNum):
        sql = "insert into witness (userNum, locNum, catNum) " \
              "values ({}, {}, {})" \
            .format(userNum, locNum, catNum)
        self._cur.execute(sql)
