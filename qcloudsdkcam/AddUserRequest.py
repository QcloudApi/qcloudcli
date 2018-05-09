# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class AddUserRequest(Request):

    def __init__(self):
        super(AddUserRequest, self).__init__(
            'cam', 'qcloudcliV1', 'AddUser', 'cam.api.qcloud.com')
