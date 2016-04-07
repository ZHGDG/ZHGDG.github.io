---
layout: post
title: 怀念童年之经典街机游戏"拳皇97"玩在Cubieboard
author: snowy
categories: HaiDoc
tags:  cubieboard share game
---

![](http://forum.cubietech.com/data/attachment/forum/201404/21/112005r9mnaxzu3p8zamgx.jpg)

相信对于很多玩过单片机的玩家,利用GPIO接口制作出一些"小玩意"已经是很菜鸟的事了
所以在Cubieboard上如何玩它的GPIO接口就不多说了<br>
Cubieboard上除了它的GPIO接口,还有没有趣味的且不用外接模组的玩法?<br>
答案是肯定有的<br>
下文将和大家分享一篇在Linux环境下使用Cubieboard移植模拟器和怎样使用模拟器玩"拳皇97"的教程<br>
Cubieboard带领大家重温童真般的街机时代!!!<br>

<!--more-->

# Cubieboard---街机移植

## 1.移植概述
大家因为学习,工作等等原因加入了Cubieboard和Linux的行列,闲暇时我们也可以用Cubieboard上玩玩游戏. 那么模拟器玩街机就是一个不错的选择. 模拟器种类繁多,这里给出一种gngeo的移植方法. <br>
本文档将介绍在Linux环境下移植模拟器和怎样使用模拟器中玩"拳皇97". 在接下来的文档中首先了解街机移植所需要的文件,与各个文件的作用. 然后在详细介绍各个文件怎样安装,并且给出在安装各个文件过程中可能出现的错误与对应错误的解决方案. 最后将已"拳皇97"为例测试模拟器. <br>

## 2.移植效果
Gngeo 模拟器界面<br>
![Gngeo 模拟器界面](http://forum.cubietech.com/data/attachment/forum/201404/21/112003a4p05j301kijqszq.jpg)
<br>
"拳皇97"界面<br>
!["拳皇97"界面](http://forum.cubietech.com/data/attachment/forum/201404/21/112005r9mnaxzu3p8zamgx.jpg)

## 3.移植流程
### 3.1源文件
#### 1)gngeo-0.6.3.tar.gz
在linux不止一个街机模拟器. Gngeo就是一款专门玩neogeo游戏的街机模拟器<br>
下载地址:[Gngeo](http://m.peponas.free.fr/gngeo/download/gngeo-0.6.3.tar.gz)<br>
#### 2)neogeo.zip
Gngeo和大多数模拟器一样也需要一个Bios文件,那就是neogeo<br>
下载地址:[Neogeo](http://www.pcsky.cn/download/SoftView/SoftView_4832.html)<br>
#### 3)xgngeo-14.tar.bz2
Gngeo的前端搭档文件<br>
下载地址:[Xgngeo](http://download.berlios.de/xgngeo/xgngeo-14.tar.bz2)<br>
#### 4)kof97.zip
"拳皇97"源码文件<br>
下载地址:[Kof97](http://www.downcn.com/down_soft.php?id=374&no=1)<br>

### 3.2移植步骤
#### 1)移植gngeo模拟器
##### a)将gngeo-0.6.3.tar.gz拷到任意一个用户家目录下
`# cp gengeo-0.6.3.tar.gz  ~/`
##### b)解压gengeo
`# tar zxvf gngeo-0.6.3.tar.gz`
##### c)拷贝gengeo配置文件到家目录下
到在自己的家目录下建立.gngeo目录,在解压完的gngeo-0.6.3目录下找到sample_gngeorc这个文件, 将它复制到.gngeo目录下并改名为gngeorc . <br>
`# mkdir  ~/.gengeo`<br>
`# cp   ~/gngeo-0.6.3/sample_gngeorc   ~/.gengeo/gngeorc`
##### d)安装gngeo
`# cd gngeo-0.6.3`<br>
`# ./configure --prefix=/usr/local `<br>
`#make`<br>
`#make install`
#### 2)加入依赖的Bios文件neogeo
`# cp -a  neogeo.zip  /usr/local/share/gngeo`<br>
`# cd  /usr/local/share/gngeo`<br>
`# unzip neogeo.zip`<br>
`# rm -f  neogeo.zip`
#### 3)安装gngeo前端搭档xgngeo
##### a)在家目录下建立roms目录,把xgngeo-14.tar.gz考到roms下
`# mkdir  ~/roms`<br>
`# tar  jxvf  xgngeo-14.tar.gz`
##### b)运行模拟器
`#  cd  xgngeo-14`<br>
`#  ./xgngeo.py`
### 3.3安装疑问
#### 1)移植gngeo:/configure --prefix=/usr/local时出现错误
error: can't find sdl-config on your system<br>
解决方案:安装依赖库<br>
`# apt-get update`<br>
`# apt-get install libsdl-*`
#### 2)移植gngeo:make 时出现错误
scanline.c: In function 'effect_scanline_update':<br>
scanline.c:31:16: error: lvalue required as left operand of assignment<br>
..............................<br>
解决方案:<br>
编辑 ~/gngeo-0.6.3/src/effect/scanline.c,在对应报错的行里,把第一次出现(uint16  *) 去掉<br>
`# vim  ~/gngeo-0.6.3/src/effect/scanline.c`
#### 3)移植gngeo:make 时出现错误
In function 'update_double':<br>
soft.c:57:16: error: lvalue required as left operand of assignment<br>
..............................<br>
解决方案:<br>
编辑 ~/gngeo-0.6.3/src/blitter/soft.c,在对应报错的行里,把第一次出现(uint16  *) 去掉<br>
`# vim  ~/gngeo-0.6.3/src/blitter/soft.c`
#### 4)移植gngeo:make时出现错误
def68k.c:1322:5:error:non-static declaration of 'clocks_movetable' follows static         declaration<br>
解决方案:<br>
编辑 ~/gngeo-0.6.3/generator68k/def68k.c ,在1322行前加一个static<br>
`# vim  ~/gngeo-0.6.3/generator68k/def68k.c +1322`
### 3.4测试运行
#### 1)将下载好的"kof97.zip"拷贝到家目录的roms目录,并执行模块器
`#  cp kof97.zip  ~/roms `<br>
`#  cd  ~/roms/ xgngeo-14`<br>
`# ./xgngeo.py`
#### 2)配置模拟器
##### a)菜单栏->config->path
Roms & Bios directory 中填入 /usr/local/share/gngeo/<br>
Path to Romrc 中填入  /usr/local/share/gngeo/romrc<br> 
##### b)菜单栏->config->Graphic
Blittter选择 YUV bitter (YV12)
##### c)菜单栏->config ->Keys
设置player1,player2按键
##### d)File -> Load From File
找到kof97.zip,想要其他的街机只需要上网上下载相应的游戏源码即可
##### e)File -> 执行


原文出处:[cubie.cc](http://forum.cubietech.com/forum.php?mod=viewthread&tid=2444&extra=page%3D1)<br>
<b>教程版权归属作者:carpediem(UID: 3110)</b> 




## 巡阅
- 150113 [Zoom.Quiet](http://zoomquiet.io/) checked




