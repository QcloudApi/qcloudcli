# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyImageSharePermissionRequest(Request):

    def __init__(self):
        super(ModifyImageSharePermissionRequest, self).__init__(
            'image', 'qcloudcliV1', 'ModifyImageSharePermission', 'image.api.qcloud.com')

    def get_AccountIds(self):
        return self.get_params().get('AccountIds')

    def set_AccountIds(self, AccountIds):
        self.add_param('AccountIds', AccountIds)

    def get_ImageId(self):
        return self.get_params().get('ImageId')

    def set_ImageId(self, ImageId):
        self.add_param('ImageId', ImageId)

    def get_Permission(self):
        return self.get_params().get('Permission')

    def set_Permission(self, Permission):
        self.add_param('Permission', Permission)
