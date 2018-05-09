# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateVpcPeeringConnectionExRequest(Request):

    def __init__(self):
        super(CreateVpcPeeringConnectionExRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'CreateVpcPeeringConnectionEx', 'vpc.api.qcloud.com')

    def get_bandwidth(self):
        return self.get_params().get('bandwidth')

    def set_bandwidth(self, bandwidth):
        self.add_param('bandwidth', bandwidth)

    def get_chargeType(self):
        return self.get_params().get('chargeType')

    def set_chargeType(self, chargeType):
        self.add_param('chargeType', chargeType)

    def get_peerRegion(self):
        return self.get_params().get('peerRegion')

    def set_peerRegion(self, peerRegion):
        self.add_param('peerRegion', peerRegion)

    def get_peerUin(self):
        return self.get_params().get('peerUin')

    def set_peerUin(self, peerUin):
        self.add_param('peerUin', peerUin)

    def get_peerVpcId(self):
        return self.get_params().get('peerVpcId')

    def set_peerVpcId(self, peerVpcId):
        self.add_param('peerVpcId', peerVpcId)

    def get_peeringConnectionName(self):
        return self.get_params().get('peeringConnectionName')

    def set_peeringConnectionName(self, peeringConnectionName):
        self.add_param('peeringConnectionName', peeringConnectionName)

    def get_qosLevel(self):
        return self.get_params().get('qosLevel')

    def set_qosLevel(self, qosLevel):
        self.add_param('qosLevel', qosLevel)

    def get_type(self):
        return self.get_params().get('type')

    def set_type(self, type):
        self.add_param('type', type)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
