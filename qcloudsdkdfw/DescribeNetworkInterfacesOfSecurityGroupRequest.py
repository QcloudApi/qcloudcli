# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeNetworkInterfacesOfSecurityGroupRequest(Request):

    def __init__(self):
        super(DescribeNetworkInterfacesOfSecurityGroupRequest, self).__init__(
            'dfw', 'qcloudcliV1', 'DescribeNetworkInterfacesOfSecurityGroup', 'dfw.api.qcloud.com')

    def get_sgId(self):
        return self.get_params().get('sgId')

    def set_sgId(self, sgId):
        self.add_param('sgId', sgId)
