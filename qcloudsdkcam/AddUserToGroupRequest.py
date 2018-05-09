# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class AddUserToGroupRequest(Request):

    def __init__(self):
        super(AddUserToGroupRequest, self).__init__(
            'cam', 'qcloudcliV1', 'AddUserToGroup', 'cam.api.qcloud.com')
