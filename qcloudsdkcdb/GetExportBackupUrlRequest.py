# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetExportBackupUrlRequest(Request):

    def __init__(self):
        super(GetExportBackupUrlRequest, self).__init__(
            'cdb', 'qcloudcliV1', 'GetExportBackupUrl', 'cdb.api.qcloud.com')

    def get_cdbInstanceId(self):
        return self.get_params().get('cdbInstanceId')

    def set_cdbInstanceId(self, cdbInstanceId):
        self.add_param('cdbInstanceId', cdbInstanceId)

    def get_date(self):
        return self.get_params().get('date')

    def set_date(self, date):
        self.add_param('date', date)

    def get_dbTableList(self):
        return self.get_params().get('dbTableList')

    def set_dbTableList(self, dbTableList):
        self.add_param('dbTableList', dbTableList)
