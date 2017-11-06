# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyVpnConnExRequest(Request):

    def __init__(self):
        super(ModifyVpnConnExRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'ModifyVpnConnEx', 'vpc.api.qcloud.com')

    def get_IKESet(self):
        return self.get_params().get('IKESet')

    def set_IKESet(self, IKESet):
        self.add_param('IKESet', IKESet)

    def get_IPsecSet(self):
        return self.get_params().get('IPsecSet')

    def set_IPsecSet(self, IPsecSet):
        self.add_param('IPsecSet', IPsecSet)

    def get_preSharedKey(self):
        return self.get_params().get('preSharedKey')

    def set_preSharedKey(self, preSharedKey):
        self.add_param('preSharedKey', preSharedKey)

    def get_spdAcl(self):
        return self.get_params().get('spdAcl')

    def set_spdAcl(self, spdAcl):
        self.add_param('spdAcl', spdAcl)

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
