# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CdbTdsqlExpandInstanceRequest(Request):

    def __init__(self):
        super(CdbTdsqlExpandInstanceRequest, self).__init__(
            'tdsql', 'qcloudcliV1', 'CdbTdsqlExpandInstance', 'tdsql.api.qcloud.com')

    def get_cdbInstanceUuid(self):
        return self.get_params().get('cdbInstanceUuid')

    def set_cdbInstanceUuid(self, cdbInstanceUuid):
        self.add_param('cdbInstanceUuid', cdbInstanceUuid)

    def get_curDeadline(self):
        return self.get_params().get('curDeadline')

    def set_curDeadline(self, curDeadline):
        self.add_param('curDeadline', curDeadline)

    def get_dbType(self):
        return self.get_params().get('dbType')

    def set_dbType(self, dbType):
        self.add_param('dbType', dbType)

    def get_newDbType(self):
        return self.get_params().get('newDbType')

    def set_newDbType(self, newDbType):
        self.add_param('newDbType', newDbType)
