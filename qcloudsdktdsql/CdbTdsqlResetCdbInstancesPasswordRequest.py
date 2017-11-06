# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CdbTdsqlResetCdbInstancesPasswordRequest(Request):

    def __init__(self):
        super(CdbTdsqlResetCdbInstancesPasswordRequest, self).__init__(
            'tdsql', 'qcloudcliV1', 'CdbTdsqlResetCdbInstancesPassword', 'tdsql.api.qcloud.com')

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

    def get_password(self):
        return self.get_params().get('password')

    def set_password(self, password):
        self.add_param('password', password)

    def get_userName(self):
        return self.get_params().get('userName')

    def set_userName(self, userName):
        self.add_param('userName', userName)
