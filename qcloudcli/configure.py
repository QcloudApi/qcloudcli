#/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
from . import handleParameter
import platform
#from . import handleCmd

PY2 = sys.version_info[0] == 2

def handleConfigure():
    handler = ConfigureCommand()
    handler._run()

class QcloudCredentials:
    qcloud_access_key_id = "qcloud_secretid"
    qcloud_access_key_secret = "qcloud_secretkey"

class QcloudConfig(object):
    def __init__(self,configWriter = None):
        if configWriter is None:
            configWriter = ConfigFileWriter()
        self._configWriter = configWriter
        self.home = ".qcloudcli"
        self.configure = "configure"
        self.credentials = "credentials"
        self.qcloudConfigurePath = os.path.join(self.findConfigureFilePath(),self.home)
        self.parser = handleParameter.handleParameter()

    def getConfig(self,profilename = None):
        if profilename is None:
            profilename = 'default'
        config = {}
        _configFileName = self.getConfigFileName()
        _credsFileName = self.getCredsFileName()
        self._getConfigFromFile(config, profilename, _configFileName)
        self._getConfigFromFile(config, profilename, _credsFileName)
        return config

    def _getConfigFromFile(self, config, profile, filename):
        #filename = 'C:' + filename
        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                contents = f.readlines()
                if profile == 'default':
                    _sectionName = '%s'%profile
                else:
                    _sectionName = 'profile %s'%profile
                if self._configWriter.hasSectionName(_sectionName,contents)[0]:
                    sectionStart = self._configWriter.hasSectionName(_sectionName,contents)[1]
                    j = sectionStart
                    sectionEnd = self._configWriter._getSectionEnd(j,contents)
                    while j < sectionEnd:
                        line = contents[j]
                        if line.strip():
                            key = self._configWriter._getKey(line)
                            config[key] = self._configWriter._getValue(line)
                        j = j+1
                else:
                    pass
        else:
            pass

    def getConfigFileName(self):
        configFileName = os.path.join(self.qcloudConfigurePath,self.configure)
        return configFileName

    def getCredsFileName(self):
        credsFileName = os.path.join(self.qcloudConfigurePath,self.credentials)
        return credsFileName


    def findConfigureFilePath(self):
        homePath = ""
        if platform.system() == "Windows":
            homePath = os.environ['HOMEPATH']
            pass
        else:
            homePath = os.environ['HOME']
            pass
        return homePath


    def _getUserRegion(self):
        _keyValues = self.parser._getKeyValues()
        _profileName = _keyValues.get('profile')
        if _profileName is not None and len(_profileName)>0:
            _profileName = _profileName[0]
        _config = self.getConfig(_profileName)
        _region = _config.get('region')
        return _region

    def _getUserFormat(self):
        _keyValues = self.parser._getKeyValues()
        _profileName = _keyValues.get('profile')
        if _profileName is not None and len(_profileName)>0:
            _profileName = _profileName[0]
        _config = self.getConfig(_profileName)
        _format = _config.get('output')
        return _format


    def _getUserKey(self):
        _keyValues = self.parser._getKeyValues()
        _profileName = _keyValues.get('profile')
        if _profileName is not None and len(_profileName)>0:
            _profileName = _profileName[0]
        _config = self.getConfig(_profileName)
        _userKey = _config.get(QcloudCredentials.qcloud_access_key_id)
        return _userKey

    def _getUserSecret(self):
        _keyValues = self.parser._getKeyValues()
        _profileName = _keyValues.get('profile')
        if _profileName is not None and len(_profileName)>0:
            _profileName = _profileName[0]
        _config = self.getConfig(_profileName)
        _secretId = _config.get(QcloudCredentials.qcloud_access_key_secret)
        return _secretId


class InteractivePrompter(object):
    def __init__(self):
        pass
    def get_value(self, current_value, config_name, prompt_text=''):
        if config_name in ('qcloud_secretid', 'qcloud_secretkey'):
            if current_value != '' and not current_value is None:
                current_value = _mask_value(current_value)
        if PY2:
            response = raw_input("%s [%s]: " % (prompt_text, current_value))
        else:
            response = input("%s [%s]: " % (prompt_text, current_value))
        if response is '':
            response = None
        return response

def _mask_value(current_value):
    if current_value is None:
        return 'None'
    else:
        if len(current_value) <4:
            count = 20 - len(current_value)
            return ('*'* count) + current_value[-4:]
        else:
            return ('*' * 16) + current_value[-4:]

def _createFile(filename):
    namePath = os.path.split(filename)[0]
    if not os.path.isdir(namePath):
        os.makedirs(namePath)
        with os.fdopen(os.open(filename,
                               os.O_WRONLY | os.O_CREAT, 0o600), 'w'):
            pass

class ConfigFileWriter(object):
    def __init__(self):
        pass

    def _updateConfig(self,new_values,config_filename):
        sectionName  = new_values.pop('__section__','default')
        if not os.path.isfile(config_filename):
            _createFile(config_filename)
            self._insertNewSection(sectionName,new_values,config_filename)
            return
        with open(config_filename, 'r') as f:
            contents = f.readlines()
        try:
            if self.hasSectionName(sectionName,contents)[0]:
                self._updateSectionContents(sectionName,contents, new_values)
                with open(config_filename, 'w') as f:
                    f.write(''.join(contents))
            else:
                self._insertNewSection(sectionName,new_values,config_filename)
        finally:
            f.close()



    def hasSectionName(self,sectionName,contents):
        result = False
        start = -1
        _sectionName = '['+sectionName+']'
        for i in range(len(contents)):
            line = contents[i]
            if line.strip():
                if line.strip().startswith(('#', ';')):
                    continue
                if line.strip().find(_sectionName)  >=0:
                    result = True
                    start = i
                    break
        return result,start

    def _updateSectionContents(self,sectionName,contents,new_values):
        new_values = new_values.copy()
        sectionStart = self.hasSectionName(sectionName,contents)[1]
        j = sectionStart
        sectionEnd = self._getSectionEnd(j,contents)
        while j < sectionEnd:
            line = contents[j]
            key = self._getKey(line)
            if key in new_values:
                new_value = new_values[key]
                new_line =  '%s = %s\n' % (key, new_value)
                contents[j] = new_line
                del new_values[key]
            j = j +1
        if new_values:
            if not contents[-1].endswith('\n'):
                contents.append('\n')
            self._insertNewValues(sectionEnd,contents,new_values)

    def _getSectionEnd(self,num,contents):
        k = len(contents)
        num = num +1
        while num <len(contents):
            line = contents[num]
            if line.strip():
                if line.strip().startswith(('#', ';')):
                    num += 1
                    continue
                if line.find('[') >=0 and line.find(']') :
                    return num
            num = num +1
        return k

    def _insertNewValues(self,num,contents,keyValues):
        new_contents = []
        for key, value in list(keyValues.items()):
            new_contents.append('%s = %s\n' % ( key, value))
            del keyValues[key]
        contents.insert(num, ''.join(new_contents))


    def _insertNewSection(self,sectionName,new_values,config_filename,num =0):
        with open(config_filename, 'a') as f:
            f.write('[%s]\n' % sectionName)
            contents = []
            self._insertNewValues(num ,contents,new_values)
            f.write(''.join(contents))


    def _getKey(self,line):
        key = None
        if line is not None and  line.strip().find('=') >0 :
            key = line.split("=",1)[0].strip()
        return key
    def _getValue(self,line):
        value = None
        if line is not None and  line.strip().find('=') >0 :
            value = line.split("=",1)[1].strip()
        return value
    def _getValueInSlice(self,start,end,key,contents):
        value = None
        while start <end:
            line = contents[start]
            start = start+1
            if key ==self._getKey(line):
                value = self._getValue(line)
                return value
        return value

class ConfigValue(object):

    def __init__(self, value, config_type, config_loc):
        self.value = value
        self.config_type = config_type
        self.config_loc = config_loc

    def mask_value(self):
        if self.value is None:
            return
        self.value = _mask_value(self.value)

class ConfigureCommand(object):
    def __init__(self,qcloudConfig= None,prompter =None,configWriter =None):
        from . import handleCmd
        if prompter is None:
            prompter = InteractivePrompter()
        self._prompter = prompter
        if configWriter is None:
            configWriter = ConfigFileWriter()
        self._configWriter = configWriter
        if qcloudConfig is None:
            self.qcloudConfig = QcloudConfig()
        self.handleCmd = handleCmd.handleCmd()

    name2prompt = [
        ('qcloud_secretid', "Qcloud API SecretId"),
        ('qcloud_secretkey', "Qcloud API SecretKey"),
        ('region', "Region Id(gz,hk,ca,sh,shjr,bj,sg)"),
        ('output', "Output Format(json,table,text)"),
    ]

    def _run(self):
        new_values = {}
        all_values = {}
        keyValues = self.qcloudConfig.parser._getKeyValues()
        _profilename = None
        _profilenameList = keyValues.get('profile')
        if _profilenameList is not None:
            if len(_profilenameList) > 0:
                _profilename = _profilenameList[0]
        config = self.qcloudConfig.getConfig(_profilename)
        for name, prompt in self.name2prompt:
            value = config.get(name)
            new_value = self._prompter.get_value(value, name, prompt)
            if new_value is not None and new_value != value:
                new_values[name] = new_value
        config_filename = self.qcloudConfig.getConfigFileName()

        if new_values:
            #self._writeCredsToOssFile(new_values)
            self._writeCredsToFile(new_values,_profilename)
            if _profilename is not None :
                new_values['__section__']=('profile %s' % _profilename)
            self._configWriter._updateConfig(new_values,config_filename)

    def _writeCredsToFile(self,new_values,profilename):
        credential_file_values = {}
        if 'qcloud_secretid' in new_values:
            credential_file_values['qcloud_secretid'] = new_values.pop(
                'qcloud_secretid')
        if 'qcloud_secretkey' in new_values:
            credential_file_values['qcloud_secretkey'] = new_values.pop(
                'qcloud_secretkey')
        creds_filename = self.qcloudConfig.getCredsFileName()
        if credential_file_values:
            if profilename is not None:
                credential_file_values['__section__'] = ('profile %s' % profilename)
            self._configWriter._updateConfig(credential_file_values,creds_filename)


if __name__ == "__main__":
    pass
