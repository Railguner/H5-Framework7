//Framework7


var myApp = new Framework7({
        pushState: true,
        cache: true,
        domeCache: true

    }),
    $$ = Dom7,
    mainView = myApp.addView('.view-main', {
        domCache: true
    }),
    snap = document.getElementById('snap'),
    upload = document.getElementById('upload'),
    display = document.getElementById('display'),
    btn = document.getElementById('button'),
    count = 0,
    FileSet = [],
    str = ''

document.getElementById('a').addEventListener('click', function() {

    var local = window.location.href
    if (local.substr(local.length - 4) == 'post') {
        window.location.href = 'record'
    }
    mainView.router.back()
})



//检测浏览器
if (typeof FileReader === 'undefined') {
    myApp.modal({
        title: '抱歉',
        text: '您的浏览器不支持上传图片'
    })
    setTimeout('myApp.closeModal()', 1000)
    snap.setAttribute('disabled', 'disabled')
    upload.setAttribute('disabled', 'disabled')
}


snap.addEventListener('click', function() {
    upload.click()
})

//选取图片

upload.addEventListener('change', function() {
    snap.setAttribute('disabled', 'disabled')

    if (count == 9) {
        myApp.modal({
            title: '抱歉',
            text: '上传图片仅限9张'
        })
        setTimeout('myApp.closeModal()', 500)
        return false
    } else {

        var i = this.files.length

        while (i > 0) {
            i = i - 1

            var reader = new FileReader()
            reader.readAsDataURL(this.files[i])

            reader.onload = function(e) {
                var div = display
                div.innerHTML = div.innerHTML +
                    '<div style="position:relative;"><img id="img' + i +
                    '" src="' + this.result +
                    '"/><div id="' + count + '" onclick="deleteImg(this,this.id)" class="playImg">' +
                    '<i class="f7-icons icon">close_round</i>' +
                    '</div></div>'

                FileSet[count] = this.result.split(',')[1] //base64形式,消除头部

                count = count + 1




            }
        }
        display.style.display = 'block'
        snap.removeAttribute('disabled')


    }
})

function deleteImg(link, id) {
    var parent = link.parentNode
    parent.parentNode.removeChild(parent)
    FileSet[id] = ''
    count = count - 1
}



//高德地图api

mapObj = new AMap.Map('iCenter')
mapObj.plugin('AMap.Geolocation', function() {
    geolocation = new AMap.Geolocation({
        enableHighAccuracy: true,
        timeout: 5000,
        maximumAge: 0,
        convert: true,
        showButton: true,
        buttonPosition: 'LB',
        buttonOffset: new AMap.Pixel(10, 20),
        showMarker: true,
        showCircle: true,
        panToLocation: true,
        zoomToAccuracy: true
    })
    mapObj.addControl(geolocation)

    geolocation.getCurrentPosition(function(status, result) {

        str = result.formattedAddress
        console.log(str)
    })
})


//ajax-防空-防注入
btn.onclick = function() {

    btn.setAttribute('disabled', 'disabled')

    var formData = new FormData(),
        wharf = document.getElementById('wharf').value,
        description = document.getElementById('description').value,
        add_str = str,
        FileSetLoad = FileSet

    if (wharf == '') {
        myApp.modal({
            title: '缺少信息',
            text: '请输入码头'
        })
        setTimeout('myApp.closeModal()', 1000)
        btn.removeAttribute('disabled')

    } else if (description == '') {
        myApp.modal({
            title: '缺少信息',
            text: '请输入描述和评测'
        })
        setTimeout('myApp.closeModal()', 1000)
        btn.removeAttribute('disabled')
    } else {
        formData.append("wharf", wharf) //need
        formData.append("ship", document.getElementById('ship').value)
        formData.append("car", document.getElementById('car').value)
        formData.append("bulk", document.getElementById('bulk').value)
        formData.append("place", document.getElementById('place').value)
        formData.append("to_where", document.getElementById('to_where').value)
        formData.append("description", description) //need

        if (typeof(add_str) == 'undefined') {
            add_str = '未知地点信息'
        }
        if (add_str == '') {
            myApp.modal({
                title: '未获取到地点信息',
                text: '请稍后或刷新'
            })
            setTimeout('myApp.closeModal()', 900)
            btn.removeAttribute('disabled')

        } else {
            formData.append("local", add_str) //need

            var FinalSet = [],
                flag = true

            function minify() {
                var length = FileSetLoad.length,
                    i = 0
                while (i < length) {
                    if (FileSetLoad[i] !== '') {
                        FinalSet[FinalSet.length] = FileSetLoad[i]
                    }
                    i = i + 1
                }
            }
            minify()




            if (FinalSet[0] !== '') {

                formData.append("img0", FinalSet[0])
                formData.append("img1", FinalSet[1])
                formData.append("img2", FinalSet[2])
                formData.append("img3", FinalSet[3])
                formData.append("img4", FinalSet[4])
                formData.append("img5", FinalSet[5])
                formData.append("img6", FinalSet[6])
                formData.append("img7", FinalSet[7])
                formData.append("img8", FinalSet[8])
                // } else if (imgData !== '') {

                // formData.append("img",imgData);

            } else {
                myApp.modal({
                    title: '缺少信息',
                    text: '请加上图片'
                })
                flag = false
                setTimeout('myApp.closeModal()', 1000)
                btn.removeAttribute('disabled')
                return false
            }

            if (flag) {
                $$.ajax({
                    'url': '/wens_wharf_parts/push',
                    'method': 'POST',
                    'data': formData,
                    'dataType': 'text',
                    'timeout': 10000,
                    'success': function(data) {
                        myApp.modal({
                            title: '记录成功'
                        })
                        setTimeout('myApp.closeModal()', 900)
                        setTimeout("window.location.href = 'record'", 1100)
                    }
                })
            }
        }

    }
}








// if (!/image\/\w+/.test(file.type)) {
//     console.log("文件必须为图片！")
//     return false
// }

// //拍照
// var imgData = ''
// var mediaStream = ''
// var track = ''
// function camera() {
//     var video = $q("video")
//     video.style.display = 'block'
//     var videoObj = { "video": true }
//     var errBack = function(error) {
//         console.log("Video capture error: " + error.message, error.code)
//     }

//     $q('snap').style.display = 'block'

//     navigator.getUserMedia(videoObj, function(stream) {
//         mediaStream = stream
//         video.src = window.URL.createObjectURL(stream)
//         track = stream.getTracks()[0]
//         video.play()
//     }, errBack)

//     $q('snap').addEventListener("click", function() {
//         var canvas = $q("canvas")
//         var context = canvas.getContext("2d")

//         canvas.width = video.videoWidth
//         canvas.height = video.videoHeight
//         context.drawImage(video, 0, 0)

//         $q('canvas').style.display = 'block'
//         $q('video').style.display = 'none'

//         imgData = canvas.toDataURL("image/jpeg")

//         imgData = imgData.split(',')[1]
//         // console.log(imgData.split(',')[1])
//         $q('snap').style.display = 'none'

//         // imgData = dataURItoBlob(imgData);


//         console.log(track)

//         if (track != null) {
//             if (track.stop) {
//                 track.stop();
//             }
//         }

//     }, false)
// }

// //base64转文件
// function dataURItoBlob(base64Data) {
//     var byteString;
//     if (base64Data.split(',')[0].indexOf('base64') >= 0) {
//         byteString = atob(base64Data.split(',')[1]);
//     } else {
//         byteString = unescape(base64Data.split(',')[1]);
//     }

//     var mimeString = base64Data.split(',')[0].split(':')[1].split(';')[0];
//     var ia = new Uint8Array(byteString.length);
//     for (var i = 0; i < byteString.length; i++) {
//         ia[i] = byteString.charCodeAt(i);
//     }
//     return new Blob([ia], { type: mimeString });
// }


// //模拟弹出框
// $$('.open-vertical-modal').on('click', function() {
//     myApp.modal({
//         title: '选取上传方式',
//         text: '',
//         verticalButtons: true,
//         buttons: [{
//                 text: '拍照',
//                 close: true,
//                 onClick: function() {
//                     $q('display').style.display = 'none'
//                     $q('canvas').style.display = 'none'
//                     file = ''
//                     imgData = ''
//                     camera()
//                 }
//             },
//             {
//                 text: '文件选取',
//                 close: true,
//                 onClick: function() {
//                     $q('video').style.display = 'none'
//                     $q('canvas').style.display = 'none'
//                     $q('snap').style.display = 'none'
//                     imgData = ''
//                     file = ''
//                     $q('upload').click()
//                     $q('display').style.display = 'block'
//                 }
//             },

//             {
//                 text: '取消',
//                 close: true
//             }
//         ]
//     })
// })
//
//function $q(el) {
//    return document.getElementById(el)
//}