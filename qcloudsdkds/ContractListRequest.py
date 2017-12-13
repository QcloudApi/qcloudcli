# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ContractListRequest(Request):

    def __init__(self):
        super(ContractListRequest, self).__init__(
            'ds', 'qcloudcliV1', 'ContractList', 'ds.api.qcloud.com')

    def get_beginTime(self):
        return self.get_params().get('beginTime')

    def set_beginTime(self, beginTime):
        self.add_param('beginTime', beginTime)

    def get_download(self):
        return self.get_params().get('download')

    def set_download(self, download):
        self.add_param('download', download)

    def get_endTime(self):
        return self.get_params().get('endTime')

    def set_endTime(self, endTime):
        self.add_param('endTime', endTime)

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
