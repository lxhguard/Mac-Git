window.onload = function () {

    var oTBody = document.getElementById("itbody");
    var oBtnAdd = document.getElementById("btnadd");
    var submitIT = document.getElementById("submitIT");
    var a;

    oBtnAdd.onclick = function (event) {
        // window.preventDefault(event);
        //alert(oTBody);
        oTBody.innerHTML += "<tr><td class=\"tdOrder\" id=\"tdOrder\">请输入语言项</td><td  class=\"tdName\" id=\"tdName\">请输入意义</td><td><input type=\"button\" value=\"删除\" class=\"btndel\"> <input type=\"button\" value=\"修改\" class=\"btnupdate\" > <input value=\"保存\" type=\"button\" class=\"btnsave\"></td></tr>";
        registerEvent();//注册事件

    }


    function registerEvent() {


                var oBtndels = document.getElementsByClassName("btndel");
                for (i = 0; i < oBtndels.length; i++) {
                    oBtndels[i].onclick = function () {
                        this.parentElement.parentElement.remove(this.parentElement);

                    }
                }
                //-------
                var oBtnUpdate = document.getElementsByClassName("btnupdate");
                for (i = 0; i < oBtnUpdate.length; i++) {
                    oBtnUpdate[i].onclick = function (event) {
                        // window.preventDefault(event);
                        //alert("修改");
                        var oTdOrder = this.parentElement.parentElement.getElementsByClassName("tdOrder");
                        oTdOrder[0].innerHTML = "<input type=\"text\" class=\"iorder\"  value=" + oTdOrder[0].innerText + " />";
                        var otdName = this.parentElement.parentElement.getElementsByClassName("tdName");
                        otdName[0].innerHTML = "<input type=\"text\" class=\"iname\"  value=" + otdName[0].innerText + " />";
                    }
                }
                var obtnsave = document.getElementsByClassName("btnsave");
                for (i = 0; i < obtnsave.length; i++) {
                    obtnsave[i].onclick = function (event) {
                        // window.preventDefault(event);
                        //更改订单号
                        var oTdOrders = this.parentElement.parentElement.getElementsByClassName("tdOrder");
                        //alert(oTdOrders);
                        var ivalue = oTdOrders[0].getElementsByClassName("iorder")[0].value;
                        oTdOrders[0].removeChild(oTdOrders[0].getElementsByClassName("iorder")[0]);
                        oTdOrders[0].innerText = ivalue;
                        //更改商品名称
                        var oTdNames = this.parentElement.parentElement.getElementsByClassName("tdName");
                        //alert(oTdOrders);
                        var iname = oTdNames[0].getElementsByClassName("iname")[0].value;
                        oTdNames[0].removeChild(oTdNames[0].getElementsByClassName("iname")[0]);
                        oTdNames[0].innerText = iname;
                    }
                }

                submitIT.onclick = function () {
                    var xmlhttp;
                    if (window.XMLHttpRequest) {
                        //  IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
                        xmlhttp = new XMLHttpRequest();
                    } else {
                        // IE6, IE5 浏览器执行代码
                        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
                    }
                    xmlhttp.onreadystatechange = function () {
                        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {

                        }
                    }
                    var AllTdOrder = document.getElementsByClassName('tdOrder');
                    var AllTdOrderValue = new Array();
                    var AllTdName = document.getElementsByClassName('tdName');
                    var AllTdNameValue = new Array();
                    var length = 0;
                    var json = [];
                    var j = {
                        pk: '',
                        fields: {}
                    };
                    for (var i = 0; i < AllTdOrder.length; i++) {
                        AllTdOrderValue[i] = AllTdOrder[i].innerHTML;
                        AllTdNameValue[i] = AllTdName[i].innerHTML;
                        length++;
                    }
                    for (i = 0; i < length; i++) {
                        j.pk = AllTdOrder[i].innerHTML;
                        j.fields.dingyi = AllTdName[i].innerHTML;
                        json.push(j);
                    }
                    a = JSON.stringify(json);
                    alert(a);
                    // console.log("length:"+length);
                    // console.log("AllTdOrderValue:" + AllTdOrderValue);
                    xmlhttp.open("POST", "1", true);
                    xmlhttp.send(a);
                }
    }


















}