# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class UpdateUserRequest(Request):

    def __init__(self):
        super(UpdateUserRequest, self).__init__(
            'cam', 'qcloudcliV1', 'UpdateUser', 'cam.api.qcloud.com')
