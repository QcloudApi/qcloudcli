# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreatePolicyGroupRequest(Request):

    def __init__(self):
        super(CreatePolicyGroupRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'CreatePolicyGroup', 'monitor.api.qcloud.com')

    def get_conditions(self):
        return self.get_params().get('conditions')

    def set_conditions(self, conditions):
        self.add_param('conditions', conditions)

    def get_groupName(self):
        return self.get_params().get('groupName')

    def set_groupName(self, groupName):
        self.add_param('groupName', groupName)

    def get_projectId(self):
        return self.get_params().get('projectId')

    def set_projectId(self, projectId):
        self.add_param('projectId', projectId)

    def get_viewName(self):
        return self.get_params().get('viewName')

    def set_viewName(self, viewName):
        self.add_param('viewName', viewName)
