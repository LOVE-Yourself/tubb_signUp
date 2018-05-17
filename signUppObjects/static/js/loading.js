//获取浏览器页面可见高度和宽度
var _PageHeight = document.documentElement.clientHeight,
    _PageWidth = document.documentElement.clientWidth;
//计算loading框距离顶部和左部的距离（loading框的宽度为215px，高度为61px）
var _LoadingTop = _PageHeight > 389 ? (_PageHeight - 389) / 2 : 0,
    _LoadingLeft = _PageWidth > 397 ? (_PageWidth - 397) / 2 : 0;
//在页面未加载完毕之前显示的loading Html自定义内容
var _LoadingHtml = '<div id="loadingDiv" style="position:absolute;left:0;width:100%;height:' + _PageHeight + 'px;top:0;background: rgb(255,255,255);opacity:1;filter:alpha(opacity=80);z-index:10000;"><div style="position: absolute; cursor: wait; left: ' + _LoadingLeft + 'px; top:' + _LoadingTop + 'px; width: 397px; height: 389px; line-height: 57px; padding-left: 50px; padding-right: 5px; background: rgb(255,255,255) url(/images/Loading.gif) no-repeat scroll 5px 10px; color: #696969; font-family:\'Microsoft YaHei\';"><!--Loading...  --></div></div>';
//呈现loading效果
document.write(_LoadingHtml);

//window.onload = function () {
//    var loadingMask = document.getElementById('loadingDiv');
//    loadingMask.parentNode.removeChild(loadingMask);
//};

//监听加载状态改变
document.onreadystatechange = completeLoading;

//加载状态为complete时移除loading效果
function completeLoading() {
    if (document.readyState == "complete") {
        var loadingMask = document.getElementById('loadingDiv');
        loadingMask.parentNode.removeChild(loadingMask);
    }
}

$(window).resize(function (e) {

    var winWidth = $(window).width();
    if (winWidth >768) {
        if ($(".operationMenu.hidden").length != 0) {
            $(".operationMenu").removeClass("hidden");
        }

    }else {
        $(".operationMenu").addClass("hidden");

    }
})

init();

function init() {
    var page = getQueryString();
    var pageOrder = parseInt(page["showGet"]);
    if (isEmpty(page["showGet"]))
        pageOrder = 0;
    var menu = $(".nav-nav .nav-ul .nav-li").eq(pageOrder);
    $(menu).addClass("active");
    var winWidth = $(window).width();
    if (winWidth >768) {
        if ($(".operationMenu.hidden").length != 0) {
            $(".operationMenu").removeClass("hidden");
        }

    }else {
        $(".operationMenu").addClass("hidden");

    }
}

var swith = false;
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
$(".banner").click(function () {
    // location.href="../templates/getCoupon.html"

})
$(".curriculumDetail .entryBtn").click(function () {
    location.href = "../templates/writeOrderForm.html"

})
//$(".curriculum  .detailBtn").click(function () {
//    var element = this;
//    var coupon = $(element).find("input.curri_id").val();
//    location.href = "../templates/curriculumDetail.html?curri_id=" + coupon + "&showGet=1";
//
//})

$(".nav-nav .user").click(function () {
    location.href = "../templates/personalOrder.html"

})
$(".getCouponDiv.available .getCouponBtn").click(function () {
    var element = this;
    var coupon_id = $(element).find("input.couponId").val();
    var active_id = $(element).find("input.activeId").val();
    $.ajax({
        type: 'POST',
        url: appConfig.requestUrl + "/course/get_coupon/",
        data: {coupon_id: coupon_id, active_id: active_id},
        success: function (data) {
            if (data.status == 200){
                location.reload();
            }
            if (data.status == 202) {
                showLogin();
            }
        },
        error: function (e) {

        }
    });

});
//pay
$(".orderForm  .payBtnDiv .payBtn").click(function () {
    var userName = $(".orderForm #userName").val();
    var curriculumName = $(".orderForm #curriculumName").text();
    var payMethod = $(".orderForm input[name='payMethod']:checked").val();
    var totalPayMoney = $(".orderForm #totalPayMoney").text();

    var myDate = new Date();
    Date.prototype.toStr = function()
    {
        var myDate = this;
        var thisTimeStr = "";
        thisTimeStr += myDate.getFullYear();
        thisTimeStr += myDate.getMonth()+1;
        thisTimeStr += myDate.getDate();
        thisTimeStr += myDate.getHours();
        thisTimeStr += myDate.getMinutes();
        thisTimeStr += myDate.getSeconds();
        return thisTimeStr;
    }
    var rand= Math.floor(Math.random () * 900) + 100;
    // console.log(rand)
    // console.log(myDate.toStr()+rand)
    console.log({payOrderId:myDate.toStr()+rand,userName: userName, payMethod: payMethod,curriculumName:curriculumName,totalPayMoney:totalPayMoney});
    var regname=/^[a-zA-Z0-9_]{3,4}$/ ;
    if(regname.test(userName)){
        $(".orderForm .error").html("请输入姓名");
    }else {
        $(".orderForm .error").html("");

    }
    console.log(userName+payMethod);
    $.ajax({
        type: 'POST',
        url: 'test.tuobaba.cn:5020'+ "/pay/payfor/",
        data: {orderId:myDate.toStr()+rand,userName: userName, payMethod: payMethod,curriculumName:curriculumName,totalPayMoney:totalPayMoney},
        success: function (data) {
            if (data.status == 200){
                // alert("报名成功！")
                location.href=data.payUrl;
            }

        },
        error: function (e) {

        }
    });

});


$('.paySuccessMain .lookOrderBtn').click(function () {

    location.href = "../templates/personalOrder.html"


})

if (typeof WeixinJSBridge == "undefined") {
    // return true;
}

$(function () {
    $(".panel-heading a").click(function (e) {
        /*切换折叠指示图标*/
        $(this).find("li").toggleClass("fa-chevron-down");
        $(this).find("li").toggleClass("fa-chevron-up");
    });
});


$('.personalRight').click(function () {
    var winWidth = $(window).width();
    console.log(winWidth);
    if (winWidth <= 768) {
        if ($(".operationMenu.hidden").length == 0) {
            $(".operationMenu").addClass("hidden");
            $(".individualCenter .menuToRightBtn i ").toggleClass("fa-angle-right");
            $(".individualCenter .menuToRightBtn i").toggleClass("fa-angle-left");
        }

    }

})


$(".tabs span").click(function () {
    var elem = $(this);
    console.log(elem);


})

$(".panel-body").click(function () {
    var elem = this;
    $(".displayContent").css("display", "none");
    var targetElem = $(elem).parent("a").attr("aria-controls");
    console.log(targetElem);
    $(targetElem).css("display", "block");
    var winWidth = $(window).width();
    if (winWidth <= 768) {
        if ($(".operationMenu.hidden").length == 0) {
            $(".operationMenu").addClass("hidden");
            $(".individualCenter .menuToRightBtn i ").toggleClass("fa-angle-right");
            $(".individualCenter .menuToRightBtn i").toggleClass("fa-angle-left");
        }
    }

})


$('.tabs span').each(function (index, item) {
    $(item).click(function () {
        $('.tabs span').removeClass("active");
        $(".tabs span").eq(index).addClass("active");
        $(".tabContent").removeClass("active");
        $(".tabContent").eq(index).addClass("active");
    })
});

$(".userInf .realNameDiv .fa-edit").click(function () {
    $(".personalRight .realNameDiv input").toggleClass("editable");
    $(".personalRight .realNameDiv input").toggleClass("Disable");
    // $(".userInf .realNameDiv .fa-edit").remove();


})

function userNameChange() {
    // $(".realNameDiv button[type=\"submit\"]").css("display","inline-block");

    $(".realNameDiv button[type=\"submit\"]").click();

}

$(".userIconDiv #userIcon img").click(function () {
    var elem = $(this);
    console.log(elem);
    // $("#head").click();

})


// 上传图片前预览
function previewImage(file) {
    var MAXWIDTH = 120;  // 最大图片宽度
    var MAXHEIGHT = 120;  // 最大图片高度
    if (file.files && file.files[0]) {
        var img = document.getElementById('preview');
        img.onload = function () {
            var rect = getZoomParam(MAXWIDTH, MAXHEIGHT, img.offsetWidth, img.offsetHeight);
            img.width = rect.width;
            img.height = rect.height;
        }
        var reader = new FileReader();
        reader.onload = function (evt) {
            img.src = evt.target.result;
        }
        reader.readAsDataURL(file.files[0]);
    } else {
        //兼容IE
        file.select();
        var src = document.selection.createRange().text;
        var img = document.getElementById('preview');
        img.filters.item('DXImageTransform.Microsoft.AlphaImageLoader').src = src;
    }
}

// 获取缩放的尺寸
function getZoomParam(maxWidth, maxHeight, width, height) {
    var param = {top: 0, left: 0, width: width, height: height};
    if (width > maxWidth || height > maxHeight) {
        rateWidth = width / maxWidth;
        rateHeight = height / maxHeight;
        if (rateWidth > rateHeight) {
            param.width = maxWidth;
            param.height = Math.round(height / rateWidth);
        } else {
            param.width = Math.round(width / rateHeight);
            param.height = maxHeight;
        }
    }
    param.left = Math.round((maxWidth - param.width) / 2);
    param.top = Math.round((maxHeight - param.height) / 2);
    param.height = 120;
    return param;
}

function showLogin() {
    $("#loginMask").css("display", "block");

}

function hidenLogin() {
    $("#loginMask").css("display", "none");

}

$(".closeLoginModule button").click(function () {
    hidenLogin();
})
$("button.menuToRightBtn").click(function () {
    $(".individualCenter .operationMenu").toggleClass("hidden");
    $(".individualCenter .menuToRightBtn i ").toggleClass("fa-angle-right");
    $(".individualCenter .menuToRightBtn i").toggleClass("fa-angle-left");
})
setTimeout(function () {
    showLogin();
}, 1000)

