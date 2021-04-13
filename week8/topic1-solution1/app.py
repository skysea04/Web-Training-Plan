from flask import Flask, render_template, redirect, request, url_for, session, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import time
import os

app = Flask(__name__)
app.secret_key = os.urandom(16).hex()


@app.route('/')
def index():
    # 如果有名為user的cookie，驗證value是否為使用者，否則返回主頁
    if request.cookies.get('user') and request.cookies.get('user_hash'):
        return redirect(url_for('member'))
    return render_template('index.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    account = request.values['account']
    password = request.values['password']
    if (account == 'test') & (password =='test'):
        # 將user coookie的value設為test的雜湊值，並將cookie傳給client
        res = make_response(redirect(url_for('member')))
        user_hash = generate_password_hash('test')
        res.set_cookie(key='user', value='test', expires=time.time() + 24*3600 )
        res.set_cookie(key='user_hash', value=user_hash, expires=time.time() + 24*3600 )
        return res
    return redirect(url_for('error'))

@app.route('/member/')
def member():
    # 如果有名為user的cookie，驗證value是否為使用者，否則返回主頁
    if request.cookies.get('user') and request.cookies.get('user_hash'):
        user_cookie = request.cookies.get('user')
        user_hash_cookie = request.cookies.get('user_hash')
        if check_password_hash(user_hash_cookie, user_cookie):
            return render_template('member.html')
    return redirect(url_for('index'))

@app.route('/error/')
def error():
    return render_template('error.html')

@app.route('/signout')
def logout():
    # 刪除session
    res = make_response(redirect(url_for('index')))
    res.set_cookie(key='user', value='', expires=0)
    return res



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)