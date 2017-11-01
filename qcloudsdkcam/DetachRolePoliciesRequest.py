# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DetachRolePoliciesRequest(Request):

    def __init__(self):
        super(DetachRolePoliciesRequest, self).__init__(
            'cam', 'qcloudcliV1', 'DetachRolePolicies', 'cam.api.qcloud.com')
