# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ResetCdbInstancesPasswordRequest(Request):

    def __init__(self):
        super(ResetCdbInstancesPasswordRequest, self).__init__(
            'cdb', 'qcloudcliV1', 'ResetCdbInstancesPassword', 'cdb.api.qcloud.com')

    def get_cdbInstanceId(self):
        return self.get_params().get('cdbInstanceId')

    def set_cdbInstanceId(self, cdbInstanceId):
        self.add_param('cdbInstanceId', cdbInstanceId)

    def get_password(self):
        return self.get_params().get('password')

    def set_password(self, password):
        self.add_param('password', password)
