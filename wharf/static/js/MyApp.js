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
$q('a').onclick = function() {
    window.location.href = 'record'
}

//
function $q(el) {
    return document.getElementById(el)
}

//检测浏览器
if (typeof FileReader === 'undefined') {
    myApp.modal({
        title: '抱歉',
        text: '您的浏览器不支持上传图片'
    })
    setTimeout('myApp.closeModal()', 1000)
    $q('snap').setAttribute('disabled', 'disabled')
    $q('upload').setAttribute('disabled', 'disabled')
}


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


$q('snap').onclick = function() {
    $q('upload').click()
}





//选取图片
var file = []
var count = 0
var FileSet = []
var img = ''
var width = ''
var height = ''
$q('upload').addEventListener('change', function() {
    $q('upload').setAttribute('disabled', 'disabled')

    if (FileSet.length == 9) {
        myApp.modal({
            title: '抱歉',
            text: '上传图片仅限9张'
        })
        setTimeout('myApp.closeModal()', 500)
        return false
    } else {


        for (var i = 0; i < this.files.length; i++) {
            file[file.length] = this.files[i]

            //判断图片
            // if (!/image\/\w+/.test(file.type)) {
            //     console.log("文件必须为图片！")
            //     return false
            // }

        }

for (var i = 0; i < file.length; i++) {
    
            var reader = new FileReader()
            file[i] = reader.readAsDataURL(file[i]) //readasBinaryString()

            reader.onload = function(e) {

                file[i] = e.currentTarget.result //file是base64形式


                $q('display').innerHTML = $q('display').innerHTML +
                    '<div style="position:relative;"><img id="img' + i +
                    '" src="' + this.result +
                    '"/><div id="' + count + '" onclick="deleteImg(this,this.id)" style="position:absolute;top:0;right:0;' +
                    'height:50px;width:50px;background-color:transparent;">' +
                    '<i class="f7-icons" style="background:black;font-size:50px!important;color:white;">delete_round</i>' +
                    '</div></div>'


                //压缩图片
                var canvas = document.createElement('canvas')
                var ctx = canvas.getContext('2d')
                img = document.getElementById('img' + i)

                img.onload = function() {
                    width = img.width;
                    height = img.height;

                    canvas.width = width
                    canvas.height = height

                    ctx.drawImage(img, 0, 0, width, height)
                    file[i] = canvas.toDataURL('image/jpeg',0.4)

                    FileSet[count] = file[i].split(',')[1]
                }
                   
                 count = count + 1
                }

            }


    

    }
    $q('display').style.display = 'block'
    $q('upload').removeAttribute('disabled')
})

function deleteImg(link, id) {
    link.parentNode.parentNode.removeChild(link.parentNode)
    FileSet[id] = ''
}





//高德地图api
var str = ''
mapObj = new AMap.Map('iCenter')
mapObj.plugin('AMap.Geolocation', function() {
    geolocation = new AMap.Geolocation({
        enableHighAccuracy: true,
        timeout: 10000,
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
$q('button').onclick = function() {
    $q('button').setAttribute('disabled', 'disabled')
    var formData = new FormData()
    if ($q('wharf').value == '') {
        myApp.modal({
            title: '缺少信息',
            text: '请输入码头'
        })
        setTimeout('myApp.closeModal()', 1000)
        $q('button').removeAttribute('disabled')
    } else if ($q('description').value == '') {
        myApp.modal({
            title: '缺少信息',
            text: '请输入描述和评测'
        })
        setTimeout('myApp.closeModal()', 1000)
        $q('button').removeAttribute('disabled')
    } else {
        formData.append("wharf", $q('wharf').value) //need
        formData.append("ship", $q('ship').value)
        formData.append("car", $q('car').value)
        formData.append("bulk", $q('bulk').value)
        formData.append("place", $q('place').value)
        formData.append("to_where", $q('to_where').value)
        formData.append("name", name)
        formData.append("description", $q('description').value) //need
        if (typeof(str) == 'undefined') {
            str = ''
        }
        if (str == '') {
            myApp.modal({
                title: '未获取到地点信息',
                text: '请稍后或刷新'
            })
            setTimeout('myApp.closeModal()', 900)
            $q('button').removeAttribute('disabled')

        } else {
            formData.append("local", str) //need

            var flag = true;


            var FinalSet = new Array()

            function deleteSet() {
                for (var i = 0; i < FileSet.length; i++) {
                    if (FileSet[i] !== '') {
                        FinalSet[FinalSet.length] = FileSet[i]
                    }
                }
            }
            deleteSet()


            if (FinalSet[0] !== '') {
                // for (var i = 0; i < FileSet.length; i++) {
                //     FileSet[i] = FileSet[i].split(',')[1]//消掉base64前缀
                // }
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

                //     formData.append("img",imgData);

            } else {
                myApp.modal({
                    title: '缺少信息',
                    text: '请加上图片'
                })
                flag = false
                setTimeout('myApp.closeModal()', 1000)
                $q('button').removeAttribute('disabled')
                return false
            }

            if (flag) {
                $$.ajax({
                    'url': '/wens_wharf_parts/push',
                    'method': 'POST',
                    'data': formData,
                    'dataType': 'text',
                    'timeout': 10000,
                    success: function(data) {

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