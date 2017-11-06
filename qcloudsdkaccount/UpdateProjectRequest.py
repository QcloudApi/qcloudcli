# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class UpdateProjectRequest(Request):

    def __init__(self):
        super(UpdateProjectRequest, self).__init__(
            'account', 'qcloudcliV1', 'UpdateProject', 'account.api.qcloud.com')

    def get_projectDesc(self):
        return self.get_params().get('projectDesc')

    def set_projectDesc(self, projectDesc):
        self.add_param('projectDesc', projectDesc)

    def get_projectId(self):
        return self.get_params().get('projectId')

    def set_projectId(self, projectId):
        self.add_param('projectId', projectId)

    def get_projectName(self):
        return self.get_params().get('projectName')

    def set_projectName(self, projectName):
        self.add_param('projectName', projectName)
