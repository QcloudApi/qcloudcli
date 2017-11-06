# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyNetworkAclRequest(Request):

    def __init__(self):
        super(ModifyNetworkAclRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'ModifyNetworkAcl', 'vpc.api.qcloud.com')

    def get_networkAclId(self):
        return self.get_params().get('networkAclId')

    def set_networkAclId(self, networkAclId):
        self.add_param('networkAclId', networkAclId)

    def get_networkAclName(self):
        return self.get_params().get('networkAclName')

    def set_networkAclName(self, networkAclName):
        self.add_param('networkAclName', networkAclName)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
