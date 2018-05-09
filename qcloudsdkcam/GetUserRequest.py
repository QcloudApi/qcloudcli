# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetUserRequest(Request):

    def __init__(self):
        super(GetUserRequest, self).__init__(
            'cam', 'qcloudcliV1', 'GetUser', 'cam.api.qcloud.com')
