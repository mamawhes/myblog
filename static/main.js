function AppendNavElement(nav,text,href){
    var a=document.createElement("a");
    a.href=href;
    a.appendChild(document.createTextNode(text));
    nav.appendChild(a);
}
function SetNav(){
    var nav =document.getElementsByTagName("nav")[0];
    AppendNavElement(nav,"网站导航","/");
    AppendNavElement(nav,"博客","/");
    AppendNavElement(nav,"关于我","/");   
}