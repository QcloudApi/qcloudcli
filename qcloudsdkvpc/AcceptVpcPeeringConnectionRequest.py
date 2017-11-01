# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class AcceptVpcPeeringConnectionRequest(Request):

    def __init__(self):
        super(AcceptVpcPeeringConnectionRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'AcceptVpcPeeringConnection', 'vpc.api.qcloud.com')

    def get_peeringConnectionId(self):
        return self.get_params().get('peeringConnectionId')

    def set_peeringConnectionId(self, peeringConnectionId):
        self.add_param('peeringConnectionId', peeringConnectionId)
