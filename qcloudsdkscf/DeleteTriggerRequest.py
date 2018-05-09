# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteTriggerRequest(Request):

    def __init__(self):
        super(DeleteTriggerRequest, self).__init__(
            'scf', 'qcloudcliV1', 'DeleteTrigger', 'scf.api.qcloud.com')

    def get_functionName(self):
        return self.get_params().get('functionName')

    def set_functionName(self, functionName):
        self.add_param('functionName', functionName)

    def get_triggerDesc(self):
        return self.get_params().get('triggerDesc')

    def set_triggerDesc(self, triggerDesc):
        self.add_param('triggerDesc', triggerDesc)

    def get_triggerName(self):
        return self.get_params().get('triggerName')

    def set_triggerName(self, triggerName):
        self.add_param('triggerName', triggerName)

    def get_type(self):
        return self.get_params().get('type')

    def set_type(self, type):
        self.add_param('type', type)

    def get_version(self):
        return self.get_params().get('version')

    def set_version(self, version):
        self.add_param('version', version)
