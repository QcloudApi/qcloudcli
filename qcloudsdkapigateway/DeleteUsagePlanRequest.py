# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteUsagePlanRequest(Request):

    def __init__(self):
        super(DeleteUsagePlanRequest, self).__init__(
            'apigateway', 'qcloudcliV1', 'DeleteUsagePlan', 'apigateway.api.qcloud.com')

    def get_usagePlanId(self):
        return self.get_params().get('usagePlanId')

    def set_usagePlanId(self, usagePlanId):
        self.add_param('usagePlanId', usagePlanId)
