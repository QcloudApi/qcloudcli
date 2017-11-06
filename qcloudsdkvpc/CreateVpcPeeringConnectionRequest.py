# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateVpcPeeringConnectionRequest(Request):

    def __init__(self):
        super(CreateVpcPeeringConnectionRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'CreateVpcPeeringConnection', 'vpc.api.qcloud.com')

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

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
