import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='website'
)

cursor = db.cursor()

##  select函式使用方法：看要找什麼就在參數寫x='x' 
##  範例
##  db_select(username='ply', password='ply')
def db_select(**kargs):
    sql='SELECT * FROM user WHERE '
    for key in kargs:
        sql += f'{ key } = \'{ kargs[key] }\' and '
    sql = sql[:-5]   
    cursor.execute(sql)
    user = cursor.fetchone()
    if not user:
        return None
    userData = dict(zip(cursor.column_names, user))
    return userData

##  insert函式使用方法：看要找什麼就在參數寫x='x'
##  範例
##  db_insert(name='澎澎', username='ply', password='ply')
def db_insert(**kargs):
    sql ='INSERT INTO user '
    column = '('
    value = '('

    for key in kargs:
        column += key + ','
        value += f'\'{kargs[key]}\','
    
    column = column[:-1] + ')'
    value = value[:-1] + ')'
    sql += column + ' VALUES ' + value
    print(sql)
    cursor.execute(sql)
    db.commit()

# db_insert(name=name, username=username, password=password)
