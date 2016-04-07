---
layout: post
author: zoomq
title: 如何在M$系统中管理 Gitcafe 的Pages 内容发布?
description: ~ 基于 msysgit,在M$ 系统中使用Git 来管理 Gitcafe 的Pages 发布Blog! 
categories: Howto
tags:  git gitcafe pages
---

[![msysgit-logo.png(PNG 图像,220x256 像素)](http://msysgit.github.com/img/msysgit-logo.png)](http://code.google.com/p/msysgit)
为杯具的 M$ 环境,一键式提供了 `git` 环境!

那么如何使用 gitcafe 提供的 pages 服务?
------------------------------------------------------------

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
<!--more-->


###强调一下思路

- `gitcafe-pages` 本质是在服务端的 `jekyll <http://jekyllrb.com/>`_ 服务
- 所以,我们在本地写文章时,只需要记住:
    - 所有文章组织在 `_posts` 目录中
    - 使用的文件名格式为:

{% highlight bash %}
2012-12-19-usage-msysgit-make-pages.md
|   |  |    |                      +- 后綴名指使用 Markdown 语法的结构化纯文本
|   |  |    +- 以减号间隔开始的有意义的E文 文章名,将成为访问时的URL 一部分
|   |  +- 日期
|   +- 月份
+- 年份

{% endhighlight %}


以及文本的前几行使用固定格式来声明一些文章信息:

{% highlight bash linenos %}
---
layout: post
title: 如何在M$系统中管理 Gitcafe 的Pages 内容发布?
description: ~ 基于 msysgit,在M$ 系统中使用Git 来管理 Gitcafe 的Pages 发布Blog! 
categories: Howto
tags:  git gitcafe pages
---

...正文
{% endhighlight %}

具体说明:

1. `---` 约定控制标识符
2. `layout: ` 指出使用哪个模板,不要修改!除非你知道怎么回事儿!
3. `title: ` 文章标题
4. `description: ` 简述,有的模板首页只有简述没有正文的,输出的就是这儿的文字
5. `categories: ` 分类标签,使用空格区分多个
6. `tags: ` 内容标签,使用空格区分多个
7. `---` 约定控制标识符
8. 最好有个空行同正文分开


`注意!!!` ~ 所有的配置声明格式为: `变量:`+空格+`配置内容` ,少了空格会引发各种问题的!


以上就是写文章所要知道的一切了,以下所有配置什么的, 99% 都是为了在 `M$` 中使用 `git` 而已...

- 真实的 html 页面是在服务端生成到 `_site` 目录中的
- 大家在本地,反而不必要一定先生成 html 页面的
- 甚至于,一般使用 `.gitignore` 配置文件,强制 `git` 忽略 `_site` 目录的变化,不进行版本监控!



###安装 msysgit 整备环境

- 下载: [msysGit-netinstall-1.8.0-preview20121022.exe](http://msysgit.googlecode.com/files/msysGit-netinstall-1.8.0-preview20121022.exe)
- 参考:
    - [在windows安装配置Git开发环境](http://www.starming.com/index.php?action=plugin&v=wave&tpl=union&ac=viewgrouppost&gid=32767&tid=1000002148)
    - [Windows 系统下Git安装图解 | Drupal中国](http://drupalchina.cn/content/windows-xi-tong-xia-gitan-zhuang-tu-jie)
- `注意`: `...选择Git文件夹,右键,选择Git Bash Here,会弹出shell命令行界面` 可能不一定有
- 不过,可以自然的进入 msysgit 安装目录中, 点击 `git-cmd.bat` 
    - 在其中调用 `bin` 下的 `bash.exe` 进入方便的 shell 环境
    - 就可以自动的引用到 `ssh-kengen.exe` 生成对应的 `SSH` 密匙对!

![0-bash.png](/img/msysgit/0-bash.png)


命令形如: 
{% highlight bash %}
bash-3.1$ ssh-keygen -C "zhouqi@ijinshan.com" 
Your identification has been saved in /c/Documents and Settings/Administrator/.s
sh/id_rsa.
Your public key has been saved in /c/Documents and Settings/Administrator/.ssh/i
d_rsa.pub.
The key fingerprint is:
cf:1b:90:1b:25:0a:12:61:ff:ad:71:d0:ec:cd:5f:55 zhouqi@ijinshan.com

{% endhighlight %}

- 输出的提示中清晰的指出了生成的密匙对文件在哪个目录
- 只是形式同平时 `cmd` 环境中的有点不同,少了恶心的 `:` 以及分隔线是 UNIX 形式的
- 所以, `/c/Documents and Settings/Administrator/.ssh` 
- 就是 `C:\Documents and Settings\Administrator\.ssh`
- 从对应的文件中复制出公匙字串,这里是 `id_rsa.pub` 发布为个人帐号的公匙:

![00-cafe-pubkey](/img/sourcetree/00-cafe-pubkey.png)


再由仓库管理员加 `gitcafe` 帐号为 `blogging` 仓库的协作人员:

![04-cafe-team](/img/sourcetree/04-cafe-team.png)


并在本地配置合理的全局变量:
{% highlight bash %}
bash-3.1$ git config --global user.name "zhouqi"
bash-3.1$ git config --global user.email "zhouqi@ijinshan.com"
{% endhighlight %}



可以使用git 命令观察是否生效:
{% highlight bash %}
bash-3.1$ git config --list
# ...
http.sslcainfo=/mingw/bin/curl-ca-bundle.crt
sendemail.smtpserver=/mingw/bin/msmtp.exe
diff.astextplain.textconv=astextplain
rebase.autosquash=true
user.name=zhouqi
user.email=zhouqi@ijinshan.com
{% endhighlight %}




###使用 git 命令初始化本地工作仓库

从仓库首页可以获得有写入权限的 `URI`:

![00-gituri.png](/img/sourcetree/00-gituri.png)


在合适的空白目录中 `clone` 远程仓库到本地,并同时切换为指定的 `gitcafe-pages` 分支:

{% highlight bash %}
bash-3.1$ pwd
/c/msysgit 

bash-3.1$ git clone  --branch gitcafe-pages git@gitcafe.com:Liebao/Liebao.git blog
Cloning into 'blog'...
The authenticity of host 'gitcafe.com (50.116.2.223)' can't be established.
RSA key fingerprint is 84:9e:c9:8e:7f:36:28:08:7e:13:bf:43:12:74:11:4e.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'gitcafe.com,50.116.2.223' (RSA) to the list of known
 hosts.
remote: Counting objects: 127, done.
remote: Compressing objects: 100% (122/122), done.
remote: Total 127 (delta 47), reused 0 (delta 0)
Receiving objects: 100% (127/127), 458.50 KiB | 377 KiB/s, done.
Resolving deltas: 100% (47/47), done.
{% endhighlight %}

- 参考: [[2012/10/31]GitCafe正式推出Pages服务](http://blog.gitcafe.com/116.html)


在资源管理器中就可以见到整个基于 [jekyll](http://jekyllrb.com/) 的团队blog 工程了!

![2-cloned.png](/img/msysgit/2-cloned.png)


####推荐配置

在 git 配置文件中声明有意义的别名:

修订 仓库目录中 .git/cofig 文件
- 即,如果 `clone` 的仓库目录是 `C:\msysgit\blog`
- 则,仓库配置文件就在 `C:\msysgit\blog\.git`

默认内容类似:
{% highlight ini %}
[remote "origin"]
    url = git://gitcafe.com/Liebao/Liebao.git
    fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
    remote = cafe
    merge = refs/heads/master
{% endhighlight %}



追加一节:
{% highlight ini %}
[remote "cafe"]
    url = git@gitcafe.com:Liebao/Liebao.git
    fetch = +refs/heads/*:refs/remotes/origin/*
{% endhighlight %}



- 以后就可以使用 `cafe` 来替代 `origin` 来指代当前仓库名了!


![1-config.png](/img/msysgit/1-config.png)





###使用 markdownpad 进行文章编辑

- 免费好编辑器! [http://www.markdownpad.com/](http://www.markdownpad.com/)
- 下载,安装,没什么好说的
- 完全吻合 word 式编辑的环境! 左窗写 markdown,右窗自动编译成最终效果:

![3-markdownpad.png](/img/msysgit/3-markdownpad.png)


编辑保存后,使用 `status` 可以观察到变化:
{% highlight bash %}
bash-3.1$ git status
# On branch gitcafe-pages
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#       modified:   _posts/2012-12-10-git-note.md
#
no changes added to commit (use "git add" and/or "git commit -a")
{% endhighlight %}




使用 `add` 收录变更,才能 `commit`, 最后 `push` 后,才能发布到 `gitcafe` 的团队仓库:
{% highlight bash %}
bash-3.1$ git add . 

bash-3.1$ git commit -m "zhouqi throught XP + msysgit"
[gitcafe-pages 6f50b04] zhouqi throught XP + msysgit
 1 file changed, 4 insertions(+)
 
bash-3.1$ git push cafe
warning: push.default is unset; its implicit value is changing in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the current behavior after the default changes, use:

  git config --global push.default matching

To squelch this message and adopt the new behavior now, use:

  git config --global push.default simple

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

Counting objects: 7, done.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 426 bytes, done.
Total 4 (delta 3), reused 0 (delta 0)
To git@gitcafe.com:Liebao/Liebao.git
   89db4d6..6f50b04  gitcafe-pages -> gitcafe-pages
{% endhighlight %}

   

- `注意!` git 的提示非常智能,会好心提醒我们忘记的参数,不过,一般都是可以智能猜中我们的期待,完成合理的操作!   
- 基于以上的操作,在远程仓库中就可以见到自个儿的提交了!

![11-cafe-same](/img/sourcetree/11-cafe-same.png)



####技巧: 图形化版本树!
{% highlight bash %}
bash-3.1$ git log --graph --pretty=oneline --abbrev-commit
* 59a267c 快速使用 README 教程M$+SourceTree 使用
*   3fa9827 Merge branch 'gitcafe-pages' of gitcafe.com:Liebao/Liebao into gitcafe-pages
|\  
| * 6f50b04 zhouqi throught XP + mysysgit
| * 89db4d6 使用协作人員的身份对仓库进行 add+ci
* | 2d7c376 before merge ci 先
|/  
* f20f7ef 根据协同过程,增补使用说明+++格式追加分层
* 7e9496e 根据协同过程,增补使用说明++
* 5f1e4bf 根据协同过程,增补使用说明
* 80846ab 演示多人协同时的流程+
*   e8b5e0f Merge branch 'gitcafe-pages' of gitcafe.com:Liebao/Liebao into gitcafe-pages
|\  
| * 9783bab 尝试另外成员本地的协同过程
* | ce33b2e 增补res 目录,准备发布可能的幻灯资料..
|/  
* 61f39ee 增补本地图片使用样例
...
{% endhighlight %}


- 当有复杂的团队多人协作时,可以用来观察各种版本的合并关系
- 进一步的:
    - [个性化你的Git Log的输出格式](http://hisea.me/p/git-log-output-formats)
    - [pimping out git log - Bart's Blog](http://floss.zoomquiet.org/data/20120216152624/index.html)
    - 等等分享经验基础上,可以定制出我们自个儿喜欢的文字式图树表达来,比如笔者在 `bash` 中的情景:


![121219-git-ll](/img/121219-git-ll.png)


小结
------------------------------

总之使用 `git+gitcafe pages` 在 `M$` 中的日常操作命令只有:

1. `git clone --branch gitcafe-pages ...`
2. `git add .`
3. `git commit -a -m "注释"`
4. `git push cafe gitcafe-pages`
5. `git pull cafe gitcafe-pages`


而基础协同流程就两种:

- 第一次建立本地工作环境: `1->2->3->4`
- 以后平时: `5->2->3->4` 的循环



参考
------------------------------

- 什么是 `SSH` ? ~ [SSH原理与运用(一):远程登录 - 阮一峰的网络日志](http://www.ruanyifeng.com/blog/2011/12/ssh_remote_login.html)
- 什么是 [gitflow](https://github.com/nvie/gitflow)
    - [Why aren't you using git-flow? - Jeff Kreeftmeijer](http://jeffkreeftmeijer.com/2010/why-arent-you-using-git-flow/)
    - 中译:[你为神马不用git-flow呢? | Jeff的妙想奇境](http://www.jeffkit.info/2010/12/860/)



## 巡阅
- 150113 [Zoom.Quiet](http://zoomquiet.io/) checked



