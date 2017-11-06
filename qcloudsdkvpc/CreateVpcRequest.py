# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateVpcRequest(Request):

    def __init__(self):
        super(CreateVpcRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'CreateVpc', 'vpc.api.qcloud.com')

    def get_cidrBlock(self):
        return self.get_params().get('cidrBlock')

    def set_cidrBlock(self, cidrBlock):
        self.add_param('cidrBlock', cidrBlock)

    def get_subnetSet(self):
        return self.get_params().get('subnetSet')

    def set_subnetSet(self, subnetSet):
        self.add_param('subnetSet', subnetSet)

    def get_vpcName(self):
        return self.get_params().get('vpcName')

    def set_vpcName(self, vpcName):
        self.add_param('vpcName', vpcName)
