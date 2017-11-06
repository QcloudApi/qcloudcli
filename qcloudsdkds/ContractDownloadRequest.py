# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ContractDownloadRequest(Request):

    def __init__(self):
        super(ContractDownloadRequest, self).__init__(
            'ds', 'qcloudcliV1', 'ContractDownload', 'ds.api.qcloud.com')

    def get_contractNo(self):
        return self.get_params().get('contractNo')

    def set_contractNo(self, contractNo):
        self.add_param('contractNo', contractNo)

    def get_module(self):
        return self.get_params().get('module')

    def set_module(self, module):
        self.add_param('module', module)

    def get_operation(self):
        return self.get_params().get('operation')

    def set_operation(self, operation):
        self.add_param('operation', operation)
