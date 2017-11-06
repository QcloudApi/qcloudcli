# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateSubnetAclRuleRequest(Request):

    def __init__(self):
        super(CreateSubnetAclRuleRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'CreateSubnetAclRule', 'vpc.api.qcloud.com')

    def get_networkAclId(self):
        return self.get_params().get('networkAclId')

    def set_networkAclId(self, networkAclId):
        self.add_param('networkAclId', networkAclId)

    def get_subnetIds(self):
        return self.get_params().get('subnetIds')

    def set_subnetIds(self, subnetIds):
        self.add_param('subnetIds', subnetIds)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
