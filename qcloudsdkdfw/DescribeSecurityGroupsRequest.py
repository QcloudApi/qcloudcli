# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeSecurityGroupsRequest(Request):

    def __init__(self):
        super(DescribeSecurityGroupsRequest, self).__init__(
            'dfw', 'qcloudcliV1', 'DescribeSecurityGroups', 'dfw.api.qcloud.com')

    def get_instanceId(self):
        return self.get_params().get('instanceId')

    def set_instanceId(self, instanceId):
        self.add_param('instanceId', instanceId)

    def get_projectId(self):
        return self.get_params().get('projectId')

    def set_projectId(self, projectId):
        self.add_param('projectId', projectId)

    def get_sgId(self):
        return self.get_params().get('sgId')

    def set_sgId(self, sgId):
        self.add_param('sgId', sgId)

    def get_sgName(self):
        return self.get_params().get('sgName')

    def set_sgName(self, sgName):
        self.add_param('sgName', sgName)
