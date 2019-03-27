---
layout: post
title: HOA.6 算法故事小结
author: zoomq
categories: Events
tags:  gdg cbi event hoa summary
---


    大雨, 瓢泼!
    算法, 奇诡!
    珠海, 社区!
    活动, 纪要...



去年珠海GDG 组织了19场活动,在九个月的时间里,
整体感觉:

- 学生为主,但,多数无法坚持;问了原因,说,听不大懂;
- 分享者基本是在职工程师,也无法坚持,原因,大妈也明白,太忙

所以,今年,根据GDG 的精神,社区决定调整策略:

- 倾向进入大学,以激励在校生开始真正的编程/创新 为主
- 但是,时间长了,作为技术社区总是说些入门级的,也就没有了行业影响力了
- 所以,不时的总是要将珠海本地,IT 技术圈好玩的事儿,拿出来讲讲,至少让自个儿爽一下

所以,有了这次 `算法故事` 的主题分享;
果然,来者了了.

![](http://0.zoomquiet.top/ZHGDG/2014/140511-hoa6-algorithm/140511-hoa6-7.png)

<!--more-->

总计:

- G+ 报名18人; 报名表单 12人
- 到场 4人(其中一人是因为加班,顺道进来的)
- 加上讲师,现场一共7人
- 不过,好在是进行网络直播的,通过 Youtube 的直播,也有另外11人旁观了下来


## 流水

- 14:30 - 14:55   门卫签到
    - 其实没有签到,嘦对门口的大横幅自豪的说:"来参加 GDG活动的!" 就能进入了

- 14:55 - 15:00   开场
    - 录音:[140511_zhoa.6-0-intro.MP3](http://0.zoomquiet.top/ZHGDG/2014/140511-hoa6-algorithm/140511_zhoa.6-0-intro.MP3)
    - 快速介绍什么是GDG ,什么是珠海GDG ,为什么有这次活动
    - 另外,也收集了难得的,冒雨来参加人员的自述
    - 有MM !

- 15:00 - 16:00   Richard Liao ~ 分布式存储系统的节点间元数据同步算法

![](http://ww4.sinaimg.cn/bmiddle/53809965jw1egacozep4yj20y019cajw.jpg)

- 录音: [140511_zhoa.6-1-liao.MP3](http://0.zoomquiet.top/ZHGDG/2014/140511-hoa6-algorithm/140511_zhoa.6-1-liao.MP3)
- 幻灯: [ZHGDG_HOA.6_分布式元数据快速同步算法 // Speaker Deck](https://speakerdeck.com/zoomquiet/zhgdg-hoa-dot-6-fen-bu-shi-yuan-shu-ju-kuai-su-tong-bu-suan-fa)

老寥以从容淡定的态度以及语速, 回顾了自个儿一个私人开源项目的有关算法结论:

https://github.com/richardliao/swarmstorage

面对海量数据库髙频同步的场景,
ODS(Orthogonal Digest Sync)算法 比较合适,
但是,依然要配合各种相关环境的支撑.

因为不涉及代码,也没有涉及整体项目的发展故事,
大家听的很不过瘾,下次,值得再邀请来详细讲一下,算法是怎么从论文/公式变成 golang 代码的.


- 16:00 - 16:45   [鹄思乱想](http://blog.zhgdg.org/2013-09/dm4-sphinx/) ~ [Sorting Algorithm Visualization](http://www.thinkingincrowd.me/algorithm/)

![](http://ww4.sinaimg.cn/bmiddle/53809965jw1egaepga3z8j219c0y0tir.jpg)

- 录音: [140511_zhoa.6-2-visualization.MP3](http://0.zoomquiet.top/ZHGDG/2014/140511-hoa6-algorithm/140511_zhoa.6-2-visualization.MP3)
- 幻灯: [ZHGDG_HOA.6_为什么去学算法 // Speaker Deck](https://speakerdeck.com/zoomquiet/zhgdg-hoa-dot-6-wei-shi-yao-qu-xue-suan-fa)

自述说,自个儿业余时间折腾这事儿,是受到
![](http://tp4.sinaimg.cn/1401880315/50/40054262531/1)[@左耳朵耗子](http://weibo.com/haoel)
的启发,同时,因为参加 Coursera 的 MOOC ,也顺便能学以至用.

现场大妈最有共鸣的体验是:

    自己想, 想, 想 
    (深刻体会: 
        坚持就能想出来
    )

这才是真实写过代码的人,才有的朴素真理体验.

时间关系,也没有更好的展示在 AngularJS 的帮助下,是如何将一个算法动画,
用不同模型快速实现的,
有哪些AngularJS特性是这一命题解决过程中好的,哪些是挫的?

最后,建议:

- 及时整理好文档,分享给同在 Coursera 的同学,鼓励其它人通过可视化加深理解
- 也可以分享给 Coursera 组织本身,用来改进在线课件.


- 17:50 - 17:27   大妈 ~ 一切从游戏开始

![](http://0.zoomquiet.top/ZHGDG/2014/140511-hoa6-algorithm/140511-hoa6-5.png)

- 幻灯: [ZHGDG_HOA.6_从游戏开始](http://s5.zoomquiet.io/140511-hoa6-start4game/index.html)
- 录音: [140511_zhoa.6-2-zq-4game.MP3](http://0.zoomquiet.top/ZHGDG/2014/140511-hoa6-algorithm/140511_zhoa.6-2-zq-4game.MP3)

整理这一故事时,大妈才惊讶的发现,这居然是 `12` 年前的故事了!

- 来源一则维基文章: [一切从游戏开始 - Woodpecker Wiki for CPUG](http://wiki.woodpecker.org.cn/moin/AllStartFromGame)
- 而这文章,又是从另外一个社区维基来的
    - [一切从游戏开始 - ChinesePython Wiki](http://chinesepython.sourceforge.net/cgi-bin/moingb.cgi/_d2_bb_c7_d0_b4_d3_d3_ce_cf_b7_bf_aa_ca_bc)

只是因为中国人对中文编程的天然奇怪的反感,
中蠎没有流行起来,以至后来的周蠎也没有.

但是,这一隽永的算法小故事,大妈记住了,总算有机会分享出来了.

所有10段脚本,都没有超过30行,可见Python 的表述能力.

正如大妈在回答现场 暨大MM 的问题所言:

- 算法并不是不再常用
    - 而是太常用了,因为,绝大多数算法早已成熟的内置在各种标准库/模块/框架中了
    - 以致现今程序猿每天写代码完全没有查觉自个儿在调用多少包含了什么 算法的代码
- 另外,正如故事中所以描述的
    - 一个算法的不断改进,是需要大量专注时间和精力的
    - 一般公司根本没有资源和心态愿意付出这种时间
    - 所以,绝大多数程序猿,究其一生也没有机会体验这种算法改进的 `to hack` 体验
- 当然,现代企业中,是有算法专职部门的
    - 在豆瓣曰为 豆瓣科学院
    - 配合数学专家,将各种算法模型,变成可调运的高效组件
    - 只是,这种职位不是一般人可以竞争到的
- 不过, `世界上没有任何力量,可以阻止我们作自个儿想作的`
    - 如果真的想学习算法
    - 体验算法的威力
    - 这就开始学习吧
    - 放弃 `炸鸡+啤酒` 的低级乐趣
    - 追寻算法代表的髙能智力快乐呗.


## 资料
视频: [HOA.6 for Zhuhai GDG](https://www.youtube.com/watch?v=PmB-88vCIEQ)

照片: [HOA.6 算法故事](https://plus.google.com/u/1/events/gallery/cdq8u7q98e6f2cab380o9bl2u3c)

- 特别鸣谢, guest 专程从澳门赶回来,给予了摄影支持!现场的图片品质一下子高了一个档次 ;-)

幻灯:
    
- [ZHGDG_HOA.6_分布式元数据快速同步算法 // Speaker Deck](https://speakerdeck.com/zoomquiet/zhgdg-hoa-dot-6-fen-bu-shi-yuan-shu-ju-kuai-su-tong-bu-suan-fa)
- [ZHGDG_HOA.6_为什么去学算法 // Speaker Deck](https://speakerdeck.com/zoomquiet/zhgdg-hoa-dot-6-wei-shi-yao-qu-xue-suan-fa)
- [ZHGDG_HOA.6_从游戏开始](http://s5.zoomquiet.io/140511-hoa6-start4game/index.html)

录音:

- [140511_zhoa.6-0-intro.MP3](http://0.zoomquiet.top/ZHGDG/2014/140511-hoa6-algorithm/140511_zhoa.6-0-intro.MP3)
- [140511_zhoa.6-1-liao.MP3](http://0.zoomquiet.top/ZHGDG/2014/140511-hoa6-algorithm/140511_zhoa.6-1-liao.MP3)
- [140511_zhoa.6-2-visualization.MP3](http://0.zoomquiet.top/ZHGDG/2014/140511-hoa6-algorithm/140511_zhoa.6-2-visualization.MP3)
- [140511_zhoa.6-2-zq-4game.MP3](http://0.zoomquiet.top/ZHGDG/2014/140511-hoa6-algorithm/140511_zhoa.6-2-zq-4game.MP3)




## 是也乎
本次没有意外的,参与者只有个位数的活动,
个人最大的体验:

- <img src="http://zoomq.qiniudn.com/ZHGDG/2014/140511-hoa6-algorithm/140511-hoa6-4.png" height="240"/>
    - 大妈,真心月半了...即使发型儿可以回到7年前

- 暨南大学,计算机系有靠谱 MM:
    - ![](http://0.zoomquiet.top/ZHGDG/2014/140511-hoa6-algorithm/140511-hoa6-6.png)
    - 就是因为,听过大妈一次上门分享,记住了珠海GDG
    - 然后,因为专业关系,想知道算法的真正使用情景,就来了
    - 认真作笔记,努力理解,勇敢提问
    - 中国有希望哪...

### 有关活动形式: 
`HOA`

- E文名: Hangout on Air
- 中文名: 技术无界分享会
- 常规技术分享,通过 Hangout 服务直播为 YouTube 视频
- 平均每月至少会组织一次




## 巡阅
- 150113 [Zoom.Quiet](http://zoomquiet.io/) checked





