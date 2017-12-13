# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class TemplateDownloadRequest(Request):

    def __init__(self):
        super(TemplateDownloadRequest, self).__init__(
            'ds', 'qcloudcliV1', 'TemplateDownload', 'ds.api.qcloud.com')

    def get_module(self):
        return self.get_params().get('module')

    def set_module(self, module):
        self.add_param('module', module)

    def get_operation(self):
        return self.get_params().get('operation')

    def set_operation(self, operation):
        self.add_param('operation', operation)

    def get_templateResId(self):
        return self.get_params().get('templateResId')

    def set_templateResId(self, templateResId):
        self.add_param('templateResId', templateResId)
