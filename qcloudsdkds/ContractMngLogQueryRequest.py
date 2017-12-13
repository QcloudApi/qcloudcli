# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ContractMngLogQueryRequest(Request):

    def __init__(self):
        super(ContractMngLogQueryRequest, self).__init__(
            'ds', 'qcloudcliV1', 'ContractMngLogQuery', 'ds.api.qcloud.com')

    def get_contractResId(self):
        return self.get_params().get('contractResId')

    def set_contractResId(self, contractResId):
        self.add_param('contractResId', contractResId)

    def get_download(self):
        return self.get_params().get('download')

    def set_download(self, download):
        self.add_param('download', download)

    def get_filtering(self):
        return self.get_params().get('filtering')

    def set_filtering(self, filtering):
        self.add_param('filtering', filtering)

    def get_module(self):
        return self.get_params().get('module')

    def set_module(self, module):
        self.add_param('module', module)

    def get_operation(self):
        return self.get_params().get('operation')

    def set_operation(self, operation):
        self.add_param('operation', operation)

    def get_paging(self):
        return self.get_params().get('paging')

    def set_paging(self, paging):
        self.add_param('paging', paging)

    def get_sorting(self):
        return self.get_params().get('sorting')

    def set_sorting(self, sorting):
        self.add_param('sorting', sorting)
