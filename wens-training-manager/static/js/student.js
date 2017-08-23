//range
function change(el) {

    // var form = document.getElementById(id)

    // for (var i = 0; i < 10; i++) {

    //     (function(x) {

    //         form.elements[x].addEventListener('input', function(e) {

    //             form.querySelectorAll(id)[x].innerHTML = form.elements[x].value + '分'
    //         }, false)
    //     })(i)
    // }
    
    var dis = el.parentNode.parentNode.parentNode.parentNode.parentNode.previousSibling.previousSibling.childNodes[1].childNodes[1].childNodes[3]

    dis.innerHTML = el.value + '分'
}

function submit(id) {

    var data = new FormData(document.getElementById(id)),
        flag = false

    data.forEach(function(e) {
        if (e == '') {
            flag = !flag
        }
        if (!flag) {
            AlertBox('缺少信息!请检查')
        }
    })

    if (flag) {
        $$.ajax({
            'url': '/wens_training_manager/student_assess',
            'method': 'POST',
            'data': data,
            'dataType': 'json',
            'success': function(data) {
                if (data) {
                    AlertBox('评价成功')
                } else {
                    AlertBox('评价失败')
                }
            },
            error: function(error) {
                console.log(error)
            }
        })
    }
}