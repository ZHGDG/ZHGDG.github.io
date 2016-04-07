---
title: 珠海GDG的硬件资源平台---Cubieboard,手把手带你玩
author: snowy
layout: post
categories: Events
tags:  gdg cbi event summary
---


![](http://cubieboard.org/wp-content/uploads/2013/09/lubuntu-default-wallpaper-310x190.png)

作为珠海GDG的硬件资源平台---Cubieboard的菜鸟粉丝,我想分享一个人人都能做的,基于Cubieboard板子的"两只老虎"的音乐小demo. 

<!--more-->


###原理:

主要是通过更改蜂鸣器的频率来改编歌曲

###硬件:

CubieTruck+DVK570

![CubieTruck](http://www.waveshare.net/photo/development-board/CubieTruck/CubieTruck-5.jpg)

![CubieTruck](http://www.waveshare.net/photo/accBoard/DVK570/DVK570-intro.jpg)

###源码关键点:

####头文件:
stdio.h,stdlib.h,fcntl.h,errno.h,unistd.h,sys/ioctl.h,string.h

####音阶频率转换:
\#define 名称 "echo 频率 > /sys/class/pwm-sunxi/pwm0/period"

如:\#define PWM_PERIOD1 "echo 2093hz > /sys/class/pwm-sunxi/pwm0/period"

####使蜂鸣器发声:
system(名称);

如:system(PWM_PERIOD1);

####延时:
usleep(时间);

如:usleep(500*500);

["两只老虎"音乐源码](http://forum.cubietech.com/forum.php?mod=viewthread&tid=2970&extra=page%3D1)

想看演示效果?[点我](http://www.meipai.com/media/65895457)

![](http://b175.photo.store.qq.com/psb?/V12iMJn01q9o6X/92lno93JdDcl3bNfr7Kj6HZ3ix3y5Nv.Rj9uMgizo6Q!/b/dNWVVmjRKQAA&bo=3QHdAQAAAAADByI!&rf=viewer_4)

是不是很简单呢?大家可以找一个简单的乐谱,来调一首自己喜欢的音乐～

另附一份[音阶频率表](http://wenku.baidu.com/view/b3921b22192e45361066f5b3.html?re=viewl)




## 巡阅
- 150113 [Zoom.Quiet](http://zoomquiet.io/) checked




