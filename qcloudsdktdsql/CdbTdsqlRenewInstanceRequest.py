# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CdbTdsqlRenewInstanceRequest(Request):

    def __init__(self):
        super(CdbTdsqlRenewInstanceRequest, self).__init__(
            'tdsql', 'qcloudcliV1', 'CdbTdsqlRenewInstance', 'tdsql.api.qcloud.com')

    def get_cdbInstanceUuid(self):
        return self.get_params().get('cdbInstanceUuid')

    def set_cdbInstanceUuid(self, cdbInstanceUuid):
        self.add_param('cdbInstanceUuid', cdbInstanceUuid)

    def get_dbType(self):
        return self.get_params().get('dbType')

    def set_dbType(self, dbType):
        self.add_param('dbType', dbType)

    def get_period(self):
        return self.get_params().get('period')

    def set_period(self, period):
        self.add_param('period', period)
