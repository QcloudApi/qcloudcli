# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ContentTranscodeRequest(Request):

    def __init__(self):
        super(ContentTranscodeRequest, self).__init__(
            'wenzhi', 'qcloudcliV1', 'ContentTranscode', 'wenzhi.api.qcloud.com')

    def get_tohtml(self):
        return self.get_params().get('tohtml')

    def set_tohtml(self, tohtml):
        self.add_param('tohtml', tohtml)

    def get_url(self):
        return self.get_params().get('url')

    def set_url(self, url):
        self.add_param('url', url)
