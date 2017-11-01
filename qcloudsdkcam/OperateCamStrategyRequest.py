# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class OperateCamStrategyRequest(Request):

    def __init__(self):
        super(OperateCamStrategyRequest, self).__init__(
            'cam', 'qcloudcliV1', 'OperateCamStrategy', 'cam.api.qcloud.com')
