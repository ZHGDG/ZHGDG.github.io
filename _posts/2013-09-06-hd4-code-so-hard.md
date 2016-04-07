---
layout: post
author: zoomq
title: 海选文章:4 编程真难啊
description: ~ 得要相信,大妈法眼
categories: HaiDoc
tags:  gdg 海选文章 hd wechat thinking
---

据说在每一个编辑部,都有一个扫地的老太太. 
很偶然地,当她经过你身边,扫一眼屏幕上的CMS,
会低声提醒:小心,专题链接应用target=_blank. 




![holding_head.png(PNG 图像,250x319 像素)](http://www.dealingwithdifficultpeople.org/wp-content/themes/default/images/holding_head.png)

明天周末,所以,发布个轻松的,来自 2009年9月3日 陈皓 的Blog:

http://coolshell.cn/articles/1391.html


<!--more-->


上周,在Sun的Java论坛上出现了一个这样的帖子,这个贴子的链接如下:

http://forums.sun.com/thread.jspa?threadID=5404590&start=0&tstart=0

LZ的贴子翻译如下:

    大家好,我是一个Java的新手,我有一个简单的问题:
    请问我怎么才能反转一个整数的符号啊. 比如把-12转成+12. 
    是的,毫无疑问这是个简单的问题,但我弄了一整天我也找不到什么好的方法. 
    非常感谢如果你能告诉我Java有什么方法可以做到这个事,
    或者告诉我一个正确的方向--比如使用一些数学库或是二进制方法什么的. 
    谢谢!

这个贴子的沙发给出了答案:

    n = -n;


LZ在四楼回复到:

    我知道是个很简单的事,
    可我没有想到居然这么简单,我觉得你可能是对的. 
    谢谢你. 

过了一会,又回复到:

    不开玩笑地说,我试了,真的没有问题耶!

看到这样的贴子,就能想到国内论坛上很多这样的 `"问弱智问题的贴子"` ,结果可能都会是比较惨!
是的,国外的互联网文化和国内差不多,都是恶搞的人多于热心的人,呵呵. 
不过,国外的网民们有一点是好的,再恶搞也是就事搞事,不会有侮辱人的语言,这点真是值国内的人学习. 


这本是一个平淡无奇的贴子,不过回复中那些恶搞的"解决方案"太强大了,在这里例举一下吧. 

贴子的板凳给出了这样的答案(这是恶搞的开始)


{% highlight java %}
int x = numberToInvertSign;
boolean pos = x > 0;
for(int i = 0; i < 2*Math.abs(x); i++){
    if(pos){
        numberToInvertSign--;
    }
    else{
        numberToInvertSign++;
    }
}
{% endhighlight %}


然后,有人说,n = -n 可以是可以,但不够晦涩,于是一个晦涩的解决方案出现了:

    
{% highlight java %}
int n = ....;
 n = (0xffffffff ^ n) + 1;
{% endhighlight %}

然后,又出现了一些看似简单,其实是比较晦涩的方案

{% highlight java %}
n = ~n + 1;
{% endhighlight %}

 

{% highlight java %}
n = ~--n;
{% endhighlight %}

 

继续,有才的人从来就不少:

{% highlight java %}
n^= 0xffffffff;
int m;
for (m= 1; m != 0 && ((n&m) != 0); m<<= 1);
n|= m;
if (m == 0) n= m;
else for (m >>= 1; m != 0; n^= m, m>>=1);
{% endhighlight %}

 

呵呵,开始越来越强大了,我以前也向大家介绍过<<如何加密/弄乱C源代码>>的文章,和这些恶搞的人可能有点相似吧. 上面这个例子一出,大家都在讨论上面例子中的for循环语句,呵呵,很费解啊. 

然后,后面几个就开始乱来了:
{% highlight java %}
public int invert(int i) {
  return i - (i + i);
}

switch (i)
{
  case 1: return -1;
  case 2: return -2;
  case 3: return -3;
  // ... etc, you get the proper pattern
}
{% endhighlight %}

不过事情还没有结束,看看下面这个吧,OMG. 

{% highlight java %}
int absoluteValue(int num)
{
 int max = 0;
 for(int i = 0; true; ++i)
 {
  max = i > max ? i : max;
  if(i == num)
  {
   if(i >= max)
    return i;
   return -i;
  }
 }
}
{% endhighlight %}

 还有用字符串的解决方案:

{% highlight java %}
public int invert(int n) {
    String nStr = String.valueOf(n);
  
    if (nStr.startsWith("-")) {
        nStr = nStr.replace("-", "");
    } else {
        nStr = "-" + nStr;
    }
  
    return Integer.parseInt(nStr);
}
{% endhighlight %}

别忘了面象对象,有最新Java支持的模板库: 

{% highlight java %}
public interface Negatable<T extends Number> {
  T value();
  T negate();
}
  
  
  
public abstract class NegatableInteger implements Negatable<Integer> {
  private final int value;
  
  protected NegatableInteger(int value) {
    this.value = value;
  }
  
  public static NegatableInteger createNegatableInteger(int value) {
    if (value > 0) {
      return new NegatablePositiveInteger(value);
    }
    else if (value == Integer.MIN_VALUE) {
      throw new IllegalArgumentException("cannot negate " + value);
    }
    else if (value < 0) {
      return new NegatableNegativeInteger(value);
    }
    else {
      return new NegatableZeroInteger(value);
    }
  }
  
  public Integer value() {
    return value;
  }
  
  public Integer negate() {
    String negatedString = negateValueAsString ();
    Integer negatedInteger = Integer.parseInt(negatedString);
    return negatedInteger;
  }
  
  protected abstract String negateValueAsString ();
}
  
  
  
public class NegatablePositiveInteger extends NegatableInteger {
  public NegatablePositiveInteger(int value) {
    super(value);
  }
  
  protected String negateValueAsString () {
    String valueAsString = String.valueOf (value());
    return "-" + valueAsString;
  }
}
  
  
  
public class NegatableNegativeInteger extends NegatableInteger {
  public NegatableNegativeInteger (int value) {
    super(value);
  }
  
  protected String negateValueAsString () {
    String valueAsString = String.valueOf (value());
    return valueAsString.substring(1);
  }
}
  
  
  
public class NegatableZeroInteger extends NegatableInteger {
  public NegatableZeroInteger (int value) {
    super(value);
  }
  
  protected String negateValueAsString () {
    return String.valueOf (value());
  }
}
{% endhighlight %}

 

这个贴子基本上就是两页,好像不算太严重,如果你这样想的话,你就大错特错了. 

这个贴子被人转到了 reddit.com,于是一发不可收拾,在上面的回贴达到了 `490` 多条. 链接如下:

http://www.reddit.com/r/programming/comments/9egb6/programming_is_hard/

有人说,要用try catch;
有人说要使用XML配置文件... ,
程序员们在追逐更为变态和疯狂的东西,并从中找到快乐,呵呵. 

看完后,正如reddit.com所说-- `"编程好难啊"!`

无独有偶,这并不是第一次,也不会是最后一次,
让我们看看在PHP的官网上发生的类似的一幕--讨论PHP的 `abs`取绝对值函数的函数说明文档中的回复:

http://us.php.net/manual/en/function.abs.php#58508

又是一个长贴,还带着很多性能分析,真的很好很强大!


### 所以?

从中,你可以看出什么来?
欢迎回复,反馈你心中最激昂的那块儿槽,大妈们会整理为另外一篇文章,继续 `好难` 下去;

最精彩回复的作者,俺建议可以直接送一张 9.14 DevFest 珠海的门票 ;-)



### PS:

若无意外,题图都是从原文提取或是通过 Google 图片搜索出来的, 版权属左, 不负责任 ;-)


## 9.14 珠海首届 DevFest:

- 预订问卷: http://f.jeffkit.info/zoomquiet/devfest914zh/     
- 持续一整天的 开发者 节日
- 多种前沿技术的体验分享
- 丰富的活动形式
- 给力的 BBQ 午餐
- ... 
- 及时报名,才有席位哪!



## 巡阅
- 150113 [Zoom.Quiet](http://zoomquiet.io/) checked




