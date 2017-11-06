# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CdbTdsqlDeleteUserRequest(Request):

    def __init__(self):
        super(CdbTdsqlDeleteUserRequest, self).__init__(
            'tdsql', 'qcloudcliV1', 'CdbTdsqlDeleteUser', 'tdsql.api.qcloud.com')

    def get_cdbInstanceId(self):
        return self.get_params().get('cdbInstanceId')

    def set_cdbInstanceId(self, cdbInstanceId):
        self.add_param('cdbInstanceId', cdbInstanceId)

    def get_dbMode(self):
        return self.get_params().get('dbMode')

    def set_dbMode(self, dbMode):
        self.add_param('dbMode', dbMode)

    def get_host(self):
        return self.get_params().get('host')

    def set_host(self, host):
        self.add_param('host', host)

    def get_userName(self):
        return self.get_params().get('userName')

    def set_userName(self, userName):
        self.add_param('userName', userName)
