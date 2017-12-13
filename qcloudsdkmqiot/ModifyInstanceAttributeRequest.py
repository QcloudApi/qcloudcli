# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyInstanceAttributeRequest(Request):

    def __init__(self):
        super(ModifyInstanceAttributeRequest, self).__init__(
            'mqiot', 'qcloudcliV1', 'ModifyInstanceAttribute', 'mqiot.api.qcloud.com')

    def get_instanceId(self):
        return self.get_params().get('instanceId')

    def set_instanceId(self, instanceId):
        self.add_param('instanceId', instanceId)

    def get_instanceName(self):
        return self.get_params().get('instanceName')

    def set_instanceName(self, instanceName):
        self.add_param('instanceName', instanceName)
