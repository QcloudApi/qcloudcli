# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyVpcPeeringConnectionExRequest(Request):

    def __init__(self):
        super(ModifyVpcPeeringConnectionExRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'ModifyVpcPeeringConnectionEx', 'vpc.api.qcloud.com')

    def get_bandwidth(self):
        return self.get_params().get('bandwidth')

    def set_bandwidth(self, bandwidth):
        self.add_param('bandwidth', bandwidth)

    def get_peeringConnectionId(self):
        return self.get_params().get('peeringConnectionId')

    def set_peeringConnectionId(self, peeringConnectionId):
        self.add_param('peeringConnectionId', peeringConnectionId)

    def get_peeringConnectionName(self):
        return self.get_params().get('peeringConnectionName')

    def set_peeringConnectionName(self, peeringConnectionName):
        self.add_param('peeringConnectionName', peeringConnectionName)
