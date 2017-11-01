# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class AcceptVpcPeeringConnectionExRequest(Request):

    def __init__(self):
        super(AcceptVpcPeeringConnectionExRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'AcceptVpcPeeringConnectionEx', 'vpc.api.qcloud.com')

    def get_peeringConnectionId(self):
        return self.get_params().get('peeringConnectionId')

    def set_peeringConnectionId(self, peeringConnectionId):
        self.add_param('peeringConnectionId', peeringConnectionId)
