# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CdbTdsqlSetBackupTimeRequest(Request):

    def __init__(self):
        super(CdbTdsqlSetBackupTimeRequest, self).__init__(
            'tdsql', 'qcloudcliV1', 'CdbTdsqlSetBackupTime', 'tdsql.api.qcloud.com')

    def get_cdbInstanceId(self):
        return self.get_params().get('cdbInstanceId')

    def set_cdbInstanceId(self, cdbInstanceId):
        self.add_param('cdbInstanceId', cdbInstanceId)

    def get_eBackupTime(self):
        return self.get_params().get('eBackupTime')

    def set_eBackupTime(self, eBackupTime):
        self.add_param('eBackupTime', eBackupTime)

    def get_sBackupTime(self):
        return self.get_params().get('sBackupTime')

    def set_sBackupTime(self, sBackupTime):
        self.add_param('sBackupTime', sBackupTime)
