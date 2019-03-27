---
title: HOA.9 LitePyCon
author: zoomq
layout: post
categories: Events
tags:  gdg hoa event summary
---


![](http://0.zoomquiet.top/ZQCollection/foto/140816-hoa9_4.pic.jpg?imageMogr2/thumbnail/800x/crop/!600x300a120a250)

再一次硬技术话题,纯粹程序媛集会 ;-()

    #gdg 
    #zhouhai
    #hoa 
    #gdl 
    #rport
    #2014

<!--more-->


总计:

- G+报名: 22人 表单报名: 8人
- 现场: 12人
- 直播: 17人


## 流水

- 14:35 - 15:00   门卫签到
    - 抓到了野生 赖总 现场签名!

![签名](http://0.zoomquiet.top/ZQCollection/foto/140816-hoa9_8.pic.jpg?imageMogr2/thumbnail/800x/crop/!600x320a120a350)

墨宝哪,一看就是专门练过的...`当然,大妈提供的专用签字笔也是有功的;-)`

![book](http://0.zoomquiet.top/ZQCollection/foto/140816-hoa9_7.pic.jpg?imageMogr2/thumbnail/800x/crop/!640x460a120a150)


- 15:05 - 15:15   GDG自述
    - [幻灯](https://speakerdeck.com/zoomquiet/2-dot-22-sod-zq-zhgdg-intro) ;录音:[140816-0-intro-zhgdg.MP3](http://0.zoomquiet.top/ZHGDG/2014/140816-hoa9-litepycon/140816-0-intro-zhgdg.MP3)

- 15:20 - 16:05   涛哥 "SequoiaDB的Python 驱动"
    - [幻灯](https://speakerdeck.com/zoomquiet/140810-intro-sequoiadb) ;录音: [140816-1-SequoiaDB-Py.MP3](http://0.zoomquiet.top/ZHGDG/2014/140816-hoa9-litepycon/140816-1-SequoiaDB-Py.MP3)

![sequoiaDB](http://0.zoomquiet.top/ZQCollection/foto/140816-hoa9_6.pic.jpg?imageMogr2/thumbnail/800x/crop/!600x320a120a150)

~ 国产原创通用NoSQL数据库!


- 16:10 - 17:05   赖总 "python web dev 的困惑与突破"
    - [幻灯](https://speakerdeck.com/zoomquiet/zhgdg-hoa-dot-9-pyde-kun-huo-he-tu-po) ;录音: [140816-2-py-web-big-question.MP3](http://0.zoomquiet.top/ZHGDG/2014/140816-hoa9-litepycon/140816-2-py-web-big-question.MP3)

![laiyh](http://0.zoomquiet.top/ZQCollection/foto/140816-hoa9_5.pic.jpg?imageMogr2/thumbnail/800x/crop/!600x320a120a120)

现场赶工完成的简洁幻灯,包含了一个大工程:
[laiyonghao/wa](https://github.com/laiyonghao/wa)
可能改变整个儿 Python 世界格局的设想!

- 17:05 - 17:10   现场合影
- 17:10 - 17:45   大妈 "在移动设备上用Python完成App原型"
    - 幻灯:[QPy 101](https://speakerdeck.com/zoomquiet/zhgdg-hoa-dot-9-intro-qpython); 录音: [140819-3-qpy-intro.MP3](http://0.zoomquiet.top/ZHGDG/2014/140816-hoa9-litepycon/140819-3-qpy-intro.MP3)


## 资料

- `2:46` [视频](https://www.youtube.com/watch?v=hJBWF4mkfcA)
- 录音[下载](http://0.zoomquiet.top/ZHGDG/2014/140816-hoa9-litepycon/index.html)
- 幻灯:
    - [2.22-SOD-ZQ-ZHGDG_intro.](https://speakerdeck.com/zoomquiet/2-dot-22-sod-zq-zhgdg-intro)
    - [140810-intro_sequoiaDB](https://speakerdeck.com/zoomquiet/140810-intro-sequoiadb)
    - [ZHGDG_HOA.9_Py的困惑和突破](https://speakerdeck.com/zoomquiet/zhgdg-hoa-dot-9-pyde-kun-huo-he-tu-po)
    - [ZHGDG_HOA.9_intro QPython](https://speakerdeck.com/zoomquiet/zhgdg-hoa-dot-9-intro-qpython)


## 纪要
活动的名字有两层含义:

- Lite ~ 轻量的,我们只是一个下午的日常分享活动
- PyCon ~ Python年会,这次都是Py 主题内容,另外也是对 11/15 珠海场大会的预演
    给没有来珠海的亲们,先认个道儿

![现场](http://0.zoomquiet.top/ZQCollection/foto/140816-hoa9_9.pic.jpg?imageMogr2/thumbnail/800x/crop/!600x320a160a160)



虽然只有三个主题,但都是实打实的硬话题:

- SequoiaDB 是由来自 IBM 等传统 RDBMS 厂商资深工程师的原创作品,包含了企业级应用的实战经验,比 Mongo 这种意外的作品相比,更加有针对性,考虑的更加周全,从一开始就针对长期运行的DB系统要求进行了逐一的攻关
    - 核心能力在 HA
    - 只是当前 Py 接口,仅为简单的对原有 C++ 接口的包装,没有考虑到 Pythonic 的体验
    - 好在,团队对开源社区有强烈的认同感,愿意认真对待
    - 从资深大妈的角度,建议:
        - 专人负责
        - 持续投入
        - 规范运营

- 赖总有关 Py 的 web 应用开发的思考,已经持续了至少3年
    - 现在终于通过 [laiyonghao/wa](https://github.com/laiyonghao/wa) 项目
    - 回答了自身的设问: `到底框架和语言哪个更加重要?`
    - 当前的思考成果是:
        - 用户方案最重要
        - 只有一个有足够市场(用户),解决长期刚性需求的易用方案
        - 配合规范/稳定/可扩展/零学习 的插件体系
        - 领域成果才可能持续汇集起来

- 大妈长期关系怎么在 移动平台上用 Py 完成应用,这才发现了 [QPy](http://wiki.qpython.org/)

基于样例[CodinGirls/qpy-goo - GitCafe](https://gitcafe.com/CodinGirls/qpy-goo)
折腾出了推荐的开发流程整体图景(基于`CLI`工具的串接):


    [本地电脑]
            qpy-goo/
               |   `->修订代码
               |        `-> cURL 测试
            fabfile              |  
               |                 |
    [Android Linux]~~~~~~~~~~~~~~~~~~~~~~~~~~~
               V                 |
        [busybox+SSHDroid]       |
          +-> scp                | 
          +-> reset env          | 
          +-> qpython restart    |
                                 V
                        [  qpy-goo 实例   ]


### CodinGirl.us
并期望,基于这种关联多个领域知识,又是移动应用的内容,

推行: **[程序媛轻松会(CodinGirl.us)](http://codingirl.us/)**

原创品牌活动.

### 有关活动形式: 

`HOA`

- E文名: `Hangout on Air`
- 中文名: `技术无界分享会`
- 常规技术分享,通过 Hangout 服务直播为 YouTube 视频
- 平均每月至少会组织一次

## 是也乎

HOA 的形式打破了分享的空间约束,是种先进的分享形式,
但是,用好不简单,
推荐参考: [Hangout 墙内使用指南](http://blog.zhgdg.org/2014-01/hangout-guider/)




## 巡阅
- 150113 [Zoom.Quiet](http://zoomquiet.io/) checked




