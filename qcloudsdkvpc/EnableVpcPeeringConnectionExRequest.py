# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class EnableVpcPeeringConnectionExRequest(Request):

    def __init__(self):
        super(EnableVpcPeeringConnectionExRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'EnableVpcPeeringConnectionEx', 'vpc.api.qcloud.com')

    def get_peeringConnectionId(self):
        return self.get_params().get('peeringConnectionId')

    def set_peeringConnectionId(self, peeringConnectionId):
        self.add_param('peeringConnectionId', peeringConnectionId)
