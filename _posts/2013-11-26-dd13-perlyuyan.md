---
layout: post
author: zoomq
title: D码点评:13 文言文编程
description: ~ 麻辣评点,善意满盈
categories: gDgcoDe
tags:  gdg D码点评 dd wechat coding
---

    We use it just because we can, 
    muggle! 


![200px-AudreyTang060527.jpg(JPEG 图像,200x150 像素)](http://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/AudreyTang060527.jpg/200px-AudreyTang060527.jpg)

# PerlYuYan

转自: [BT雷人的程序语言(大全) | 酷壳 - CoolShell.cn](http://coolshell.cn/articles/4458.html#more-4458)

是一个能令人使用中文文言文开发程式 Perl 程式的 Perl 模块,由唐凤于2002年一月发表. 它是中文编程语言的尝试. 作者利用中文的特质,将许多指令改成以一个中国汉字来表示,因而造成了文言语法的感觉. 

<!--more-->

看看下面的这段代码,相当的文言文啊. 有兴趣可以去CPAN上下载回来玩玩. 
http://search.cpan.org/~autrijus/Lingua-Sinica-PerlYuYan-0.03/


    #!/usr/local/bin/perl
    use Lingua::Sinica::PerlYuYan;

    用警兮用嚴. 

    印道
    一至一
    哉兮

    印編曰雜申雜申矣
      又纖曰龍鼠矣
        又曰一矣

    亂曰
    國無人莫我知兮    又何懷乎故都
    既莫足與為美政兮  吾將從彭咸之所居

还有下面这个五言. 

    # The Sieve of Eratosthenes - 埃拉托斯芬篩法
    use Lingua::Sinica::PerlYuYan;

      用籌兮用嚴. 井涸兮無礙
    . 印曰最高矣  又道數然哉. 
    . 截起吾純風  賦小入大合. 
    . 習予吾陣地  並二至純風. 
    . 當起段賦取  加陣地合始. 
    . 陣地賦篩始  繫繫此雜段. 
    . 終陣地兮印  正道次標哉. 
    . 輸空接段點  列終註泰來. 


已经迁移到 github:
https://github.com/audreyt/lingua-sinica-perlyuyan


## 唐鳳
唐凤(英文名:Audrey Tang,1981年4月18日－),原名唐宗汉(autrijus),台湾的自由软件程式员,Pugs专案的发起人,领导Haskell和Perl社群协力开发Perl 6语言. 

唐凤也致力于自由软件的国际化工作,包括设计Kwiki,RT及Slash等系统的国际化架构,并发起多项开放源码书籍的翻译计划. 

在CPAN上,唐凤负责维护100余项的Perl相关专案,包括Perl Archive Toolkit (PAR) 这项跨平台封装及建置工具,以及CPAN的自动测试及数位签署系统等. 

### 生平

唐凤的父亲唐光华是<<中国时报>>前副总编辑,母亲李雅卿曾任<<中国时报>>采访部的副主任,是台湾的自主学习,在家自学推动者之一. 

在14岁时就因适应不了学校生活而拒绝上学,即多所倡言自学及安那其思想(αναρχία ~ 理想化的无政府主义). 

于2005年进行变性手术,故由原来的男性化名字"唐宗汉",改名为女性化名字"唐凤". 

### 相关书籍

<<成长战争>>,李雅卿,台北市商智文化,1998年,ISBN 957-98739-3-3
<<她是我哥哥>>(英文书名:Luna, ISBN 0-316-01127-4),原文作者:Julie Anne Peters;译者:丁凡,唐凤 ISBN 978-986-82433-0-9
<<我的电脑探索>>,台北市资讯人文化,1995年,ISBN 957-99640-3-3


# 是也乎

西元2002年1月,唐凤发表了"perlyuyan",是能使用文言文开发程序(Perl程序)的Perl模组,"perlyuyan"是中文编程语言的尝试. 唐凤利用中文汉语的特质,将许多指令改成以一个一个中国汉字来表示,因而造成了文言文法的感觉. 

为什么要创造这一语言?
作者指出应该先看 Lingua::Romana::Perligata

这是老外,想将代码写成 `拉丁散文` 的尝试,使用相同的手法, 
通过精心选择 专用单字 来替代开发语言的关键词,再用空格来标定结构,
从而在形式上令程序象文章一般...


其实,当我们介绍某种技术/语言/框架的时候,一般有两种潜台词;

1. 这种东西做起来很顺手而且快,可以让你节省更多的时间去提升你的逼格;
2. We use it just because we can, muggle! 

这就是我们闪亮的 BQuotation!一般有人问为什么的时候,我内心都在说第二个答案!


其实,编程很多时候都要扭曲我们作为人类的自然思维,强行使用电脑可以理解的数据类型/编辑结构来描述问题以及问题的解决过程,
所以,现代开发语言发展的这么快,
就是程序猿一直在尝试对 可用/可理解/有趣 完成平衡.

所以,中文编程,也是提高编程效率的一种尝试途径,没有什么特殊之处...

只是, 高德纳 早已提出了 文学化编程,
将编程的本质思维过程,用文学化的形式记录下来,通过其它途径 `混出` 为电脑可以编译的代码文本,
这才是从根本上解决人的自然思维同电脑的二进制思维间的可取思路哪...

是的,有关这一方面,大妈准备在 PyCon2013CHina 珠海场,深入分享!

欢迎大家报名来参加!




# 当期活动 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## 12.8 PyCon2013CHina 珠海场

- Python 年度大会
- Pythonner 大趴
- Pythonista 相亲集会
- Pythonic 体验交流

请及时举报你身边的 华蠎行者!

- 举报热线: zoomquiet+pycon (AT) gmail.com
- 官网: http://cn.pycon.org/2013
- [[12.8]PyCon2013China 珠海场报名表](https://docs.google.com/forms/d/1uFSa6PZNfl1ab3oO20CaoafOhfkavhpqg_CN4I36W_A/viewform)







## 巡阅
- 150113 [Zoom.Quiet](http://zoomquiet.io/) checked



