# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetThFederationTokenRequest(Request):

    def __init__(self):
        super(GetThFederationTokenRequest, self).__init__(
            'cam', 'qcloudcliV1', 'GetThFederationToken', 'cam.api.qcloud.com')

    def get_app_id(self):
        return self.get_params().get('app_id')

    def set_app_id(self, app_id):
        self.add_param('app_id', app_id)

    def get_duration(self):
        return self.get_params().get('duration')

    def set_duration(self, duration):
        self.add_param('duration', duration)

    def get_open_access_token(self):
        return self.get_params().get('open_access_token')

    def set_open_access_token(self, open_access_token):
        self.add_param('open_access_token', open_access_token)

    def get_user_access_token(self):
        return self.get_params().get('user_access_token')

    def set_user_access_token(self, user_access_token):
        self.add_param('user_access_token', user_access_token)
