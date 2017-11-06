# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class AssociateRouteTableRequest(Request):

    def __init__(self):
        super(AssociateRouteTableRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'AssociateRouteTable', 'vpc.api.qcloud.com')

    def get_routeTableId(self):
        return self.get_params().get('routeTableId')

    def set_routeTableId(self, routeTableId):
        self.add_param('routeTableId', routeTableId)

    def get_subnetId(self):
        return self.get_params().get('subnetId')

    def set_subnetId(self, subnetId):
        self.add_param('subnetId', subnetId)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
