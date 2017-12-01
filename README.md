# 腾讯云命令行工具

[![pypi version](https://img.shields.io/pypi/v/qcloudcli.svg)](https://pypi.python.org/pypi/qcloudcli)
[![Build Status](https://travis-ci.org/QcloudApi/qcloudcli.svg?branch=master)](https://travis-ci.org/QcloudApi/qcloudcli)

For English users, pelase refer to document [README.rst](https://github.com/QcloudApi/qcloudcli/blob/master/README.rst)

腾讯云命令行工具 qcloudcli 基于腾讯云 API 开发。

qcloudcli 支持 Python 2.7.x 到 3.6.x 版本环境。

详细介绍请参考[官网文档](https://www.qcloud.com/document/product/440/6176)。

## 安装

推荐使用 [pip](https://pip.pypa.io/en/stable/) 安装：

```
$ pip install --user qcloudcli
```

`--user` 选项会将 qcloudcli 只安装到当前用户环境中，这意味着不需要 sudo 权限。
注意：如果是在 virtualenv 环境下，`--user` 选项是不支持的。

升级：

```
$ pip install --user --upgrade qcloudcli
```

卸载:

```
$ pip uninstall --yes qcloudcli
```

### 命令补全

qcloudcli 为 bash 环境提供了命令补全功能，但是不是默认开启的。开启的方式：

```
$ complete -C qcloud_completer qcloudcli
```

将该命令加入 `~/.bashrc` 以默认开启。

## 使用指南

查看版本号：

```
$ qcloudcli --version
```

### 配置系统参数

qcloudcli 需要提供账号信息才能访问腾讯云各服务。登录腾讯云[控制台](https://console.cloud.tencent.com/)，进入[API密钥管理](https://console.cloud.tencent.com/cam/capi)页面查看密钥，如果没有则需要新建密钥。SecretId 相当于账号，SecretKey 相当于密码，为保护你的资产，请不要将 SecretKey 透露给其他人。

执行如下命令，根据提示配置 qcloudcli ：

```
$ qcloudcli configure
Qcloud API SecretId [None]: foo
Qcloud API SecretKey [None]: bar
Region Id(gz,hk,ca,sh,shjr,bj,sg) [None]: gz
Output Format(json,table,text) [None]: json
```

这些信息会放在当前用户的根路径下，例如 Linux 操作系统位于 `~/.qcloudcli/configure` 和 `~/.qcloudcli/credentials` 两个文件中。

`~/.qcloudcli/configure` 内容示例如下：

```
[default]
output = json
region = gz
```

`~/.qcloudcli/credentials` 内容示例如下：

```
[default]
qcloud_secretkey = bar
qcloud_secretid = for
```

注意：这些信息是明文存储的，依赖于用户家目录下正确的文件权限设置控制访问。例如：

```
$ ls -l ~/.qcloudcli/
total 8
4 -rw-rw-r-- 1 john john 36 Nov 29 23:35 configure
4 -rw------- 1 john john 55 Nov 29 23:35 credentials
```

注意：当前版本中，当卸载 qcloudcli 时，这两个文件并不会自动删除，你需要手动将其删除掉。

### 获取帮助信息

运行命令，获取qcloudcli的功能列表，其中包含qcloudcli的configure命令，和所有支持的服务模块：

```
$ qcloudcli help
```

运行命令，获取特定的服务模块的帮助信息，例如获取cvm模块的帮助信息，其中包含了cvm模块下的接口列表：

```
$ qcloudcli cvm help
```

运行命令，获取特定模块下特定接口的帮助信息，例如获取查询虚拟机列表DescribeInstances接口的帮助信息，其中包含了接口的参数列表：

```
$ qcloudcli cvm DescribeInstances help
```

### 使用复杂结构体的参数

对于基本数据类型的参数，例如字符串、数字，可以直接输入。

例如，查询虚拟机列表，使用默认的API版本，指定参数limit=10，只返回10个虚拟机，则直接输入：

```
$ qcloudcli cvm DescribeInstances --limit 10
```

对于复杂的结构体，例如列表，字典等类型，需要输入json格式的字符串。

例如，查询虚拟机列表，使用默认的API版本，指定instanceIds参数，只返回id为qcvmf4b542ad7b4cd49f2db57a733368d5b1和id为qcvmaf636dd06a816765b4f2c51595f2d84d的两台虚拟机，需要输入：

```
$ qcloudcli cvm DescribeInstances --instanceIds '["qcvmf4b542ad7b4cd49f2db57a733368d5b1", "qcvmaf636dd06a816765b4f2c51595f2d84d"]'
```

例如，查询虚拟机列表，使用2017-03-12 API版本，指定Filters参数，返回部署在zone为ap-guangzhou-2的虚拟机，需要输入：

```
$ qcloudcli cvm DescribeInstances --Filters '[{"Name":"zone","Values":["ap-guangzhou-2"]}]'
```

### 过滤返回字段

我们使用[jmespath](https://github.com/jmespath/jmespath.py)做json路径解析。

对于返回比较复杂的情况，可以使用--filter参数指定返回部分内容。

注意使用前你必须清楚返回的数据的具体结构才能正确引用。

例如查看安全组列表，只获取安全组id列表，由于每个安全组元素是在data字段表示的列表里，如果用具体的下标，则只返回对应的元素，用`*`表示返回所有：

```
$ qcloudcli dfw DescribeSecurityGroups --filter data[*].sgId
[
    "sg-icy671l9",
    "sg-o9rfv42p",
    "sg-pknfyaar",
    "sg-2rjokpt7",
    "sg-4ehjaoh3"
]
```

例如使用CVM API 2017-03-12版本，查看虚拟机，只获取安全组列表字段，这里由于只指定了一台虚拟机，InstanceSet下的第0个元素必定是该虚拟机，则可以如下表示：

```
$ qcloudcli cvm DescribeInstances --InstanceIds '["ins-od1laqxs"]' --filter Response.InstanceSet[0].SecurityGroupIds
[
    "sg-4ehjaoh3"
]
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

### 使用代理

如果是在代理环境下使用qcloudcli，且`*.api.qlcoud.com`域名不在代理的白名单列表中，则需要配置HTTPS代理才能正常使用。
目前仅支持不含账户信息的全局代理，仅在Linux和Windows系统上测试过。

在Linux操作系统BASH环境下，使用`export https_proxy=YourProxyRealHost:YourProxyRealPort`设置环境变量后即可。
注意，将示例中的YourProxyRealHost和YourProxyRealPort替换为代理的实际值。
你还可以将该行放在BASH配置文件`~/.bashrc`中，以避免每次新开终端都要配置一遍。

在Windows操作系统下，使用`set https_proxy=YourProxyRealHost:YourProxyRealPort`设置环境变量后即可。
注意，将示例中的YourProxyRealHost和YourProxyRealPort替换为代理的实际值。
你还可以在“计算机-属性-高级系统设置-环境变量-系统变量”中设置该值，以避免每次新开终端都要配置一遍。
