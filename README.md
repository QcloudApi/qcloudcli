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

## 指定API版本

打开配置文件``~/.qcloudcli/configure``，在对应的profile下增加如下内容

```
api_versions =
    cvm = 2017-03-12
```

即指定了使用的cvm API版本为2017-03-12

如果指定的版本不存在，则运行任意cvm相关命令后会报错并提示可用版本。
如无任何可用版本，则不需要设置相关信息，请在配置文件中删除该行。
如果没有指定任何版本，即配置项为空，则CLI会使用默认版本。
