# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteFunctionRequest(Request):

    def __init__(self):
        super(DeleteFunctionRequest, self).__init__(
            'scf', 'qcloudcliV1', 'DeleteFunction', 'scf.api.qcloud.com')

    def get_functionName(self):
        return self.get_params().get('functionName')

    def set_functionName(self, functionName):
        self.add_param('functionName', functionName)

    def get_namespace(self):
        return self.get_params().get('namespace')

    def set_namespace(self, namespace):
        self.add_param('namespace', namespace)

    def get_version(self):
        return self.get_params().get('version')

    def set_version(self, version):
        self.add_param('version', version)
