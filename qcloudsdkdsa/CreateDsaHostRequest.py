# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateDsaHostRequest(Request):

    def __init__(self):
        super(CreateDsaHostRequest, self).__init__(
            'dsa', 'qcloudcliV1', 'CreateDsaHost', 'dsa.api.qcloud.com')

    def get_host(self):
        return self.get_params().get('host')

    def set_host(self, host):
        self.add_param('host', host)

    def get_https(self):
        return self.get_params().get('https')

    def set_https(self, https):
        self.add_param('https', https)

    def get_origin(self):
        return self.get_params().get('origin')

    def set_origin(self, origin):
        self.add_param('origin', origin)

    def get_projectId(self):
        return self.get_params().get('projectId')

    def set_projectId(self, projectId):
        self.add_param('projectId', projectId)

    def get_rspHeader(self):
        return self.get_params().get('rspHeader')

    def set_rspHeader(self, rspHeader):
        self.add_param('rspHeader', rspHeader)
