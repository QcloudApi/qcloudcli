# The Qcloud CLI (Command Line Interface)

Qcloud Api的命令行工具。

CLI支持python 2.6.5到3.6版本环境。

详细介绍请参考[官网文档](https://www.qcloud.com/document/product/440/6176)。

## 更新历史

* [2017/8/21] 兼容python2和python3版本；支持pip安装使用

## 安装
    $ pip install qcloudcli

或者下载源码安装

    $ git clone https://github.com/QcloudApi/qcloudcli.git
    $ cd qcloudcli
    $ python setup.py install

## 使用指南

### 获取帮助信息

运行命令，获取qcloudcli的功能列表，其中包含qcloudcli的configure命令，和所有支持的服务模块：

```
qcloudcli help
```

运行命令，获取特定的服务模块的帮助信息，例如获取cvm模块的帮助信息，其中包含了cvm模块下的接口列表：

```
qcloudcli cvm help
```

运行命令，获取特定模块下特定接口的帮助信息，例如获取查询虚拟机列表DescribeInstances接口的帮助信息，其中包含了接口的参数列表：

```
qcloudcli cvm DescribeInstances help
```

### 使用复杂结构体的参数

对于基本数据类型的参数，例如字符串、数字，可以直接输入。

例如，查询虚拟机列表，使用默认的API版本，指定参数limit=10，只返回10个虚拟机，则直接输入：

```
qcloudcli cvm DescribeInstances --limit 10
```

对于复杂的结构体，例如列表，字典等类型，需要输入json格式的字符串。

例如，查询虚拟机列表，使用默认的API版本，指定instanceIds参数，只返回id为qcvmf4b542ad7b4cd49f2db57a733368d5b1和id为qcvmaf636dd06a816765b4f2c51595f2d84d的两台虚拟机，需要输入：

```
qcloudcli cvm DescribeInstances --instanceIds '["qcvmf4b542ad7b4cd49f2db57a733368d5b1", "qcvmaf636dd06a816765b4f2c51595f2d84d"]'
```

例如，查询虚拟机列表，使用2017-03-12 API版本，指定Filters参数，返回部署在zone为ap-guangzhou-2的虚拟机，需要输入：

```
qcloudcli cvm DescribeInstances --Filters '[{"Name":"zone","Values":["ap-guangzhou-2"]}]'
```

### 指定API版本

打开配置文件``~/.qcloudcli/configure``，在对应的profile下增加如下内容

```
api_versions =
    cvm = 2017-03-12
```

即指定了使用的cvm API版本为2017-03-12

如果指定的版本不存在，则运行任意cvm相关命令后会报错并提示可用版本。
如无任何可用版本，则不需要设置相关信息，请在配置文件中删除该行。
如果没有指定任何版本，即配置项为空，则CLI会使用默认版本。
