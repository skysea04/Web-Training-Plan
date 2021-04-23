from flask import Flask, render_template, redirect, request, url_for, session, make_response
from cryptography.fernet import Fernet
import time
import os

app = Flask(__name__)
app.secret_key = os.urandom(16).hex()
key = Fernet.generate_key()
fernet = Fernet(key)


@app.route('/')
def index():
    # 如果有名為user的cookie，驗證value是否為使用者，否則返回主頁
    if request.cookies.get('user'):
        return redirect(url_for('member'))
    return render_template('index.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    account = request.values['account']
    password = request.values['password']
    if (account == 'test') & (password =='test'):
        # 將user coookie的value加密，送到使用者端
        res = make_response(redirect(url_for('member')))
        encrypt_value = fernet.encrypt(bytes('test', 'utf-8'))
        res.set_cookie(key='user', value=encrypt_value, expires=time.time() + 24*3600 )
        return res
    return redirect(url_for('error'))

@app.route('/member/')
def member():
    # 如果有名為user的cookie，解密驗證value是否為使用者，否則返回主頁
    if request.cookies.get('user'):
        user_value = request.cookies.get('user')
        user_value = bytes(user_value, 'utf-8')
        decrypt_user_value = fernet.decrypt(user_value).decode('utf-8')
        if decrypt_user_value == 'test':
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