
$(function () {
   $("#submit-btn").click(function (event) {
       event.preventDefault();
       var telepInput = $("input[name='telephone']");
       var passwdInput = $("input[name='password']");

       var telephone = telepInput.val();
       var password = passwdInput.val();

       zlajax.post({
           'url':'/cms/signin/',
           'data':{
               'telephone':telephone,
               'password':password
           },
           'success':function (data) {
               if(data['code'] == 200){
                   window.location = '/cms/'
               }
               else{
                  zlalert.alertInfo(data['message']);
               }
           }
       })
   })
});