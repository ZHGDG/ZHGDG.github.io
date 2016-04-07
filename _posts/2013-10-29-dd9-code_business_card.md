---
layout: post
author: zoomq
title: D码点评:9 卡片代码
description: ~ 麻辣评点,善意满盈
categories: gDgcoDe
tags:  gdg D码点评 dd wechat coding
---

~名片光线跟踪

#[Decyphering the Business Card Raytracer](http://fabiensanglard.net/rayTracing_back_of_business_card/index.php)

<!--more-->


    #include <stdlib.h>   // card > aek.ppm
    #include <stdio.h>
    #include <math.h>
    typedef int i;typedef float f;struct v{
    f x,y,z;v operator+(v r){return v(x+r.x
    ,y+r.y,z+r.z);}v operator*(f r){return
    v(x*r,y*r,z*r);}f operator%(v r){return
    x*r.x+y*r.y+z*r.z;}v(){}v operator^(v r
    ){return v(y*r.z-z*r.y,z*r.x-x*r.z,x*r.
    y-y*r.x);}v(f a,f b,f c){x=a;y=b;z=c;}v
    operator!(){return*this*(1/sqrt(*this%*
    this));}};i G[]={247570,280596,280600,
    249748,18578,18577,231184,16,16};f R(){
    return(f)rand()/RAND_MAX;}i T(v o,v d,f
    &t,v&n){t=1e9;i m=0;f p=-o.z/d.z;if(.01
    <p)t=p,n=v(0,0,1),m=1;for(i k=19;k--;)
    for(i j=9;j--;)if(G[j]&1<<k){v p=o+v(-k
    ,0,-j-4);f b=p%d,c=p%p-1,q=b*b-c;if(q>0
    ){f s=-b-sqrt(q);if(s<t&&s>.01)t=s,n=!(
    p+d*t),m=2;}}return m;}v S(v o,v d){f t
    ;v n;i m=T(o,d,t,n);if(!m)return v(.7,
    .6,1)*pow(1-d.z,4);v h=o+d*t,l=!(v(9+R(
    ),9+R(),16)+h*-1),r=d+n*(n%d*-2);f b=l%
    n;if(b<0||T(h,l,t,n))b=0;f p=pow(l%r*(b
    >0),99);if(m&1){h=h*.2;return((i)(ceil(
    h.x)+ceil(h.y))&1?v(3,1,1):v(3,3,3))*(b
    *.2+.1);}return v(p,p,p)+S(h,r)*.5;}i
    main(){printf("P6 512 512 255 ");v g=!v
    (-6,-16,0),a=!(v(0,0,1)^g)*.002,b=!(g^a
    )*.002,c=(a+b)*-256+g;for(i y=512;y--;)
    for(i x=512;x--;){v p(13,13,13);for(i r
    =64;r--;){v t=a*(R()-.5)*99+b*(R()-.5)*
    99;p=S(v(17,16,8)+t,!(t*-1+(a*(R()+x)+b
    *(y+R())+c)*16))*3.5+p;}printf("%c%c%c"
    ,(i)p.x,(i)p.y,(i)p.z);}}


使用如下命令编译:

    c++ -O3 -o card card.cpp
    ./card > card.ppm


再运行, 作者的 MacBook Air 上, 用27秒,可以生成以下图片!

![fab.png(PNG 图像,512x512 像素)](http://fabiensanglard.net/rayTracing_back_of_business_card/fab.png)


拥有复杂光线追踪能力的程序!


代码来自这一页面的活动:
http://fabiensanglard.net/rayTracing_back_of_business_card/index.php

作者想将 Paul Heckbert 在
1984年5月4日提出的有关光线追踪挑战赛的代码,
精简到一张名片的背面!

并包含以下功能:


- 世界由精心组织的球体构成
- 存在指定样式的地板和质感
- 天空有很好的颜色梯度
- 阴影是柔的
- 妈呀,还必须有景深的模糊梯度!

最终这哥儿们作到了,并在此逐步分享了实现的过程!


## 是也乎

大家可能第一反应是,这这么折腾有用嘛!?

好的,其实是有用的,很多用途, 但是,大妈就不扫盲了!

今天分享这段代码,其实是因为昨天看到了这幅漫画:

[为毛你不该打扰程序员?!](http://weibo.com/1894238970/Ag9dc6A9f)

所以,想展示一下, 编程,这门手艺一个极端的案例,
来请大家设想一下, 全神贯注思考问题时, 程序猿的脑海里,
可能凭空创造出多么美丽的世界!

是的,人的大脑是没有界限的,只要我们愿意激发之!

编程是各种激发行为中,最值得尝试的!




# 当期活动 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## 珠海GDG[10.26]相约美丽.程序媛专场活动

期待已久的技术美女活动结束了,研究有什么惊喜?!

❤共同期待❤


# 筹备活动 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## PyCon2013CHina 珠海场

- Python 年度大会
- Pythonner 大趴
- Pythonista 相亲集会
- Pythonic 体验交流

请及时举报你身边的 华蠎行者!
举报热线: zoomquiet+pycon (AT) gmail.com



## 巡阅
- 150113 [Zoom.Quiet](http://zoomquiet.io/) checked





