---
layout: post
title: Merge by MailChimp使用速记
author: zoomq
categories: Howto
tags:  gdg guider mailchimp
---

~ 如何Merge by MailChimp 进行邮件群发

来自:

```
from:    Alpha Yang
reply-to:    china-gdg-managers-forum@googlegroups.com
date:    Thu, Mar 13, 2014 at 6:06 PM
subject:     向大家介绍直接在Google Drive里利用Docs和Spreadsheet发送活动邮件
```

一切都是因为 Google Driver 的接口开放!

<img src="http://skm.zoomquiet.io/data/20140313181550/getaddons.jpg"
    height="150">


<!--more-->

事实上,随着 Chrome OS 的发布,Google 早已静静的在所有 Chrome 能展示的服务中,
加入了自个儿的 `Add-ons` 市场!

对社区活动来说,最大的困难,可能是活动组织中
各种邀请/谢绝/通知/问卷 等等邮件的发送,
无论使用什么手工/联系人导入/脚本 等等,
都解决不了送达率追踪的问题, 究其原因:

1. 批量邮件发送时,在邮件过滤体系里
    (MTA(邮件传输代理)过滤,MDA(邮件投递代理)过滤,MUA(邮件用户代理)过滤)
    中国各种邮件服务的等级很低,基本上都会判定为垃圾
1. 这种批量邮件,难以简单的进行关键信息的替换,又或是使用富格式邮件


现在结合 Google Docs 服务以及 MailChimp 服务的扩展:

![](http://skm.zoomquiet.io/data/20140313181550/mergedescription.jpg)

就可以轻易解决以上问题,

整体过程:

1. 新建一个Spreadsheet,用一列来维护收件人列表. 
2. 新建一个Doc,写通知正文,图片文字任意. 
3. 在Doc中安装Merge By MailChimp的插件,参考:[官方文档](http://kb.mailchimp.com/article/what-is-merge-by-mailchimp)
4. 从文档的 `Add-ons` 菜单中进入 `Merge by MailChimp` 扩展

![](http://skm.zoomquiet.io/data/20140313181550/mergeinstalled.jpg)

然后自然的选择数据表,选择动态字段,配置邮件信息,而且可以实时 预览
![](http://0.zoomquiet.top/ZHGDG/wechat/140314-merge-0.png)

只需几分钟,几百封活动通知就会发出去了. 

有爱的发送条件自检

![](http://0.zoomquiet.top/ZHGDG/wechat/140314-merge-1.png)


成功后的 `High Fives`

![](http://0.zoomquiet.top/ZHGDG/wechat/140314-merge-2.png)

收到的邮件

![](http://0.zoomquiet.top/ZHGDG/wechat/140314-merge-end.png)

最贴心的是可以实时观察邮件的送达/阅读情况

<img src="http://skm.zoomquiet.io/data/20140313181550/reportsdetails.jpg"
    height="400">


简单原理:

- 通过网页扩展机制,调用 [Google Apps Script](https://script.google.com/) 使用 Docs 服务的接口, 读取Doc的内容,其实就是html,
- 再读取Spreadsheet中的数据,
- 拼成邮件内容,
- 最后调用MailChimp的API发送. 

`限制`:

- 一次1000人以下的收件人发送
- 每个月限额6000封. 

目测,对于一般社区足够了,
何况这是每个 Gmail 帐号的限制,完全可以注册多个帐号,轮用!







## 巡阅
- 150113 [Zoom.Quiet](http://zoomquiet.io/) checked





