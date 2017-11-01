# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class BatchOperateCamStrategyRequest(Request):

    def __init__(self):
        super(BatchOperateCamStrategyRequest, self).__init__(
            'cam', 'qcloudcliV1', 'BatchOperateCamStrategy', 'cam.api.qcloud.com')
