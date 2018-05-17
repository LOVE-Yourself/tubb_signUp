loadPage();
$(window).resize(function () {
    loadPage();
});

function loadPage() {
    var bodyHeight = $(window).height();
    var $loginBg = $(".loginBg");
    $loginBg.css('height', +bodyHeight - 310 + 'px');
}

var swith = false;
var getCallNum = true;
var secs =60;
$(".getPhoneVerifyNum").click(function () {
    if(getCallNum){
        var user={};
        user.phone= user.phone = $("#phone").val();
        user.send_type = user.send_type = $('#send_type').val();
        $.ajax({
            type: 'POST',
            url: appConfig.requestUrl + "/users/getCode/",
            data: user,
            success: function (data) {
                if(data.status==200)
                  alert("成功");
                else {
                    alert("请求频繁");
                }
            },
            error: function (e) {
            }
        });
        $(".getPhoneVerifyNum").addClass("get");
        $(".getPhoneVerifyNum span").text("60s");

       var timers= setInterval(function () {
            if(secs>0){
                secs--;
                $(".getPhoneVerifyNum span").text(secs+"s");
            }else {
                clearInterval(timers);
                getCallNum=true;
                secs=60;
                $(".getPhoneVerifyNum span").text("点击获取验证码");
                $(".getPhoneVerifyNum").removeClass("get");
            }

        },1000);
        getCallNum=false;
    }
});

$(".switchMenuBtn").click(function () {
    swith = !swith;
    if (swith) {
        $(".nav-nav").css("display", "block");
        $(".switchMenuBtn span.two").css("width", "0px");
        $(".switchMenuBtn span.one").css("transform", "rotate(45deg) translate(4px,7px)");
        $(".switchMenuBtn span.three").css("transform", "rotate(-45deg) translate(4px,-7px)");
    } else {
        $(".nav-nav").css("display", "none");
        $(".switchMenuBtn span.two").css("width", "62%");
        $(".switchMenuBtn span.one").css("transform", "rotate(0deg) translate(0)");
        $(".switchMenuBtn span.three").css("transform", "rotate(0deg) translate(0)");

    }

})

function validate() {
    var reg = /^1[356789]\d{9}$/;
    var user={};

    user.phone = $("#phone").val();
    user.password = $("#password").val();
    user.verifyNum = $("#verifyNum").val();
    user.csrf = $("#frscValue").val();
    var errorText = "";
    user.isPass = true;
    $(".inputDiv .error.fa").removeClass("fa-close fa-check fa-minus");

    if (isNaN( user.phone) ||  user.phone.length != 11) {
        errorText += " 手机号码为不11位数字";
        user.isPass = false;
    } else {
        if (!reg.test( user.phone)) {
            errorText += "  </br>   号码格式不正确";
            user.isPass = false;
        }
    }
    if ( user.password.length > 5 &&  user.password.length < 18) {
        var checkPassword=$("#checkPassword");
        if(checkPassword.length>0){
            if(user.password!=checkPassword.val()){
                errorText += "  </br>   密码两次输入不一致";
                user.isPass = false;
            }
        }

    } else {
        errorText += "  </br>   密码在6-12位";
        user.isPass = false;

    }

    if ( user.verifyNum.length!=4) {
        errorText += " </br> 校验码为四个字符";
        user.isPass = false;

    }
    if (!user.isPass) {
        console.log(errorText)
        $(".errorInf span").html(errorText);

    }else {
        $(".errorInf span").html("");

    }
    return user;

}

$(".login-table .submit").click(function () {
    var result=validate();
//    console.log(result);
//    if (result.isPass) {
//        $.ajax({
//            type: 'POST',
//            url: "users/login/",
//            data: result,
//            success: function (data) {
//                if(data.status==200)
//                    alert("成功");
//                else {
//                    alert("!=200成功");
//
//                }
//            },
//            error: function (e) {
//                alert("运气不大好");
//            }
//        });
//    } else {
//    }
});

//$(".register-table .submit").click(function () {
//    var result=validate();
//    if (result.isPass) {
//        $.ajax({
//            type: 'POST',
//            url: "/",
//            data: result,
//            success: function (data) {
//                if(data.status==200)
//                    alert("成功");
//                else {
//                    alert("!=200成功");
//
//                }
//            },
//            error: function (e) {
//                alert("运气不大好");
//            }
//        });
//    } else {
//    }
//});

// $(".login-table .submit").click(function () {
//     if(){
//
//     }
//
// });
