import os,sys
import platform
from .advance import userProfileHandler
from .advance import userConfigHandler
from . import configure
from . import handleParameter

class QcloudCredentials:
    qcloud_secretid = "qcloud_secretid"
    qcloud_secretkey = "qcloud_secretkey"

def get_python_lib():
    for path in sys.path:
        if path and os.path.isdir(path):
            objects = os.listdir(path)
            for object in objects:
                if object.startswith('qcloudsdk') and os.path.isdir(os.path.join(path, object)):
                    return path
class handleCmd:
    def __init__(self):
        if 'Linux' in platform.system():
            self.begin = '\033[1m'
            self.red = '\033[31m'
            self.end = '\033[0m'
        if 'Windows' in platform.system():
            self.begin = ''
            self.red = ''
            self.end = ''
        else:
            self.begin = ''
            self.red = ''
            self.end = ''
        self.configure = "configure"
        self.credentials = "credentials"
        self.globalConfigure = configure.QcloudConfig()
        self.parameter = handleParameter.handleParameter()
    #show qcloudcli help
    def showQcloudCliHelp(self):
        ConfigurePath = self.showQcloudConfigurePath()
        if not os.path.isdir(ConfigurePath):
            print(self.red + "\nThis is the first time you use qcloudcli, please use command 'qcloudcli configure' to set your personal information." + self.end)
        print(self.begin + "\nNAME:" + self.end)
        print("\tqcloudcli")
        print(self.begin + "\nDESCRIPTION:" + self.end)
        print("\n\tThe Qcloud Command Line Interface is a unified tool to manage your qcloud services.")
        print(self.begin + "\nCONFIGURE:" + self.end)
        print("\n\tBefore using qcloudcli, you should use the command as follow:")
        print(self.red + "\n\tqcloudcli configure" + self.end)
        print("\n\tThis command will save your SecretId and SecretKey and the default output format (json text or table).")
        print(self.begin + "\nFORMATE:" + self.end)
        print("\n\tYou should use qcloudcli as this format:\n")
        print(self.red + "\tqcloudcli <module> <action> [options and parameters]" + self.end)
        print("\n\tYou can check our site to see the detail of using qcloudcli.")
        print(self.begin + "\nAVAILABLE MODULES:" + self.end + "\n")
        modules = self.getAllmodules()
        self.showAsTwoLines(modules)
        print(self.begin + "\nAVAILABLE ACTIONS:" + self.end + "\n")
        print("\tYou can use the command " + self.red + "qcloudcli <module> --help " + self.end + "to know the module corresponding actions.")

    def showQcloudConfigurePath(self):
        configurePathName = ".qcloudcli"
        sysHomePath = ''
        if 'Windows' in platform.system():
            sysHomePath = os.environ['HOMEPATH']
        else:
            sysHomePath = os.environ['HOME']
            pass
        qcloudConfigurePath = os.path.join(sysHomePath, configurePathName)
        return qcloudConfigurePath

    def getAllmodules(self):
        #from distutils.sysconfig import get_python_lib
        site_packages_path = get_python_lib()
        all_python_packages = os.listdir(site_packages_path)
        modules = list()
        if all_python_packages is not None:
            for package in all_python_packages:
                if package.startswith('qcloudsdk') and os.path.isdir(os.path.join(site_packages_path,package)):
                    module = package.split('qcloudsdk', 1)[1]
                    if len(module) > 0 and module not in['core']:
                        modules.append(module)
        return modules

    def showAsTwoLines(self, data):
        mlist = list()
        for item in data:
            mlist.append(item)
        mlist.sort()
        if len(mlist)%2 == 0:
            k=len(mlist) // 2
        else:
            k=len(mlist) // 2 + 1
        mlist2 = list()
        for item in mlist:
            mlist2.append(item)
        for i in range(0,k):
            mlist2[2 * i] = mlist[i]
        for i in range(k,2*k-1):
            mlist2[i-(2*k-1-i)] = mlist[i]
        count = 0
        tmpList = list()
        for item in mlist2:
            tmpList.append(item)
            count = count+1
            if len(tmpList) == 2:
                print('\t'+'{0:30}'.format(tmpList[0])+'\t|'+format(tmpList[1],'<10'))
                tmpList = list()
            if len(tmpList) == 1 and count == len(mlist2):
                print('\t'+tmpList[0]+'\n')

    def showVersion(self):
        from .__init__ import __version__ as version
        print(version)

    def configureQcloudcli(self):
        configure.handleConfigure()

    def showconfigure(self):
        _configHandler = userConfigHandler.ConfigHandler()
        _configHandler.showConfig()

    def addprofile(self):
        _keyvalues= self.parameter._getKeyValues()
        _profileHandler = userProfileHandler.ProfileHandler()
        _profileHandler.addProfileCmd(_keyvalues)

    def useprofile(self):
        _cmd = self.parameter._getCommand()
        _keyvalues= self.parameter._getKeyValues()
        _profileHandler = userProfileHandler.ProfileHandler()
        _profileHandler.useProfileCmd(_cmd, _keyvalues)

    def delprofile(self):
        _cmd = self.parameter._getCommand()
        _keyvalues= self.parameter._getKeyValues()
        _profileHandler = userProfileHandler.ProfileHandler()
        _profileHandler.delProfileCmd(_cmd, _keyvalues)

    def getUserRegion(self):
        handler = configure.QcloudConfig()
        return handler._getUserRegion()
    def getUserFormat(self):
        handler = configure.QcloudConfig()
        return handler._getUserFormat()
    def getUserKey(self):
        handler = configure.QcloudConfig()
        return handler._getUserKey()
    def getUserSecret(self):
        handler = configure.QcloudConfig()
        return  handler._getUserSecret()

if __name__ == "__main__":
    pass
