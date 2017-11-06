# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class AssociateSecurityGroupsV3Request(Request):

    def __init__(self):
        super(AssociateSecurityGroupsV3Request, self).__init__(
            'cdb', 'qcloudcliV1', 'AssociateSecurityGroupsV3', 'cdb.api.qcloud.com')

    def get_instanceIds(self):
        return self.get_params().get('instanceIds')

    def set_instanceIds(self, instanceIds):
        self.add_param('instanceIds', instanceIds)

    def get_securityGroupId(self):
        return self.get_params().get('securityGroupId')

    def set_securityGroupId(self, securityGroupId):
        self.add_param('securityGroupId', securityGroupId)
