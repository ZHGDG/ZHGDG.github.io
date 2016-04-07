---
layout: post
author: zoomq
title: D码点评:5 30 年的 Hello world
description: ~ 麻辣评点,善意满盈
categories: gDgcoDe
tags:  gdg D码点评 dd wechat coding
---

据说在每一个电视台里,都有一个扫地的老太太. 很偶然地,当她经过一个主持人身边时,看了一会主持,会低声提醒对方说:小心,情声气结合又错了. 



# 30 Years of Hello, World

- 原文: http://www.wintellect.com/blogs/jlikness/30-years-of-hello-world
- 翻译: http://www.oschina.net/translate/30-years-of-hello-world

最近我在7月4日这一天所在的那周休假了. 休假期间,我利用大把的时间对我时至今日的职业生涯进行了反思.  意识到我现在写代码都写了快30年了,不免让我有些许震惊. 因此我决定,要利用这段美好的休闲时光,写篇博文来怀怀旧,探究一下我在过去30年的工作中所用到的所有编程语言. 且谨以此篇文章献给我以编写"Hello, World."开始而学习各种新语言的30年美好时光. 

TI BASIC是我所学习的第一门编程语言. 它是由微软专为TI 99/4A微型计算机编写的一种特殊类型的BASIC方言. BASIC是Beginner's All-purpose Symbolic Instruction Code的缩写,意思是初学者的通用符号指令代码. 对于困在家中又无游戏可玩的7岁孩子来说,BASIC是再好不过的一门编程语言了. 该语言采用行号来组织多行代码,要想在屏幕上显示点什么就可以象下面这样把要显示的内容"print出来": 

<!--more-->


## 1981 – TI BASIC 
![10225321_OjeF.jpg(JPEG 图像,376x291 像素)](http://static.oschina.net/uploads/img/201307/10225321_OjeF.jpg)

我花了几个月的时间用这种BASIC编写了一些"choose your own adventure(请你来选择你要扮演的角色来进行游戏)"类型的游戏,甚至花了更多的时间听着用来保存和恢复数据的黑色盒式磁带录音机发出的滋滋,啪啪和嘶嘶声.  我人生中最令我激动和最关键的时刻恐怕是多年后我父母把一台Commodore 64带回家的那个时刻. 这个机器随机带有Commodore BASIC,或者叫做PET BASIC,而且可开箱即用. 这种BASIC也是由微软编写的,它基于6502 Microsoft BASIC,也就是微软专为6520系列芯片而编写的BASIC,而苹果的机器那时所采用的也正好是这个系列的芯片.  

## 1985 – 6502 机器码

![10225322_njbp.jpg(JPEG 图像,391x391 像素)](http://static.oschina.net/uploads/img/201307/10225322_njbp.jpg)

这段小程序会将一个索引装载到"Y-加法器"中,然后将始于$C100的内存中的字符一个一个的发送给ROM中的一个子程序,从而将这些字符显示出来. 这就是for循环(for y = 0; y <= 0x0d, y++)所对应的机器码. RTS命令会从子程序中返回. 为了执行这个程序,你还得使用内建的SYS命令呼叫出内存地址(很不幸,为此你不得不将16进制的$C000转换成10进制的49152,但除此之外其它的运行起来那叫一个顺畅). 我将表示"HELLO, WORLD"的PETSCII字符存储在了内存地址$C100处(是的,Commodore 64有它自己特殊的字符页(character page)). 程序运行结果如下: 

![10225322_MS2C.jpg(JPEG 图像,407x297 像素)](http://static.oschina.net/uploads/img/201307/10225322_MS2C.jpg)

当然,当我从原始的机器码转战到汇编语言时,日子就稍微好过了点. 使用汇编语言,我就可以预先规划我的软件,而且还不用死记内存地址了,只需用标签来标记内存地址即可. 上面那段机器码对应的完全相同的汇编程序可以如下来编写: 

## 1986 – 6502 汇编语言

    * = $C000       ;set the initial memory address
    CHROUT = $FFD2  ;set the address for the character out subroutine
             LDY #$00 
    LOOP     LDA HELLO, Y 
             CMP #$00          BEQ END 
             JSR CHROUT 
             INY 
             BNE LOOP 
    END      RTS
    HELLO    ASC 'HELLO, WORLD.' ; PETSCII
    HELLOEND DFB 0 ; zero byte to mark the end of the string 


大约也就是这个时候,我意识到我是真的喜欢编写软件了. 高中时我参加了一些课程,但他们教的不过是一些很愚蠢的小型Pascal语言,设计这种语言就是为了使学习如何编程变得"轻松一些". 真是轻松了吗?经过使用"机器监视器"徒手编写复杂的程序之后,我感觉Pascal实在是太过于轻松了. 我还真是不得不承认,用Pascal编写"Hello, World"的语法实在是太简单了.  

## 1989 – Pascal

    program HelloWorld;
    begin
      writeln('Hello, World.');
    end


我想,在这时候,很时尚的小子们都在用C编程序呢. C是一种非常灵活的语言,它感觉就象是汇编语言之上的一些功能性的宏,而不像是一门新语言. 因此我额外自学了C,但C我却只用了不长的一段时间. 

## 1990 – C 

    #include <stdio.h>
    main()
    {
      printf("Hello World");
    }

这段小程序包含了一个处理标准输入/输出的库,然后就在屏幕上输出了一段文字. C中的库使得C可以开发跨平台的应用 -- 不管是在Windows还是在Linux中调用的都是同一个函数,但库本身实现了能够运行于目标机的所有底层子程序. 上面这段代码也是我多年后在Linux机器上首选摆弄的代码. 如果那时你还没有入计算机这个行当,有些情况是我光用语言很难说明白的,那时要是你不弄个Linux自定义安装版,大家就觉得你不是个真正的程序员. 我所说的"弄个自定义安装版",意思是梳理Linux的源代码,将其按照你自己独特的硬件对Linux进行定制. 其中最有意思的要数对显卡的处理了,要掌握监视器的"点时钟"情况,其中还需要施展各种奇巧淫技才能让主板很好的配合图形芯片一起工作. 好吧,我跑题了.  

C对我来说学起来真的不算是个挑战,但我很快就搞明白了,耍酷的小子们在做着不同的事情,正在学习一种称为"面向对象编程"的编程范型. 机器码和汇编语言可能是和OO距离最远的东西了,从面向过程的编程转向面向对象的编程对我来说是个我乐于接受的挑战. 在那时你还无法仅仅通过在线搜索来寻找学习资料(搜是可以搜的,但搜索机制和现在不同而且搜索结果也少之又少),因此我就出去买了一摞C++的书.  C++的确支持"对象"这个概念. 它甚至还使用对象来表示流和管道,能够以对象的方式来对它们进行操作. 面向对象还引入了命名空间的概念,以此来更好的管理代码的划分. 说了这么多,这次"Hello, World"变成这样了:


## 1992 – C++

    #include <iostream>
    using namespace std;
    int main()
    {
      cout << "Hello World";
      return 0;
    }

我一猛子扎进了大学,但令我失望的是,我的大学里并没有开设教授我所感兴趣的象C和C++这样的现代语言的课程. 相反,我不得不应付差事的课程却是让我在一个叫做"Cypher"的大型机上用一种叫做Fortran的很有趣的语言来写作业. Fortran这种语言竟然很在意你把代码放到哪一栏中!没错,那时这种语言规定第1栏用来写注释,第1到5栏写语句的标签,第6栏用于续行字符,只有从第7栏你才能开始写真正的代码,我学到了足够多的Fortran,使我认识到我以后再也不想用这种语言编程了. 


## 1993 – Fortran

       PROGRAM HELLOWORLD
       PRINT *, 'Hello, World!'
       END

那时我翘了大部分课程,把晚上的大部分时光花在了计算机房. 在那里我使用的是我们大学的大型Unix机. 在机房里我发现了Internet,学到了安装软件的"老式"的方法:下载软件源代码,build出可执行程序,查看错误,然后进行相应的调整和修复才能得到一个好用的软件. 实话说,我还真不知道不学会那时的编程技术,你怎么才能学会使用Unix. 那时我不断地探索和学习使用计算机系统的方式. 当时我所做的最常见的一件事就是执行一个能够倒出大量信息的命令之后,再使用一些非常"顺手"的命令行工具对这些信息进行解析. 那年我学到的最酷的语言之一就是PERL. 虽然用"Hello, World."这样简陋的例子做演示对PERL来说很不公平,但就先将就一下吧: 

## 1993 – PERL

      $welcome = "Hello World";
      print "$welcome\n";

与此同时我很快发现了大量的World Wide Web(是的,那时我们就是这么称呼Internet的. Internet中运行的就是Gopher和Archie这类好玩的程序,World Wide Web只是Internet之上的一写文档而已). HTML对我来说又是令一个飞跃,它使我第一次接触到了描述性UI. 不用装入变量或字面量并使用一些关键字或子程序,我就能够将内容组织到一个页面之中. 你可能会惊奇,直到20年后的今天,HTML页面的基本语法实际上根本都没怎么变

## 1993 – HTML  

    <html>
    <head><title>Hello, World</title></head>
    <body><h1>Hello, World</h1></body>
    </html>

 对我来说这是一段很有意思的时光. 我从个人计算机(TI-99/4A和Commodore 64,还在很短的一段时间中用过Amiga)转向的大型机, 忽然之间我的PC真的只是变成了用来连接到Unix大型机的终端而已. 我还在PC上运行了一个Linux操作系统,这是因为Linux是连接到Internet和网络的最快最方便的方式 -- Linux内置了TCP/IP协议栈,无需想老版本的Windows那样在操作系统之上再安装这个协议栈了(还有人记得NETCOM吗?)我的大部分工作是在大型机上完成的. 

我真地意识到了,我在间接失去同PC世界的联系. 显然那时疯狂的个人计算时代已经结束了,有两种机器渐渐成了接灰的摆设了:一种是对于我们中的大部分人来说的运行Windows的PC,另外一种就是对于设计者而言的Mac机器. PC已经过时了就是我当时的信念. 那时我有个室友成天围着Mac转,用Mac来设计各种优惠卷. 他有一大堆漂亮的图形设计程序,经常会把一个叫做Quark的软件调出来,然后问我:"你的PC里有这样的软件吗?"我会耸耸肩然后提醒他,我连一个圆或者正方形都不画,我要这样的图形软件有什么用?我喜欢我的PC,因为我懂软件,而且我也会数学,即使我没有画什么图,我肯定能够利用数学在计算机上画出分形图形或者粒子风暴图. 当然要做到这些就需要有图形卡,通过TELNET连接到Unix机可干不了这些事,所以我开始学习PC编程了. 那时在PC上用来编程的就是Win32和C++了. 即使在今天的Visual Studio 2012中,你依然能够运行下面我说的这个例子. 我不会用我原先在Win32下编写的有150多行代码的"HELLO.C"程序来烦你的.  


## 1994 – Win32 / C++ (这个例子要稍稍新一些)

![10225322_l6Pz.jpg(JPEG 图像,429x241 像素)](http://static.oschina.net/uploads/img/201307/10225322_l6Pz.jpg)

 打开一个命令行窗口然后运行这个程序后会得到这样的结果:

![10225322_0ceD.jpg(JPEG 图像,441x228 像素)](http://static.oschina.net/uploads/img/201307/10225322_0ceD.jpg)


我的粒子流程序和曼德布洛特集合程序肯定在找工作方面帮不上什么忙,所以我必须再找另外的办法. 令人啼笑皆非的是,我的职业在开始时同计算机竟然没有丝毫的关系. 刚开始我为一家保险公司工作,工作内容是处理来自西班牙的电话索赔事务. 情况就是这么个情况. 在为一个薪水较低的工作接受面试时,我准备安心用这份微薄的薪水来户口,晚上再熬夜搞PC编程,我偶然提到我会说西班牙语. 他们叫来他们的双语业务代表来面试我,我通过了测试. 就在一周之内我得到了一个薪水更高的职位,因为我在短短的几个电话中学到了比我在整个高中几年里学到的还有多的西班牙语.  


那时我还年轻,求胜心切. 我们的级别是基于每天我们成功完成的索赔总数来计算的. 我不想就因为我所使用的软件每隔一段时间就要崩溃而被甩在后面. 我们使用的对我来说是一套全新的系统 -- AS/400 (现在叫做iSeries) -- 但是我还是想出了办法,学会了在索赔软件每次崩溃之后如何重启它. 公司的IT部门很快明白了是怎么回事了,并把我叫到了一边. 起初我担心我惹上麻烦了,但是实际上他们向我提供了一个转入IT部门的机会. 我又开始了我的第三次转折,工作内容基本上就是维护AS/400系统,为打印保险单和理赔表的大型打印机换打印盒. 

在这个工作中,换打印盒的过程占据了整个工作中的大部分时间. 这是因为有些表格只用黑墨,而有些别的表格却还需要绿色或红色的墨. 那些打印机里只能装一种墨,所以在碰到不同类型的表格时,打印机就会提示我们去换上所需的墨. 我认为这种做法太荒谬了,所以我花时间自学了RPG. 我编写了一个程序,能够将打印作业同墨的颜色匹配起来,然后对打印作业队列进行排序,把所有的黑色打印作业排到一起,然后是所有的绿色打印作业,等等. 这样一来,原先8小时的工作就变成只需2个小时就能完成,我就有更多的时间来学习RPG了. RPG最初的版本 -- RPG II和RPG III --  还都非常原始,其最初的设计只是用来简单地模拟卡片打孔系统的方式来产生报表(其名字就是Report Generator的缩写,意思是报表产生器). RPG和Fortran一样,都是位置性的语言.  


## 1995 – RPG 

    I              'HELLO, WORLD'        C         HELO
    C           HELO      DSPLY
    C                     SETON                     LR


 请注意每行的第一个字符表明的是各行的代码类型(实际上它还应该多占几列,但我故意省略了其中的一些空白处). 第一行定义了一个常量,然后第二号将该常量显示到屏幕上,最后第三行是一个让程序结束执行的指示符. 

在开始运维工作后我又干了我的第二件大事. 每次月底结算都需要花费大量的时间和精力. 原先的系统是在一台Honeywell大型机上读取穿孔卡片. 其中有个COBOL程序从一个模拟穿孔卡片的文件中读取数据,然后输出到另外一个文件中,最后再把这个输出文件送入AS/400中进行处理. 处理完成后,还需要将各种结算数据对一下. 由于舍入错误,不支持事务以及另外的一些问题,数据几乎每次都对不上,所以就需要对整个计算过程进行调查,找出是哪里处理差子,然后再通过更新代码来修复错误. 如果我们未能找出问题所在,我们还弄了一个"紧急开关",在11点按下这个开关,就会读取输出数据然后调整结算数据来让账簿平衡. 虽然我并没有大量的COBOL编码经验,但我需要通过阅读Honeywell的COBOL代码来理解透彻它的工作过程,然后我才能够很好的处理掉发生在AS/400 这边的问题.  

## 1995 – COBOL


    IDENTIFICATION DIVISION.
    PROGRAM-ID. HELLO.
    ENVIRONMENT DIVISION.
    DATA DIVISION.
    WORKING-STORAGE SECTION.
    01 WELCOME-MESSAGE           PIC X(12).
    PROCEDURE DIVISION.
    PROGRAM-BEGIN.
        MOVE "Hello World" TO WELCOME-MESSAGE.
        DISPLAY WELCOME-MESSAGE.
    PROGRAM-DONE.
        STOP RUN.


没过多久,顶尖的RPG专家就来到我们公司,给我们上了3天的课程,这是因为最酷的事情发生在AS/400的世界中. 不仅仅是AS/400正在转向64位(大家都知道位数加倍后就会比原先好上一倍,对吧?) ,而且RPG语言也正在得到巨大的改进,版本IV比以为更多了融合了面向过程的特性以及一些面向对象的原则. 这得多酷啊?我们扎入培训中后心里乐开了花,因为睁大所有的老式RPG开发者都在为努力学习这种"新的编程风格"而挠头时,我心里的石头终于落地了,终于能够回到我用C和C++时更为熟悉的面向过程的编程风格了,再也无需使用过去的那种刻板而受局限的基于指示符和列的RPG语言了.  

很多开发者可能会因为某个特性而感到高兴,这些特性也的确让人刮目相看. 语言要求指令开始于一个确定的列,输入在指令之前. 这里局限性很大,你只有加载少量的常量字符,或者你不得不把它指明为常量或者数据结构,并把它们读入. 新语言则把关键字列移动到右边,就有更大的空间给"factor one". 这意味着我们现在可以用几行代码来写"Hello,World" 了. 这种语言也是程序化的,所以你可以通过返回而不是在指示器中设置来中止一个程序. (尽管我记得正确的话,在主程序中返回就是设置封装的指示器)

## 1996 – RPG/ILE


    C     'HELLO, WORLD' DSPLY 
    C                    RETURN


AS/400在操作系统中内置了一个叫做DB2数据库. 在很长一段时间内,该数据库只支持通过RPG或其它的软件同其直接交互,并不支持SQL语法. 后来出了个专门的叫做SQL/400的软件包,但DB2在底层就对SQL提供了支持. 为此我还在1998年是发表了我的第一篇文章,写的就是关于如何在AS/400中如何自己接入对SQL的支持(Create an Interactive SQL Utility). 在SQL中实现"Hello, World"的方法可能会数不胜数,但最简单地要数这个了:

## 1998 – SQL 

    SELECT 'HELLO, WORLD' AS HELLO

我要为打乱时间顺序道歉,但SQL似乎完全可以看作是我"主要的"或者"获得报酬的"工作的一部分. 同时我一直都在疯狂玩着游戏,刚开始玩的是DOOM(这是第一个给我留下深刻印象的游戏,我竟然还花钱买了这个游戏的完整版),后来借着玩了DOOM II和HEXEN,最后玩得最High的要数Quake了. 如果你不熟悉第一人称射击游戏(FPS)的发展史,我还得告诉你,Quake还是一个改变了游戏历史的游戏. 这个游戏为玩家提供了史上第一个"真正的"3D游戏环境(之前的那些游戏都是用2D映射表来模拟出3D的地板和具有一定高度的天花板),通过对TCP/IP的支持彻底改变了死亡比赛的模式, 它采用了非常高级的编程技术,从而允许比以往任何时候都多的玩家在同一个地图中同时玩游戏.  

Quake的可定制化程度也极高. 虽然我在美工方面不怎么地,从来没弄明白怎么创建自己的模型或地图,但我直接扎近了编程来对它进行定制. Quake提供了一种基于C的编程语言,名为QuakeC. 这种语言能够编译为跨平台的字节码,而这种字节码可以在能够运行Quake的所有目标平台之上. 很快我就编写了一些改造性的程序,能够做到让玩家着火,让铁钉从墙上逼真地反弹回来等等类似的事情. 在一个聊天室里,有个人说了一个点子让我编程实现一下,后来就因为我编写的这个叫做"MidnightCTF"的功能而为大家所知. 其实就是直接在现有的任何地图上将所有的等都关闭,但为每个玩家配备一个手电. Quake是第一个支持真正的3D音效的游戏,这为游戏增添了一种有趣的可玩性. 

甚至还有人从我的那些改造性的程序中拿出了一段代码,放到了"编程语言字典"中的QuakeC词条之下. 下面这段用QuakeC编写的"Hello, World"代码实际上就是将一条广播消息发送给了当前游戏中的所有玩家.  


## 1996 – QuakeC

    bprint("Hello World\n");


 此时我意识到了Internet真地要发展起来了. 1993年我还在上大学时发现了这一点,但我非常沮丧,因为根本没有人真正明白我在说什么,但仅仅在几年之后,每个人都在为了抢着进入Internet领域而乱作一团(有些公司,比如AOL和微软的MSN,都想打造属于每个公司自己的互联网. . . 但最终都无功而返,接入了我们现在所说的这个大的Internet). 我发现我在大型机上的工作马上就会过时,或者最好的情况下我只能成为一个藏在后面的某个角落中,鼓捣"那些个老系统"的开发人员. 我想接触这些新东西. 

后来我转到了一个在工作中使用这些新东西的部门 -- 用VB6(COM+)和ASP编写一个应用,把几个不同的系统连接起来,从而可以让所有供应商都能看到其中的数据.  


## 1998 – VB6 (COM)和ASP 

    Public Class HelloWorld
        Shared Public Function GetText() As String 
            return "Hello World"
        End Function
    End Class

    <%@ Page Language="VB" %>
    <OBJECT RUNAT=SERVER SCOPE=Session ID=MyGreeting PROGID="MyLibrary.HelloWorld">
    </OBJECT>
    <HTML>
    <HEAD><TITLE><%= MyGreeting.GetText() %></TITLE></HEAD>
    <BODY><H1><%= MyGreeting.GetText() %></H1></BODY>
    </HTML>


那时我有幸能同一位颇具天赋的架构师一起共事,他设计了一个系统,其架构在当时来讲还是非常神奇的. 我们的COM+组件都可以接受一个单个的字符串作为参数,这是因为它们收到的信息都是XML格式的. 这样一来,我们的组件就能够和接收来自网站的消息一样,轻松地接收来自第三方系统发来的数据. 这就是真正的"web service",我在真正的理解这个词是什么意思之前就干了这有的事. 客户端的表单由JavaScript来解析并打包成XML,然后发回服务器, 因此从页面发回的数据同其它服务发过来的数据并无二致. 服务也会将XML作为返回数据的格式. 这样就能够把这些返回数据同一个UI模版(该模版名为PXML,是Presentation XML的缩写)结合,然后用一个XSLT模版将其转换为可供显示用的格式. 这样我们就能够在不改变底层代码的情况下对UI进行微调,有点象是个效率不太高的XAML引擎. 这还是在.NET出来之前我们干的活呢. 

JavaScript可是个折磨我们的东西,因为那时我们还要找出如何处理不同的浏览器的办法. 是啊,一说到JavaScript和跨浏览器的兼容性,就不得不说,这个相同的问题15年前就出现了,直到现在还依然存在. 幸运的是,所有的浏览器在向用户弹出对话框时采用的方法还是一致的.  

## 1998 – JavaScript

    alert('Hello, World.');


很多时间都被我被花在了Microsoft XML DLLs上面 (如果你以前编写过那就会记得注册MSXML解析器). MSXML3.DLL很快就成了我的朋友,下面是一个将XML通过XSLT转换为HTML的例子. 

## 1998 – XML/XSLT to HTML

    <?xml version="1.0"?>
    <hello>Hello, World!</hello>

    <?xml version='1.0'?>
    <xsl:stylesheet version="1.0"
          xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
        <xsl:template match="hello">
            <html>
                <head><title><xsl:value-of select="."/></title></head>
                <body><h1><xsl:value-of select="."/></h1></body>
            </html>
        </xsl:template>
    </xsl:stylesheet>

    <%
    Const MSXMLClass = "MSXML2.DOMDocument" 
    Set XSLT = Server.CreateObject(MSXMLClass)
    Set XDoc = Server.CreateObject(MSXMLClass) 
    XDoc.load(Server.MapPath("hello.xml"))
    XSLT.load(Server.MapPath("hello.xsl")) 
    Response.Clear
    Response.Charset = "utf-8"
    Response.Write XDoc.transformNode(XSLT)
    %>


那个模式上我花了几年时间. 那段时间中我个人经历了一些转变,体重减轻了70磅,腰围从44英尺减少到32英尺,由于健康我充满了激情. 我兼职开了一家自己的公司,甚至从当时的公司辞职,我在这家专为医院提供翻译服务和拥有一个在线的西班牙语节食程序小公司担任IT理事. 我能再次够提高我的西班牙语能力,因为翻译是从英语到西班牙语,反之亦然. 我甚至将整个用ASP和内嵌了西班牙语硬编码的SQL语句的程序重写. 使其成为了完全数据驱动的,标白的(为了品牌)和本地化的(公司想把他弄成其他像法语之类的分支). 在微软公司的技术栈的那段时间,我还是相当令人兴奋的. 但由于工具和服务器的花费,让我在开自己公司的时候接触了开源社区. 那时,为了开发我学了所有像LAMP栈..Linux系统,Apache的Http服务器,MySQL数据库和PHP之类的技术. 讽刺的是,由于这些经历,当微软试图为了让开源社区拥抱Sliverlight的时候,我成为了其短期咨询...但那又是另外一个故事了.  


## 2002 – PHP 

    <?php
     $hello = 'Hello, World.';
     echo "$hello";
    ?>

在特定的平台工作了许多年后,我终于有机会进入到新公司的另一个软件开发岗位. 我是一个当时还不出名的创业公司的第三个职员. 如果你曾在Panera或Chick-fil-A吃饭或在Caribou喝过咖啡,那你可能就使用过我参与过编写的,或为了无线热点体验而最近升级过的软件. 当我加入这家公司的时候,初始平台是用Java编写的. 我在这个语言上,我曾用其做过很多"修补"工作,因此加上C++和微软栈上的技能我很快的就将其重新捡了起来.  

## 2004 – Java 

    public class Hello {
        public static void main(String[] args) {
            System.out.println("Hello, World");
        }
    }

在语言当中我对Java并不感冒,但是我们要用到的特殊东西涉及到微软将要放弃的JVM,而且一个定制的服务器并不需要扩展. 当把平台迁移到了.Net平台,我很惊讶的发现IIS服务器比其他几个专用的Java服务器能处理更多的请求. 我说的"迁移",其实是重新构建了一个新平台. 我们寻求一种把J++代码转换为c#代码,但发现那确实不实用. 幸运的是C#与Java非常是接近,大多数团队都能通过现存系统的"规则"轻松的将其翻译成能在Windows运行的系统,且把MySQL迁移到SQL Server 2005. 注意Java的"Hello,World"和C#是多么的接近.  

## 2005 – C# 

    public class Hello
    {
       public static void Main()
       {
          System.Console.WriteLine("Hello, World!");
       }
    }

我们的公司那时之所以非常成功,部分原因在于我们的"控制面板"能够让我们集中在一个地方就可以管理所有的热点和访问点. 我们可以在远程对这些热点和访问点进行重启,固件更新并用一心跳信号来对他们进行监控,同时还为诊断问题保存了历史信息. 这个软件很快就发展成了一个移动设备管理(MDM,也即Mobile Device Management的缩写)平台,并成为公司现在的旗舰产品. 他们在发布产品时重新起了一个新的品牌名,但是由于我们的挑战而得到了一个能够跨平台的HTML的交互性非常强的用户体验(先前的解决方案采用的是微软定制的Java Applet). 我们用AJAX以及HTML成功的构建了一个能够打动人的系统,但我们的团队不得不在如此多的浏览器和平台上进行测试,而我们的系统又是个负责富UI系统,这对我们的是个很大的挑战. 虽然为了提高热点登录用户体验我们还需要维护这个系统,但它在管理方面更加灵活了,所以我又对一些其它的提到方案进行研究.  

当我发现Silverlight时,就对它着迷了,但我还是觉得先让我自己对它进行探索为好. 我可以在我们监控面板的概念性产品前面站几个礼拜,发现每个人都很喜欢它,所以决定大家全力投入对它进行开发. 我最乐观的估计是,采用Silverlight之后,从产品的概念到发布我们团队所需要花的时间要比采用JavaScript和HTML相关技术少4倍. 那时,HTML5还是个空中楼阁. 在我离开之前,我们的团队已经用Silverlight实现了很多的功能. 直到离开时我们一直都在同Apple在MDM方面进行合作,Apple当然不想让他们的软件同Silverlight有任何瓜葛,但是我还是享受了多年用一种可以通过XAML得到跨浏览器和平台的声明式UI的强大功能的语言编写业务程序,只要我们允许使用插件就没问题了. (我听说这些技术现在再也不流行了).  

## 2008 – Silverlight (C#和XAML)


    <UserControl x:Class="SilverlightApplication1.MainPage">
        <Grid x:Name="LayoutRoot" Background="White">
            <TextBlock x:Name="Greeting"></TextBlock>
        </Grid>
    </UserControl>

    public partial class MainPage : UserControl
    {     
        public MainPage()     
        {         
            InitializeComponent();         
            Loaded += MainPage_Loaded;     
        }     

        void MainPage_Loaded(object sender, RoutedEventArgs e)     
        {         
            Greeting.Text = "Hello, World.";     
        }
    }

当然,Silverlight后来就象一只垃圾股一样日薄西山了. 那时Silverlight仍然是一个非常有用也很有竞争力的技术,I但一旦人们发现微软不再对这种技术进行投入了,Silverlight马上就行将就木了 -- 虽然人们感觉它过时了,但这和它在那时是不是一个正确的工具没有丝毫的关系. HTML5在宣传自己是"编写一次,到处运行"方面也做得相当不错, 成百上千的公司在能够意识到他们的错误(HTML5的口红"编写一次,到处运行"的实际意思是,"编写一次,到处碰壁,然后为每个平台还得再编写一次")之前,不顾一切,争先恐后地加入了HTML5的阵营. 

然而,我们所喜欢的Silverlight中的那部分特性在Windows 8.1下的XAML和C#中存活了下来.  为了好玩,下面给出采用酷小子们惯常使用的模型－视图－视图模型(MVVM)模式编写的"Hello, World".  

## 2011 – WinRT / C#

    public class ViewModel
    {
        public string Greeting
        {
            get
            {
                return "Hello, World";
            }
        }
    }  
    <Grid Background="{StaticResource ApplicationPageBackgroundThemeBrush}">
        <Grid.DataContext>
            <local:ViewModel/>
        </Grid.DataContext>
        <TextBlock Text="{Binding Greeting}"/>
    </Grid>

虽然Windows 8.1已经让我忙于写作和兼职项目有一段时间了,但是对于大部分公司来讲,它还是比较新的,很多公司想要的是基于Web的解决方案. 这就意味着要使用HTML和JavaScript,而我在大部分时间中就是忙于这方面的工作. 没错,一旦我发现我离开了这套技术,它们总是能够又把我拉回来. 在对我用HTML和JavaScript进行Web开发时所痛恨的地方进行一番深思熟虑之后,我觉得其中必有更好的方式来实现它们. 我们的团队拧成一股绳,对各种可能的解决方案进行了调查研究,最好找到了一个非常酷的解决方案. 最近有一种新发布的语言,叫做TypeScript,它是JavaScript的一个超集. 它没有试图要改变语法,因此所有有效的JavaScript代码同样也是有效的TypeScript代码. 然而,这个语言提供了一些开发时特性,比如,有助于形成API调用的接口,丰富的发现机制(它们甚至都不会出现在编译所产生的代码中)以及支持继承的类,强类型变量,静态修饰符等,而所有这些最终都会编译成非常有效的,跨浏览器的JavaScript代码. 

采用TypeScript是个轻松的决定. 尽管它还处于beta测试阶段,但它产生的代码100%可以直接用在产品中,所以如果我们发现它产生的代码有什么问题的话,我们完全可以跳过TypeScript,直接在JavaScript中进行修补. 最后证明,TypeScript可用性相当高 -- 我们的团队中有几个人对JavaScript有纯正癖,痛恨对"修改JavaScript这种语言"的所有企图都恨之入骨,即使他们几个人刚开始持有怀疑的态度,最后也一致认为,TypeScript为我们提供了更高一层的控制力度,用它还能够进行重构,它也支持并行开发,对我们能够发布高质量的基于Web的代码有着极大的促进作用.  


## 2012 – TypeScript 

    class Greeter {
        public static greeting: string = "Hello, World";
        public setGreeting(element: HTMLElement): void {
            element.innerText = Greeter.greeting;
        }
    }  var greeter: Greeter = new Greeter();
    var div: HTMLElement = document.createElement("div");
    greeter.setGreeting(div);
    document.body.appendChild(div);



TypeScript不是我所在的唯一的改变. 我们还想消除在为对象设置数据绑定时的繁文琐节. 当时我们所采用的Knockout也是一个非常不错的框架,但它所需要的工作还是比我们所想的要多. 我们团队中诱人对一些替代方案进行了调查研究,最后选定了AngularJS. 刚开始我对它还是有所怀疑的,但很快发现,这个方案真的同用于Web的XAML方案非常类似. 采用它我们可以在使用声明式UI的情况下,还能解决另外一个问题,就是我们还可以将命令逻辑从中隔离出来. 到现在为止已经有几个月了,我们的团队在使用TypeScript和AngularJS这些相关技术时一直都很愉快,并且相当的爱用这套技术.  我现在正在参加WintellectNOW的一个课程,因为我决定这事关重大. 然而,要说30年的经验教会了我什么的话,那就是:今天还存在,明天就消失. 我不是一个C#开发人员,也不是一个JavaScript开发者,更不是一个AngularJS奇才. 绝不是!我只是一个编程人员,一个程序员,纯正的,朴素的,简单的程序员. 各种编程语言只不过是个工具,我只是碰巧学会了很多编程语言而已. 好吧,再来一次 "Hello, World". 我希望你能喜欢这段旅程. . . 一段直到现在的旅程.  


##  2013 – AngularJS

    <div ng-app>
        <div ng-init="greeting = 'Hello, World'">
            {{greeting}}
        </div>
    </div>

"再见了,读者朋友. " 


    本文中的所有译文仅用于学习和交流目的,转载请务必注明文章译者,出处,和本文链接
    我们的翻译工作遵照 CC 协议,如果我们的工作有侵犯到您的权益,请及时联系我们 
    http://zh.wikipedia.org/wiki/Wikipedia:CC


# 是也乎

大妈是读的很HIGH 了,
基本上提及的语言都用过, 当然,特殊平台上的语言在天朝基本是没有机会体验的,
但是,大约在学习第5门开发语言时,就感觉不对了!

编程语言是给人用的, 当然,有一堆语言在计算机发展早期是给机器用的,并不考虑人脑的因素;

现在所有语言都尽可能的减少工程师的心理负担, 提高生产效率,降低出错几率.

但是,真心没有哪种语言是不可解决所有领域问题的, 只是代价高低而已;
有的语言几乎就是针对领域问题发明的, 比如说 HTML ,如果不用HTML 来输出网页,
而是发明一个专用语言以及配套的客户端,解析特殊的数据, 当然也可以,
只是实事证明都是心肝要死的, 比如: Flash,Silverlight...

所以? 选择开发语言,就是要针对领域问题,
开发语言的学习应该大同小异,但是,每种语言的范儿, 或是说解决问题的思路/模式/框架,
那是天差地别, 需要大量训练的...

所以! 选择一门通用的友好语言,面对领域问题时,先使用执行效率可能很低, 但是代码易读好懂好改进,
先完成业务要求,然后在实际运行中不断的优化,甚至于使用领域专用语言进行改写,组件替换!
这才是 Pythonic 思维....

是的, 大妈推荐的语言就是 Python !






## 巡阅
- 150113 [Zoom.Quiet](http://zoomquiet.io/) checked





