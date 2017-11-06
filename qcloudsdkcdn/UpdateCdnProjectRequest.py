# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class UpdateCdnProjectRequest(Request):

    def __init__(self):
        super(UpdateCdnProjectRequest, self).__init__(
            'cdn', 'qcloudcliV1', 'UpdateCdnProject', 'cdn.api.qcloud.com')

    def get_hostId(self):
        return self.get_params().get('hostId')

    def set_hostId(self, hostId):
        self.add_param('hostId', hostId)

    def get_projectId(self):
        return self.get_params().get('projectId')

    def set_projectId(self, projectId):
        self.add_param('projectId', projectId)
