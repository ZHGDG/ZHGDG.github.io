---
layout: post
title: HwH 之 SAE初体验-回顾小结
author: zoomq
categories: Events
tags:  gdg HwH summary
---


![140927-hwh-8.pic.jpg(JPEG 图像,500x333 像素)](http://0.zoomquiet.top/ZQCollection/foto/140927-hwh-8.pic.jpg?imageMogr2/crop/!900x600a70a100|imageView2/2/w/500|watermark/2/text/Wm9vbS5RdWlldA==/fill/V2hpdGU=/fontsize/400/dissolve/85)

有关活动形式 ~ HwH

- E文名: `Hand with Hand`
- 中文名: `手把手极限实训`
- 完全0基础编程实战培训, 相比 `CodeLab` 有完备的教程, `HwH` 更加看重现场的主动实践
- 通过整个下午的持续的,系列小任务的自主达成,在导师合理指点下完成全新技术领域的探索

首次折腾的怎么样儿呢?

    #gdg 
    #zhouhai
    #rport
    #2014

<!--more-->

感谢 北师珠 师生的支持, 得以令 珠海GDG 又进入一个大学 ;-)


总计:

- G+报名: 4人
- Docs报名: 21
- 现场: 44人(讲师+助教3人)
- 线上: 6人


## 流水

- 14:00 ~ 14:30 现场班会,推荐 HwH 活动
- ~15:00 现场报名
    + GDG [自述](http://0.zoomquiet.top/ZHGDG/2014/140927-hwh-sae/140927-hwh-0-gdg.MP3)
    + [活动解释](http://0.zoomquiet.top/ZHGDG/2014/140927-hwh-sae/140927-hwh-1-intro.MP3)
    + [学员自述](http://0.zoomquiet.top/ZHGDG/2014/140927-hwh-sae/140927-hwh-2-intro-self.MP3)
- ~18:00 边说边练
    + 幻灯:[GDGZH_HwH-SAE-101_v140927.pdf](http://0.zoomquiet.top/ZHGDG/HwH/sae101/GDGZH_HwH-SAE-101_v140927.pdf)

![140927-hwh-11.pic.jpg(JPEG 图像,500x333 像素)](http://0.zoomquiet.top/ZQCollection/foto/140927-hwh-11.pic.jpg?imageMogr2/crop/!900x600a150a200|imageView2/2/w/500|watermark/2/text/Wm9vbS5RdWlldA==/fill/V2hpdGU=/fontsize/400/dissolve/85)


## 资料

- 教学资源: [sae101/](http://0.zoomquiet.top/ZHGDG/HwH/sae101)
- 录音:
    + [140927-hwh-0-gdg.MP3](http://0.zoomquiet.top/ZHGDG/2014/140927-hwh-sae/140927-hwh-0-gdg.MP3)
    + [140927-hwh-1-intro.MP3](http://0.zoomquiet.top/ZHGDG/2014/140927-hwh-sae/140927-hwh-1-intro.MP3)
    + [140927-hwh-3-live-record.MP3](http://0.zoomquiet.top/ZHGDG/2014/140927-hwh-sae/140927-hwh-3-live-record.MP3)
- 视频:
    - [导入](https://www.youtube.com/watch?v=f0twLKylinA)
    - [实况](https://www.youtube.com/watch?v=rzi5A8IRadk)

## 回顾

整体上,通过报名,从而收到包含环境部署指南的邀请邮件的同学,
不足现场1/4, 最后留下来并带电脑,参加真实 coding learnning 的
只有13人,甚至于,还有3位同学,中途退出了.

不过,令人惊喜的是, 其中4位同学,之前是真心一点儿 Python 程序也没有写过,
现场跟上引导,在2小时的极短时间里,仅仅靠,文档和直觉,就真的完成了一组任务,
形成了以下,正是向初学者建议的,无论什么操作系统中,都应该先配置好的 `Pythonic`
开发流程:

    [ SAE ]
     ^   ^
     |   |\
     |   | \
     |   |  +- svn commit   -+
     |   |    or             |
     |   +- seacloud deploy -+
     |                       ^
     |                       |
     |                  [local .py]
     |       dev_server.py <-+
     |        run ->|
     |              V
     |       [localhost:8080]
     |              ^
     |<- test ->    |        
     +----------- cURL        


也证明了
    
    Python
    不学用之

的体验, 嘦有任何编程经验,都可以自然的过渡到 Python 的交互式开发体验中来.
完全可以边用边学, 以达成需求/创意 为第一要旨,
而且,Python 也有足够的能力,可以随着我们明确了思路可行后,
快速发布变成真正服务,供给小伙伴们使用.

### 困难

当然,过程中,有几个困难,要认真准备下次,逐一弥补:

1. 学员水平不均:
    - 且没有相互帮助的氛围;以至无法形成帮带小组
    - 下次要先进行破冰游戏,结对编程
2. 学员系统环境不同:
    - M$ 环境配置标准开发环境如此艰难,以至其它内置环境的学员,无法等待
    - 下次,一定要事先充分宣传/沟通/报名,根据系统,分班,才可能有效引导
3. 时间太短,导师太少:
    - 难以完成真正一对一/Hand with Hand 的引导  


## 资源

- [HwH 之 SAE初体验-导入手册](http://blog.zhgdg.org/2014-09/hwh-sae-pre-guider/)
- [Index of /ZHGDG/HwH/sae101 {gen. by gen4idx.py v13.4.18}](http://res.zoomquiet.io/ZHGDG/HwH/sae101/index.html)
- [What's Included in ActivePython 2.7](http://docs.activestate.com/activepython/2.7/whatsincluded.html)




## 巡阅
- 150113 [Zoom.Quiet](http://zoomquiet.io/) checked





