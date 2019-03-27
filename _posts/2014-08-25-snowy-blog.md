---
layout: post
title: 手把手教你用git发布blog
author: snowy
categories: Howto 
tags:  gdg howto snowy
---

<img src="http://mikemclin.net/mmwp/wp-content/uploads/2013/03/markdown-syntax-language.png"
    width="540">

是的社区的 blog 文章很早就改进为基于 .md 的静态发布了,
但是,具体怎么折腾的呢?

由我们的小言现学现卖给大家伙儿 ;-)

<!--more-->

## 背景
如果用过 Wordpress 之类 CMS 系统为基础的 blog 环境,就知道,
一个 blog 网站不是那么简单的,至少包含以下关键性功能:

- 用户管理
- 撰写
- 发布
- rss
- cleanurl
- tag
- 分类
- 评注
- ...

而这所有的功能,又都要围绕一个数据库来折腾,
所以,传统的 blog 系统,至少要包含:

- 数据库
- 应用系统
- 发布系统

三大部分都要进行分别的安装/配置/测试/运维...

而且,即使 Wordpress 专注开发了10多年, 其在线文章编辑器,依然那么的难以使用...

所以,一切,在 [Markdown](https://gitcafe.com/GitCafe/Help/wiki/Markdown-%E8%AF%AD%E6%B3%95%E9%80%9F%E6%9F%A5%E8%A1%A8#wiki) 出现后终于进化了!

## 概述
现在 珠海GDG 的官方Blog ,是无网站全静态发布!

- [GitCafe](https://gitcafe.com/GitCafe/Help/wiki/pages) 作为代码托管服务, 替代了以往专用系统的
    - 用户管理
    - 撰写
- [GitCafe Pages 服务](https://gitcafe.com/GitCafe/Help/wiki/Pages-%E7%9B%B8%E5%85%B3%E5%B8%AE%E5%8A%A9#wiki),替代了:
    - 发布
    - rss
- 而隐藏在 pages 服务中的, Jekyll 替代了专用系统的:
    - cleanurl
    - tag
    - 分类
- [Disqus](https://disqus.com/about/) 纯JS 嵌入式评注服务,替代了专用系统的:
    - 评注

即,现在 blog 文章的撰写/修订/发布/管理,只需要:

+ 使用 markdown 格式在本地编辑 `.md` 文本
+ 通过 git 向 gitcafe 推送编辑结果

其它一切都自动化完成了!


### 参考:

- [Markdown 语法速查表](https://gitcafe.com/GitCafe/Help/wiki/Markdown-%E8%AF%AD%E6%B3%95%E9%80%9F%E6%9F%A5%E8%A1%A8#wiki)
    - [Markdown写作浅谈 - 阳志平的网志](http://www.yangzhiping.com/tech/r-markdown-knitr.html)
    - [图灵社区 : 阅读 : 用Markdown来写自由书籍-开源技术的方案](http://www.ituring.com.cn/article/828)
    - [所见即所得?---谈谈Markdown at 逸·Ease](http://floss.qiniudn.com/data/20070306124345/index.html)

- [安装和设置 Git](https://gitcafe.com/GitCafe/Help/wiki/%E5%A6%82%E4%BD%95%E5%AE%89%E8%A3%85%E5%92%8C%E8%AE%BE%E7%BD%AE-Git#wiki)
    - [Git 使用基础与技巧](https://gitcafe.com/GitCafe/Help/blob/master/Git.md#code)
    - [SSH 相关帮助文档](https://gitcafe.com/GitCafe/Help/blob/master/SSH.md#code)

- [GitCafe Pages 服务](https://gitcafe.com/GitCafe/Help/wiki/Pages-%E7%9B%B8%E5%85%B3%E5%B8%AE%E5%8A%A9#wiki)

- [jekyll/jekyll](https://github.com/jekyll/jekyll)
    - [Larry Cai - 5分钟快速架设个人博客](http://larrycaiyu.com/2012/03/16/setup-blog-in-5minutes.html)
    - [基于jekyll的github建站指南](http://jiyeqian.github.io/2012/07/host-your-pages-at-github-using-jekyll/)


## 过程
以下以 小言 多方尝试后的最终成果来罗列

- 环境: `Ubuntu`
- 如果想对应 Windows 环境中的操作,请自行搜索相关文章,或是请小言 哈根达斯 一次,来增补相关内容 ;-)

### 初始化
在本地建立基于 pages 服务的静态化blog 文章维护环境,是一次的,建立好后,
以后就再也不用折腾的了.

1. 安装git

`sudo apt-get install git`


2. 注册 [gitcafe](https://gitcafe.com) 进入 [zhgdg/zhgdg - GitCafe](https://gitcafe.com/zhgdg/zhgdg)

点击右上角的"派生", 生成自己专用的社区文章仓库分支.

3. 初始化本地仓库

```
# 进入合适的本地目录
$ cd ~/blog
# 克隆自己的文章分支仓库
$ git clone https://gitcafe.com/你的帐号名/zhgdg.git

...

```

4. 进入pages 专用分支:

进入目录:

`cd zhgdg`


```
# 察阅当前分支
$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/gitcafe-pages
  remotes/origin/master

# 切换pages 分支
$ git checkout gitcafe-pages
Branch gitcafe-pages set up to track remote branch gitcafe-pages from origin.
Switched to a new branch 'gitcafe-pages'

# 检查当前状态
$ git branch -a
* gitcafe-pages
  master
  remotes/origin/HEAD -> origin/master
  remotes/origin/gitcafe-pages
  remotes/origin/master
# 也可以用 status 命令
$ git status
On branch gitcafe-pages
Your branch is up-to-date with 'origin/gitcafe-pages'.
...

```


5. 配置提交口令

修订本地仓库的配置文件,可以通过 https 协议,自动输入用户/口令,来提交修订

- 进入本地仓库的 `.ssh` 目录
- 用文本编辑器,修订 `conf` 文件, 修订以下部分

```
...
[remote "origin"]
    #url = git@gitcafe.com:你的帐号名/zhgdg.git
    #将这一行替换为
    url = https://你的帐号:你的口令@gitcafe.com/你的帐号名/zhgdg.git
    fetch = +refs/heads/*:refs/remotes/origin/*
...

```
#### SSH 支持

- 生成公钥 (可选,用以 SSH 无口令提交内容)

`ssh-keygen -C "your email" -f ~/.ssh/github`

输入以上指令后,会出现一段内容. 

其中 

```
...
Your public key has been saved in /home/用户名/.ssh/github.pub
                                        |
                                        +-- 即新公钥所存放的位置

...
```

查阅公钥:
```
# 进入目录
$ cd /home/用户名/.ssh/
# 打印公匙
cat github.pub
...
```
cat之后出现的那一大段字符就是你的SSH公钥了


- 注册gitcafe,然后在 [您的 SSH 公钥 - GitCafe](https://gitcafe.com/account/public_keys) 上传公匙,

`以便使用 SSH 协议进行加密无口令提交!`

这样就不用将真实的用户和口令,暴露在本地配置文本中了

### 撰写
以下只是文章撰写前后要进行的工作,
而具体文章撰写的要求,参考专门的说明: [珠海GDG 社区文章 撰写指南](http://blog.zhgdg.org/2014-09/gdg-writer-guider/)


- 进入_posts目录,并查看过往文章
- 对过往文章,可以进行修订
- 也可以参照以往文章的格式,创建新文章,分享自个儿的想法/心得/体验

只是注意,每次编辑完要及时:

```
# 查阅当前仓库状态
$ git status

# 追加新增文件
$ git add .

# 提交文件修订
$ git commit -am "提交注释..."

```

注:可用"git log"查看提交日志

### 发布
在不同角色背景下, 文章的发布是有不同管理流程的.

#### frok-pull request 流程
这是 git 首创的社区协同流程,可以最大限制的接受最广泛的贡献.

但是,涉及 git 的多种操作建议认真参考:

- [Mort | Pull Request的正确打开方式(如何在GitHub上贡献开源项目)](http://www.soimort.org/posts/149/)
    - [4.1. Fork + Pull模式 — GotGitHub](http://www.worldhello.net/gotgithub/04-work-with-others/010-fork-and-pull.html)
    - [Git - 为项目作贡献](http://git-scm.com/book/zh/%E5%88%86%E5%B8%83%E5%BC%8F-Git-%E4%B8%BA%E9%A1%B9%E7%9B%AE%E4%BD%9C%E8%B4%A1%E7%8C%AE)
    - [Github 發 Pull Request & 貢獻流程速查](https://gist.github.com/timdream/5968469)
    - [Fork A Repo · GitHub Help](https://help.github.com/articles/fork-a-repo)
    - [github - undo git remote add upstream? - Stack Overflow](http://stackoverflow.com/questions/21940225/undo-git-remote-add-upstream)

我们的社区文章仓库也一样,和当前 小言 自个儿的私人分支仓库的关系,
决定了,小言的文章想最终发布到官方网站
http://blog.zhgdg.org/

得经过以下步骤:

1. 礼貌的同步官方仓库,整理好自个儿的提交
2. 提交整理好的 修订
3. 发起 pull request
4. 等候管理员合并 pull request 

##### 礼貌整理
简单的说,就是将自个儿多次修订,压平为一次提交,并解决可能的冲突

1. 追加上游仓库(一次性的)

```
$ git remote add upstream https://gitcafe.com/zhgdg/zhgdg.git
# 检查状态
$ git remote -v

```

2. 获得上游更新

```
$ git fetch upstream
```

3. 尝试合并上游更新

```
$ git rebase upstream/gitcafe-pages
# 如果有冲突,根据提示完成修订

```



##### 提交修订
提交合并后的成果
,是标准的 git 推送操作

```
$ git push -f

```
##### 发起PR

进入自个儿的仓库界面,点击右上角的"合并请求"/"pull request". 

进入以下界面后填写相关内容,点击"发送合并请求"

![140825-gitcafe.jpg(JPEG 图像,750x423 像素)](http://0.zoomquiet.top/ZHGDG/wechat/140825-gitcafe.jpg)

##### 完成合并
管理员将在主仓库的 `合并请求` 列表中看到新的 PR
点击 `接受请求` 就可以在服务端完成合并,以及 Jekyll 编译和发布了.

#### 主仓库流程
是的,如果小伙伴们长期向社区提交文章的 pull request ,当然的会赢得大妈们的信任,
就可以列为仓库成员,直接对
[zhgdg/zhgdg - GitCafe](https://gitcafe.com/zhgdg/zhgdg)
进行操作了,

嘦在本地重新检出一下 [zhgdg/zhgdg - GitCafe](https://gitcafe.com/zhgdg/zhgdg)
而不用自个儿 分支出来的那个私人仓库,
那么发布文章就一步:

```
$ git push
```

所以,坚持贡献,最后总是能获得更多的信任,以及更加快捷的分享渠道 ;-)

## 总结

整体上:

```
[一次性]
  + gitcafe reg. 
  |
  + frok zhgdg
  |
  + git clone U-FROK/zhgdg.git
  |   \
  |    +- 修订配置,使用https 协议+明文口令
  |   or
  |    +- ssh-keygen 生成本地密匙对,部署 SSH 公钥在 gitcafe
  |       使用 git 协议,用 SSH 认证,进行无口令提交
  |
  + git checkout gitcafe-pages
  |
[日常的]
    +- git add .          追加新文件
    +- git commit -am ".."提交变更
    |\ (有主仓库权限)
    | +- git push         直接推送修订即可
    |
    |  (没有主仓库权限, 以 pull request 流程发布)
    +- git remote add upstream https://gitcafe.com/zhgdg/zhgdg.git
    |
    +- git fetch upstream
    |
    +- git rebase upstream/gitcafe-pages
    |
    `- git push           推送整理后的修订
    到gitcafe 界面,发起 pull request,等待管理员接受,合并.

```


## 教训

在整个儿的探索/尝试过程中, 小言 也有一些的自然 Nive 理解,在此作为FAQ 提供给大家

## Changelog

- 140910 大妈 SriLanka 回来检查作业,重构一次
- 140825 成功完成第一个 RP 合并,当然不是规范的
- 140820 提交第一个版本
- 140812 月例会,倡议每周一篇文章,小言认领了此篇




## 巡阅
- 150113 [Zoom.Quiet](http://zoomquiet.io/) checked
- 150115 [Jeremy] checked




