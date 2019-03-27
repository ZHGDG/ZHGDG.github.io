---
layout: post
title: Hangout 墙内使用指南
author: zoomq
categories: Howto
tags:  gdg guider hangout
---

![3472_1.jpg(JPEG 图像,500x324 像素)](http://www.williamlong.info/upload/3472_1.jpg)


这是内置 G+ 平台上的多媒体会议服务,免费!跨平台!好用!

而且有很多用法儿,值得指南一下.

<!--more-->


## 基础

- 首先, 稳定翻越
- 其次, 使用 Chrome
- 最后, 要有 G+ 账号,并关联好 Youtube

注意:

- 若创建Event时指定为 HoA 类型,则:
    - 没有地理地址的选项,
    - 且,后期更改类型的话,直播地址丢失!
    - 活动也不能删除,否则这个HoA Live的视频将会失效. 


### HOA 的创建过程:

1. 创建者发起一次 HOA
1. 邀请其它人加入
1. 在Hangout 控制界面上 点击 `直播`


Frank R. 曰:
如果断时间关闭HOA窗口,然后在回来(`URI`不变时)
Youtube录像会继续. 中断的时间播放类似下面的画面. 

![hoa-blank-image.png(PNG 图像,512x300 像素)](http://0.zoomquiet.top/ZHGDG/wechat/hao-guider/hoa-blank-image.png?imageView2/2/w/512)


前提是记住URI. 如何获得URI,见:[hangout url - Google Drive](https://docs.google.com/document/d/1_0wo43NfgpoWs2tygUa6uTPfNUW-koURxwK7uGVYLH4/edit)

### HOA 的参与礼节

会议型HOA 中,虽然 Hangout 能自动根据每个终端的声音输入,自动切换主屏幕,
但是,出于礼节:

1. 进入 HOA 会议前,先关闭外部音频,使用耳机,以免多个音源诱发啸声
1. 进入一个 HOA 会议后,首先,关闭音频输入,视网络情况选择视频是否打开
1. 要发言时,再点击 MIC 图标打开音频

### HOA 的管理技巧
![](http://0.zoomquiet.top/ZHGDG/2014/140813-hoa8-go4gae/140813-zq-gae-go.png?imageView2/2/w/512)

如截屏, Hangout 内置了很多工具,常用的:

- "屏幕共享": 可以指定桌面窗口,输出到 HOA 中
- "工具箱": 可以配置字幕,输出到 HOA 中
- "QA栏": 可以文字讨论,暂时没有弹幕功能


## 进阶

Hangout 是种灵活的实时沟通服务,可以组织进行多种形式的交流,
一般有:

1. 网络会议
1. 结对编程
1. 网络培训
1. 活动直播
1. ...etc.

对于GDG 社区,用的多的,应该是 `活动直播`

### 珠海GDG 的HOA直播
珠海经过多次 HOA 直播的折腾,形成 HOA Live 的布局是这样的:
    
    ===========[ 投影幕布 ]==============

        (^o^)[讲师]        

             @[webcam]
             |
             v
        +- [主播电脑]
        |
        | +-[幻灯播放]
        V V
    (^.^)[导播]
    

- 现场设立 `导播` 一名,控制两台电脑
- `主播电脑` 接 webcam, 使用 `社区G+帐号` 创建 HOA, 并邀请一个帐号(一般是个人G+)进入频道
- `幻灯播放` 使用个人G+帐号登录接受 HOA 邀请,进入频道
    - 事先收集好讲师的幻灯
    - 使用合理的工具在本地播放
    - 通过 `屏幕共享` 发送到 HOA 频道中
- 这样活动开始后, `主播电脑` 的 Hangout 控制界面上只有两个视频源:
    - 现场讲师和投影的实时视频
    - `屏幕共享` 而来的清晰幻灯图像
- 然后在活动进行中, `导播` 根据演讲的进展
    - 手工跟随讲师翻页
    - 并在合适的时机在 `现场视频` 和 `幻灯图像` 间切换
    - 形成 Youtube 直播视频流中,清晰的幻灯图像和现场讲师情况以及稳定的持续音频 结合的完整直播

即,通过现场的 `导播` ,不用后期合成,
直接在 Youtube 上形成最终可异步自学的流畅视频.

### 设备
可见,在现场要实时收录现场的音频/视频,而且空间关系, `主播电脑` 需要频繁操作,
使用内置摄像头,就太不人道了,

所以,珠海GDG 选购,配置了: `罗技(Logitech)Pro C920 高清网络摄像头`

![2709051_C92003_thumb.jpg(JPEG 图像,500x375 像素)](http://img0.pconline.com.cn/pconline/1203/19/2709051_C92003_thumb.jpg)

~ 卡尔·蔡司镜头,双立体声麦克风, Fluid Crystal™ 技术,最高1500万像素

关键是 `C920` 兼容 MAC 系统!
而且,使用下来, Chrome 的 Hangout 插件,可以直接识别出来,不用特殊驱动!

### 录音

但是,一般来说,大家是难以上 Youtube 来回看的,
而从 youtube 转载视频到墙内服务,不仅慢,而且有广告的问题.

所以,珠海GDG 一般习惯,现场用录音笔,实时完成现场录音,
在后期纪要时,统一发布: `幻灯+录音+视频+文字点评` 的综合纪要.

足以支持无法现场/线上参与者的异步自学.

## 高阶

当然,以上都是指国内的 HOA 情景,
但是,HOA 真正威力的地方,是可以随时和全球的技术人员实时沟通!

所以,有更高的组织技巧...


Cheng Lu <chenglu99@gmail.com>经验分享

### HOA同声传译

- 方案1:纯Hangouts

找一个专用的房间,最好是周晓雯口译专业的教室(或录音室)
请周晓雯负责再请一到三位同专业的同学,为I/O Keynote的不同话题和演讲嘉宾分角色进行同声传译

需要解决技术难题:

多人同时进行翻译,最好每个人一台电脑,如何保证每个人的看到的I/O Keynote直播画面是同步的(包括听到的声音)?如果每台电脑上都通过Youtube观看直播,视频播放的进度会有先有后. Hangouts中的Youtube插件可以帮助同步. 但是,声音播放和录音不能同时进行---播放视频的时候,麦克风会被静音;如果打开麦克风(push to talk),Youtube视频又会被静音. 并且,每台电脑只允许开一个Hangout---必须要有两个设备,比如一台电脑通过Hangout的Youtube插件观看直播,一部手机加入我们自己的HOA进行另外的直播(和录像)
如果用一台电脑,需要负责翻译的同学都在同一个屋子里,脑袋挤在一起. 这样不见得不好,方便他们彼此沟通. 

- 方案2:Skype录音

参考:
[linux skype recorder - Google Search](https://www.google.com/search?q=linux+skype+recorder&oq=linux+skype+recorder&aqs=chrome..69i57j69i65l2j69i59l3.6365j0j7&sourceid=chrome&es_sm=122&ie=UTF-8)
    - [Automatically Record Skype Calls In Linux With Skype Call Recorder ~ Web Upd8: Ubuntu / Linux blog](http://www.google.com/url?q=http%3A%2F%2Fwww.webupd8.org%2F2014%2F03%2Fautomatically-record-skype-calls-linux-skype-call-recorder.html&sa=D&sntz=1&usg=AFQjCNEx5fV4oh1RzFn_MX9OUok4Ttx_gg)
    - [Skype Call Recorder | Download](http://www.google.com/url?q=http%3A%2F%2Fatdot.ch%2Fscr%2Fdownload%2F&sa=D&sntz=1&usg=AFQjCNEQK9-I2FFmjt2VRZ0Y9OYoMMqdrA)



### 如何提高录音质量

提高录音质量是一个无底洞---要想把声音质量做好,需要专业的设备. 动不动几千块钱. 相信下面的设备不是老百姓玩儿得起的. 
[Wireless microphone - Wikipedia, the free encyclopedia](http://www.google.com/url?q=http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FWireless_microphone&sa=D&sntz=1&usg=AFQjCNElRP9_yhmLZ7rH99gMBiLlX9M3tg)


如果演讲人(和提问的观众)的手机安装了Google+ Hangouts,
为什么不让他们在说话之前加入进来呢

---用手机当无线麦克(和耳机,如果需要助听的话)

- 可以关闭视频
- 插上带麦克的耳机线... 需要测试一下,会不会有回声
    - ~测试过了,使用N5和原配耳机线,能够将回声降低到最小;如果只用手机,不接耳机线,回声会很明显.
- ... 还有延迟(如果公放)
    - ~ 在同样的测试中,PC使用EC2新加坡出口,手机使用Linode东京出口,有不到一秒钟的延迟. 

正式推荐组合:

- G+ Hangout 
- + 手机等移动设备(Android,iPhone,iPad,iPod都支持)
- + 带麦克的耳机线

可以代替无线麦克,实现高质量的录音. 

还考虑过蓝牙耳麦. 但是电池可能不能坚持很久. 

有人已经做了类似的服务(收费的),
[Crowd Mics - Android Apps on Google Play](https://play.google.com/store/apps/details?id=com.crowdmics)


TODO eval

- [Smart Voice Recorder - Android Apps on Google Play](https://play.google.com/store/apps/details?id=com.andrwq.recorder)
- [Easy Voice Recorder - Android Apps on Google Play](https://play.google.com/store/apps/details?id=com.coffeebeanventures.easyvoicerecorder)

顺便推荐索尼的录音机软件

- [Audio Recorder - Android Apps on Google Play](https://play.google.com/store/apps/details?id=com.sonymobile.androidapp.audiorecorder)
## 是也乎

感谢社区中大家分享的经验,包含:

- 上海GDG Sting/Cheng Lu 
- 中国GDE 韩国恺





## 巡阅
- 150113 [Zoom.Quiet](http://zoomquiet.io/) checked




