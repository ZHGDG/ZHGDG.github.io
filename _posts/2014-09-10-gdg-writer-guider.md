---
layout: post
title: 珠海GDG 社区文章 撰写指南
author: zoomq
categories: Doc
tags:  gdg guider blog
---

![1047006431871611098_sourse_.jpg(JPEG 图像,400x274 像素)](http://i.niurenqushi.com/2013/3/1/1047006431871611098_sourse_.jpg)

俺常常说的:

    忘记的就是不重要的
    不知道就是不必要的
    现实往往不是这样的

可以套用在各种方面呢...

<!--more-->

## 准入
~ 想理解以下内容,先明确:

- `习惯` 用最喜爱的文本编辑器编辑一切
- `习惯` [Markdown](https://gitcafe.com/GitCafe/Help/wiki/Markdown-%E8%AF%AD%E6%B3%95%E9%80%9F%E6%9F%A5%E8%A1%A8#wiki)
- `习惯` 用E文半角标点
- 承认并接受 HTML 是重要的,但是,不应该是人工编辑的


## 背景

对比: 

- [adc9cb46: 2014-08-25-snowy-blog.md - zhgdg/zhgdg - GitCafe](https://gitcafe.com/zhgdg/zhgdg/blob/adc9cb46d676848e143fa87ad78a0d853cfcb230/_posts/2014-08-25-snowy-blog.md)
- [e0a0abc7: 2014-08-25-snowy-blog.md - zhgdg/zhgdg - GitCafe](https://gitcafe.com/zhgdg/zhgdg/blob/e0a0abc786dc502c50677147d1f655a3d7a76ef3/_posts/2014-08-25-snowy-blog.md)

这是 [手把手教你用git发布blog](http://blog.zhgdg.org/2014-08/snowy-blog/) 文章的增补过程.

前一个版本, 是小言,努力了一周折腾明白基于 Jekyll 的静态Blog 网站文章怎么发布后,
写的 `教程` .

后一版本,是大妈想发布为微信文章时,实在无法忍受,重构后的版本.

## 分析
大妈为什么无法忍受?
参考: 

- [Writing a PyCon Proposal | brian curtin](http://blog.briancurtin.com/posts/writing-a-pycon-proposal.html)
- [pyenvな夏 in 2013 — MemoBlog](http://yymm.bitbucket.org/blog/html/2013/08/18/pyenv.html)
- [FreeBSD unionfsの改善提案および修正状況](http://people.freebsd.org/~daichi/unionfs/index-ja.html)
- [康托尔,哥德尔,图灵---永恒的金色对角线(rev#2)](http://mindhacks.cn/2006/10/15/cantor-godel-turing-an-eternal-golden-diagonal/)
- [数学常数e的含义 - 阮一峰的网络日志](http://www.ruanyifeng.com/blog/2011/07/mathematical_constant_e.html)
- 等等,那些令人叹服的好文档吧...

在各种技术的自学过程中,大妈通过 Google 接触到了无数优良的文章/教程/文档.

他们都有共同的气质:

    完备

即, 尽力将一个命题/问题的所有方面都探讨穷尽,将一篇文章写死,写到后人几乎无从增补的地步.
只是,为什么呢? 要这么累?!

后来,当大妈,也尝试写类似文章时,才发现:
([How to from Jekyll jump into Pelican |蠎周刊 |汇集全球蠎事儿 !-)](http://weekly.pychina.org/chaos/jekyll-to-pelican.html))

正如: [学习学习再学习 - xiaolai](http://xiaolai.github.io/alpha/on-learning/)
中指出的:

![](http://upload.wikimedia.org/wikipedia/commons/3/34/Impossible_staircase.svg)

    初级的知识需要对高级知识深入了解才能真正深入了解

正如以上自我相悖的图片表述的内在无限自我循环性.

每当, 我们想向大众分享体验/经验/技巧时,
因为, 受众知识水平的不可控性,
导致, 我们必须不断的在叙述过程中,持续的加入各种概念/知识点/理论/常识的阐述.
最终, 只有形成一种渐进式的,帮助情况实时出现的,引导读者跟上文字内容的反复的,螺旋式递进结构,才可能真正将想传达的事物,最大保真度的得以传达.


## 建议
社区官方blog 的文章,不是我们自个儿的私人笔记,是需要长期传播,
可以在任何情景任意读者面前,都可以充分的传达一个问题/命题的阐述.

所以,大妈建议,文章尽可能的应该包含以下部分:

    缘起 ~ 背景历史
    现象 ~ 问题描述
    尝试 ~ 自个儿探索过程/思路/关键代码...
    分析 ~ 将问题分析为几个关键子问题,进行逐一分析,解释
    解决 ~ 最终方案的具体实施过程
    要点 ~ 过程中,必须注意的操作,容易出错的地方
    总结 ~ 从整体上回顾问题/解决/思路,对同类问题进行建议
    参考 ~ 收集过程中各种给予自个儿有力帮助的资源/文章/代码

即,对一个命题的阐述,尽可能完备到,任何水平的人,都可以根据文章的描述,对相同的问题,独立解决.


## Pelican 格式细节
除了要习惯[Markdown](https://gitcafe.com/GitCafe/Help/wiki/Markdown-%E8%AF%AD%E6%B3%95%E9%80%9F%E6%9F%A5%E8%A1%A8#wiki)之外,
珠海GDG 深入定制了 [Pelican](http://getpelican.com/) 完成了通常 Blog 有的各种文章功能点.

对应到每篇文章的 `.md` 格式中,是有约定的在此逐一说明一下

通常文章的文件名结构是:

    2014-08-01-dm32-un-useless.md
        |       | |   | |     +- 统一为 md 后缀文件名
        |       | |   | +- 文章主题内容的纯小写e文关键词
        |       | |   |    将成为链接的一部分,不得使用中文
        |       | |   +- 多个词使用 - 分隔
        |       | +- 分类文章总序号
        |       +- 栏目文章有固定的分类缩写
        |               G术图书 (gb)
        |               D码点评 (dd)
        |               G说公论 (gt)
        |               珠的自白(dm)
        |               海选文章(hd)
        |               活动报道(et)
        |           其它文章,可以自定,但是,一定要坚持统一使用
        +- yyyy-mm-dd 格式日期前缀,将决定文章出现在归档中的位置       


通常文章的文本结构是:

    ---
    layout: post
    title: 珠海GDG 社区文章 撰写指南
    author: zoomq
    categories: Doc
    tags:  gdg guider blog
    ---

    ![题图](URI; 宽度 <540px)

    引文

    <!--more-->

    正文

    ...



### 引文切分

`<!--more-->` 这是一个插件应用,
将文章切分为引文和正文,
以便网站页面只显示多篇文章的引文.

`其实,是 html 标准语法的应用`

### 头声明

每个 `.md` 文本头部,由两个 `---` 框起来的文本,
是用来向 `Pelican` 系统声明文章基础信息的,
必须有,而且,有固定的格式要求

### 排版声明
`不用修订`

`layout: post` 含义

- 排版基于 `post` 模板

### 文章标题
`必须对应修订`

`title: 珠海GDG 社区文章 撰写指南` 含义

- 文章标题是 `珠海GDG 社区文章 撰写指南` 
- 请根据文章内容,给出一个精确概括性的标题


### 作者
`必须对应修订`

`author: zoomq` 含义

- 文章作者是 配置文件中 `zoomq` 变量指代的对象
- 必须事先在 `_config.yml` 中有相应配置的作者,在此声明才有效

![](http://0.zoomquiet.top/ZHGDG/wechat/140911-blog-matter-author.png)

以上,标题下方, `Author` 引导的一系列作者的私人信息对应配置是:

```
...
authors: 
    zoomq:
        name: Zoom Quiet
        display_name: Zoom.Quiet
        gravatar: 26221c6d3cedc50c506aa699e2765252
        email: i@zoomquiet.io
        web: http://zoomquiet.io
        github: ZoomQuiet
        gittip: https://www.gittip.com/ZoomQuiet/
        coderwall: zoomquiet
```

涉及的网络个人信息服务:


- http://gravatar.com/      头像代理
- http://github.com/        代码社交
- https://www.gittip.com/   私人捐助
- https://coderwall.com/    技能徵章


### 分类文章
`必须对应修订`

`categories: Doc` 含义

- 文章所属分类为 `Doc`
- 社区文章尽可能的归为固定的分类,以便在 [Categories](http://blog.zhgdg.org/categories.html) 索引中快速定位

当前固化的分类:

```
GdgBook G术图书 
gDgcoDe D码点评 
GdgTime G说公论 
gDgdaMa 珠的自白
HaiDoc  海选文章
EvenTs  活动报道
Think   领域思考
Doc     社区文档
Howto   手册教程
```

### 文章标签
`必须对应修订`

`tags:  gdg guider blog` 含义

- 当前文章的标签是:
    - gdg
    - guider
    - blog

参考:

- [如何分类? - 阮一峰的网络日志](http://skm.zoomquiet.io/data/20080316011918/index.html)
- [Tag的语言问题](http://skm.zoomquiet.io/data/20050222113305/index.html)
- [如何规划blog的标签(tag)和分类 - 心内求法 - 博客园](http://www.cnblogs.com/holbrook/archive/2012/11/05/2755268.html)

所以,大妈建议:

- tag 至少3个,最多5个
- 不用中文
- 尽可能从文章的多种维度进行标签
- 通常的维度:
    - 分类
    - 文章性质
    - 作者
    - 内容层次
    - 领域范畴

## 修订记录

- 140911 惊情完成
- 140910 为小言的发布指南增补专门说明

![writing-3.jpg(JPEG 图像,480x270 像素)](http://www.danichols.com/wp-content/uploads/2013/11/writing-3.jpg)


### 参考
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




## 巡阅
- 150113 [Zoom.Quiet](http://zoomquiet.io/) checked




