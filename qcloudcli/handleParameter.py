import sys


class handleParameter():
    def __init__(self):
        self.args = []
        for arg in sys.argv[1:]:
            if sys.platform == 'win32' and sys.stdin.encoding == 'cp936':
                arg = arg.decode('gbk')
            self.args.append(arg)

    def getAction(self):
        if self.args.__len__() >= 2:
            return self.args[1]

    def _getCommand(self):
        if self.args.__len__() >= 1:
            return self.args[0]

    def _getOperations(self):
        operations = []
        i = 1
        _len = self.args.__len__()
        if _len >= 2:
            while i < _len:
                if self.args[i].strip().find('--'):
                    operations.append(self.args[i])
                else:
                    break
                i = i+1
        if len(operations):
            return operations
        else:
            return None

    def _getKeyValues(self):
        keyValues = dict()
        argslen = len(self.args)
        if argslen >= 2:
            current = 1
            while current < argslen:
                if self.args[current].strip().startswith('--'):
                    start = current + 1
                    if '=' in self.args[current].strip():
                        a = self.args[current].strip().split('=', 2)[0]
                        b = self.args[current].strip().split('=', 2)[1]
                        self.args[current] = a
                        self.args.insert(current + 1, b)
                        argslen = len(self.args)
                    key = self.args[current].strip()
                    values = list()
                    length = len(self.args)
                    while (start < length and
                           not self.args[start].strip().startswith('--')):
                        values.append(self.args[start].strip())
                        start = start + 1
                    keyValues[key] = values
                    current = start
                else:
                    current = current+1
        keys = list(keyValues.keys())
        result = dict()
        for key in keys:
            value = keyValues.get(key)
            key = key.replace('--', '')
            result[key] = value
        return result

    def getUserDefinedOutPutFormat(self, keyValues):
        keys = list(keyValues.keys())
        for key in keys:
            if key == 'output':
                return keyValues.get(key)
        return None

    def getTempKeyAndSecret(self):
        keyValues = dict()
        len = self.args.__len__()
        keystr = "--SecretId"
        secretstr = "--SecretKey"
        _key = None
        _secret = None
        if len >= 3:
            for index in range(2, len):
                currentValue = self.args[index]
                if currentValue.find('--') >= 0:
                    index = index+1
                    values = list()
                    while index < len and self.args[index].find('--') < 0:
                        values.append(self.args[index])
                        index = index + 1
                    keyValues[currentValue] = values
        if keystr in keyValues and keyValues[keystr].__len__() > 0:
            _key = keyValues[keystr][0]
        if secretstr in keyValues and keyValues[secretstr].__len__() > 0:
            _secret = keyValues[secretstr][0]
        return _key, _secret

    def getAllExtensionCommands(self):
        cmds = list()
        cmds = ['help', '-h', '--help', ]
        return cmds

    def _getOpenApiKeyValues(self, map):
        keys = list(map.keys())
        newMap = dict()
        for key in keys:
            value = map.get(key)
            key = key.replace('--', '')
            newMap[key] = value
        return newMap

    def getExtensionKeyValues(self, map):
        pass
