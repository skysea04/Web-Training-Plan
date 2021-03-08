const ham = document.querySelector(".hamburger")
const navBar = document.querySelector('header')
const nav = document.querySelector(".nav-container")
const gallery = document.querySelector('.gallery')
const loadButton = document.querySelector('.load')
let attractionCount = 0

function toggleNavBar(){
    nav.classList.toggle("nav-display")
}

//圖片製造機
const appendAttractions = async () => {
    const res = await fetch('https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json')
    const data =await res.json()
    const attractions = data.result.results
        for(let i = attractionCount; i < attractionCount + 8; i++){
            const stitle = attractions[i]['stitle']
            const jpgURL = 'http:' + attractions[i]['file'].split('http:')[1]
            
            const imgContainer = document.createElement('div')
            imgContainer.classList.add('img-container')
            const imgContain = document.createElement('div')
            imgContain.classList.add('img-contain')
            const imgSelf = document.createElement('img')
            imgSelf.classList.add('img-self')
            const imgBottom = document.createElement('div')
            imgBottom.classList.add('img-bottom')

            // console.log(jpgURL)
            // console.log(stitle)
            imgSelf.setAttribute('src', jpgURL)
            imgBottom.textContent = stitle
            imgBottom.setAttribute('title', stitle)
            imgContain.appendChild(imgSelf)
            imgContainer.append(imgContain, imgBottom)
            gallery.appendChild(imgContainer)
        }
    attractionCount += 8
}

ham.addEventListener('click', toggleNavBar)
loadButton.addEventListener('click', appendAttractions)
appendAttractions()

