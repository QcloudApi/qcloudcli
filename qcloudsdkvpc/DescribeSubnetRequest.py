# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeSubnetRequest(Request):

    def __init__(self):
        super(DescribeSubnetRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DescribeSubnet', 'vpc.api.qcloud.com')

    def get_subnetId(self):
        return self.get_params().get('subnetId')

    def set_subnetId(self, subnetId):
        self.add_param('subnetId', subnetId)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
