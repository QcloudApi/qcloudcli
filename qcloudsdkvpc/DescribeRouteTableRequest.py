# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeRouteTableRequest(Request):

    def __init__(self):
        super(DescribeRouteTableRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DescribeRouteTable', 'vpc.api.qcloud.com')

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

    def get_routeTableId(self):
        return self.get_params().get('routeTableId')

    def set_routeTableId(self, routeTableId):
        self.add_param('routeTableId', routeTableId)

    def get_routeTableName(self):
        return self.get_params().get('routeTableName')

    def set_routeTableName(self, routeTableName):
        self.add_param('routeTableName', routeTableName)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
