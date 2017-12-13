# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetInstanceAttributeRequest(Request):

    def __init__(self):
        super(GetInstanceAttributeRequest, self).__init__(
            'mqiot', 'qcloudcliV1', 'GetInstanceAttribute', 'mqiot.api.qcloud.com')

    def get_instanceId(self):
        return self.get_params().get('instanceId')

    def set_instanceId(self, instanceId):
        self.add_param('instanceId', instanceId)
