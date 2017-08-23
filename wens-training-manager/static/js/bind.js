document.getElementById('a').addEventListener('click', function() {

    var local = window.location.href
    if (local.substr(local.length - 4) == 'bind') {
        go('index')
    }
    mainView.router.back()
})

document.getElementById('button').onclick = function() {
    $$.ajax({
        'url': '/wens_training_manager/bind_change',
        'method': 'POST',
        'data': document.getElementById('course').value,
        'dataType': 'json',
        'success': function(data) {
            if (data == 1) {
                AlertBox('修改成功')
            } else {
                AlertBox('修改失败')
            }
        },
        error: function(error) {
            console.log(error)
        }
    })
}