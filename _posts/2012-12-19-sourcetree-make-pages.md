---
layout: post
author: zoomq
title: 使用SourceTree 来管理 Gitcafe 的Pages 发布Blog!
description: 最美的版本控制客户端 ~ 用SourceTree 来管理 Gitcafe 的Pages 发布Blog!
categories: Howto
tags:  git gitcafe pages
---



有个好爹的 SourceTree
------------------------------

[![footer_sourcetree_logo.png(PNG 图像,354x78 像素)](http://www.sourcetreeapp.com/img/footer_sourcetree_logo.png)](http://www.sourcetreeapp.com/)
是来自 [JIRA](http://www.atlassian.com/software/jira/overview) 的娘家
[Bitbucket](https://bitbucket.org/) 的新东家
[![confluence_48_trans.png(PNG 图像,48x48 像素)](https://confluence.atlassian.com/images/logo/confluence_48_trans.png)](http://www.atlassian.com/) ATLASSIAN.com

- 一家成功的,对敏捷软件工程拥有全栈式支持的商业公司,
- 所推出的 MAC 专用, SVN+Hg+Git 客户端!

的确非常好用,虽然是全E文界面的,俺来快速演示一下如何...

<!--more-->

用 SourceTree 发布 Pages
------------------------------

整体思路,参考:

- [[2012/10/31]GitCafe正式推出Pages服务 | Blog – GitCafe](http://blog.gitcafe.com/116.html)
- [Creating Project Pages manually · github:help](https://help.github.com/articles/creating-project-pages-manually)


在 `Gitcafe` 中发布 `Pages` 也是同样的过程:

+ 注册帐号,部署 `SSH公匙`
+ 将帐号加入对应仓库的成员列表
    - 当然,也可以走 `github` 倡议的 `Frok->code->Pull Requests->Pull+merged` 流程
+ 在本地 `clone` 出仓库复本,进行写作
    - `注意:` 必须在约定的 `gitcafe-pages` 分支中建立 `Jekll` 工程,才会被当成 `Pages` 业务被编译!
+ 解决可能的冲突后,`push` 到 `Gitcafe` 完成自动编译,发布



###环境整备


###环境整备

- 先要有 `gitcafe` 帐号,并发布有正当的 `SSH公匙`

![00-cafe-pubkey](/img/sourcetree/00-cafe-pubkey.png)

- 并由管理员增加为成员

![04-cafe-team](/img/sourcetree/04-cafe-team.png)


###初始化本地复本

- 获取对应仓库的可写 `URI`

![00-gituri.png](/img/sourcetree/00-gituri.png)

- 在 [SourceTree]](http://www.sourcetreeapp.com/) 中定义仓库的 `clone` 信息,并指定合理的目录,以及想检出的分支:

![01-st-clone](/img/sourcetree/01-st-clone.png)
![01-st-cloned](/img/sourcetree/01-st-cloned.png)

- 完成时的情景

![02-st-bookmarks](/img/sourcetree/02-st-bookmarks.png)

- 富有苹果味儿的主窗口,所有关键功能一目了然!
- `注意!` 内置支持 [gitflow](https://github.com/nvie/gitflow)

![03-st-mainwin](/img/sourcetree/03-st-mainwin.png)


###日常处置

- 双击文件就可以编辑
- 保存后,就知道了变化:

![05-md-changed](/img/sourcetree/05-md-changed.png)

- 使用 `Commit` ,在窗口中选择 `Selected files` 就等于自动先完成 `git add .`

![06-st-ci-add](/img/sourcetree/06-st-ci-add.png)

- 完成 `Commit`, 可以注意到 `Push` 已经出现数字,表示在末 `Push` 的变更

![07-st-cied](/img/sourcetree/07-st-cied.png)

- 使用 `Push`, 注意,有各种常用选项

![08-st-pu](/img/sourcetree/08-st-pu.png)

- 完成 `Push`:

![09-st-pushed](/img/sourcetree/09-st-pushed.png)
`
![10-st-pued-main](/img/sourcetree/10-st-pued-main.png)


- 果然成功的发布到了 `Gitcafe

![11-cafe-same](/img/sourcetree/11-cafe-same.png)



参考
------------------------------

- 什么是 `SSH` ? ~ [SSH原理与运用(一):远程登录 - 阮一峰的网络日志](http://www.ruanyifeng.com/blog/2011/12/ssh_remote_login.html)
- 什么是 [gitflow](https://github.com/nvie/gitflow)
    - [Why aren't you using git-flow? - Jeff Kreeftmeijer](http://jeffkreeftmeijer.com/2010/why-arent-you-using-git-flow/)
    - 中译:[你为神马不用git-flow呢? | Jeff的妙想奇境](http://www.jeffkit.info/2010/12/860/)



## 巡阅
- 150113 [Zoom.Quiet](http://zoomquiet.io/) checked



