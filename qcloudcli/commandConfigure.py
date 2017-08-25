from . import showHelp
from . import handleData

class commandConfigure:
    def __init__(self):

        self.main_options = ['output', 'SecretId', 'SecretKey']
        self.helper = showHelp.showHelp()
        self.open_api_headler = handleData.handleData()

    def getExtensionOptions(self, cmd, operation):
        if cmd is None or operation is None:
            return None
        if operation in handleData.version_cmds:
            return None
        return None


    def showExtensionOperationHelp(self, cmd, operation):
        parameterList = list()
        self.helper.showParameterError(cmd, operation, parameterList)

    def appendList(self, parameterList, optionList):
        for item in optionList:
            parameterList.append(item)


if __name__ == '__main__':
    pass
