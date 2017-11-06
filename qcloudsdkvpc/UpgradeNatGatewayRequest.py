# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class UpgradeNatGatewayRequest(Request):

    def __init__(self):
        super(UpgradeNatGatewayRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'UpgradeNatGateway', 'vpc.api.qcloud.com')

    def get_maxConcurrent(self):
        return self.get_params().get('maxConcurrent')

    def set_maxConcurrent(self, maxConcurrent):
        self.add_param('maxConcurrent', maxConcurrent)

    def get_natId(self):
        return self.get_params().get('natId')

    def set_natId(self, natId):
        self.add_param('natId', natId)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
