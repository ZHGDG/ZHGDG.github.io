---
layout: post
title: Gmail 生活指南
description: ~ 如何通过正当的使用gmail来让自个儿的生活自在
author: zoomq
categories: Howto
tags:  gdg guider gmail
---


![gmail.png(PNG 图像,512x512 像素)](https://machias.edu/assets/images/icons/gmail.png)

在以往多年互联网生涯过程中,体验过各种邮件之苦.
慢慢的,形成了当前相对舒适的邮件处理习惯.足以 cover 住常见的邮件管理情景.

特此简要分享出来,以便有心的小伙伴上手...


<!--more-->

准入条件:

- `习惯` 科学上网
- `习惯` 用 Chrome/Safari/Firefox ,万不得以也可以安装 Opera, 死也不能用 IE !
- `习惯` 配置为E文语言界面

参考:

- 幻灯: [2.22-SOD-Kaoupulity-email](https://speakerdeck.com/zoomquiet/2-dot-22-sod-kaoupulity-email)
- 录音: [ZHGDG/2014/140219-skill4mail {gen. by gen4idx.py v13.4.18}](http://0.zoomquiet.top/ZHGDG/2014/140219-skill4mail/index.html)

## 俺的gmail

获得邀请: 040817

    from:    Gmail Team <gmail-noreply@google.com>
    to:  Zoom Quiet <zoom.quiet@gmail.com>
    date:    Fri, Aug 27, 2004 at 5:21 PM

- 邮件总数: 346,009 (140423 20:17)
- 邮件总量: 26.8 GB 
- 25+ 别名邮箱
- 140+ 标签
- 280+ 过滤器

## 俺的习惯

是从 Foxmail->the Bat!->Thunderbird 一系列邮件客户端积累下来的邮件处理习惯,
逐步配合所有的工作场景,以及处理流程后才形成的,
其时间跨度长达 15+年.

所以,必定是特化的...

## 配置

- Language: `English(US)`
    - 这样才能享受最新,最稳定功能
- Default reply behavior: `Replay all`
    - 多了删除,比加要快
- Keyboard shortcuts: `on`
    - 如果这个功能不开启,那么 gmail 的邮箱处理效能就少了 80%
- Outgoing message encoding: `Use Unicode (UTF-8) encoding for outgoing messages`
    - 不用 UTF-8 就是耍流氓!
- Stars: 手工调整为彩虹色 
    - ![starts](http://0.zoomquiet.top/ZHGDG/wechat/gmail-guider/starts.png)
    - 习惯的心理含义:
        - 红星: 紧急且重要
        - 橙>>: 需要跟进的事儿
        - 黄!:  警告,有问题的
        - 绿勾: 已完成,但是,近期可能要复用的
        - 兰i: 关键配置信息/知识点/备用文档
        - 紫?: 跟进有疑问的事儿
    - 用快捷键: `s` 快速对选中的邮件循环星标切换
- Labs: 实验室功能,常年开启
    - Authentication icon for verified senders
    - Auto-advance
    - Custom keyboard shortcuts
        - `Archive` -> `A`
    - Quote selected text
    - Smartlabels
    - Undo Send
    - Unread message icon

## 邮件处置
列举几个最常用的处置流程,其它不常见的就不说了....

### Inbox为空

目标:

- 收件箱总为空, 无心理压力
- 所有邮件又都能及时获得处理

行为:

- 上午关键任务没有完成前,不处理邮件
- 高速清除收件箱邮件:
    1. 所有邮件的标题快速看过
    1. 在自动标签辅助下,当场决定是否看,是否回复,是否标注
        - `enter` 进入邮件,看正文
        - `u` 返回 conversations 列表
    1. 需要回复/跟进/转发/收藏..处置的,立即打上对应的星标
        - `*U*I->A` 归档所有未读正文的不必要处置的邮件
        - 面对少了 90% 邮件的 conversations 列表,再确认是否要阅读/回复
        - `*A->A` 选择所有并归档

### 定期处置星标邮件

目标:

- 长期追踪的任务不会丢失
- 只在自个儿方便的时候处理

行为:

- 一般在下午上班的第一个时段, 否则就是下班后
- `g->s` 进入星标邮箱
- 逐一 review 邮件,分别进行快速处置:
    - 红星: 立即回复,并根据事务,切换为其它星标/取消星标
    - 橙>>: 查阅内容,决定是否戳
    - 黄!:  同 红星 处置
    - 绿勾: 跳过
    - 兰i: 跳过
    - 紫?: 决定是否再次询问

### 任务板

目标:

- 对长期追踪,又不重要的事儿,合理追踪,不忘记
- 以最舒服的形式

行为:
(一般现在只对 徣书 的备报邮件进行如下处置)

- 使用 `j`/`k` 快速定位到相关邮件
- `x->g->k` 选择并丢入任务板
    - ![tasks](http://0.zoomquiet.top/ZHGDG/wechat/gmail-guider/tasks.png)
- 未来如果还了书
    - 进入任务板
    - 点击对应借条的关联邮件
    - 回复确认已收到还书
    - 点击 任务条目的完成


### 别名邮箱

背景:

- 因为管理多个社区的域名邮箱
- 而 Gmail 只允许配置最多 5 个外部邮箱的提取

方案:

- 将有权限又不常用的邮箱配置为别名邮箱收发
- 即:
    - [Send mail from a different address or alias - Gmail Help](https://support.google.com/mail/answer/22370?hl=en&ctx=mail)
    - 外部邮箱配置好自动转发,将所有邮件转发给 gmail 
    - 而 gmail 则通过 Google 的 SMTP 服务,以外部邮箱的名义发送邮件
- 这样就突破了 `Check mail from other accounts (using POP3)` 的功能上限


## Gmail 之伤

背景:

- 网络不可靠
- 浏览器不可靠
- 网页不可靠
- JS 是会抽疯的

方案:

- 安装: 
[It's All Text ! :: Add-ons for Firefox - Mozilla Add-ons](https://addons.mozilla.org/en-US/firefox/addon/its-all-text/)
- 配置快捷键 `Ctrl-e` 调用本地习惯的编辑器, 俺现在是 Sublime Text 2
- 回复邮件时,就变成了:
    1. `enter` 进入邮件
    1. `a` 回复全部,进入编辑框
    1. `Ctrl-e` 跳出页面,进入 subl 编辑
    1. `It's All Text!` 在本地硬盘目录中创建了缓存用 `.txt` 文本,用 subl 编辑时,每次保存时,能自动刷新内容到对应网页的对应编辑框中
    1. 在本地编辑器中完成内容编辑后,保存,回到网页,点击发送.
- 这样,既然网络/浏览器/网页.. 发生问题,俺在本地都有一个包含完备的邮件回复内容的纯文本文件,可以随时重启浏览器/网络后,手工恢复回去...

桑心:

- 但是, G+ 爆起后,逼 gmail 升级
- 现在邮件回复的编辑框不是标准的 html textarea 了,`It's All Text!` 无法锁定进行提取并进行辅助的外部编辑
- 回复邮件时,就变成了:
    1. `enter` 进入邮件
    1. `a` 回复全部,进入编辑框
    1. `Ctrl-a` 复制所有内容
    1. 打开常备的 subl 的常用缓存文件 `stuff.txt` `Ctrl-v` 粘贴进来
    1. 在本地编辑器中完成内容编辑后,保存,`Ctrl-a` 复制所有内容
    1. 回到网页,`Ctrl-a->Ctrl-v` 替换粘贴进来,再点击发送.


## 是也乎
~ 为毛?

- [珠海GDG社区行动手册之邮件列表](http://blog.zhgdg.org/2013-06/zh-gdg-mailing/)
- 演讲:
    - [2.22-SOD-Kaoupulity-email](https://speakerdeck.com/zoomquiet/2-dot-22-sod-kaoupulity-email)
    - [140222_sod-cbi_4_email.MP3](http://res.zoomquiet.io/ZHGDG/2014/140222-sod-cbi/140222_sod-cbi_4_email.MP3)
    - [140219_wps2_work_mail.MP3](http://res.zoomquiet.io/ZHGDG/2014/140219-skill4mail/140219_wps2_work_mail.MP3)


简单的说,坚持,才能出效率...


## 修订记录

- 140423 释放初稿
- 140401 设定章节
- 140221 意动,创建 draft




## 巡阅
- 150113 [Zoom.Quiet](http://zoomquiet.io/) checked




