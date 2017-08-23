document.getElementById('teacher_login').addEventListener('click', function(e) {
    var data = new FormData(document.querySelector("#teacher_form")),
        flag = true
    data.forEach(function(e) {
        if (e == '') {
            flag = !flag
            if (!flag) {
                AlertBox('缺少信息!请检查')
            }
        }
    })

    if (flag) {
        $$.ajax({
            'url': '/wens_training_manager/teacher_login',
            'method': 'POST',
            'data': data,
            'dataType': 'json',
            'success': function(data) {
                if (data == 0) {
                    AlertBox('登录错误')
                } else {
                    if (data == 1) {
                        AlertBox('登录成功')
                        go('teacher')
                    } else {
                        AlertBox('登录失败')
                    }
                }
            },
            error: function(error) {
                console.log(error)
            }
        })
    }
}, false)

document.getElementById('student_login').addEventListener('click', function(e) {

    var data = new FormData(document.getElementById('student_form')),
        flag = true

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
            'url': '/wens_training_manager/student_login',
            'method': 'POST',
            'data': data,
            'dataType': 'text',
            'success': function(data) {
                if (data) {
                    AlertBox('登录成功')
                    go('bind?id=' + data)

                } else {
                    AlertBox('登录失败')
                }
            },
            error: function(error) {
                console.log(error)
            }
        })
    }
}, false)



document.getElementById('manager_login').addEventListener('click', function(e) {

    var data = new FormData(document.getElementById('manager_form')),
        flag = true

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
            'url': '/wens_training_manager/manager_login',
            'method': 'POST',
            'data': data,
            'dataType': 'text',
            'success': function(data) {
                if (data == 1) {
                    AlertBox('记录成功')
                    go('manager')
                } else {
                    AlertBox('登录失败')
                }
            },
            error: function(error) {
                console.log(error)
            }
        })
    }
}, false)