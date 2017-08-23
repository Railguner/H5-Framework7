var myApp = new Framework7({
    pushState: true,
    cache: true
})

var $$ = Dom7

var mainView = myApp.addView('.view-main', {
    domCache: true
})


function AlertBox(str) {
    myApp.modal({
        title: str
    })
    setTimeout('myApp.closeModal()', 700)
}

function go(str) {
    var str = str
    setTimeout(function() { window.location.href = str }, 900)
}