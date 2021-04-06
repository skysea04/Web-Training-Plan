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

    user = db_select(username=username, password=password)
    # 如果有該user，給session後重新導向到會員頁
    if user:
        session['username'] = user['username']
        return redirect(url_for('member'))
    message = '帳號或密碼輸入錯誤'
    return redirect(url_for('error', message = message))

# 會員頁
@app.route('/member/')
def member():
    if 'username' in session:
        user = db_select(username=session['username'])
        return render_template('member.html', name=user['name'], username=session['username'])
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

# 查詢會員資料api
@app.route('/api/users')
def api_users():
    username = request.args.get('username')
    user = db_select(username=username)
    if user:
        data = {'data':{
            'id': user['id'],
            'name': user['name'],
            'username': user['username']
        }}
        return data
    else:
        data = {
            'data': None
        }
        return data

# 修改會員姓名api
@app.route('/api/user', methods=['POST'])
def api_user():
    if 'username' in session:
        data = request.get_json('name')
        
        sql = 'UPDATE user SET name=%s WHERE username=%s'
        val = (data['name'], session['username'])
        cursor.execute(sql, val)
        db.commit()
        # print(data['name'], session['username'])
        user = db_select(name=data['name'], username=session['username'])
        # print(user)
        if user:
            data = {'ok': True}
            return data
        data = {'error': True}
        return data
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)