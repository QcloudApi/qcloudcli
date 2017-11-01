# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class TemplateDetailRequest(Request):

    def __init__(self):
        super(TemplateDetailRequest, self).__init__(
            'ds', 'qcloudcliV1', 'TemplateDetail', 'ds.api.qcloud.com')

    def get_module(self):
        return self.get_params().get('module')

    def set_module(self, module):
        self.add_param('module', module)

    def get_operation(self):
        return self.get_params().get('operation')

    def set_operation(self, operation):
        self.add_param('operation', operation)

    def get_tplResId(self):
        return self.get_params().get('tplResId')

    def set_tplResId(self, tplResId):
        self.add_param('tplResId', tplResId)
