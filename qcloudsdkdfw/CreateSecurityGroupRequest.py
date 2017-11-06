# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateSecurityGroupRequest(Request):

    def __init__(self):
        super(CreateSecurityGroupRequest, self).__init__(
            'dfw', 'qcloudcliV1', 'CreateSecurityGroup', 'dfw.api.qcloud.com')

    def get_projectId(self):
        return self.get_params().get('projectId')

    def set_projectId(self, projectId):
        self.add_param('projectId', projectId)

    def get_sgName(self):
        return self.get_params().get('sgName')

    def set_sgName(self, sgName):
        self.add_param('sgName', sgName)

    def get_sgRemark(self):
        return self.get_params().get('sgRemark')

    def set_sgRemark(self, sgRemark):
        self.add_param('sgRemark', sgRemark)
