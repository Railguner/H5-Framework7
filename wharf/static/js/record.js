//Framework7
var myApp = new Framework7({
    pushState: true,
    cache: true,
    domeCache: true

})

var $$ = Dom7

var mainView = myApp.addView('.view-main', {
    domCache: true
})


function $q(el) {
    return document.getElementById(el)
}

$q('a').onclick = function() {
    window.location.href = 'index'
}
$q('b').onclick = function() {
    window.location.href = 'post'
}