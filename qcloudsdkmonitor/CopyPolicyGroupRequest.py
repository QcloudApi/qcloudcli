# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CopyPolicyGroupRequest(Request):

    def __init__(self):
        super(CopyPolicyGroupRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'CopyPolicyGroup', 'monitor.api.qcloud.com')

    def get_groupId(self):
        return self.get_params().get('groupId')

    def set_groupId(self, groupId):
        self.add_param('groupId', groupId)

    def get_groupName(self):
        return self.get_params().get('groupName')

    def set_groupName(self, groupName):
        self.add_param('groupName', groupName)

    def get_projectId(self):
        return self.get_params().get('projectId')

    def set_projectId(self, projectId):
        self.add_param('projectId', projectId)
