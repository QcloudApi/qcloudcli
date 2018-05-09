# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateLoadBalancerRequest(Request):

    def __init__(self):
        super(CreateLoadBalancerRequest, self).__init__(
            'lb', 'qcloudcliV1', 'CreateLoadBalancer', 'lb.api.qcloud.com')

    def get_domainPrefix(self):
        return self.get_params().get('domainPrefix')

    def set_domainPrefix(self, domainPrefix):
        self.add_param('domainPrefix', domainPrefix)

    def get_forward(self):
        return self.get_params().get('forward')

    def set_forward(self, forward):
        self.add_param('forward', forward)

    def get_internetAccessible(self):
        return self.get_params().get('internetAccessible')

    def set_internetAccessible(self, internetAccessible):
        self.add_param('internetAccessible', internetAccessible)

    def get_ispId(self):
        return self.get_params().get('ispId')

    def set_ispId(self, ispId):
        self.add_param('ispId', ispId)

    def get_lbChargePrepaid(self):
        return self.get_params().get('lbChargePrepaid')

    def set_lbChargePrepaid(self, lbChargePrepaid):
        self.add_param('lbChargePrepaid', lbChargePrepaid)

    def get_lbChargeType(self):
        return self.get_params().get('lbChargeType')

    def set_lbChargeType(self, lbChargeType):
        self.add_param('lbChargeType', lbChargeType)

    def get_loadBalancerName(self):
        return self.get_params().get('loadBalancerName')

    def set_loadBalancerName(self, loadBalancerName):
        self.add_param('loadBalancerName', loadBalancerName)

    def get_loadBalancerType(self):
        return self.get_params().get('loadBalancerType')

    def set_loadBalancerType(self, loadBalancerType):
        self.add_param('loadBalancerType', loadBalancerType)

    def get_number(self):
        return self.get_params().get('number')

    def set_number(self, number):
        self.add_param('number', number)

    def get_projectId(self):
        return self.get_params().get('projectId')

    def set_projectId(self, projectId):
        self.add_param('projectId', projectId)

    def get_special(self):
        return self.get_params().get('special')

    def set_special(self, special):
        self.add_param('special', special)

    def get_subnetId(self):
        return self.get_params().get('subnetId')

    def set_subnetId(self, subnetId):
        self.add_param('subnetId', subnetId)

    def get_tgwGroup(self):
        return self.get_params().get('tgwGroup')

    def set_tgwGroup(self, tgwGroup):
        self.add_param('tgwGroup', tgwGroup)

    def get_vips(self):
        return self.get_params().get('vips')

    def set_vips(self, vips):
        self.add_param('vips', vips)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
