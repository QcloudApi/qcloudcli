# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class SetSSLVpnDomainRequest(Request):

    def __init__(self):
        super(SetSSLVpnDomainRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'SetSSLVpnDomain', 'vpc.api.qcloud.com')

    def get_acl(self):
        return self.get_params().get('acl')

    def set_acl(self, acl):
        self.add_param('acl', acl)

    def get_groupId(self):
        return self.get_params().get('groupId')

    def set_groupId(self, groupId):
        self.add_param('groupId', groupId)

    def get_ipPool(self):
        return self.get_params().get('ipPool')

    def set_ipPool(self, ipPool):
        self.add_param('ipPool', ipPool)

    def get_sslVpnId(self):
        return self.get_params().get('sslVpnId')

    def set_sslVpnId(self, sslVpnId):
        self.add_param('sslVpnId', sslVpnId)

    def get_sslVpnPort(self):
        return self.get_params().get('sslVpnPort')

    def set_sslVpnPort(self, sslVpnPort):
        self.add_param('sslVpnPort', sslVpnPort)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
