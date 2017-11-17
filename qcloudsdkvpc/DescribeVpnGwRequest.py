# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeVpnGwRequest(Request):

    def __init__(self):
        super(DescribeVpnGwRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DescribeVpnGw', 'vpc.api.qcloud.com')

    def get_dealId(self):
        return self.get_params().get('dealId')

    def set_dealId(self, dealId):
        self.add_param('dealId', dealId)

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

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)

    def get_vpnGwAddressSet(self):
        return self.get_params().get('vpnGwAddressSet')

    def set_vpnGwAddressSet(self, vpnGwAddressSet):
        self.add_param('vpnGwAddressSet', vpnGwAddressSet)

    def get_vpnGwId(self):
        return self.get_params().get('vpnGwId')

    def set_vpnGwId(self, vpnGwId):
        self.add_param('vpnGwId', vpnGwId)

    def get_vpnGwName(self):
        return self.get_params().get('vpnGwName')

    def set_vpnGwName(self, vpnGwName):
        self.add_param('vpnGwName', vpnGwName)
