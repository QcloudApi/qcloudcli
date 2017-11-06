# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class LexicalAnalysisRequest(Request):

    def __init__(self):
        super(LexicalAnalysisRequest, self).__init__(
            'wenzhi', 'qcloudcliV1', 'LexicalAnalysis', 'wenzhi.api.qcloud.com')

    def get_code(self):
        return self.get_params().get('code')

    def set_code(self, code):
        self.add_param('code', code)

    def get_text(self):
        return self.get_params().get('text')

    def set_text(self, text):
        self.add_param('text', text)

    def get_type(self):
        return self.get_params().get('type')

    def set_type(self, type):
        self.add_param('type', type)
