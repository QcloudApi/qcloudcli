# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class RegisterBatchIpRequest(Request):

    def __init__(self):
        super(RegisterBatchIpRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'RegisterBatchIp', 'vpc.api.qcloud.com')

    def get_ipClass(self):
        return self.get_params().get('ipClass')

    def set_ipClass(self, ipClass):
        self.add_param('ipClass', ipClass)

    def get_ipList(self):
        return self.get_params().get('ipList')

    def set_ipList(self, ipList):
        self.add_param('ipList', ipList)

    def get_subnetId(self):
        return self.get_params().get('subnetId')

    def set_subnetId(self, subnetId):
        self.add_param('subnetId', subnetId)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
