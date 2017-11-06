# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateNatGatewayRequest(Request):

    def __init__(self):
        super(CreateNatGatewayRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'CreateNatGateway', 'vpc.api.qcloud.com')

    def get_assignedEipSet(self):
        return self.get_params().get('assignedEipSet')

    def set_assignedEipSet(self, assignedEipSet):
        self.add_param('assignedEipSet', assignedEipSet)

    def get_autoAllocEipNum(self):
        return self.get_params().get('autoAllocEipNum')

    def set_autoAllocEipNum(self, autoAllocEipNum):
        self.add_param('autoAllocEipNum', autoAllocEipNum)

    def get_bandwidth(self):
        return self.get_params().get('bandwidth')

    def set_bandwidth(self, bandwidth):
        self.add_param('bandwidth', bandwidth)

    def get_maxConcurrent(self):
        return self.get_params().get('maxConcurrent')

    def set_maxConcurrent(self, maxConcurrent):
        self.add_param('maxConcurrent', maxConcurrent)

    def get_natName(self):
        return self.get_params().get('natName')

    def set_natName(self, natName):
        self.add_param('natName', natName)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
