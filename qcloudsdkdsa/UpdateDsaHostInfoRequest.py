# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class UpdateDsaHostInfoRequest(Request):

    def __init__(self):
        super(UpdateDsaHostInfoRequest, self).__init__(
            'dsa', 'qcloudcliV1', 'UpdateDsaHostInfo', 'dsa.api.qcloud.com')

    def get_hostId(self):
        return self.get_params().get('hostId')

    def set_hostId(self, hostId):
        self.add_param('hostId', hostId)

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
