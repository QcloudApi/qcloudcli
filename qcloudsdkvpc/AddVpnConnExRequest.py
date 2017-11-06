# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class AddVpnConnExRequest(Request):

    def __init__(self):
        super(AddVpnConnExRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'AddVpnConnEx', 'vpc.api.qcloud.com')

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

    def get_userGwAddr(self):
        return self.get_params().get('userGwAddr')

    def set_userGwAddr(self, userGwAddr):
        self.add_param('userGwAddr', userGwAddr)

    def get_userGwCidrBlock(self):
        return self.get_params().get('userGwCidrBlock')

    def set_userGwCidrBlock(self, userGwCidrBlock):
        self.add_param('userGwCidrBlock', userGwCidrBlock)

    def get_userGwId(self):
        return self.get_params().get('userGwId')

    def set_userGwId(self, userGwId):
        self.add_param('userGwId', userGwId)

    def get_userGwName(self):
        return self.get_params().get('userGwName')

    def set_userGwName(self, userGwName):
        self.add_param('userGwName', userGwName)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)

    def get_vpnConnName(self):
        return self.get_params().get('vpnConnName')

    def set_vpnConnName(self, vpnConnName):
        self.add_param('vpnConnName', vpnConnName)

    def get_vpnGwId(self):
        return self.get_params().get('vpnGwId')

    def set_vpnGwId(self, vpnGwId):
        self.add_param('vpnGwId', vpnGwId)
