# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetGroupRequest(Request):

    def __init__(self):
        super(GetGroupRequest, self).__init__(
            'cam', 'qcloudcliV1', 'GetGroup', 'cam.api.qcloud.com')
