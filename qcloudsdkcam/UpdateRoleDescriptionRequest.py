# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class UpdateRoleDescriptionRequest(Request):

    def __init__(self):
        super(UpdateRoleDescriptionRequest, self).__init__(
            'cam', 'qcloudcliV1', 'UpdateRoleDescription', 'cam.api.qcloud.com')
