# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeAssociateSecurityGroupsRequest(Request):

    def __init__(self):
        super(DescribeAssociateSecurityGroupsRequest, self).__init__(
            'dfw', 'qcloudcliV1', 'DescribeAssociateSecurityGroups', 'dfw.api.qcloud.com')

    def get_sgIds(self):
        return self.get_params().get('sgIds')

    def set_sgIds(self, sgIds):
        self.add_param('sgIds', sgIds)
