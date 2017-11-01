# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DetachRolePolicyRequest(Request):

    def __init__(self):
        super(DetachRolePolicyRequest, self).__init__(
            'cam', 'qcloudcliV1', 'DetachRolePolicy', 'cam.api.qcloud.com')
