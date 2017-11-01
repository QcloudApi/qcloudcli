# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyCdbInstanceNameRequest(Request):

    def __init__(self):
        super(ModifyCdbInstanceNameRequest, self).__init__(
            'cdb', 'qcloudcliV1', 'ModifyCdbInstanceName', 'cdb.api.qcloud.com')

    def get_cdbInstanceId(self):
        return self.get_params().get('cdbInstanceId')

    def set_cdbInstanceId(self, cdbInstanceId):
        self.add_param('cdbInstanceId', cdbInstanceId)

    def get_cdbInstanceName(self):
        return self.get_params().get('cdbInstanceName')

    def set_cdbInstanceName(self, cdbInstanceName):
        self.add_param('cdbInstanceName', cdbInstanceName)
