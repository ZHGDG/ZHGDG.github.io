---
layout: post
author: zoomq
title: D码点评:3 Obfuscated Python 
description: ~ 麻辣评点,善意满盈
categories: gDgcoDe
tags:  gdg D码点评 dd wechat coding
---

据说在每一个村委会办公室里,都有一个扫地的老太太. 很偶然地,当她经过一个审计师的身边,扫一眼屏幕上的EXCEL,会低声提醒对方说:小心,现金流量表不平的. 



# 谁说使用 Python 你就写不出混乱的代码?



本文是从 [Penrose Tiling in Obfuscated Python](http://preshing.com/20110822/penrose-tiling-in-obfuscated-python)
这篇文章翻译而来. 

谁说使用Python你就写不出混乱的代码?

<!--more-->

下面这段Python代码是用来生成一些[彭罗斯铺砖](http://en.wikipedia.org/wiki/Penrose_tiling)图案的. 不错,这是段可运行的Python代码:

{% highlight python %}
_                                 =\
                                """if!
                              1:"e,V=100
                            0,(0j-1)**-.2;
                           v,S=.5/  V.real,
                         [(0,0,4      *e,4*e*
                       V)];w=1          -v"def!
                      E(T,A,              B,C):P
                  ,Q,R=B*w+                A*v,B*w+C
            *v,A*w+B*v;retur              n[(1,Q,C,A),(1,P
     ,Q,B),(0,Q,P,A)]*T+[(0,C            ,R,B),(1,R,C,A)]*(1-T)"f
or!i!in!_[:11]:S       =sum([E          (*x)for       !x!in!S],[])"imp
  ort!cair               o!as!O;      s=O.Ima               geSurfac
   e(1,e,e)               ;c=O.Con  text(s);               M,L,G=c.
     move_to                ,c.line_to,c.s                et_sour
       ce_rgb                a"def!z(f,a)                :f(-a.
        imag,a.       real-e-e)"for!T,A,B,C!in[i       !for!i!
          in!S!if!i[""";exec(reduce(lambda x,i:x.replace(chr
           (i),"\n "[34-i:]),   range(   35),_+"""0]]:z(M,A
             );z(L,B);z         (L,C);         c.close_pa
             th()"G             (.4,.3             ,1);c.
             paint(             );G(.7             ,.7,1)
             ;c.fil             l()"fo             r!i!in
             !range             (9):"!             g=1-i/
             8;d=i/          4*g;G(d,d,d,          1-g*.8
             )"!def     !y(f,a):z(f,a+(1+2j)*(     1j**(i
             /2.))*g)"!for!T,A,B,C!in!S:y(M,C);y(L,A);y(M
             ,A);y(L,B)"!c.st            roke()"s.write_t
             o_png('pen                        rose.png')
             """                                       ))
{% endhighlight %}

当这段代码运行时,它会产生一个1000×1000的png格式的彭罗斯铺砖图案,里面包含有大概2212个具有3D浮雕效果的彭罗斯铺砖图. 下图是这个图片的一部分:

![](http://0.zoomquiet.top/ZHGDG/wechat/130910-dd3-penrose-cropped.jpg)

这个脚本需要 [Pycairo](http://cairographics.org/pycairo/) 代码库. 它只能运行在Python <= 2.7 版本上;Phthon 3并不支持. 最初它是一个很正常的脚本,但经过我的努力,出现了神奇的视觉效果. 

彭罗斯铺砖法是个很神奇的东西,它的图案呈不规则周期状分布--你移动角度后都找不到再次重合的图案. 它由罗杰·彭罗斯(Sir Roger Penrose)经过无数次的五边形铺拼试验而成. 

相对于C和Perl,Python很少被认为是一种容易产生混乱的代码的语言. 似乎从来没有人挑战过这种观点,网上也很少找到混乱的Python代码的例子:
你可以在 [Phthon官方问答区](http://docs.python.org/faq/programming.html#is-it-possible-to-write-obfuscated-one-liners-in-python) 里和像 
[这里](http://p-nand-q.com/python/obfuscated_python.html)
和 
[这里](http://c2.com/cgi/wiki?ObfuscatedPython)
的一些页面中发现一些. 这还有一个在
[PyCon 2011大会上的谈话](http://pycon.tv/video/46/)
上的谈话. 

我相信这是第一个能输出高分辨率图片的混乱的Python代码. 如果你还知道一些其它的,请在评论中分享出来!


## 所以!
无论多么注重规整的语言,人总是能写出非常奇葩的代码来!

所以,项目中,最不靠谱的就是人,最能靠谱的也只能是人...




## 9.14 珠海首届 DevFest:

- 预订问卷: http://f.jeffkit.info/zoomquiet/devfest914zh/     
- 持续一整天的 开发者 节日
- 多种前沿技术的体验分享
- 丰富的活动形式
- 给力的 BBQ 午餐
- ... 
- 及时报名,才有席位哪!




## 巡阅
- 150113 [Zoom.Quiet](http://zoomquiet.io/) checked



