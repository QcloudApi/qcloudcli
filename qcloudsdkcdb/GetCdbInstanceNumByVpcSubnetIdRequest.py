# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetCdbInstanceNumByVpcSubnetIdRequest(Request):

    def __init__(self):
        super(GetCdbInstanceNumByVpcSubnetIdRequest, self).__init__(
            'cdb', 'qcloudcliV1', 'GetCdbInstanceNumByVpcSubnetId', 'cdb.api.qcloud.com')

    def get_subnetIds(self):
        return self.get_params().get('subnetIds')

    def set_subnetIds(self, subnetIds):
        self.add_param('subnetIds', subnetIds)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
