# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CdbTdsqlSetRightRequest(Request):

    def __init__(self):
        super(CdbTdsqlSetRightRequest, self).__init__(
            'tdsql', 'qcloudcliV1', 'CdbTdsqlSetRight', 'tdsql.api.qcloud.com')

    def get_cdbInstanceId(self):
        return self.get_params().get('cdbInstanceId')

    def set_cdbInstanceId(self, cdbInstanceId):
        self.add_param('cdbInstanceId', cdbInstanceId)

    def get_colName(self):
        return self.get_params().get('colName')

    def set_colName(self, colName):
        self.add_param('colName', colName)

    def get_dbMode(self):
        return self.get_params().get('dbMode')

    def set_dbMode(self, dbMode):
        self.add_param('dbMode', dbMode)

    def get_dbName(self):
        return self.get_params().get('dbName')

    def set_dbName(self, dbName):
        self.add_param('dbName', dbName)

    def get_host(self):
        return self.get_params().get('host')

    def set_host(self, host):
        self.add_param('host', host)

    def get_object(self):
        return self.get_params().get('object')

    def set_object(self, object):
        self.add_param('object', object)

    def get_readOnly(self):
        return self.get_params().get('readOnly')

    def set_readOnly(self, readOnly):
        self.add_param('readOnly', readOnly)

    def get_rights(self):
        return self.get_params().get('rights')

    def set_rights(self, rights):
        self.add_param('rights', rights)

    def get_type(self):
        return self.get_params().get('type')

    def set_type(self, type):
        self.add_param('type', type)

    def get_userName(self):
        return self.get_params().get('userName')

    def set_userName(self, userName):
        self.add_param('userName', userName)
