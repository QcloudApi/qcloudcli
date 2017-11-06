# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class MigratePrivateIpAddressRequest(Request):

    def __init__(self):
        super(MigratePrivateIpAddressRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'MigratePrivateIpAddress', 'vpc.api.qcloud.com')

    def get_newNetworkInterfaceId(self):
        return self.get_params().get('newNetworkInterfaceId')

    def set_newNetworkInterfaceId(self, newNetworkInterfaceId):
        self.add_param('newNetworkInterfaceId', newNetworkInterfaceId)

    def get_oldNetworkInterfaceId(self):
        return self.get_params().get('oldNetworkInterfaceId')

    def set_oldNetworkInterfaceId(self, oldNetworkInterfaceId):
        self.add_param('oldNetworkInterfaceId', oldNetworkInterfaceId)

    def get_privateIpAddress(self):
        return self.get_params().get('privateIpAddress')

    def set_privateIpAddress(self, privateIpAddress):
        self.add_param('privateIpAddress', privateIpAddress)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
