# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreatePolicyRequest(Request):

    def __init__(self):
        super(CreatePolicyRequest, self).__init__(
            'cam', 'qcloudcliV1', 'CreatePolicy', 'cam.api.qcloud.com')
