# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class AssociateVipRequest(Request):

    def __init__(self):
        super(AssociateVipRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'AssociateVip', 'vpc.api.qcloud.com')

    def get_lanIp(self):
        return self.get_params().get('lanIp')

    def set_lanIp(self, lanIp):
        self.add_param('lanIp', lanIp)

    def get_vipId(self):
        return self.get_params().get('vipId')

    def set_vipId(self, vipId):
        self.add_param('vipId', vipId)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
