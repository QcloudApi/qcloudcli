# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateNetworkInterfaceRequest(Request):

    def __init__(self):
        super(CreateNetworkInterfaceRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'CreateNetworkInterface', 'vpc.api.qcloud.com')

    def get_eniDescription(self):
        return self.get_params().get('eniDescription')

    def set_eniDescription(self, eniDescription):
        self.add_param('eniDescription', eniDescription)

    def get_eniName(self):
        return self.get_params().get('eniName')

    def set_eniName(self, eniName):
        self.add_param('eniName', eniName)

    def get_privateIpAddressSet(self):
        return self.get_params().get('privateIpAddressSet')

    def set_privateIpAddressSet(self, privateIpAddressSet):
        self.add_param('privateIpAddressSet', privateIpAddressSet)

    def get_secondaryPrivateIpAddressCount(self):
        return self.get_params().get('secondaryPrivateIpAddressCount')

    def set_secondaryPrivateIpAddressCount(self, secondaryPrivateIpAddressCount):
        self.add_param('secondaryPrivateIpAddressCount', secondaryPrivateIpAddressCount)

    def get_sgIds(self):
        return self.get_params().get('sgIds')

    def set_sgIds(self, sgIds):
        self.add_param('sgIds', sgIds)

    def get_subnetId(self):
        return self.get_params().get('subnetId')

    def set_subnetId(self, subnetId):
        self.add_param('subnetId', subnetId)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
