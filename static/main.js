function SetHref(){
    var navs= document.getElementsByTagName("nav")[0].children;
    console.log(navs)
    for(var i=0;i<navs.length;i++){
        var element=navs[i]
        if(element.innerHTML=="网站导航"){
            element.href="/";
        }
        if(element.innerHTML=="博客"){
            element.href="/";
        }
        if(element.innerHTML=="关于我"){
            element.href="/";
        }
    }
    // navs.forEach(element => {
    
    // });

}