珠海GDG  Blogging
====================================

- 当前查阅: http://zhgdg.gitcafe.com/
- 计划发布: http://http://www.chinagdg.com/zhgdg

依赖
------------------------------------

- [Git](http://git-scm.com/)
- M$下推荐安装: [Msysgit](http://www.starming.com/index.php?action=plugin&v=wave&tpl=union&ac=viewgrouppost&gid=32767&tid=1000002148)
- 然后,通过管理员部署 Public Key,方便也安全



建议配置
------------------------------------

- 首先应该注册 gitcafe
- 然后在 [您的 SSH 公钥 - GitCafe](https://gitcafe.com/account/public_keys) 上传公匙,以便使用 SSH 协议进行加密无口令提交!

再来初始化本地仓库:

    $ git clone git@gitcafe.com:Liebao/Liebao.git


然后配置别名,以加强输入记忆, 修订 仓库目录中 .git/cofig 文件

    ...
    [remote "origin"]
        url = git://gitcafe.com/Liebao/Liebao.git
        fetch = +refs/heads/*:refs/remotes/origin/*
    [branch "master"]
        remote = cafe
        merge = refs/heads/master


追加一节:

    [remote "cafe"]
        url = git@gitcafe.com:Liebao/Liebao.git
        fetch = +refs/heads/*:refs/remotes/origin/*


- 以后就可以使用 `cafe` 来替代 `origin` 来指代当前仓库名了!


日常使用@Windows
------------------------------------

###使用 msysgit 准备环境

- 下载: http://code.google.com/p/msysgit/downloads/list
- 参考:
    - [在windows安装配置Git开发环境](http://www.starming.com/index.php?action=plugin&v=wave&tpl=union&ac=viewgrouppost&gid=32767&tid=1000002148)
    - [Windows 系统下Git安装图解 | Drupal中国](http://drupalchina.cn/content/windows-xi-tong-xia-gitan-zhuang-tu-jie)
- 注意的是: `选择Git文件夹，右键，选择Git Bash Here，会弹出shell命令行界面` 可能不一定有
- 不过,可以自然的进入 msysgit 安装目录中, 点击 `git-cmd.bat` 
    - 然后在其中调用的 bin 下的 `bash.exe` 进入方便的 shell 环境
    - 然后就可以自动的引用到 `ssh-kengen.exe` 生成对应的 `SSH` 密匙对!

![0-bash.png](https://gitcafe.com/Liebao/Liebao/blob/gitcafe-pages/img/msysgit/0-bash.png?raw=true)

命令形如: `bash-3.1$  ssh-keygen -C "zhouqi@ijinshan.com" `
    
    Your identification has been saved in /c/Documents and Settings/Administrator/.s
    sh/id_rsa.
    Your public key has been saved in /c/Documents and Settings/Administrator/.ssh/i
    d_rsa.pub.
    The key fingerprint is:
    cf:1b:90:1b:25:0a:12:61:ff:ad:71:d0:ec:cd:5f:55 zhouqi@ijinshan.com


从对应的文件中复制出公匙字串,这里是 `id_rsa.pub` 发布为个人帐号的公匙:

![00-cafe-pubkey.png](https://gitcafe.com/Liebao/Liebao/blob/gitcafe-pages/img/sourcetree/00-cafe-pubkey.png?raw=true)


再由仓库管理员加我们的 `gitcafe` 帐号为 `blogging` 仓库的协作人员:

![04-cafe-team.png](https://gitcafe.com/Liebao/Liebao/blob/gitcafe-pages/img/sourcetree/04-cafe-team.png?raw=true)


###使用 git 命令初始化本地工作仓库

从仓库首页可以获得有写入权限的 `URI`:

![00-gituri.png](https://gitcafe.com/Liebao/Liebao/blob/gitcafe-pages/img/sourcetree/00-gituri.png?raw=true)

在开始前,如前建议,在 git 配置文件中声明有意义的别名:

![1-config.png](https://gitcafe.com/Liebao/Liebao/blob/gitcafe-pages/img/msysgit/1-config.png?raw=true)

并配置合理的全局变量:

    bash-3.1$ git config --global user.name "zhouqi"
    bash-3.1$ git config --global user.email "zhouqi@ijinshan.com"


使用git 命令观察是否生效:

    bash-3.1$ git config --list
        core.symlinks=false
        core.autocrlf=true
        color.diff=auto
        color.status=auto
        color.branch=auto
        color.interactive=true
        pack.packsizelimit=2g
        help.format=html
        http.sslcainfo=/mingw/bin/curl-ca-bundle.crt
        sendemail.smtpserver=/mingw/bin/msmtp.exe
        diff.astextplain.textconv=astextplain
        rebase.autosquash=true
        user.name=zhouqi
        user.email=zhouqi@ijinshan.com


- 在合适的空白目录中 `clone` 远程仓库到本地:

`bash-3.1$ git clone git@gitcafe.com:Liebao/Liebao.git blog`

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

- 更新到约定的 `gitcafe-pages` 分支:

    bash-3.1$ cd blog
    bash-3.1$ git checkout -b gitcafe-pages remotes/origin/gitcafe-pages
        error: Not tracking: ambiguous information for ref refs/remotes/origin/gitcafe-p
        ages
        Switched to a new branch 'gitcafe-pages'


- `注意!` 一定要先进入 `clone` 下来的目录中,否则 git 不认为我们在操作合理的版本仓库!
- 参考: [[2012/10/31]GitCafe正式推出Pages服务](http://blog.gitcafe.com/116.html)


在资源管理器中就可以见到整个基于 [jekyll](http://jekyllrb.com/) 的团队blog 工程了!

![2-cloned.png](https://gitcafe.com/Liebao/Liebao/blob/gitcafe-pages/img/msysgit/2-cloned.png?raw=true)


###使用 markdownpad 进行文章编辑

- 免费好编辑器! [http://www.markdownpad.com/](http://www.markdownpad.com/)
- 下载,安装,没什么好说的
- 完全吻合 word 式编辑的环境! 左窗写 markdown,右窗自动编译成最终效果:

![3-markdownpad.png](https://gitcafe.com/Liebao/Liebao/blob/gitcafe-pages/img/msysgit/3-markdownpad.png?raw=true)


编辑保存后,使用 `status` 可以观察到变化:

    bash-3.1$ git status
    # On branch gitcafe-pages
    # Changes not staged for commit:
    #   (use "git add <file>..." to update what will be committed)
    #   (use "git checkout -- <file>..." to discard changes in working directory)
    #
    #       modified:   _posts/2012-12-10-git-note.md
    #
    no changes added to commit (use "git add" and/or "git commit -a")



使用 `add` 收录变更,才能 `commit`, 最后 `push` 后,才能发布到 `gitcafe` 的团队仓库:

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
   

- `注意!` git 的提示非常智能,会好心提醒我们忘记的参数,不过,一般都是可以智能猜中我们的期待,完成合理的操作!   
- 基于以上的操作,在远程仓库中就可以见到自个儿的提交了!

![11-cafe-same.png](https://gitcafe.com/Liebao/Liebao/blob/gitcafe-pages/img/sourcetree/11-cafe-same.png?raw=true)



####技巧: 图形化版本树!

`$ git log --graph --pretty=oneline --abbrev-commit`

    * 80846ab - (HEAD, origin/gitcafe-pages, gitcafe-pages) 演示多人协同时的流程+ 8 minutes ago
    *   e8b5e0f - Merge branch 'gitcafe-pages' of gitcafe.com:Liebao/Liebao into gitcafe-pages 26 minutes ago
    |\  
    | * 9783bab - 尝试另外成员本地的协同过程 33 minutes ago
    * | ce33b2e - 增补res 目录,准备发布可能的幻灯资料.. 67 minutes ago
    |/  
    * 61f39ee - 增补本地图片使用样例 71 minutes ago
    ...


- 当有复杂的团队多人协作时,可以用来观察各种版本的合并关系


日常使用@SourceTree
------------------------------------

[使用SourceTree 来管理 Gitcafe 的Pages 发布Blog!](http://liebao.gitcafe.com/2012-12/sourcetree-make-pages/)


日常使用@命令行
------------------------------------

以 MAC/Linux 下的操作为例:

    $ cd /path/2/你的本地工作仓库目录
    $ git branch -a     
        * master
          remotes/origin/HEAD -> origin/master
          remotes/origin/gitcafe-pages
          remotes/origin/master

        # 观察当前分支, 我们应该使用 gitcafe-pages 进行撰写

    $ git checkout -b gitcafe-pages remotes/origin/gitcafe-pages
    Branch gitcafe-pages set up to track remote branch gitcafe-pages from origin.
    Switched to a new branch 'gitcafe-pages'

        # 创建本地分支,并指定远程分支的对应关系

    $ git br -a
        * gitcafe-pages
          master
          remotes/origin/HEAD -> origin/master
          remotes/origin/gitcafe-pages
          remotes/origin/master

        # 确认变化,当前已经切换到 gitcafe-pages 分支

    $ git pl cafe gitcafe-pages
    From gitcafe.com:Liebao/Liebao
     * branch            gitcafe-pages -> FETCH_HEAD
    Already up-to-date.

        # 下拉所有当前分支内容
        # 以上是第一次建立本地工作仓库的操作,以后就不用了...

    $ cd _posts
    # 创建 yyyy-mm-dd-E文标题名.md 的文本
    # 使用自个儿喜爱的编辑器编辑
    # 确保前8行类似以下:
    ---
    layout: post
    title: 你好，世界
    description: 永远的 Hallo World
    categories: Programming
    tags:  md hallo
    ---

    $ git status
    # On branch gitcafe-pages
    # Changes not staged for commit:
    #   (use "git add <file>..." to update what will be committed)
    #   (use "git checkout -- <file>..." to discard changes in working directory)
    #
    #   modified:   README.md
    #
    no changes added to commit (use "git add" and/or "git commit -a")

    $ git add .
    $ git ci -m "变更说明 commit log..."
    # On branch gitcafe-pages
    # Changes not staged for commit:
    #   (use "git add <file>..." to update what will be committed)
    #   (use "git checkout -- <file>..." to discard changes in working directory)
    #
    #   modified:   README.md
    #
    no changes added to commit (use "git add" and/or "git commit -a")

    $ git push cafe
    Counting objects: 9, done.
    Delta compression using up to 8 threads.
    Compressing objects: 100% (5/5), done.
    Writing objects: 100% (5/5), 1.31 KiB, done.
    Total 5 (delta 3), reused 0 (delta 0)
    To git@gitcafe.com:Liebao/Liebao.git
       5e74faf..4e0ada2  gitcafe-pages -> gitcafe-pages

       # 推送你的修訂,到远程仓库

    $ git pull cafe gitcafe-pages
    remote: Counting objects: 5, done.
    remote: Compressing objects: 100% (3/3), done.
    remote: Total 3 (delta 2), reused 0 (delta 0)
    Unpacking objects: 100% (3/3), done.
    From gitcafe.com:Liebao/Liebao
       4e0ada2..3c4bcca  gitcafe-pages -> origin/gitcafe-pages
    Updating 4e0ada2..3c4bcca
    Fast-forward
     README.md |   37 ++++++++++++++++++++++++++++++++++++-
     1 file changed, 36 insertions(+), 1 deletion(-)

        # 同步仓库cafe 中他人的增补到指定分支 gitcafe-pages 中
        # 如果有冲突先要解决冲突,再增补,push



参考:创建Pages 工程时的操作
------------------------------------

以 MAC/Linux 下的操作为例:

    $ git clone git@gitcafe.com:Liebao/Liebao.git
    $ git checkout -b gitcafe-pages
    Switched to branch 'gitcafe-pages'

    $ cd Liebao/_posts
        # 创建 yyyy-mm-dd-E文标题名.md 的文本
        # 使用自个儿喜爱的编辑器编辑

    $ git add .
    $ git ci -m "变更说明 commit log..."
    $ git push


进阶
------------------------------------

在本地部署 Jekll 环境,随时发布本地网站看最终效果!

安装:

+ Ruby
+ 通过 gem 安装 Jekll



注意
------------------------------------


### 常见ERROR

Jekll 虽然简单,但是依赖相关的文本格式,非常精确,常见[jekyll使用出错](http://www.oschina.net/question/195686_71250):

    Configuration from /home/lazy/atttx123.github.com/_config.yml
    Building site: /home/lazy/atttx123.github.com -> /home/lazy/atttx123.github.com/_site
    /usr/lib/ruby/gems/1.8/gems/jekyll-0.11.2/bin/../lib/jekyll/convertible.rb:81:in `do_layout': fined method `name' for <Post: /2012/04/26/hello-world>:Jekyll::Post (NoMethodError)
        from /usr/lib/ruby/gems/1.8/gems/jekyll-0.11.2/bin/../lib/jekyll/post.rb:189:in `render'
        from /usr/lib/ruby/gems/1.8/gems/jekyll-0.11.2/bin/../lib/jekyll/site.rb:193:in `render'
        from /usr/lib/ruby/gems/1.8/gems/jekyll-0.11.2/bin/../lib/jekyll/site.rb:192:in `each'
        from /usr/lib/ruby/gems/1.8/gems/jekyll-0.11.2/bin/../lib/jekyll/site.rb:192:in `render'
        from /usr/lib/ruby/gems/1.8/gems/jekyll-0.11.2/bin/../lib/jekyll/site.rb:40:in `process'
        from /usr/lib/ruby/gems/1.8/gems/jekyll-0.11.2/bin/jekyll:250
        from /usr/bin/jekyll:19:in `load'
        from /usr/bin/jekyll:19


- 多半引发错误的是因为post文件夹下的日志文件里面有无法编译的内容比如"{%%}" 之类的特殊符号，这样会引发错误，最好的方法是使用排除法，来确定引发错误的位置，以后避免


### highlight 问题!

- 需要这么设置： {\% highlight language \%} your code {\% endhighlight \%} 
- 结束声明不是 end highlight
- 否则,会出错! 表现起来就是 gitcafe 好象不编译出新的内容修订了!


参考
------------------------------------

- [搭建一个免费的，无限流量的Blog----github Pages和Jekyll入门 - 阮一峰的网络日志](http://www.ruanyifeng.com/blog/2012/08/blogging_with_jekyll.html)
- [Github Pages极简教程 - 雁起平沙的网络日志](http://yanping.me/cn/blog/2012/03/18/github-pages-step-by-step/)
- [Mort | 像黑客一样写博客——Jekyll入门](http://www.soimort.org/posts/101/)


Changelog
------------------------------------

- 121219 以 zhouqi 角度描述使用 SourceTree 的过程
- 121214 以 Zoom.Quiet 角度描述创建过程



