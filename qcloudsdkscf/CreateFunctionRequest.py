# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateFunctionRequest(Request):

    def __init__(self):
        super(CreateFunctionRequest, self).__init__(
            'scf', 'qcloudcliV1', 'CreateFunction', 'scf.api.qcloud.com')

    def get_code(self):
        return self.get_params().get('code')

    def set_code(self, code):
        self.add_param('code', code)

    def get_codeObject(self):
        return self.get_params().get('codeObject')

    def set_codeObject(self, codeObject):
        self.add_param('codeObject', codeObject)

    def get_description(self):
        return self.get_params().get('description')

    def set_description(self, description):
        self.add_param('description', description)

    def get_functionName(self):
        return self.get_params().get('functionName')

    def set_functionName(self, functionName):
        self.add_param('functionName', functionName)

    def get_handler(self):
        return self.get_params().get('handler')

    def set_handler(self, handler):
        self.add_param('handler', handler)

    def get_memorySize(self):
        return self.get_params().get('memorySize')

    def set_memorySize(self, memorySize):
        self.add_param('memorySize', memorySize)

    def get_runtime(self):
        return self.get_params().get('runtime')

    def set_runtime(self, runtime):
        self.add_param('runtime', runtime)

    def get_timeout(self):
        return self.get_params().get('timeout')

    def set_timeout(self, timeout):
        self.add_param('timeout', timeout)
