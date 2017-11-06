# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class EipBindNatGatewayRequest(Request):

    def __init__(self):
        super(EipBindNatGatewayRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'EipBindNatGateway', 'vpc.api.qcloud.com')

    def get_assignedEipSet(self):
        return self.get_params().get('assignedEipSet')

    def set_assignedEipSet(self, assignedEipSet):
        self.add_param('assignedEipSet', assignedEipSet)

    def get_autoAllocEipNum(self):
        return self.get_params().get('autoAllocEipNum')

    def set_autoAllocEipNum(self, autoAllocEipNum):
        self.add_param('autoAllocEipNum', autoAllocEipNum)

    def get_natId(self):
        return self.get_params().get('natId')

    def set_natId(self, natId):
        self.add_param('natId', natId)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
