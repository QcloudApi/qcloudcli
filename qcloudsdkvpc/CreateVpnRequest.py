# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateVpnRequest(Request):

    def __init__(self):
        super(CreateVpnRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'CreateVpn', 'vpc.api.qcloud.com')

    def get_bandwidth(self):
        return self.get_params().get('bandwidth')

    def set_bandwidth(self, bandwidth):
        self.add_param('bandwidth', bandwidth)

    def get_isAutoRenewals(self):
        return self.get_params().get('isAutoRenewals')

    def set_isAutoRenewals(self, isAutoRenewals):
        self.add_param('isAutoRenewals', isAutoRenewals)

    def get_name(self):
        return self.get_params().get('name')

    def set_name(self, name):
        self.add_param('name', name)

    def get_period(self):
        return self.get_params().get('period')

    def set_period(self, period):
        self.add_param('period', period)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
