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

//ajax-防空-防注入
$q('button').onclick = function() {
    var formData = new FormData()
    if (!$q('login').value) {
        myApp.modal({
            title: '缺少信息',
            text: '请输入IO账号'
        })
        setTimeout('myApp.closeModal()', 1000)
    } else if (!$q('password').value) {
        myApp.modal({
            title: '缺少信息',
            text: '请输入IO密码'
        })
        setTimeout('myApp.closeModal()', 1000)
    } else {
        formData.append("login", $q('login').value) //need
        formData.append("password", $q('password').value) //need

        $$.ajax({
            'url': '/wens_wharf_parts/login',
            'method': 'POST',
            'data': formData,
            'dataType': 'json',
            'timeout': 10000,
            success: function(data) {
                console.log(data)
                if (data == '0') {
                    myApp.modal({
                        title : '登录错误'
                    })
                    setTimeout('myApp.closeModal()', 1000)
                } else {
                    myApp.modal({
                        title: '登录成功'
                    })
                    setTimeout('myApp.closeModal()', 1000)
                    setTimeout('window.location.href = "record"', 1000)
                }
            },
            error: function(error) {
                console.log(error)
            }
        })
    }
}