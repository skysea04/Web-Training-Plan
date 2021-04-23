const path = require('path')
const express = require('express')
const helmet = require('helmet')
const cookieSession = require('cookie-session')
const bodyParser = require('body-parser')
const querystring = require('querystring')
const crypto = require('crypto')
const db = require('./util/mysql_connect')
const app = express()


app.set('views', 'views')
app.set('view engine', 'ejs')

app.use(helmet())
app.use(express.static(path.join(__dirname, 'public')))
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

app.use(cookieSession({
    secret: crypto.randomBytes(32).toString('hex')
}))


app.get('/', (req, res) => {
    if(req.session.username){
        return res.redirect('/member/')
    }
    return res.render('index')
})

app.post('/signup', (req, res) => {
    const name = req.body.name
    const username = req.body.username
    const password = req.body.password
    
    db.promise().query('INSERT INTO user (name, username, password) VALUES (?, ?, ?)', [name, username, password])
        .then(()=> {
            return res.redirect('/')
        })
        .catch(() => {
            const query = querystring.stringify({
                "message": '伺服器連線錯誤，帳號註冊失敗'
            })
            return res.redirect('/error?'+query)
        })
})

app.post('/signin', (req, res) => {
    const username = req.body.username
    const password = req.body.password
    
    db.promise().query('SELECT * FROM user WHERE username=? AND password=?', [username, password])
        .then(([results, feilds]) => {
            return results[0]
        })
        .then(user => {
            if(user){
                req.session.username = user.username
                return res.redirect('/member/')
            }
            const query = querystring.stringify({
                "message": '帳號或密碼輸入錯誤'
            })
            return res.redirect('/error?'+query)
        })
        .catch(() => {
            const query = querystring.stringify({
                "message": '伺服器連線錯誤'
            })
            return res.redirect('/error?'+query)
        })
})

app.get('/member/', (req, res) => {
    if(req.session.username){
        db.promise().query('SELECT * FROM user WHERE username=?', [req.session.username])
        .then(([results, feilds]) => results[0].name)
        .then(name => res.render('member', {name:name}))
    }else{
        return res.redirect('/')
    }
})

app.get('/signout', (req, res) => {
    req.session = null
    return res.redirect('/')
})

// api
app.get('/api/users', (req, res) =>{
    const username = req.query.username
    db.promise().query('SELECT * FROM user WHERE username=?', [username])
        .then(([results, fields]) =>results[0])
        .then(user => {
            const data = {
                "id":user.id,
                "name":user.name,
                "username":user.username
            }
            return res.jsonp({"data":data})
        })
        .catch((err) => res.jsonp({"data":null}))
})

app.post('/api/user', (req, res) => {
    if(req.session.username){
        const newName = req.body.name
        db.promise().query('UPDATE user SET name=? WHERE username=?', [newName, req.session.username])
            .then(() => {
                return res.jsonp({"ok":true})
            })
            .catch((err) => {
                return res.jsonp({"error":true})
            })
    }
})


//error
app.get('/error', (req, res) => {
    const message = req.query.message
    console.log(message)
    res.render('error', {'message': message})
})

app.listen(3000)