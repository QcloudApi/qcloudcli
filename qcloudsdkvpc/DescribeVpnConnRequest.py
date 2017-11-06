# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeVpnConnRequest(Request):

    def __init__(self):
        super(DescribeVpnConnRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DescribeVpnConn', 'vpc.api.qcloud.com')

    def get_isNeedConnNet(self):
        return self.get_params().get('isNeedConnNet')

    def set_isNeedConnNet(self, isNeedConnNet):
        self.add_param('isNeedConnNet', isNeedConnNet)

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

    def get_taskId(self):
        return self.get_params().get('taskId')

    def set_taskId(self, taskId):
        self.add_param('taskId', taskId)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)

    def get_vpnConnId(self):
        return self.get_params().get('vpnConnId')

    def set_vpnConnId(self, vpnConnId):
        self.add_param('vpnConnId', vpnConnId)

    def get_vpnConnName(self):
        return self.get_params().get('vpnConnName')

    def set_vpnConnName(self, vpnConnName):
        self.add_param('vpnConnName', vpnConnName)

    def get_vpnGwId(self):
        return self.get_params().get('vpnGwId')

    def set_vpnGwId(self, vpnGwId):
        self.add_param('vpnGwId', vpnGwId)
