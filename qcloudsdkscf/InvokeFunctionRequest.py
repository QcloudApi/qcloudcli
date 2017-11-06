# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class InvokeFunctionRequest(Request):

    def __init__(self):
        super(InvokeFunctionRequest, self).__init__(
            'scf', 'qcloudcliV1', 'InvokeFunction', 'scf.api.qcloud.com')

    def get_functionName(self):
        return self.get_params().get('functionName')

    def set_functionName(self, functionName):
        self.add_param('functionName', functionName)

    def get_invokeType(self):
        return self.get_params().get('invokeType')

    def set_invokeType(self, invokeType):
        self.add_param('invokeType', invokeType)

    def get_logType(self):
        return self.get_params().get('logType')

    def set_logType(self, logType):
        self.add_param('logType', logType)

    def get_param(self):
        return self.get_params().get('param')

    def set_param(self, param):
        self.add_param('param', param)

    def get_version(self):
        return self.get_params().get('version')

    def set_version(self, version):
        self.add_param('version', version)
