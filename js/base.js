// let buka = document.getElementById("sech")
// buka.addEventListener("click",()=>{
//     buka.parentElement.style.display = "none"
//     document.getElementById("busch").style.display = "flex"
// })
//Mandar a una de las tres opciones

let susu = document.getElementById("tapaSub")

susu.addEventListener("click",()=>{
    document.getElementById("subsu").classList.toggle("ver")
})
window.addEventListener("resize",()=>{
    let nav = document.querySelector("nav")
    let body = document.querySelector("body")
    let header = document.querySelector("header")
    if(window.innerWidth > 769){
        nav.remove()
        header.insertBefore(nav,header.children.item(header.children.length-1))
    }else if(window.innerWidth <= 769){
        nav.remove()
        body.insertBefore(nav,document.querySelector("main"))
    }
})

let tools = {
    "historia":{

    },
    "personajes":{

    },
    "objetos":{

    }
}