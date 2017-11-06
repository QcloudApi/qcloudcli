# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ApplyIpsRequest(Request):

    def __init__(self):
        super(ApplyIpsRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'ApplyIps', 'vpc.api.qcloud.com')

    def get_count(self):
        return self.get_params().get('count')

    def set_count(self, count):
        self.add_param('count', count)

    def get_ipClass(self):
        return self.get_params().get('ipClass')

    def set_ipClass(self, ipClass):
        self.add_param('ipClass', ipClass)

    def get_subnetId(self):
        return self.get_params().get('subnetId')

    def set_subnetId(self, subnetId):
        self.add_param('subnetId', subnetId)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
