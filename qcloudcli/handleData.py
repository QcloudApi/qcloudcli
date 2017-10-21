import datetime
import os
import sys,imp,uuid
from qcloudcli import configure
from . import handleCmd
from . import handleParameter
import json
import site

from .__init__ import  __version__
_userAgent='qcloudcli/'+str(__version__)

version_cmds = ['ConfigVersion','ShowVersions']

def get_python_lib():
    for path in sys.path:
        if path and os.path.isdir(path):
            objects = os.listdir(path)
            for object in objects:
                if object.startswith('qcloudsdk') and os.path.isdir(os.path.join(path, object)):
                    return path

class handleData():
    def __init__(self, path=None):
        self.path = path
        self.handleCmd = handleCmd.handleCmd()
        self.parser = handleParameter.handleParameter()

    def getAllModules(self):
        #from distutils.sysconfig import get_python_lib
        site_packages_path = get_python_lib()
        all_python_packages = os.listdir(site_packages_path)
        modules = []
        if all_python_packages is not None:
            for package in all_python_packages:
                if package.startswith('qcloudsdk') and os.path.isdir(os.path.join(site_packages_path, package)):
                    module = package.split('qcloudsdk', 1)[1]
                    if len(module) > 0 and module not in ['core']:
                        modules.append(module)
        modules.append("configure")
        return modules

    def getModuleActions(self, module):
        config = configure.QcloudConfig().getConfig()
        version = config.get(module, '')

        sitepath = get_python_lib()
        modpath = os.path.join(sitepath, 'qcloudsdk' + module)
        versionpath = os.path.join(modpath, version)
        if not os.path.exists(versionpath):
            validVersions = []
            for element in os.listdir(modpath):
                if not os.path.isdir(os.path.join(modpath, element)):
                    continue
                try:
                    datetime.datetime.strptime(element, '%Y-%m-%d')
                    validVersions.append(element)
                except ValueError:
                    pass
            validVersions = ','.join(validVersions)
            print('ERROR: Unknown version %s for module %s, valid '
                  'version(s): %s' % (version, module, validVersions))
            raise SystemExit(1)
        self.path = versionpath

        actions = []
        for element in os.listdir(versionpath):
            if os.path.isdir(os.path.join(versionpath, element)):
                continue
            if element.endswith('Request.py'):
                actions.append(element.rsplit('Request.py', 1)[0])

        return actions

    # get all actions for one module
    def getModuleActionsForVersion(self, module):
        actions = []
        newactions = []
        #from distutils.sysconfig import get_python_lib
        sitepackages_path = get_python_lib()
        pre_module='qcloudsdk'
        module = pre_module+module
        moudle_path=os.path.join(sitepackages_path,module)
        for root, dirs, files in os.walk(moudle_path):
            for file_name in files:
                if file_name.endswith('Request.py') and not file_name.endswith('V3Request.py'):
                    action=file_name.split('Request.py',1)[0]
                    if len(action) >0:
                        self.path = root
                        actions.append(action)
        for root, dirs, files in os.walk(moudle_path):
            for file_name in files:
                if file_name.endswith('V3Request.py'):
                    action=file_name.split('V3Request.py',1)[0]
                    if len(action) >0:
                        self.path = root
                        newactions.append(action)
        return actions, newactions

    def isLegalAction(self, module, action):
        if module is None:
            return False
        if action is None:
            return False
        actions = self.getModuleActions(module)
        if action in actions:
            return True
        else:
            return False

    def makeInstance(self,module,action):
        if module is None or action is None or self.path is None:
            return None
        actionName = action+'Request'
        try:
            fp, pathname, desc = imp.find_module(actionName,[self.path])
            imp.load_module(actionName, fp, pathname, desc)
            modules_keys=list(sys.modules.keys())
            for key in modules_keys:
                if key==actionName:
                    try:
                        module = sys.modules[actionName]
                        mInstance= getattr(module, actionName)()
                        return mInstance
                    except Exception as err:
                        print(err)
        except Exception as err:
            print(err)
        return None

    def makeClass(self,module,action):
        if module is None or action is None or self.path is None:
            return None, None
        actionName = action+'Request'
        try:
            fp, pathname, desc = imp.find_module(actionName,[self.path])
            imp.load_module(actionName, fp, pathname, desc)
            modules_keys=list(sys.modules.keys())
            for key in modules_keys:
                if key==actionName:
                    try:
                        module = sys.modules[actionName]
                        className=getattr(module,actionName)
                        return className
                    except Exception as err:
                        print(err)
        except Exception as err:
            print(err)
        return None

    def checkInputIsEmpty(self,keyValues):
        region=self.getRegionId(keyValues)
        userKey=self.handleCmd.getUserKey()
        userSecret=self.handleCmd.getUserSecret()
        if region is None or userKey is None or userSecret is None:
            return False
        else:
            return True

    def getSetFuncs(self,classname):
        SetFuncs=[]
        keys=[]
        if classname is not None:
            keys = list(classname.__dict__.keys())
        for key in keys:
            if key.startswith('set_'):
                SetFuncs.append(key.replace('set_', ''))
        return SetFuncs

    def getFuncs(self,classname):
        SetFuncs=[]
        keys=[]
        if classname is not None:
            keys = list(classname.__dict__.keys())
        for key in keys:
            if key.startswith('set_'):
                SetFuncs.append(key)
        return SetFuncs

    def getResponse(self,cmd,operation,keyValues,instance,classname):
        setFuncs=self.getFuncs(classname)
        if len(setFuncs)>0:
            for func in setFuncs:
                key=func.split('set_',1)[1]
                if len(key)>0 and key in keyValues:
                    arg=keyValues[key]
                    if arg is not None and len(arg)>0:
                        param=arg[0]
                        if (param[0] == '[' or param[0] == '{'):
                            param = json.loads(param)
                        getattr(instance,func)(param)
        userKey=self.getUserKey()
        userSecret=self.getUserSecret()
        regionId=self.getRegionId(keyValues)
        userAgent=self.getUserAgent()
        module='qcloudsdkcore'
        try:
            instance.set_user_info(userKey,userSecret,'POST',regionId,True,3,userAgent)
            result = instance.call()
            try:
                jsonobj = json.loads(result)
            except TypeError as e:
                jsonobj = json.loads(result.decode('utf-8')) #python3.3
            return jsonobj
        except ImportError as e:
            print(module + 'is not exist!')
            return

    def getUserKey(self):
        userKey=None
        userKey, userSecret = self.parser.getTempKeyAndSecret()
        if userKey is None:
            if self.handleCmd.getUserKey() is not None:
                userKey = self.handleCmd.getUserKey()
        return userKey

    def getUserSecret(self):
        userSecret=None
        userKey, userSecret = self.parser.getTempKeyAndSecret()
        if userSecret is None:
            if not self.handleCmd.getUserSecret() is None:
                userSecret = self.handleCmd.getUserSecret()
        return userSecret

    def getRegionId(self,keyValues):
        key='RegionId'
        if key in keyValues:
            return keyValues[key][0]
        else:
            return None

    def getUserAgent(self):
        return _userAgent


if __name__ == '__main__':
    pass
