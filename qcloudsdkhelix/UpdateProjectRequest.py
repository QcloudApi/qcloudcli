# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class UpdateProjectRequest(Request):

    def __init__(self):
        super(UpdateProjectRequest, self).__init__(
            'helix', 'qcloudcliV1', 'UpdateProject', 'helix.api.qcloud.com')

    def get_desc(self):
        return self.get_params().get('desc')

    def set_desc(self, desc):
        self.add_param('desc', desc)

    def get_name(self):
        return self.get_params().get('name')

    def set_name(self, name):
        self.add_param('name', name)

    def get_projectId(self):
        return self.get_params().get('projectId')

    def set_projectId(self, projectId):
        self.add_param('projectId', projectId)
