# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class UpdateCdnHostRequest(Request):

    def __init__(self):
        super(UpdateCdnHostRequest, self).__init__(
            'cdn', 'qcloudcliV1', 'UpdateCdnHost', 'cdn.api.qcloud.com')

    def get_host(self):
        return self.get_params().get('host')

    def set_host(self, host):
        self.add_param('host', host)

    def get_hostId(self):
        return self.get_params().get('hostId')

    def set_hostId(self, hostId):
        self.add_param('hostId', hostId)

    def get_origin(self):
        return self.get_params().get('origin')

    def set_origin(self, origin):
        self.add_param('origin', origin)
