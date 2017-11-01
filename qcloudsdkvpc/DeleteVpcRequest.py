# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteVpcRequest(Request):

    def __init__(self):
        super(DeleteVpcRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DeleteVpc', 'vpc.api.qcloud.com')

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
