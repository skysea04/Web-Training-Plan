from flask import Flask, render_template, redirect, request, url_for, session
# from datetime import timedelta
import os

app = Flask(__name__)
app.secret_key = os.urandom(16).hex()

# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=5) #控制session作用時間

@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('member'))
    return render_template('index.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    account = request.values['account']
    password = request.values['password']
    if (account == 'test') & (password =='test'):
        session['user'] = account
        return redirect(url_for('member'))
    return redirect(url_for('error'))

@app.route('/member/')
def member():
    if 'user' in session:
        return render_template('member.html')
    return redirect(url_for('index'))

@app.route('/error/')
def error():
    return render_template('error.html')

@app.route('/signout')
def logout():
    # 刪除session
    session.pop('user')
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)