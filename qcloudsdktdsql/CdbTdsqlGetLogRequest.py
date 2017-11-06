# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CdbTdsqlGetLogRequest(Request):

    def __init__(self):
        super(CdbTdsqlGetLogRequest, self).__init__(
            'tdsql', 'qcloudcliV1', 'CdbTdsqlGetLog', 'tdsql.api.qcloud.com')

    def get_cdbInstanceId(self):
        return self.get_params().get('cdbInstanceId')

    def set_cdbInstanceId(self, cdbInstanceId):
        self.add_param('cdbInstanceId', cdbInstanceId)

    def get_dbMode(self):
        return self.get_params().get('dbMode')

    def set_dbMode(self, dbMode):
        self.add_param('dbMode', dbMode)

    def get_type(self):
        return self.get_params().get('type')

    def set_type(self, type):
        self.add_param('type', type)
