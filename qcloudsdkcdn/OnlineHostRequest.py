# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class OnlineHostRequest(Request):

    def __init__(self):
        super(OnlineHostRequest, self).__init__(
            'cdn', 'qcloudcliV1', 'OnlineHost', 'cdn.api.qcloud.com')

    def get_host(self):
        return self.get_params().get('host')

    def set_host(self, host):
        self.add_param('host', host)

    def get_hostId(self):
        return self.get_params().get('hostId')

    def set_hostId(self, hostId):
        self.add_param('hostId', hostId)
