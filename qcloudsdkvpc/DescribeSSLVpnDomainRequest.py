# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeSSLVpnDomainRequest(Request):

    def __init__(self):
        super(DescribeSSLVpnDomainRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DescribeSSLVpnDomain', 'vpc.api.qcloud.com')

    def get_sslVpnId(self):
        return self.get_params().get('sslVpnId')

    def set_sslVpnId(self, sslVpnId):
        self.add_param('sslVpnId', sslVpnId)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
