# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyNetworkAclEntryRequest(Request):

    def __init__(self):
        super(ModifyNetworkAclEntryRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'ModifyNetworkAclEntry', 'vpc.api.qcloud.com')

    def get_networkAclEntrySet(self):
        return self.get_params().get('networkAclEntrySet')

    def set_networkAclEntrySet(self, networkAclEntrySet):
        self.add_param('networkAclEntrySet', networkAclEntrySet)

    def get_networkAclId(self):
        return self.get_params().get('networkAclId')

    def set_networkAclId(self, networkAclId):
        self.add_param('networkAclId', networkAclId)

    def get_ruleDirection(self):
        return self.get_params().get('ruleDirection')

    def set_ruleDirection(self, ruleDirection):
        self.add_param('ruleDirection', ruleDirection)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
