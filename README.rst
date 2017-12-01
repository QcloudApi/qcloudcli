=================================================
Tencent Cloud (aka QCloud) Command Line Interface
=================================================

.. image:: https://img.shields.io/pypi/v/qcloudcli.svg
   :target: https://pypi.python.org/pypi/qcloudcli
   :alt: pypi version
.. image:: https://travis-ci.org/QcloudApi/qcloudcli.svg?branch=master
   :target: https://travis-ci.org/QcloudApi/qcloudcli
   :alt: Build Status

Tencent Cloud (aka QCloud) Command Line Interface qcloudcli is an open source tool built on top of the Tencent Cloud API that provides commands for interacting with Tencent Cloud services.

It works on Python versions:

* 2.7.x and greater
* 3.6.x and greater

-------
Install
-------

The recommended way to install qcloudcli is to use `pip <https://pip.pypa.io/en/stable/>`_:

.. code-block:: sh

    $ pip install --user qcloudcli

``--user`` option will install qcloudcli to current user path instead of system path, for Linux system, it might be ``~/.local``, which means it doesn't require ``sudo`` priviledge.

.. attention::

    If you are in a ``virtualenv`` environment, the ``--user`` option should be removed.

to upgrade:

.. code-block:: sh

    $ pip install --user --upgrade qcloudcli

to remove:

.. code-block:: sh

    $ pip uninstall --yes qcloudcli

^^^^^^^^^^^^^^^^^^
Command Completion
^^^^^^^^^^^^^^^^^^

On Unix-like systems, the qcloudcli includes a command-completion feature that enables you to use the TAB key to complete a partially typed command. This feature is not automatically installed, so you need to configure it manually.

.. code-block:: sh

    $ complete -C qcloud_completer qcloudcli

Add it to your ``~/.bashrc`` to enable it by default.

-----------
Usage Guide
-----------

Get the version of qcloudcli:

.. code-block:: sh

    $ qcloudcli --version

^^^^^^^^^^^^^
Configuration
^^^^^^^^^^^^^

qcloudcli needs account information to interact with Tencent Cloud Services. Log in Tencent Cloud `Console <https://console.cloud.tencent.com/>`_, shift to `API Credential Management <https://console.cloud.tencent.com/cam/capi>`_ page to view your credentials, if the list is empty, you will need to create a new one. ``SecretId`` is used like your account name, ``SecretKey`` is used like your password, so keep in mind that never leak your ``SecretKey`` to others.

.. attention::

    You might not be able to have such page in international site or translations in English version for now.

Run ``qcloudcli congifure`` to enter interactive mode and provide information like this:

.. code-block:: sh

    $ qcloudcli configure
    Qcloud API SecretId [None]: foo
    Qcloud API SecretKey [None]: bar
    Region Id(gz,hk,ca,sh,shjr,bj,sg) [None]: gz
    Output Format(json,table,text) [None]: json

These information will be stored in files under your home root path, for example, in Linux system, it will be ``~/.qcloudcli/configure`` and ``~/.qcloudcli/credentials``.

The content of ``~/.qcloudcli/configure`` in last example is::

    [default]
    output = json
    region = gz

The content of ``~/.qcloudcli/credentials`` in last example is::

    [default]
    qcloud_secretkey = bar
    qcloud_secretid = for

.. attention::

    These information will be stored as plain text, it relies on your correct access control of your private home directory.

In Linux system, the default priviledge is::

    $ ls -l ~/.qcloudcli/
    total 8
    4 -rw-rw-r-- 1 john john 36 Nov 29 23:35 configure
    4 -rw------- 1 john john 55 Nov 29 23:35 credentials

.. attention::

    Currently, these two configure files will not be removed when you uninstall qcloudcli, you will need to manually remove them.

^^^^^^^^
Use Help
^^^^^^^^

To get available module list, including ``configure`` command, run::

    $ qcloudcli help

To get action list of specific module, for example, cvm (Cloud Virtual Machine), run::

    $ qcloudcli cvm help

To get parameter list of specific action, for example, DescribeInstances, run::

    $ qcloudcli cvm DescribeInstances help

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Specify Complex Object Paramters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To specify base type parameters, like string and int, you can directly use it. For example, to get instance (virtual machine) list, use default API version, limit the return item to 10, run::

    $ qcloudcli cvm DescribeInstances --limit 10

For complex object parameters, like array and dictionary, you have to use json format string.

For example, to get instance list, use default API version, only query instances which id are ``qcvmf4b542ad7b4cd49f2db57a733368d5b1`` and ``qcvmaf636dd06a816765b4f2c51595f2d84d``, run::

    $ qcloudcli cvm DescribeInstances --instanceIds '["qcvmf4b542ad7b4cd49f2db57a733368d5b1", "qcvmaf636dd06a816765b4f2c51595f2d84d"]'

For example, to get instance list, use API version 2017-03-12, with ``Filters`` parameter, only return instances in ap-guangzhou-2 zone, run::

    $ qcloudcli cvm DescribeInstances --Filters '[{"Name":"zone","Values":["ap-guangzhou-2"]}]'

^^^^^^^^^^^
Filter Data
^^^^^^^^^^^

qcloudcli provides ``--filter`` option which bases on `jmespath <https://github.com/jmespath/jmespath.py>`_ to filter returned data, it is pretty useful when you want to get specific data from a bunch of items. However, you need to know the exact structure of returned json format.

For example, to get security groups and only return security gourp id, run::

    $ qcloudcli dfw DescribeSecurityGroups --filter data[*].sgId
    [
        "sg-icy671l9",
        "sg-o9rfv42p",
        "sg-pknfyaar",
        "sg-2rjokpt7",
        "sg-4ehjaoh3"
    ]

``*`` means get all elements.

For example, using CVM API version 2017-03-12, to get security groups id of a specific instance ins-od1laqxs, run::

    $ qcloudcli cvm DescribeInstances --InstanceIds '["ins-od1laqxs"]' --filter Response.InstanceSet[0].SecurityGroupIds
    [
        "sg-4ehjaoh3"
    ]

The index ``0`` means get the first instance.

^^^^^^^^^^^^^^^^^^^
Specify API Version
^^^^^^^^^^^^^^^^^^^

Some services of Tencent Cloud have multiple API versions, for example, CVM has a API version 2017-03-12, to use it, open ``~/.qcloudcli/configure`` and add the following content in profile section::

    api_versions =
        cvm = 2017-03-12

If the specified version doesn't exist, you will get an error when you run related commands.
If the service only has one version, then you don't need to add such configuration, please remove it.
If the service has multiple versions, and there is no such configuration, then the default one will be used.

^^^^^^^^^^^^^^^
Use HTTPS Proxy
^^^^^^^^^^^^^^^

If you are in an environment behinds a proxy, and ``*.api.qcloud.com`` is not in the proxy white list, then you will need to configure HTTPS proxy to get qcloudcli work.

Currently, only verified in Linux and Windows system, with proxy doesn't require user name and password.

In Linux system, to set your temporary global proxy, run::

    $ export https_proxy=YourProxyRealHost:YourProxyRealPort

Please note that replace ``YourProxyRealHost`` and ``YourProxyRealPort`` with your real proxy information.
You can add it to your ``~/.bashrc`` to active it by default.

In Windows system, to set your temporary global proxy, run::

    > set https_proxy=YourProxyRealHost:YourProxyRealPort

You can add it to your system environment variables to active it by default.
