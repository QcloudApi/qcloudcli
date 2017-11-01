# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetEventPolicyProductRequest(Request):

    def __init__(self):
        super(GetEventPolicyProductRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'GetEventPolicyProduct', 'monitor.api.qcloud.com')
