# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CdbMysqlInitRequest(Request):

    def __init__(self):
        super(CdbMysqlInitRequest, self).__init__(
            'cdb', 'qcloudcliV1', 'CdbMysqlInit', 'cdb.api.qcloud.com')

    def get_cdbInstanceId(self):
        return self.get_params().get('cdbInstanceId')

    def set_cdbInstanceId(self, cdbInstanceId):
        self.add_param('cdbInstanceId', cdbInstanceId)

    def get_charset(self):
        return self.get_params().get('charset')

    def set_charset(self, charset):
        self.add_param('charset', charset)

    def get_lowerCaseTableNames(self):
        return self.get_params().get('lowerCaseTableNames')

    def set_lowerCaseTableNames(self, lowerCaseTableNames):
        self.add_param('lowerCaseTableNames', lowerCaseTableNames)

    def get_password(self):
        return self.get_params().get('password')

    def set_password(self, password):
        self.add_param('password', password)

    def get_port(self):
        return self.get_params().get('port')

    def set_port(self, port):
        self.add_param('port', port)
