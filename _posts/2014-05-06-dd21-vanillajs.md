---
layout: post
title: D码点评:21 最强大的JS库
description: ~ 麻辣评点,善意满盈
author: zoomq
categories: gDgcoDe
tags:  gdg D码点评 dd wechat coding
---

![vanillajs.jpg(JPEG 图像,388x179 像素)](http://webification.com/wp-content/uploads/2012/09/vanillajs.jpg)

Vanilla JS is a fast, lightweight, cross-platform framework
for building incredible, powerful JavaScript applications.

<!--more-->


# vanilla-js.com

标题并不让我太震惊,所有的框架肯定都喜欢说自己是最好的最快的,然后又看到下面谁在用,列举了各个巨头,到这里也还行,一般框架肯定也会这样宣传啊. 接下来一行小字引起了我的注意:

    In fact, 
    Vanilla JS is already used on more websites 
    than jQuery, Prototype JS, MooTools, YUI, 
    and Google Web Toolkit 
    - combined.

Vanilla JS的使用量是Jquery,Prototype,YUI. . . 的总和还多,这尼玛太扯了吧,在所有的框架里面,Jquery一个就占了接近50%了,总和还多是什么概念,这么厉害我竟然从来没听过. . . 


"生产环境中不需要链接任何文件,这是因为Vanilla JS 太出名以致所有的浏览器都内置了. . . "我擦,你丫不是骗人的吧,这么厉害的库为毛我从来没听人说起过,就算我是新人也应该多多少少有所耳闻吧!


再再接下来就更犀利了,将Vanilla JS与其他库进行速度比较(这个速度也太惊人了吧. . . )

## Retrieve DOM element by ID

<table>
    <tr>
        <td>框架
        </td>
        <td>代码
        </td>
        <td>ops/sec
        </td>
    </tr>
    <tr>
        <td>Vanilla JS 
        </td>
        <td>document.getElementById('test-table');
        </td>
        <td>12,137,211
        </td>
    </tr>
    <tr>
        <td>jQuery
        </td>
        <td>$jq('#test-table');
        </td>
        <td>350,557
        </td>
    </tr>
</table>

## Retrieve DOM element by tag name

<table>
    <tr>
        <td>框架
        </td>
        <td>代码
        </td>
        <td>ops/sec
        </td>
    </tr>
    <tr>
        <td>Vanilla JS 
        </td>
        <td>    document.getElementsByTagName("span");
        </td>
        <td>8,280,893
        </td>
    </tr>
    <tr>
        <td>jQuery
        </td>
        <td>$jq('span');
        </td>
        <td>19,449
        </td>
    </tr>
</table>


## Make an AJAX call

Vanilla JS

    var r = new XMLHttpRequest(); 
    r.open("POST", "path/to/api", true); 
    r.onreadystatechange = function () { 
        if (r.readyState != 4 || r.status != 200) return; 
        alert("Success: " + r.responseText); 
    }; 
    r.send("banana=yellow");

jQuery

    <script src="//ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script> 
    <script> 
    $.ajax({ type: 'POST', 
        url: "path/to/api", 
        data: "banana=yellow", 
        success: function (data) { 
            alert("Success: " + data); 
        }, 
    }); 
    </script>


等等,这个代码怎么那么熟悉. . . 
这跟原生的写法似乎. . 没有太大区别啊. .  

然后是扩展阅读,分别是
documentation,books,plugins,
依次点击进去发现分别是Javascript的文档页,
亚马逊各种Javascript书籍,
维基百科关于Javascript框架的介绍. . . . 

我承认我是已经糊掉了,智商不够就谷歌一下吧. . 然后


Vanilla JS的另一个名字是--Javascript


以上文字来自: [最强大的JS库--Vanilla JS--竹林的博客](http://www.ziyang.me/blog.php?id=24)

以下感慨来自:
[從vanilla-js開始 | 箱猫日和](http://blog.gssxgss.me/back-to-js/)


在寫css時,我是原始人,不用compass,只用sass,less,自己寫mixin. 
但是我寫css的效率并不低,因為我對它太熟悉了. 
如果我的開發環境里沒有提供less或sass的環境,我照樣能寫css. 

可是,我並不熟悉javascript,jQuery的便捷讓我甚至不記得怎麼取Text Node. 
如果沒有在body最後引入jQuery,我就變得像流落到荒島的魯濱遜. 
那麼,從現在開始學會怎麼鑽木取火,怎麼獲取食物,怎麼在荒島生存下去吧. 
說不定哪天我還能在荒島發明出城市裡沒有的東西. 
從現在開始,還不晚. 
所以,我決定從現在開始拾起vanilla-js,迴歸到荒島上去. 

    效率,是工作上的事情. 
    知識,是自己的事情. 


## 是也乎

大妈只能无法同意更多了...

在收集 Vanilla 相关资料时,经历的心理过程和前述那位真心一样...

其实,框架/库 的出现,就是为了解决程序员对领域常见事务/问题解决时的开发效率问题.

只是,一般解决的方式,是通过隐藏关键思考/经验细节,提供一个更加舒服的接口/函式/范式,
但是,世界是多样的,问题领域一直在高速变化,
能够凝结成 框架/库 的那些经验/知识,不一定可以 cover 住当前我们面对的问题,
所以,很多时候,我们必须有 `亮剑` 精神,
敢于从0开始,一行行用纯粹语言本身的能力,
配合自个儿的经验,攻克之.

这种问题的解决才是真正的解决,因为这是用自个儿的经验完成的.

但是,这种解决,必然的需要大量的时间和反复的调试.

要不团队允许/理解 你的`亮剑`;
要不,你的 `亮剑` 和正常开发用时几乎一样.

否则,千万别亮,一亮即死...






## 巡阅
- 150113 [Zoom.Quiet](http://zoomquiet.io/) checked




