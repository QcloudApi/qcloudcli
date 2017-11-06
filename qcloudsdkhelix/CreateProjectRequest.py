# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateProjectRequest(Request):

    def __init__(self):
        super(CreateProjectRequest, self).__init__(
            'helix', 'qcloudcliV1', 'CreateProject', 'helix.api.qcloud.com')

    def get_desc(self):
        return self.get_params().get('desc')

    def set_desc(self, desc):
        self.add_param('desc', desc)

    def get_name(self):
        return self.get_params().get('name')

    def set_name(self, name):
        self.add_param('name', name)

    def get_region(self):
        return self.get_params().get('region')

    def set_region(self, region):
        self.add_param('region', region)

    def get_secretId(self):
        return self.get_params().get('secretId')

    def set_secretId(self, secretId):
        self.add_param('secretId', secretId)

    def get_secretKey(self):
        return self.get_params().get('secretKey')

    def set_secretKey(self, secretKey):
        self.add_param('secretKey', secretKey)
