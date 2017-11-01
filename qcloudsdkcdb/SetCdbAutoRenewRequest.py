# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class SetCdbAutoRenewRequest(Request):

    def __init__(self):
        super(SetCdbAutoRenewRequest, self).__init__(
            'cdb', 'qcloudcliV1', 'SetCdbAutoRenew', 'cdb.api.qcloud.com')

    def get_cdbInstanceId(self):
        return self.get_params().get('cdbInstanceId')

    def set_cdbInstanceId(self, cdbInstanceId):
        self.add_param('cdbInstanceId', cdbInstanceId)

    def get_isAutoRenew(self):
        return self.get_params().get('isAutoRenew')

    def set_isAutoRenew(self, isAutoRenew):
        self.add_param('isAutoRenew', isAutoRenew)
