# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class RemoveUserFromGroupRequest(Request):

    def __init__(self):
        super(RemoveUserFromGroupRequest, self).__init__(
            'cam', 'qcloudcliV1', 'RemoveUserFromGroup', 'cam.api.qcloud.com')
