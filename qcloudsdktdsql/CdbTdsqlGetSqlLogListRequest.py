# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CdbTdsqlGetSqlLogListRequest(Request):

    def __init__(self):
        super(CdbTdsqlGetSqlLogListRequest, self).__init__(
            'tdsql', 'qcloudcliV1', 'CdbTdsqlGetSqlLogList', 'tdsql.api.qcloud.com')

    def get_cdbInstanceId(self):
        return self.get_params().get('cdbInstanceId')

    def set_cdbInstanceId(self, cdbInstanceId):
        self.add_param('cdbInstanceId', cdbInstanceId)

    def get_count(self):
        return self.get_params().get('count')

    def set_count(self, count):
        self.add_param('count', count)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)
