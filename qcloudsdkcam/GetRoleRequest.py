# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetRoleRequest(Request):

    def __init__(self):
        super(GetRoleRequest, self).__init__(
            'cam', 'qcloudcliV1', 'GetRole', 'cam.api.qcloud.com')
