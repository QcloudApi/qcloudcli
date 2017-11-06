# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteVpnConnRequest(Request):

    def __init__(self):
        super(DeleteVpnConnRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DeleteVpnConn', 'vpc.api.qcloud.com')

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)

    def get_vpnConnId(self):
        return self.get_params().get('vpnConnId')

    def set_vpnConnId(self, vpnConnId):
        self.add_param('vpnConnId', vpnConnId)

    def get_vpnGwId(self):
        return self.get_params().get('vpnGwId')

    def set_vpnGwId(self, vpnGwId):
        self.add_param('vpnGwId', vpnGwId)
