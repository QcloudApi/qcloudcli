# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetBackupDatabaseTableListRequest(Request):

    def __init__(self):
        super(GetBackupDatabaseTableListRequest, self).__init__(
            'cdb', 'qcloudcliV1', 'GetBackupDatabaseTableList', 'cdb.api.qcloud.com')

    def get_cdbInstanceId(self):
        return self.get_params().get('cdbInstanceId')

    def set_cdbInstanceId(self, cdbInstanceId):
        self.add_param('cdbInstanceId', cdbInstanceId)

    def get_date(self):
        return self.get_params().get('date')

    def set_date(self, date):
        self.add_param('date', date)
