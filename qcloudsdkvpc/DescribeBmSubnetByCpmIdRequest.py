# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeBmSubnetByCpmIdRequest(Request):

    def __init__(self):
        super(DescribeBmSubnetByCpmIdRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DescribeBmSubnetByCpmId', 'vpc.api.qcloud.com')

    def get_instanceId(self):
        return self.get_params().get('instanceId')

    def set_instanceId(self, instanceId):
        self.add_param('instanceId', instanceId)
