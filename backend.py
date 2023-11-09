import mysql.connector as mysql
import info 


app = mysql.connect(host=info.host,user=info.user,password=info.password)
cursor = app.cursor()

cursor.execute("create database if not exists APP")
cursor.execute("use APP")

cursor.execute("create table if not exists od_manager(_id int primary key auto_increment,studID char(20),name varchar(255),OD char(255),stage int)")
cursor.execute("CREATE TABLE IF NOT EXISTS ml_manager (_ID INT AUTO_INCREMENT PRIMARY KEY,studID CHAR(20),name varchar(255),ml char(255),stage int)")
cursor.execute("CREATE TABLE IF NOT EXISTS tasks (_id INT AUTO_INCREMENT PRIMARY KEY, tasks VARCHAR(255), isDone BOOLEAN)")

app.commit()


##---------------------- functions ------------------
def add_ml(studID,name,ml):
    sql = "insert into ml_manager (studID,name,ml,stage) values(%s,%s,%s,0)"
    val = (studID,name,ml)
    cursor.execute(sql,val)
    app.commit()
    #-- new ml inserted stage is kept 0 and the user will increment value 
def increase_ml_stage(studID):
    # insert parameter as ('RA2211051010014')
    cursor.execute(f"select stage from ml_manager where studID = '{studID}'")
    stage = cursor.fetchone()[0]
    stage+=1
    sql = "update ml_manager set stage=%s where studID=%s"
    val = (stage,studID)
    cursor.execute(sql,val)
    app.commit()
def add_od(studID,name,od):
    sql = "insert into od_manager (studID,name,od,stage) values(%s,%s,%s,0)"
    val = (studID,name,od)
    cursor.execute(sql,val)
    app.commit()
def increase_od_stage(studID):
    # insert parameter as ('RA2211051010014')
    cursor.execute(f"select stage from od_manager where studID = '{studID}'")
    stage = cursor.fetchone()[0]
    stage+=1
    sql = "update od_manager set stage=%s where studID=%s"
    val = (stage,studID)
    cursor.execute(sql,val)
    app.commit()
def decrease_ml_stage(studID):
    # insert parameter as ('RA2211051010014')
    cursor.execute(f"select stage from ml_manager where studID = '{studID}'")
    stage = cursor.fetchone()[0]
    stage-=1
    sql = "update ml_manager set stage=%s where studID=%s"
    val = (stage,studID)
    cursor.execute(sql,val)
    app.commit()
def decrease_od_stage(studID):
    # insert parameter as ('RA2211051010014')
    cursor.execute(f"select stage from od_manager where studID = '{studID}'")
    stage = cursor.fetchone()[0]
    stage-=1
    sql = "update od_manager set stage=%s where studID=%s"
    val = (stage,studID)
    cursor.execute(sql,val)
    app.commit()
def add_task(task):
    #parameter is string 
    sql = f"insert into tasks (tasks,isDone) values('{task}',0)"
    cursor.execute(sql)
    app.commit()
def check_task(task):
    #takes parameter as string
    sql = f"update tasks set isDone = '1' where tasks = '{task}'"
    cursor.execute(sql)
    app.commit()




app.close()