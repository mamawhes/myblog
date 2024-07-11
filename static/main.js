function AppendNavElement(nav,text,href,is_blank=false){
    var a=document.createElement("a");
    a.href=href;
    if(is_blank){
        a.target="_blank";
    }
    a.appendChild(document.createTextNode(text));
    nav.appendChild(a);
}
function SetNav(){
    var nav =document.getElementsByTagName("nav")[0];
    AppendNavElement(nav,"博客","/");
    AppendNavElement(nav,"书影音","/");
    
    AppendNavElement(nav,"关于我","/article/0");   
}
function SetSideNav(){
    var nav =document.getElementsByClassName("side-nav")[0];
    AppendNavElement(nav,"billbill","https://space.bilibili.com/1138218681",true);
    AppendNavElement(nav,"github","https://github.com/mamawhes",true);
    AppendNavElement(nav,"gitee","https://gitee.com/mamawhes",true);  
    AppendNavElement(nav,"csdn","https://blog.csdn.net/qq_38830492",true);  
}
function InitTemplates(){
    SetNav();
    SetSideNav();
}