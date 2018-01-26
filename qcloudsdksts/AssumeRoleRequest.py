# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class AssumeRoleRequest(Request):

    def __init__(self):
        super(AssumeRoleRequest, self).__init__(
            'sts', 'qcloudcliV1', 'AssumeRole', 'sts.api.qcloud.com')

    def get_durationSeconds(self):
        return self.get_params().get('durationSeconds')

    def set_durationSeconds(self, durationSeconds):
        self.add_param('durationSeconds', durationSeconds)

    def get_roleArn(self):
        return self.get_params().get('roleArn')

    def set_roleArn(self, roleArn):
        self.add_param('roleArn', roleArn)

    def get_roleSessionName(self):
        return self.get_params().get('roleSessionName')

    def set_roleSessionName(self, roleSessionName):
        self.add_param('roleSessionName', roleSessionName)
