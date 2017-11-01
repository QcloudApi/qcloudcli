# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DetachRolesPolicyRequest(Request):

    def __init__(self):
        super(DetachRolesPolicyRequest, self).__init__(
            'cam', 'qcloudcliV1', 'DetachRolesPolicy', 'cam.api.qcloud.com')
