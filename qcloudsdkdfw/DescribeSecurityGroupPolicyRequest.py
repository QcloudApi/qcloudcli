# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeSecurityGroupPolicyRequest(Request):

    def __init__(self):
        super(DescribeSecurityGroupPolicyRequest, self).__init__(
            'dfw', 'qcloudcliV1', 'DescribeSecurityGroupPolicy', 'dfw.api.qcloud.com')

    def get_sgId(self):
        return self.get_params().get('sgId')

    def set_sgId(self, sgId):
        self.add_param('sgId', sgId)
