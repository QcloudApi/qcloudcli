# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class TextSentimentRequest(Request):

    def __init__(self):
        super(TextSentimentRequest, self).__init__(
            'wenzhi', 'qcloudcliV1', 'TextSentiment', 'wenzhi.api.qcloud.com')

    def get_content(self):
        return self.get_params().get('content')

    def set_content(self, content):
        self.add_param('content', content)

    def get_type(self):
        return self.get_params().get('type')

    def set_type(self, type):
        self.add_param('type', type)
