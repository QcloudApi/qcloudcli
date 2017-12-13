# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeNetworkInterfacesRequest(Request):

    def __init__(self):
        super(DescribeNetworkInterfacesRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DescribeNetworkInterfaces', 'vpc.api.qcloud.com')

    def get_eniDescription(self):
        return self.get_params().get('eniDescription')

    def set_eniDescription(self, eniDescription):
        self.add_param('eniDescription', eniDescription)

    def get_eniName(self):
        return self.get_params().get('eniName')

    def set_eniName(self, eniName):
        self.add_param('eniName', eniName)

    def get_eniType(self):
        return self.get_params().get('eniType')

    def set_eniType(self, eniType):
        self.add_param('eniType', eniType)

    def get_hideSecondary(self):
        return self.get_params().get('hideSecondary')

    def set_hideSecondary(self, hideSecondary):
        self.add_param('hideSecondary', hideSecondary)

    def get_instanceId(self):
        return self.get_params().get('instanceId')

    def set_instanceId(self, instanceId):
        self.add_param('instanceId', instanceId)

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_networkInterfaceId(self):
        return self.get_params().get('networkInterfaceId')

    def set_networkInterfaceId(self, networkInterfaceId):
        self.add_param('networkInterfaceId', networkInterfaceId)

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

    def get_sgId(self):
        return self.get_params().get('sgId')

    def set_sgId(self, sgId):
        self.add_param('sgId', sgId)

    def get_showInt(self):
        return self.get_params().get('showInt')

    def set_showInt(self, showInt):
        self.add_param('showInt', showInt)

    def get_subnetId(self):
        return self.get_params().get('subnetId')

    def set_subnetId(self, subnetId):
        self.add_param('subnetId', subnetId)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
