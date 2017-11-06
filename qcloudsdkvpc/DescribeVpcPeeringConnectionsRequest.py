# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeVpcPeeringConnectionsRequest(Request):

    def __init__(self):
        super(DescribeVpcPeeringConnectionsRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DescribeVpcPeeringConnections', 'vpc.api.qcloud.com')

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_orderDirection(self):
        return self.get_params().get('orderDirection')

    def set_orderDirection(self, orderDirection):
        self.add_param('orderDirection', orderDirection)

    def get_orderField(self):
        return self.get_params().get('orderField')

    def set_orderField(self, orderField):
        self.add_param('orderField', orderField)

    def get_peeringConnectionId(self):
        return self.get_params().get('peeringConnectionId')

    def set_peeringConnectionId(self, peeringConnectionId):
        self.add_param('peeringConnectionId', peeringConnectionId)

    def get_peeringConnectionName(self):
        return self.get_params().get('peeringConnectionName')

    def set_peeringConnectionName(self, peeringConnectionName):
        self.add_param('peeringConnectionName', peeringConnectionName)

    def get_state(self):
        return self.get_params().get('state')

    def set_state(self, state):
        self.add_param('state', state)

    def get_type(self):
        return self.get_params().get('type')

    def set_type(self, type):
        self.add_param('type', type)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
