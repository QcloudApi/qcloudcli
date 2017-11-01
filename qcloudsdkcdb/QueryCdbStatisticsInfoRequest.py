# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class QueryCdbStatisticsInfoRequest(Request):

    def __init__(self):
        super(QueryCdbStatisticsInfoRequest, self).__init__(
            'cdb', 'qcloudcliV1', 'QueryCdbStatisticsInfo', 'cdb.api.qcloud.com')

    def get_cdbInstanceId(self):
        return self.get_params().get('cdbInstanceId')

    def set_cdbInstanceId(self, cdbInstanceId):
        self.add_param('cdbInstanceId', cdbInstanceId)
