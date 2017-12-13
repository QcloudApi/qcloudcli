# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class TemplateCreateRequest(Request):

    def __init__(self):
        super(TemplateCreateRequest, self).__init__(
            'ds', 'qcloudcliV1', 'TemplateCreate', 'ds.api.qcloud.com')

    def get_module(self):
        return self.get_params().get('module')

    def set_module(self, module):
        self.add_param('module', module)

    def get_name(self):
        return self.get_params().get('name')

    def set_name(self, name):
        self.add_param('name', name)

    def get_operation(self):
        return self.get_params().get('operation')

    def set_operation(self, operation):
        self.add_param('operation', operation)

    def get_signLocationKeyInfo(self):
        return self.get_params().get('signLocationKeyInfo')

    def set_signLocationKeyInfo(self, signLocationKeyInfo):
        self.add_param('signLocationKeyInfo', signLocationKeyInfo)

    def get_templateFileURL(self):
        return self.get_params().get('templateFileURL')

    def set_templateFileURL(self, templateFileURL):
        self.add_param('templateFileURL', templateFileURL)

    def get_textKeyInfo(self):
        return self.get_params().get('textKeyInfo')

    def set_textKeyInfo(self, textKeyInfo):
        self.add_param('textKeyInfo', textKeyInfo)
