# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeCvmAgentStatusRequest(Request):

    def __init__(self):
        super(DescribeCvmAgentStatusRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'DescribeCvmAgentStatus', 'monitor.api.qcloud.com')

    def get_unInstanceId(self):
        return self.get_params().get('unInstanceId')

    def set_unInstanceId(self, unInstanceId):
        self.add_param('unInstanceId', unInstanceId)
