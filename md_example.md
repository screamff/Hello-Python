This is an H1大标题
=============
This is an H2次级标题
-------------
# 这是另一种写法
#### 本文参考自http://shouce.jb51.net/markdown/#philosophy
>这里是引用符号开始处
+ 这是无序列表（示例）
- 减号标记
* 星号标记
>>嵌套引用在这
>>3. 有序列表3
>>2. 有序列表2
>>1. 有序列表1

换行跳出引用
   * 列表标记通常放在最左边， 但是其实也可以缩进， 最多3个  
   空格，使用诸如`#`、`*`等标记时要在标记后空一格,  
   *该斜体后面有俩空格*  
   如果段落内文字要换行，请在末尾加上两个空格或者空一行。

* **引用中** 要放代码块的话：
        缩进8个空格或者俩制表符
        这里就可以放
        print('Hellow world')
当然，列表也许会这样出现
2020. 全面建设小康社会

那么，转义即可

2020\. 神奇的一年

- 好的，到这里列表基本讨论完了，第 **32** 行结束

# 代码区块
    一个制表符或者缩进4格(建议使用缩进)

会在没有缩进(或者文件结尾)结束，上面原文相当于被转化成

<pre><code>代码区块.
</code></pre>
Here is an example of AppleScript:

    tell application "Foo"
        beep
    end tell
代码块中嵌入html源码
    <div class="footer">
        &copy; 2004 Foo Corporation
    </div>

* * *
分割线1第 **52** 行
***
使用星号，减号，下划线，来建立分割线
*****
星号
- - -
减号加空格
________________
下划线

# 区段元素
## 链接
常用的**行内式**[打开百度](www.baidu.com"gan")

另外一种是**参考式**[example1][mark_id]  
或者俩方括号之间加上空格[example2] [foo]  
[mark_id]: www.baidu.com (waliewalie)
[foo]: http://example.com/  "Optional Title Here"


链接内容定义的形式为：

- 方括号（前面可以选择性地加上至多三个空格来缩进），里面输入链接文字
- 接着一个冒号
- 接着一个以上的空格或制表符
- 接着链接的网址
- 选择性地接着 title 内容，可以用单引号、双引号或是括弧包着

第**81**行，方便对应原文
## 强调（加粗斜体等）
*single asterisks*

_single underscores_

**double asterisks**

__double underscores__

- 但是如果你的 * 和 _ 两边都有空白的话，它们就只会被当成普通的符号。（仅限于在文字中间）
- 如果要在文字前后直接插入普通的星号或底线，你可以用反斜线：  
\*我选择不加粗\*

如果要标记一小段行内代码，你可以用反引号把它包起来`` ` ``tab上面那个键，例如：


Use the `printf()` function.

会转化成

<p>Use the <code>printf()</code> function.</p>

代码区段的起始和结束端都可以放入一个空白，起始端后面一个，结束端前面一个，这样你就可以在区段的一开始就插入反引号：

A single backtick in a code span:  `` ` ``

A backtick-delimited string in a code span: `` `foo` ``

第` **110** `行参考行
# 图片
Markdown 使用一种和链接很相似的语法来标记图片，同样也允许两种样式： 行内式和参考式。
行内式的图片语法看起来像是：

![Alt text](/path/to/img.jpg)

![Alt text](/path/to/img.jpg "Optional title")
详细叙述如下：

- 一个惊叹号 !
- 接着一个方括号，里面放上图片的替代文字
+ 接着一个普通括号，里面放上图片的网址，最后还可以用引号包住并加上 选择性的 'title' 文字。

参考式的图片语法则长得像这样：

![Alt text][id]

「id」是图片参考的名称，图片参考的定义方式则和连结参考一样：

[id]: url/to/image  "Optional title attribute"
Markdown 支持以下这些符号前面加上反斜杠来帮助插入普通的符号：

    \   反斜线
    `   反引号
    *   星号
    _   底线
    {}  花括号
    []  方括号
    ()  括弧
    #   井字号
    +   加号
    -   减号
    .   英文句点
    !   惊叹号
