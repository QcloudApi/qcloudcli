# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class AttachRolePoliciesRequest(Request):

    def __init__(self):
        super(AttachRolePoliciesRequest, self).__init__(
            'cam', 'qcloudcliV1', 'AttachRolePolicies', 'cam.api.qcloud.com')
