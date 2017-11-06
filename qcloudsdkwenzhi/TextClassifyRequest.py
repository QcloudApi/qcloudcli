# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class TextClassifyRequest(Request):

    def __init__(self):
        super(TextClassifyRequest, self).__init__(
            'wenzhi', 'qcloudcliV1', 'TextClassify', 'wenzhi.api.qcloud.com')

    def get_content(self):
        return self.get_params().get('content')

    def set_content(self, content):
        self.add_param('content', content)

    def get_secdNav(self):
        return self.get_params().get('secdNav')

    def set_secdNav(self, secdNav):
        self.add_param('secdNav', secdNav)

    def get_title(self):
        return self.get_params().get('title')

    def set_title(self, title):
        self.add_param('title', title)

    def get_url(self):
        return self.get_params().get('url')

    def set_url(self, url):
        self.add_param('url', url)
