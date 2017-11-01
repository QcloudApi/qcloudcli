# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CdbTdsqlGetBackupTimeRequest(Request):

    def __init__(self):
        super(CdbTdsqlGetBackupTimeRequest, self).__init__(
            'tdsql', 'qcloudcliV1', 'CdbTdsqlGetBackupTime', 'tdsql.api.qcloud.com')

    def get_cdbInstanceIds(self):
        return self.get_params().get('cdbInstanceIds')

    def set_cdbInstanceIds(self, cdbInstanceIds):
        self.add_param('cdbInstanceIds', cdbInstanceIds)
