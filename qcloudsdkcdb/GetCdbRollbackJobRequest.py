# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetCdbRollbackJobRequest(Request):

    def __init__(self):
        super(GetCdbRollbackJobRequest, self).__init__(
            'cdb', 'qcloudcliV1', 'GetCdbRollbackJob', 'cdb.api.qcloud.com')

    def get_cdbInstanceId(self):
        return self.get_params().get('cdbInstanceId')

    def set_cdbInstanceId(self, cdbInstanceId):
        self.add_param('cdbInstanceId', cdbInstanceId)

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)
