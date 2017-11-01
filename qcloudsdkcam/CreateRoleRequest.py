# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateRoleRequest(Request):

    def __init__(self):
        super(CreateRoleRequest, self).__init__(
            'cam', 'qcloudcliV1', 'CreateRole', 'cam.api.qcloud.com')
