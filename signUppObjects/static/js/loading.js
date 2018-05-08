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

init();

function init() {
    var page = getQueryString();
    var pageOrder = parseInt(page["showGet"]);
    if (isEmpty(page["showGet"]))
        pageOrder = 0;
    var menu = $(".nav-nav .nav-ul .nav-li").eq(pageOrder);
    $(menu).addClass("active");
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
$(".curriculumDetial .entryBtn").click(function () {
    location.href = "../templates/writeOrderForm.html"

})
$(".curriculum  .detailBtn").click(function () {
    var element = this;
    var coupon = $(element).find("input.curri_id").val();
    location.href = "../templates/curriculumDetail.html?curri_id=" + coupon + "&showGet=1";

})
$(".getCouponDiv.available .getCouponBtn").click(function () {
    var element = this;
    var coupon = $(element).find("input.couponId").val();
    $.ajax({
        type: 'POST',
        url: "",
        data: coupon,
        success: function (data) {
            if (data.status == 200)
                alert("领取成功");
            else {
                alert("!=200成功");
            }
        },
        error: function (e) {

        }
    });

});


if (typeof WeixinJSBridge == "undefined") {
    // return true;
}

$(function(){
    $(".panel-heading a").click(function(e){
        /*切换折叠指示图标*/
        $(this).find("li").toggleClass("fa-chevron-down");
        $(this).find("li").toggleClass("fa-chevron-up");
    });
});


$('#myCollapsible').collapse({
    toggle: false
})



$(".tabs span").click(function () {
    var elem=$(this);
    console.log(elem);



})



$('.tabs span').each(function (index, item) {
    $(item).click(function () {
        $('.tabs span').removeClass("active");
        $(".tabs span").eq(index).addClass("active");
        $(".tabContent").removeClass("active");
        $(".tabContent").eq(index).addClass("active");
    })
});