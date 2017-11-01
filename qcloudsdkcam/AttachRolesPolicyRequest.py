# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class AttachRolesPolicyRequest(Request):

    def __init__(self):
        super(AttachRolesPolicyRequest, self).__init__(
            'cam', 'qcloudcliV1', 'AttachRolesPolicy', 'cam.api.qcloud.com')
