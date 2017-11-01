# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class EipBmBindVpcIpRequest(Request):

    def __init__(self):
        super(EipBmBindVpcIpRequest, self).__init__(
            'eip', 'qcloudcliV1', 'EipBmBindVpcIp', 'eip.api.qcloud.com')

    def get_eipId(self):
        return self.get_params().get('eipId')

    def set_eipId(self, eipId):
        self.add_param('eipId', eipId)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)

    def get_vpcIp(self):
        return self.get_params().get('vpcIp')

    def set_vpcIp(self, vpcIp):
        self.add_param('vpcIp', vpcIp)
