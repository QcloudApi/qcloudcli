# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateGroupRequest(Request):

    def __init__(self):
        super(CreateGroupRequest, self).__init__(
            'cam', 'qcloudcliV1', 'CreateGroup', 'cam.api.qcloud.com')
