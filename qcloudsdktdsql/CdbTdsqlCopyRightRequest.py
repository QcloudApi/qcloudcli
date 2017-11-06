# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CdbTdsqlCopyRightRequest(Request):

    def __init__(self):
        super(CdbTdsqlCopyRightRequest, self).__init__(
            'tdsql', 'qcloudcliV1', 'CdbTdsqlCopyRight', 'tdsql.api.qcloud.com')

    def get_cdbInstanceId(self):
        return self.get_params().get('cdbInstanceId')

    def set_cdbInstanceId(self, cdbInstanceId):
        self.add_param('cdbInstanceId', cdbInstanceId)

    def get_dbMode(self):
        return self.get_params().get('dbMode')

    def set_dbMode(self, dbMode):
        self.add_param('dbMode', dbMode)

    def get_dstHost(self):
        return self.get_params().get('dstHost')

    def set_dstHost(self, dstHost):
        self.add_param('dstHost', dstHost)

    def get_dstReadOnly(self):
        return self.get_params().get('dstReadOnly')

    def set_dstReadOnly(self, dstReadOnly):
        self.add_param('dstReadOnly', dstReadOnly)

    def get_dstUserName(self):
        return self.get_params().get('dstUserName')

    def set_dstUserName(self, dstUserName):
        self.add_param('dstUserName', dstUserName)

    def get_srcHost(self):
        return self.get_params().get('srcHost')

    def set_srcHost(self, srcHost):
        self.add_param('srcHost', srcHost)

    def get_srcReadOnly(self):
        return self.get_params().get('srcReadOnly')

    def set_srcReadOnly(self, srcReadOnly):
        self.add_param('srcReadOnly', srcReadOnly)

    def get_srcUserName(self):
        return self.get_params().get('srcUserName')

    def set_srcUserName(self, srcUserName):
        self.add_param('srcUserName', srcUserName)
