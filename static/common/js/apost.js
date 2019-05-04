
$(function () {
    var ue = UE.getEditor('editor',{
            'serverUrl': '/ueditor/upload/'
        });
    $("#submit-btn").click(function (event) {
        event.preventDefault();
        var titleInput = $('input[name="title"]');
        var boardInput = $('select[name="board_id"]');

        var title = titleInput.val();
        var board = boardInput.val();

        var content = ue.getContent();

        zlajax.post({
            'url':'/cms/',
            'data':{
                'title':title,
                'context':content,
                'board_id':board
            },
            'success':function (data) {
                if(data['code'] == 200){
                    window.location = '/'
                }else{
                    console.assert('出错')
                }
            }
        })
    })


});