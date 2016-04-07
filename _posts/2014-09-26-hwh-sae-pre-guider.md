---
layout: post
title: HwH 之 SAE初体验-导入手册
author: zoomq
categories: Howto
tags:  gdg HwH guider
---

![](http://sae.sina.com.cn/static/image/home/logo.png)
+
![round_activepython.jpg(JPEG 图像,100x100 像素)](http://templates.activestate.com/images/product_logos/round_activepython.jpg)

有关活动形式 ~ HwH

- E文名: `Hand with Hand`
- 中文名: `手把手极限实训`
- 完全0基础编程实战培训, 相比 `CodeLab` 有完备的教程, `HwH` 更加看重现场的主动实践
- 通过整个下午的持续的,系列小任务的自主达成,在导师合理指点下完成全新技术领域的探索

但是,怎么进入呢?

<!--more-->

- 首先...
- 你...
- 得...
- 有...
- 个...
- 女朋友...

闹! 错了... `首先你得报名参加哪!`

## 报名有几个意思

1. 表明,你是主动参加的,不是 `被参加的` ~ 众所周知的原因,但凡是 `被` 的都不怎么科学
2. 这样,才能收到邀请邮件, 获得正确的进入引导, 因为,为了现场效能,我们只能开小班加强交流,所以,是有选择标准的,不是所有人都能获得邀请的
3. 然后, 才有然后: 在活动之后,才能有针对性的通过你的邮箱进行持续的支持


## 整体概述:

活动整体上,以现场主动自学为主,不过,分成小组, 相互帮助,高度精力集中,在

    规定时间期限
    规定任务完成

具体节奏:

1. 导入+通介演讲
2. 实战编程
3. 小组回顾, 现场讲述过程中,最难受的坎儿

`注意!`

- 全程录音/录像/直播
- 请大家作好准备!


## 预备条件:
- 参与同学有私人笔记本电脑
- 参与同学有一定的任意编程语言基础,独立完成超过100行可运行代码的撰写
- 自行在个人电脑上安装好 activepython
    - [activestate.com/activepython](http://www.activestate.com/activepython)
- 自行完成 SAE 的注册并能根据文档创建 demo 工程
    - [sae.sina.com.cn](http://sae.sina.com.cn)
- 预习: Python — SAE文档中心 1.0 文档 
    - [sae.sina.com.cn/doc/python](http://sae.sina.com.cn/doc/python/index.html)
    - 最好能完成文档中简单 demo 的部署和运行
- 参考在线高级教程:
  - [42分钟乱入 SAE 手册!-) — chaos2sae 1.0.120425 documentation](http://chaos2.zoomquiet.io/sae/build/html/)

任何问题,随时将珠海GDG 组织者邮件咨询:

- **gdg-zhuhai[AT]googlegroups.com**
- 将 `[AT]` 替换为 `@` 即为目标邮箱 ;-)

## 环境安装手册

目标,无论 M$/Linux/OS X 环境中,都可以进行完备的针对 SAE 的:

- Python 脚本编辑
- 本地应用测试
- 代码部署推送

以上嘦完整的安装:

- Python
- SAE 以及依赖
- (只有M$ 用户需要,SVN客户端)

### NGU/Linux 或是 MAC

因为这些对开发者友好的系统,都内置了 Python, 以及完备的代码编辑工具,
所以,只需要安装 SAE 环境就好,
而且,操作也基本一致:

    $ git clone https://github.com/sinacloud/sae-python-dev-guide.git
    $ cd sae-python-dev-guide/dev_server
    $ python setup.py install


### M$
也就稍微复杂一丁点儿点儿...

1. 从 [ActivePython Downloads](http://www.activestate.com/activepython/downloads) 下载安装,对应 CPU 类别的版本,安装之
1. 然后下载 SAE 的依赖包: [packages4sae.7z](http://res.zoomquiet.io/ZHGDG/HwH/sae101/packages4sae.7z)
    - 解压缩需要安装 [7-zip](http://res.zoomquiet.io/ZHGDG/HwH/sae101/7z920-x64.msi)
    - 进入 `packages4sae` 目录
    - 使用 `pip` 完成批量本地安装  


```
pip install --index-url=file://[/path/2/]local_packages/simple/ -r requirements.txt

# [path/2/] 的形式根据系统不同而不同
# Windows
# index_url = file:///C:/pip2pi/simple/

# Linux
# index_url = file:///home/myusername/.pip2pi/simple/

# Mac
index_url = file:///Users/myusername/.pip2pi/simple/
```

1. 下载 [sae-python-dev-guide.7z](http://res.zoomquiet.io/ZHGDG/HwH/sae101/sae-python-dev-guide.7z) 安装 SAE 本地测试环境
    - 解压缩需要安装 [7-zip](http://res.zoomquiet.io/ZHGDG/HwH/sae101/7z920-x64.msi)
    - 进入 `sae-python-dev-guide/dev_server` 目录
    - 使用 `Python` 自身完成安装  

```
python setup.py install
```

1. 最好,安装一个靠谱的编辑器,推荐 [npp.5.8](http://res.zoomquiet.io/ZHGDG/HwH/sae101/npp.5.8.bin.7z) ~ 绿色版本
1. 以及,一个科学的本地网络测试工具: `cURL` for win[32](http://res.zoomquiet.io/ZHGDG/HwH/sae101/curl-7.38.0-win32-local.msi)/[64](http://res.zoomquiet.io/ZHGDG/HwH/sae101/curl-7.38.0-win64-local.msi)
1. 最后,安装可爱的小乌龟(TortoiseSVN) ~ SVN 客户端
    - [TortoiseSVN-1.8.8.25755-win32-svn-1.8.10.msi](http://res.zoomquiet.io/ZHGDG/HwH/sae101/TortoiseSVN-1.8.8.25755-win32-svn-1.8.10.msi)
    - or [TortoiseSVN-1.8.8.25755-x64-svn-1.8.10.msi](http://res.zoomquiet.io/ZHGDG/HwH/sae101/TortoiseSVN-1.8.8.25755-x64-svn-1.8.10.msi)
    - 当然别忘记中文包, for [32位](http://res.zoomquiet.io/ZHGDG/HwH/sae101/LanguagePack_1.8.8.25755-win32-zh_CN.msi)/[64位](http://res.zoomquiet.io/ZHGDG/HwH/sae101/LanguagePack_1.8.8.25755-x64-zh_CN.msi)


## 思考
你想开发什么?

## 资源

- [Index of /ZHGDG/HwH/sae101 {gen. by gen4idx.py v13.4.18}](http://res.zoomquiet.io/ZHGDG/HwH/sae101/index.html)
- [What's Included in ActivePython 2.7](http://docs.activestate.com/activepython/2.7/whatsincluded.html)





## 巡阅
- 150113 [Zoom.Quiet](http://zoomquiet.io/) checked




