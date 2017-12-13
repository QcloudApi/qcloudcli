# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class TemplateDeleteRequest(Request):

    def __init__(self):
        super(TemplateDeleteRequest, self).__init__(
            'ds', 'qcloudcliV1', 'TemplateDelete', 'ds.api.qcloud.com')

    def get_module(self):
        return self.get_params().get('module')

    def set_module(self, module):
        self.add_param('module', module)

    def get_operation(self):
        return self.get_params().get('operation')

    def set_operation(self, operation):
        self.add_param('operation', operation)

    def get_templateList(self):
        return self.get_params().get('templateList')

    def set_templateList(self, templateList):
        self.add_param('templateList', templateList)
