# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ResetTiDBPasswordRequest(Request):

    def __init__(self):
        super(ResetTiDBPasswordRequest, self).__init__(
            'tidb', 'qcloudcliV1', 'ResetTiDBPassword', 'tidb.api.qcloud.com')

    def get_instanceId(self):
        return self.get_params().get('instanceId')

    def set_instanceId(self, instanceId):
        self.add_param('instanceId', instanceId)
