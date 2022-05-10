# Egbenz for Education

[ [官网](http://www.egbenz.com) | [示例](http://www.egbenz.com/example) | [GITHUB](https://github.com/JerryZhuyi/Egbenz-for-Education) ]

Egbenz for Education(以下简称Egbenz-ed)是一个由Python和JS驱动的免费，持续更新的个人笔记本工具。

Egbenz期待提供一个代码简单，存储本地化，功能自定义，存储稳定可轻易切换平台的最小化代码版本的笔记本工具。



**简单** Egbenz-ed遵循最小化依赖原则，方便初学者阅读代码，降低理解成本。

客户端由原生ES6语法的JS编写。除了依赖nanoid,axios两个遵循MIT License的小型功能性组件，没有依赖其他任何JS衍生技术或框架，最小化依赖原则为初学者或非专业编程人士提供一个良好环境。

服务端由Python-flask驱动。后端仅实现了一个简单的新增，修改数据库管理系统。您可以自行接入Mysql,Pg等流行数据库进行文档管理。最早版本的Egbenz-ed后端代码仅160行

**安全** 所有的存储行为默认在本地且无需网络环境。您可以根据项目的需要自行调整存储的介质和加密方式。

**通用** 底层存储实际为JSON格式。尽管默认的存储文件格式后缀为.ez，实际您可以使用任何支持Json的存储介质。

**易扩展** 所有文档元素被定义为Mod,您可以通过Mod接口快速扩展功能。



Egbenz-ed遵守MIT License, 您可以使用源代码进行使用、复制、修改、合并、出版发行、散布、再授权及贩售软件及软件的副本。

亦可以可根据程序的需要修改授权条款为适当的内容。

如果您有任何技术问题可以在Github向作者发起一个[ISSUE](https://github.com/JerryZhuyi/Egbenz-for-Education/issues),或者发送邮件至zhuyi@egbenz.com。



## 目录

### 依赖环境

**浏览器：**仅在Chrome内核浏览器测试通过，建议使用Google Chrome.



*注意！以下环境在V1正式版本后均不需要，已经默认安装*

~~**客户端 - JS ES6：**~~

~~[Nanoid](https://github.com/ai/nanoid/blob/main/README.zh-CN.md) - 一个用于生成ID的小型工具~~

~~[Axios](https://github.com/axios/axios/blob/master/LICENSE) - 用于和后端通信的API接口，可用JQuery或原生request代码替换~~

~~（以上Module均已经默认安装，不需要特别引入）~~

~~**服务端 - Python 3.6以上版本：**~~

```
pip install flask
```

~~请确保服务端Python环境安装了Flask.（推荐使用virtualenv或其他虚拟环境包工具）~~



### 安装

Clone/download 项目包解压到指定文件夹即可



### 启动

切换到项目根目录，双击"启动.cmd"即可启动



### 项目结构

app-web/前端代码

database/文档存储位置

dist/前端执行代码

env/服务器环境

server/服务器逻辑代码



### API

待补充



### 其他功能

##### 更换主题

修改index.html中的

```html
<!--- 省略代码 --->
<link rel="stylesheet" type="text/css" href='<< url_for("static", filename="css/defaultTheme.css") >>'>
<!--- 选择上下任意一个CSS --->
<link rel="stylesheet" type="text/css" href='<< url_for("static", filename="css/darkTheme.css") >>'>
<!--- 省略代码 --->
```

感谢知乎@parox 帮助编写并提供的两个主题



### 贡献

架构 

beta版本核心架构 github @JerryZhuyi

7大模块主要功能   github @JerryZhuyi

tools主要功能        知乎     @parox 

  

主题

defaultTheme   - 知乎@parox 

darkTheme        - 知乎@parox



### 社区

您有任何想法、问题、求助可以邮件zhuyi@egbenz.com。

Make code **Brevity、Understandable、Free**, is our goal.
We hope you can make progress together with us.

### 历史版本

[2022-05-10 V1]

- 增加F5默认刷新事件
- 调整Mod继承关系，明确3大基础Mod,BaseText,BaseBlock,BaseExt,同时扩展基本继承方法和属性。
- 调整开发者环境，增加Webpack打包优化代码。
- 调整目录结构，database单独形成一级目录
- html2Ez增加A标签识别，增加ModLink 模块
- 新增数学公式-ModKatex模块
- 大幅度提升页面加载速度。由3s下降为1s左右。
- 增加便捷启动，双击目录下"启动.cmd"即可自动启动笔记本，并自动打开首页

[2022-05-03 Beta Version] 

- 首发测试版本，实现用原生JS完全接管contenteditable,实现本地化笔记本常用功能。