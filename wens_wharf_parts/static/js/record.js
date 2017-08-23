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

function BigImg(id) {
	var name = new FormData()
    name.append('id',id)
    $$.ajax({
        'url': '/wens_wharf_parts/big_image',
        'method': 'POST',
        'data': name,
        'dataType': 'text',
        'timeout': 100000,
        success: function(data) {
        	var modal = document.getElementById('my_modal')
        	modal.innerHTML = '<div style="width: 100%;display: block"><img src="data:image/jpeg;base64,'
        	+ data + '" style="top:100px;position:absolute;width:100%;"></div>'
        	modal.style.display = 'block'
            modal.addEventListener('click',function (e) {
                    modal.innerHTML = ''
                    modal.style.display = 'none'
            })
        }
    })
}
