var isdebug=true;

/***
 * utils 调试打印
 */
function tbblog(text) {
    if (isdebug) {
        console.log("**********************************tbbdebug*****************");
        console.log(text);
    }

}

/***
 *  localstorage本地存储
 * @param keyname
 * @param obj
 */
function saveObjTolocalStorage(keyname, obj) {
    var savejson = JSON.stringify(obj);
    localStorage.setItem(keyname, savejson) //存储名字为name值为savejson的变量
}

/***
 * localstorage获取本地数据
 * @param keyname
 */
function getObjFromlocalStorage(keyname) {
    return JSON.parse(localStorage.getItem(keyname)); //转为JSON
}

function removeLocalStorageBykey(keyname) {
    localStorage.removeItem(keyname);
}
/***
 * 更新supposedPage 的值
 * @param id
 * @param url
 */
function updatesupposedPage(id, url) {
    var supposedPage = {};
    supposedPage.supposedPageID = id;
    supposedPage.url = url;
    saveObjTolocalStorage("supposedPage", supposedPage);
}


/**
 * 音频播放时间换算
 * @param {number} value - 音频当前播放时间，单位秒
 */
function transTime(value) {
    var time = "";
    var h = parseInt(value / 3600);
    value %= 3600;
    var m = parseInt(value / 60);
    var s = parseInt(value % 60);
    if (h > 0) {
        time = formatTime(h + ":" + m + ":" + s);
    } else {
        time = formatTime("0:" + m + ":" + s);
    }

    return time;
}

/**
 * 格式化时间显示，补零对齐
 * eg：2:4  -->  02:04
 * @param {string} value - 形如 h:m:s 的字符串
 */
function formatTime(value) {
    var time = "";
    var s = value.split(':');
    var i = 0;
    for (; i < s.length - 1; i++) {
        time += s[i].length == 1 ? ("0" + s[i]) : s[i];
        time += ":";
    }
    time += s[i].length == 1 ? ("0" + s[i]) : s[i];

    return time;
}

/**
 * 浏览器url 页面传参  参数获取
 * */
function getQueryString() {
    var qs = location.search.substr(1), // 获取url中"?"符后的字串
        args = {}, // 保存参数数据的对象
        items = qs.length ? qs.split("&") : [], // 取得每一个参数项,
        item = null,
        len = items.length;

    for (var i = 0; i < len; i++) {
        item = items[i].split("=");
        var name = decodeURIComponent(item[0]),
            value = decodeURIComponent(item[1]);
        if (name) {
            args[name] = value;
        }
    }
    return args;
}
function isEmpty(obj) {
    return (typeof (obj)) == "undefined" || obj == null;
}