---
title: HOA.8 go在GAE
author: zoomq
layout: post
categories: Events
tags:  gdg hoa event summary
---


首次跨城市HOA联合活动

![](http://0.zoomquiet.top/ZHGDG/2014/140813-hoa8-go4gae/140813-zq-gae-go.png?imageView2/2/w/600)

(国内,今年;-)

    #gdg 
    #zhouhai
    #rport
    #2014

<!--more-->


感谢苏州的 Frank 策动,大妈只是在规定时间,规定地点,完成了规定内容的分享 ;-)


总计:

- G+报名: 34人
- 现场: 10人(珠海2人)
- 线上: 23人

## 流水

- 18:45 ~ 19:05 苏州现场暖场
- 19:05 ~ 19:21 网络调试,好容易 Hangout 上毕竟是多重翻越
- 19:25 ~ 20:15 主题分享
- 20:20 ~ 20:45 QA


## 资料

- 教程: [42分钟乱入 GAE(with go1) !-) — chaos2go1](http://chaos2.qiniudn.com/go1/build/html/)
- 录音: [140813HOA.8-go4gae.MP3](http://0.zoomquiet.top/ZHGDG/2014/140813-hoa8-go4gae/140813HOA.8-go4gae.MP3)
- 视频(U2B): [X Startup Station: GAE/Golang](https://www.youtube.com/watch?v=JeT7ZPJwhps)

## 纪要
Frank 找到大妈来吼,是因为很久以前,大妈写的[42分钟乱入 GAE(with go1) !-) — chaos2go1](http://chaos2.qiniudn.com/go1/build/html/) ;
但是,现场沟通才知道:

- 90% 的人没有写过 go 代码
- 80% 的人没有深入使用过 GAE, 除了部署 goagent

果断没有超过 大妈的预期,所以,现场大妈的讲述集中在工具链以及整体开发流程的分享,
而没说 go 语言本身.

要点内容其实很少:

全部最新代码在: [ZoomQuiet/urisago1](https://github.com/ZoomQuiet/urisago1)

本地开发环境真正的[下载](https://console.developers.google.com/storage/appengine-sdks/deprecated/)

本地运行时:

    $ /path/2/YOUR/dev_appserver.py urisago1/


向GAE 部署代码时, [参考](https://developers.google.com/appengine/docs/go/tools/uploadinganapp), 而日常命令依然是:

    $ /path/2/YOUR/appcfg.py update urisago1/     

推荐的开发流程整体图景(基于命令行工具的串接):

    [墙内本地]
    dev_server.py 运行起本地应用
            urisago1/
               |   `->修订代码
               |      ^ `-> cURL 测试
            fabfile   |      |   |  
               |      +------/   |
    [out GFW]~~~~~~~~~~~~~~~~~~~~|~~~~~~~
               V                 |
        [VPS or HOST]            |
          +-> git pl             | 
          +-> appcfg.py update   |
                \                V
                 `->deploy>>[  GAE 实例   ]


对比测试的日常形式:

    #   本地模拟
    $ curl -d "uri=http://hmdc0.com" localhost:8080/chk
    #   真机使用
    $ curl -d "uri=http://hmdc0.com" urisago1.appsp0t.com/chk


可用的钓鱼样本网站有:
    
    hmdc0.com
    0x00000000c0.000000233.0x000000a4.0x000020
    yg9255.com



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




