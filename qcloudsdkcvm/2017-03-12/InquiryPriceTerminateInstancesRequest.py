# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class InquiryPriceTerminateInstancesRequest(Request):

    def __init__(self):
        super(InquiryPriceTerminateInstancesRequest, self).__init__(
            'cvm', 'qcloudcliV1', 'InquiryPriceTerminateInstances', 'cvm.api.qcloud.com')

    def get_InstanceIds(self):
        return self.get_params().get('InstanceIds')

    def set_InstanceIds(self, InstanceIds):
        self.add_param('InstanceIds', InstanceIds)
