//
// $(function () {
//    $('#search_btn').click(function (event) {
//        event.preventDefault();
//
//        var textInput = $('input[name="search_text"]');
//
//        var text = textInput.val();
//
//        zlajax.post({
//            'url':'/s/',
//            'data':{
//                'text':text
//            },
//            'success':function (data) {
//                if(data['code'] == 200){
//                     // window.location.reload();
//                     console.assert(window.location)
//                }else{
//                     console.assert('error');
//                }
//            }
//
//        })
//    })
// });