# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyVpcPeeringConnectionRequest(Request):

    def __init__(self):
        super(ModifyVpcPeeringConnectionRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'ModifyVpcPeeringConnection', 'vpc.api.qcloud.com')

    def get_peeringConnectionId(self):
        return self.get_params().get('peeringConnectionId')

    def set_peeringConnectionId(self, peeringConnectionId):
        self.add_param('peeringConnectionId', peeringConnectionId)

    def get_peeringConnectionName(self):
        return self.get_params().get('peeringConnectionName')

    def set_peeringConnectionName(self, peeringConnectionName):
        self.add_param('peeringConnectionName', peeringConnectionName)
