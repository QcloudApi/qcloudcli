# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateRoleRequest(Request):

    def __init__(self):
        super(CreateRoleRequest, self).__init__(
            'cam', 'qcloudcliV1', 'CreateRole', 'cam.api.qcloud.com')

    def get_description(self):
        return self.get_params().get('description')

    def set_description(self, description):
        self.add_param('description', description)

    def get_policyDocument(self):
        return self.get_params().get('policyDocument')

    def set_policyDocument(self, policyDocument):
        self.add_param('policyDocument', policyDocument)

    def get_roleName(self):
        return self.get_params().get('roleName')

    def set_roleName(self, roleName):
        self.add_param('roleName', roleName)

    def get_roleType(self):
        return self.get_params().get('roleType')

    def set_roleType(self, roleType):
        self.add_param('roleType', roleType)
