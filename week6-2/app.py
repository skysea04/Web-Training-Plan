from flask import Flask, render_template, redirect, request, url_for, session
from datetime import timedelta
import os
from mysql_connect import cursor, db, db_select, db_insert

app = Flask(__name__)
app.secret_key = os.urandom(16).hex()

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1) #控制session作用時間

# 首頁
@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('member'))
    return render_template('index.html')

# 註冊
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    name = request.values['name']
    username = request.values['username']
    password = request.values['password']
    # sql = "SELECT username FROM user WHERE username=%s"
    # validate_user = (username, )
    # cursor.execute(sql, validate_user)
    # user = cursor.fetchone()
    user = db_select(username=username)
    ##如果使用者已存在，回傳錯誤頁面;若不存在則註冊帳號
    if user:
        message = '帳號 %s 已經被註冊'%(username)
        return redirect(url_for('error', message=message))
    else:
        db_insert(name=name, username=username, password=password)
        return redirect(url_for('index'))

# 登入
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    username = request.values['username']
    password = request.values['password']
    # sql = "SELECT name, username FROM user WHERE username=%s and password=%s"
    # validate_user = (username, password)
    # cursor.execute(sql, validate_user)
    # user = cursor.fetchone()
    user = db_select(username=username, password=password)
    # 如果有該user，給session後重新導向到會員頁
    if user:
        session['name'] = user['name']
        session['username'] = user['username']
        return redirect(url_for('member'))
    message = '帳號或密碼輸入錯誤'
    return redirect(url_for('error', message = message))

# 會員頁
@app.route('/member/')
def member():
    if 'username' in session:
        return render_template('member.html', name=session['name'])
    return redirect(url_for('index'))


# 登出
@app.route('/signout')
def logout():
    # 刪除session
    session.clear()
    return redirect(url_for('index'))

# 錯誤頁面
@app.route('/error/')
def error():
    message = request.args.get('message')
    return render_template('error.html', message=message)




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)