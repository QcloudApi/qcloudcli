# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ContractDownloadRequest(Request):

    def __init__(self):
        super(ContractDownloadRequest, self).__init__(
            'ds', 'qcloudcliV1', 'ContractDownload', 'ds.api.qcloud.com')

    def get_contractBakDel(self):
        return self.get_params().get('contractBakDel')

    def set_contractBakDel(self, contractBakDel):
        self.add_param('contractBakDel', contractBakDel)

    def get_contractResId(self):
        return self.get_params().get('contractResId')

    def set_contractResId(self, contractResId):
        self.add_param('contractResId', contractResId)

    def get_module(self):
        return self.get_params().get('module')

    def set_module(self, module):
        self.add_param('module', module)

    def get_operation(self):
        return self.get_params().get('operation')

    def set_operation(self, operation):
        self.add_param('operation', operation)
