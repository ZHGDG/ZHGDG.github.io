---
layout: post
author: zoomq
title: G说公论:1 千万要避免的五种程序注释方式
description: ~ 时评杂文,新旧不拘
categories: gdGTime
tags:  gdg G说公论 gt wechat coding
---

大家好,这里是珠海GDG 的微信订阅号!

- 今天是周三,每周一篇儿,分享组委大妈印象深刻的事件/杂文!
- 为毛自称 `大妈` ? 说起来都是桑心事儿,以后再解释!-)


# [千万要避免的五种程序注释方式 | 外刊IT评论网](http://www.aqee.net/5-types-of-comments-to-avoid-making-in-your-code/)

你是否有过复查程序时发现有些注释毫无用处?程序注释是为了提高代码的可读性,为了让原作者以外的其他开发人员更容易理解这段程序. 

我把这些让人郁闷的注释方式归为了五类,同时把写出这些注释的程序员也归为了五类. 我希望读了这篇文章后你感觉自己不属于其中的任何一种类型. 如果你有兴趣的话可以读一下另外一篇文章 五种程序员(英文),和这篇讲到的五种程序员对比一下. 

<!--more-->

## 1. 高傲的程序员

{% highlight cpp %}
    public class Program
    {
        static void Main(string[] args)
        {
            string message = "Hello World!";  // 07/24/2010 Bob
            Console.WriteLine(message); // 07/24/2010 Bob
            message = "I am so proud of this code!"; // 07/24/2010 Bob
            Console.WriteLine(message); // 07/24/2010 Bob
        }
    }
{% endhighlight %}

这种程序员是如此的欣赏自己的程序,以至于不得不在每行代码上都署上自己的大名. 应该让版本控制系统来提供程序变更的信息,他这样做一眼看去并不能说明谁对这行代码负责. 

## 2. 过时的程序员

{% highlight cpp %}
    public class Program
    {
        static void Main(string[] args)
        {
            /* 这段程序已经不再有用
            * 因为我们发现千年虫问题只是一场虚惊
            * 我们的系统不会恢复到1/1/1900 */
            //DateTime today = DateTime.Today;
            //if (today == new DateTime(1900, 1, 1))
            //{
            //    today = today.AddYears(100);
            //    string message = "The date has been fixed for Y2K.";
            //    Console.WriteLine(message);
            //}
        }
    }
{% endhighlight %}


如果一段程序不再有用(比如废弃了),那就删了它吧--不要被几行没用的注释搞的程序混乱不堪. 即使你可能以后重用这段代码,你也可以使用版本控制系统,用它把你的程序恢复到以前的样子. 


## 3. 天真的程序员

{% highlight cpp %}
    public class Program
    {
        static void Main(string[] args)
        {
            /* 这个程序是用来在屏幕上
             * 循环打印1百万次"I Rule!"
             * 每次输出一行. 循环计数
             * 从0开始,每次加1. 
             * 当计数器等于1百万时,
             * 循环就会停止运行*/

            for (int i = 0; i < 1000000; i++)
            {
                Console.WriteLine("I Rule!");
            }
        }
    }
{% endhighlight %}


基本的编程语法规则我们大家都知道--我们不需要"编程入门". 你不需要浪费时间来解释一个显而易见的东西,我们更希望知道的是你的程序功能--那是浪费空间了. 

## 4. 传奇的程序员

{% highlight cpp %}
    public class Program
    {
        static void Main(string[] args)
        {
           /* 有一天我在大街上的一家星巴克里
            * 和销售部的Jim讨论问题,他告诉我
            * 销售代表是依据以下的比例提取佣金的. 
            * 周五: 25%
            * 周三: 15%
            * 其它日期: 5%
            * 我是否告诉你过我点了一个卡拉梅
            * 铁咖啡和两份的Espresso?
           */
            double price = 5.00;
            double commissionRate;
            double commission;
            if (DateTime.Today.DayOfWeek == DayOfWeek.Friday)
            {
                commissionRate = .25;
            }
            else if (DateTime.Today.DayOfWeek == DayOfWeek.Wednesday)
            {
                commissionRate = .15;
            }
            else
            {
                commissionRate = .05;
            }
            commission = price * commissionRate;
        }
    }
{% endhighlight %}


如果你不得不在注释里写明需求,那也不要提到人名. 销售员Jim很可能在公司里不再是销售. 而且大多数读到这段注释的程序员未必都知道Jim是谁. 你描述的是实际情况但跟我们的内容不相干,所以就省掉吧. 

## 5. 未来程序员

{% highlight cpp %}
    public class Program
    {
        static void Main(string[] args)
        {
           //TODO: 将来我会修复这个问题 – 07/24/1995 Bob
           /* 我知道这个问题很难解决而且
            * 我现在依赖于这个Contains函数,但
            * 我以后会用一种更有意义,更
            * 优雅的方式打印这段代码. 
            * 我只是现在没时间. 
           */
           string message = "An error has occurred";
           if(message.Contains("error"))
           {
               throw new Exception(message);
           }
        }
    }
{% endhighlight %}


这种注释是一种集大成者,它包含了上面所说的注释的所有问题. TODO注释在一个项目最初的开发阶段是非常有用的,但这个注释看起来是在好几年前的产品程序里的--它证明了程序有问题. 如果程序有问题需要解决,马上解决,不要拖到日后再解决. 

如果你写过这样的注释,或者是你正在寻找一种最好的注释方案,我推荐你读一读Steve McConnell写的 `Code Complete`这本书. 这是我推荐给所有程序员必读的六本书中的一种. 或者你可以学学如何停止注释你的程序(英文). 

你是否在你的程序里还见到过其它种没有意义的或讨厌的注释?欢迎共享. 

## 总之

作人呢,最要紧的就是要快乐,有空不如给自个儿煮碗面也不能这么遗祸人间!

当然,多数这种蛋痛的情况都出于程序猿的寂寞,,,,因为没有人关心你写的代码,只会问功能完成了没有?!

所以,现代敏捷工程解决这种问题的方式,一般两种:

1. 进行 code review,坚持同行评议,确保所有人的所有代码,有两个以上的小伙伴看过,并理解,但是,这对创业团队或是号称创业的企业很难作到...
1. 部署 CI 系统,将代码的注释要求使用 *lint 工具,进行自动化检验,让 寂寞的程序猿跟自个儿写的脚本进行对话吧!



## 近期活动


9.14 珠海首届 DevFest:

- 预订问卷: http://f.jeffkit.info/zoomquiet/devfest914zh/     
- 持续一整天的 开发者 节日
- 多种前沿技术的体验分享
- 丰富的活动形式
- 给力的 BBQ 午餐
- ... 
- 及时报名,才有席位哪!


## 微信栏目
当前应该是: 

        周一: G术图书 (gb:推荐好书,书无中外)
        周二: D码点评 (dd:麻辣评点,善意满盈)
        周三: G说公论 (gt:时评杂文,新旧不拘)
        周四: 珠的自白(dm:大妈自述,每周一篇)
        周五: 海选文章(hd:得要相信,大妈法眼)


如果认真分析当前社区各种沟通渠道,其实都不是很好的意见表述渠道:

- 邮件列表,倾向异步的理性技术讨论,对于多数并没有太多开发背景的同学们而言,总是佷有隔阂感;
- weibo,虽然也是很主流的SNS 渠道,但是,太过公开,而且只有140字的限制,很难将一个具体问题,深入的交流起来;
- G+ 无论 page 或是 community 虽然功能很美好,但是,毕竟是墙外的服务,无法令所有社员简单的都享受起来
- 新发现还没有被和谐的 Google 汇问,则更加专注具体主题的共同思考,无法自在的进行双向交流
- BBS? `形式决定内容` 在这种平台上,大家已经条件反射性的除了点赞已经忘记了其它交流... 

所以?! 目测,当前可以全体都有,随时翻阅,长文可发,相对封闭,基本友好的交流渠道,只有 wechat 了!

所以! 珠海的组委大妈们,决定开始坚持发文,从 技术的方方面面,细细同大家分享/交流

所以! 请大家告诉大家,  `珠海生活中的技术社区` 已经认真回归 微信,都来订阅吧!

### 订阅方法

- 搜索微信号 `GDG-ZhuHai` 
- 或查找公众号: `GDG珠海`



## 巡阅
- 150113 [Zoom.Quiet](http://zoomquiet.io/) checked



