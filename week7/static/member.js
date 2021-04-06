const userSearchForm = document.querySelector('.search-user')
const changeUsernameForm = document.querySelector('.change-username')

// 查詢會員姓名
function searchUser(e){
    e.preventDefault()
    const search = this.querySelector('input').value
    const searchResult = this.querySelector('p')
    let url = `/api/users?username=${search}`

    fetch(url)
        .then(res => res.json())
        .then(data => {
            const name = data['data']['name']
            const username = data['data']['username']
            searchResult.innerText = `${name}(${username})`
        })
        .catch(fail => {
            searchResult.innerText = '無此使用者'
        })
}

// 更新會員姓名
function changeUsername(e){
    e.preventDefault()
    const url = '/api/user'
    const newName = this.querySelector('input').value
    const changeResult = this.querySelector('p')
    const data = {
        'name': newName
    }
    fetch(url, {
        method: 'POST',
        headers:{
            'Contnet-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(data => {
        if(data['ok']){
            changeResult.innerText = '更新成功'
            const helloUser = document.querySelector('.log')
            helloUser.innerText = `${newName}，歡迎登入系統`
        }else{
            changeResult.innerText = '更新失敗'
        }
    })
}

userSearchForm.addEventListener('submit', searchUser)
changeUsernameForm.addEventListener('submit', changeUsername)