# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetTaskResultRequest(Request):

    def __init__(self):
        super(GetTaskResultRequest, self).__init__(
            'cns', 'qcloudcliV1', 'GetTaskResult', 'cns.api.qcloud.com')
