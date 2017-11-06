# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeCdbSlowQueryLogRequest(Request):

    def __init__(self):
        super(DescribeCdbSlowQueryLogRequest, self).__init__(
            'cdb', 'qcloudcliV1', 'DescribeCdbSlowQueryLog', 'cdb.api.qcloud.com')

    def get_cdbInstanceId(self):
        return self.get_params().get('cdbInstanceId')

    def set_cdbInstanceId(self, cdbInstanceId):
        self.add_param('cdbInstanceId', cdbInstanceId)

    def get_date(self):
        return self.get_params().get('date')

    def set_date(self, date):
        self.add_param('date', date)

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)
