# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteUserRequest(Request):

    def __init__(self):
        super(DeleteUserRequest, self).__init__(
            'cam', 'qcloudcliV1', 'DeleteUser', 'cam.api.qcloud.com')
