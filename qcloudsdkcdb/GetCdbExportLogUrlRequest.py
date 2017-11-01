# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetCdbExportLogUrlRequest(Request):

    def __init__(self):
        super(GetCdbExportLogUrlRequest, self).__init__(
            'cdb', 'qcloudcliV1', 'GetCdbExportLogUrl', 'cdb.api.qcloud.com')

    def get_cdbInstanceId(self):
        return self.get_params().get('cdbInstanceId')

    def set_cdbInstanceId(self, cdbInstanceId):
        self.add_param('cdbInstanceId', cdbInstanceId)

    def get_type(self):
        return self.get_params().get('type')

    def set_type(self, type):
        self.add_param('type', type)
