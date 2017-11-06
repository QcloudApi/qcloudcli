# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DetachClassicLinkVpcRequest(Request):

    def __init__(self):
        super(DetachClassicLinkVpcRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DetachClassicLinkVpc', 'vpc.api.qcloud.com')

    def get_instanceIds(self):
        return self.get_params().get('instanceIds')

    def set_instanceIds(self, instanceIds):
        self.add_param('instanceIds', instanceIds)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
