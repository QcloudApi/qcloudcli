# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateNetworkAclRequest(Request):

    def __init__(self):
        super(CreateNetworkAclRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'CreateNetworkAcl', 'vpc.api.qcloud.com')

    def get_networkAclName(self):
        return self.get_params().get('networkAclName')

    def set_networkAclName(self, networkAclName):
        self.add_param('networkAclName', networkAclName)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
