# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class AssignPrivateIpAddressesRequest(Request):

    def __init__(self):
        super(AssignPrivateIpAddressesRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'AssignPrivateIpAddresses', 'vpc.api.qcloud.com')

    def get_networkInterfaceId(self):
        return self.get_params().get('networkInterfaceId')

    def set_networkInterfaceId(self, networkInterfaceId):
        self.add_param('networkInterfaceId', networkInterfaceId)

    def get_privateIpAddressSet(self):
        return self.get_params().get('privateIpAddressSet')

    def set_privateIpAddressSet(self, privateIpAddressSet):
        self.add_param('privateIpAddressSet', privateIpAddressSet)

    def get_secondaryPrivateIpAddressCount(self):
        return self.get_params().get('secondaryPrivateIpAddressCount')

    def set_secondaryPrivateIpAddressCount(self, secondaryPrivateIpAddressCount):
        self.add_param('secondaryPrivateIpAddressCount', secondaryPrivateIpAddressCount)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
