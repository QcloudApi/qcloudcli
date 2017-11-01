# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class RefreshCdnUrlRequest(Request):

    def __init__(self):
        super(RefreshCdnUrlRequest, self).__init__(
            'cdn', 'qcloudcliV1', 'RefreshCdnUrl', 'cdn.api.qcloud.com')

    def get_urls(self):
        return self.get_params().get('urls')

    def set_urls(self, urls):
        self.add_param('urls', urls)
