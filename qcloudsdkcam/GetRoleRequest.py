# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetRoleRequest(Request):

    def __init__(self):
        super(GetRoleRequest, self).__init__(
            'cam', 'qcloudcliV1', 'GetRole', 'cam.api.qcloud.com')

    def get_roleId(self):
        return self.get_params().get('roleId')

    def set_roleId(self, roleId):
        self.add_param('roleId', roleId)

    def get_roleName(self):
        return self.get_params().get('roleName')

    def set_roleName(self, roleName):
        self.add_param('roleName', roleName)
