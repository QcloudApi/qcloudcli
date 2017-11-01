# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteRoleRequest(Request):

    def __init__(self):
        super(DeleteRoleRequest, self).__init__(
            'cam', 'qcloudcliV1', 'DeleteRole', 'cam.api.qcloud.com')
