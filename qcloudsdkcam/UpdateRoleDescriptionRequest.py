# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class UpdateRoleDescriptionRequest(Request):

    def __init__(self):
        super(UpdateRoleDescriptionRequest, self).__init__(
            'cam', 'qcloudcliV1', 'UpdateRoleDescription', 'cam.api.qcloud.com')

    def get_description(self):
        return self.get_params().get('description')

    def set_description(self, description):
        self.add_param('description', description)

    def get_roleId(self):
        return self.get_params().get('roleId')

    def set_roleId(self, roleId):
        self.add_param('roleId', roleId)

    def get_roleName(self):
        return self.get_params().get('roleName')

    def set_roleName(self, roleName):
        self.add_param('roleName', roleName)
