# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateBmNatGatewayRequest(Request):

    def __init__(self):
        super(CreateBmNatGatewayRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'CreateBmNatGateway', 'vpc.api.qcloud.com')

    def get_assignedEipSet(self):
        return self.get_params().get('assignedEipSet')

    def set_assignedEipSet(self, assignedEipSet):
        self.add_param('assignedEipSet', assignedEipSet)

    def get_autoAllocEipNum(self):
        return self.get_params().get('autoAllocEipNum')

    def set_autoAllocEipNum(self, autoAllocEipNum):
        self.add_param('autoAllocEipNum', autoAllocEipNum)

    def get_ips(self):
        return self.get_params().get('ips')

    def set_ips(self, ips):
        self.add_param('ips', ips)

    def get_maxConcurrent(self):
        return self.get_params().get('maxConcurrent')

    def set_maxConcurrent(self, maxConcurrent):
        self.add_param('maxConcurrent', maxConcurrent)

    def get_natName(self):
        return self.get_params().get('natName')

    def set_natName(self, natName):
        self.add_param('natName', natName)

    def get_subnetAll(self):
        return self.get_params().get('subnetAll')

    def set_subnetAll(self, subnetAll):
        self.add_param('subnetAll', subnetAll)

    def get_subnetIds(self):
        return self.get_params().get('subnetIds')

    def set_subnetIds(self, subnetIds):
        self.add_param('subnetIds', subnetIds)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
