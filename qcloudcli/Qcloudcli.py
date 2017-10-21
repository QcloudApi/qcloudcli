#!/usr/bin/env python
# -*- coding: utf-8 -*-

import errno
import socket
import sys
import time
import traceback

from . import handleParameter
from . import handleData
from . import handleCmd
from . import result
from . import showHelp
from . import autoComplete

try:
    reload(sys)  # Python 2.7
    sys.setdefaultencoding('utf8')
except NameError:
    try:
        from importlib import reload  # Python 3.4+
        reload(sys)
    except ImportError:
        from imp import reload  # Python 3.0 - 3.3
        reload(sys)

def main():
    handle = QcloudCLI()
    handle.main()

class QcloudCLI:
    def __init__(self):
        self.user_input = sys.argv[1:]
        self.handleParameter = handleParameter.handleParameter()
        self.handleCmd = handleCmd.handleCmd()
        self.handleData = handleData.handleData()
        self.showHelp = showHelp.showHelp()
        self.completer = autoComplete.Completer()

    def main(self):
        module = ''
        #get module such as cvm cdb..maybe extra cmd such as help,version
        if self.user_input.__len__() > 0:
            module = self.user_input[0].lower()

        #show qcloudcli help
        help_cmd = ['help','-h','--help']
        if not module or module.lower() in help_cmd:
            self.handleCmd.showQcloudCliHelp()
            return

        #show version
        version_cmd = ['version','--version']
        if module.lower() in version_cmd:
            self.handleCmd.showVersion()
            return

        #configure qcloudcli
        configure_cmd = ['configure']
        if module.lower() in configure_cmd:
            self.handleCmd.configureQcloudcli()
            return

        #showconfigure qcloudcli
        showconfigure_cmd = ['showconfigure']
        if module.lower() in showconfigure_cmd:
            self.handleCmd.showconfigure()
            return

        #addprofile qcloudcli
        addprofile_cmd = ['addprofile']
        if module.lower() in addprofile_cmd:
            self.handleCmd.addprofile()
            return

        # useprofile qcloudcli
        useprofile_cmd = ['useprofile']
        if module.lower() in useprofile_cmd:
            self.handleCmd.useprofile()
            return

        # useprofile qcloudcli
        useprofile_cmd = ['delprofile']
        if module.lower() in useprofile_cmd:
            self.handleCmd.delprofile()
            return


        # get action,such as DescribeInterfaces
        action = self.handleParameter.getAction()

        # get paramlist
        keyValues = self.handleParameter._getKeyValues()
        outPutFormat = self.handleParameter.getUserDefinedOutPutFormat(keyValues)
        if outPutFormat is not None and len(outPutFormat) != 0:
            outPutFormat = outPutFormat[0]
        else:
            outPutFormat = self.handleCmd.getUserFormat()
            if outPutFormat is None or outPutFormat == "":
                outPutFormat = 'json'

        if module in self.handleData.getAllModules():
            moduleAllActions = self.handleData.getModuleActions(module)
            if action in moduleAllActions:
                instance = self.handleData.makeInstance(module, action)
                instance_version = self.handleData.makeInstance(module, action)
                in_class = self.handleData.makeClass(module, action)
                in_class_version = self.handleData.makeClass(module, action)
                is_version = 0
                if module == 'cvm' and action+'V3' in moduleAllActions:
                    is_version = 1
                    in_class_version = self.handleData.makeClass(module, action+'V3')
                    instance_version = self.handleData.makeInstance(module, action+'V3')
                if (instance is not None or instance_version is not None) and (in_class is not None or in_class_version is not None):
                    helpcmds = ['-h', '--help', 'help']
                    cmdlen = self.user_input.__len__()
                    if cmdlen >= 3:
                        for i in range(2, cmdlen):
                            if self.user_input[i] in helpcmds:
                                self.showHelp.showParameterError(module, action, is_version, self.completer._help_to_show_instance_attribute(in_class, in_class_version)[0],self.completer._help_to_show_instance_attribute(in_class, in_class_version)[1],self.completer._help_to_show_instance_attribute(in_class, in_class_version)[2], self.completer._help_to_show_instance_attribute(in_class, in_class_version)[3])
                                return
                    if keyValues.get("RegionId") is None and keyValues.get("regionId") is None and keyValues.get("Regionid")is None and keyValues.get("regionid") is None:
                        keyValues["RegionId"] = [self.handleCmd.getUserRegion()]
                    if not self.handleData.checkInputIsEmpty(keyValues):
                        print('Your [SecretId] or [SecretKey] or [RegionId] is absence!')
                        return
                    try:
                        if not keyValues.get("Version") is None and self.is_valid_date(keyValues.get("Version")[0]) and is_version == 1:
                            outcome = self.handleData.getResponse(module, action, keyValues, instance_version, in_class_version)
                        else:
                            outcome = self.handleData.getResponse(module, action, keyValues, instance, in_class)
                        if outcome is None:
                            return
                        result.display_result(action, outcome, outPutFormat, keyValues)
                    except socket.error as e:
                        print(e)
                        if e.errno == errno.ETIMEDOUT:
                            print('Connection aborted due to timeout exception.')
                            print('Please check your network connection, firewall and router settings.')
                            print('If you are behind a proxy, you need to set the https_proxy environment variable.')
                        else:
                            print(traceback.format_exc())
                    except Exception as e:
                        print(e)
                        print(traceback.format_exc())
                else:
                    print('qcloudcli internal error, please try again.')
            else:
                self.showHelp.showActionError(module)
        else:
            self.showHelp.showModuleError()

    def is_valid_date(self, str):
        try:
            time.strptime(str, "%Y-%m-%d")
            return True
        except:
            return False

if __name__ == '__main__':
    main()

