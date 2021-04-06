const forms = document.querySelectorAll('form')

forms.forEach(form => {
    const nameInput = form.querySelector('input[name="name"]')
    const userInput = form.querySelector('input[name="username"]')
    const pwInput = form.querySelector('input[name="password"]')
    function alertToInput(e){
        e.preventDefault()
        if(nameInput && nameInput.value==''){
            alert('請輸入姓名')
        }else if(userInput.value == ''){
            alert('請輸入帳號')
        }else if(pwInput.value == ''){
            alert('請輸入密碼')
        }else{
            //如果都有輸入，那就submit一波
            this.submit()
        }
    
    }
    form.addEventListener('submit', alertToInput)
})