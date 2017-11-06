# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class AddProjectRequest(Request):

    def __init__(self):
        super(AddProjectRequest, self).__init__(
            'account', 'qcloudcliV1', 'AddProject', 'account.api.qcloud.com')

    def get_projectDesc(self):
        return self.get_params().get('projectDesc')

    def set_projectDesc(self, projectDesc):
        self.add_param('projectDesc', projectDesc)

    def get_projectName(self):
        return self.get_params().get('projectName')

    def set_projectName(self, projectName):
        self.add_param('projectName', projectName)
