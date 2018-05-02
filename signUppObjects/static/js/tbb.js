$(window).scroll(function(){
    if($(window).scrollTop()>86){
        $(".nav").css("background","rgba(255,255,255,0.8)");
        $(".nav").css("height","50px");
        $(".nav").find(".nav-s .nav-nav .nav-ul").css("height","50px");
        $(".nav").find(".nav-s .nav-log").css("height","52px");
        $(".nav").find(".nav-s .nav-nav .nav-ul .nav-li").css("height","50px");
        $(".nav").find(".nav-s .nav-nav .nav-ul .nav-li .nav-con").css("padding-top","12px");
        $(".nav").find(".nav-s .nav-nav .nav-ul .nav-li .nav-con").css("height","42px");

    }
    else{
        $(".nav").css("background","rgba(255,255,255,1)");
        $(".nav").css("height","66px");
        $(".nav").find(".nav-s .nav-nav .nav-ul").css("height","60px");
        $(".nav").find(".nav-s .nav-log").css("height","66px");
        $(".nav").find(".nav-s .nav-nav .nav-ul .nav-li").css("height","66px");
        $(".nav").find(".nav-s .nav-nav .nav-ul .nav-li .nav-con").css("padding-top","26px");
        $(".nav").find(".nav-s .nav-nav .nav-ul .nav-li .nav-con").css("height","56px");
    }
})

$(function(){
    $(".getttt").each(function(i){
        $(".getttt").eq(i).click(function(){
            $.get("get-kit.php",{classid:$(".getttt").eq(i).find("i").text()},function(data){
                $(".kit-div").html(data);
            })
        })
    })
})
$(function(){
    $(".but").click(function(){
        $("#videos-show").css("display","block");
        $.get("get-video.php",{},function(data){
            $("#videos-show").html(data);
        })
    })
})
$(function(){
    $(".box-show").click(function(){
        $("#videos-show").css("display","none");
    })
})
$(function(){
    $(".t-li-z").each(function(i){
        $(".t-li-z").eq(0).next(".co-li").show();
        $(".t-li-z").eq(0).find(".ii").addClass("ii-z");
        $(".t-li-z").eq(i).find(".ii").click(function(){
            if($(".t-li-z").eq(i).next(".co-li").is(":hidden")) {
                $(this).addClass("ii-z");
                $(".t-li-z").eq(i).next(".co-li").show(300);
            }else{
                $(this).removeClass("ii-z");
                $(".t-li-z").eq(i).next(".co-li").hide(250);
            }
        })
    })
})

$(function(){
    var $h=$(window).height();
    //var $w=$(window).width();
    //$("#videos-show").css("width",$w);
    $("#videos-show").css("height",$h);
    //$("#videos-s").attr("height",$h);
    //$("#videos-s").attr("width",$w);
})