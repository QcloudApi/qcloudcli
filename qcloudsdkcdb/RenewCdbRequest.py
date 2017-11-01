# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class RenewCdbRequest(Request):

    def __init__(self):
        super(RenewCdbRequest, self).__init__(
            'cdb', 'qcloudcliV1', 'RenewCdb', 'cdb.api.qcloud.com')

    def get_cdbInstanceId(self):
        return self.get_params().get('cdbInstanceId')

    def set_cdbInstanceId(self, cdbInstanceId):
        self.add_param('cdbInstanceId', cdbInstanceId)

    def get_period(self):
        return self.get_params().get('period')

    def set_period(self, period):
        self.add_param('period', period)
