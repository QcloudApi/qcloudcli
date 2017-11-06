# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteRouteTableRequest(Request):

    def __init__(self):
        super(DeleteRouteTableRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DeleteRouteTable', 'vpc.api.qcloud.com')

    def get_routeTableId(self):
        return self.get_params().get('routeTableId')

    def set_routeTableId(self, routeTableId):
        self.add_param('routeTableId', routeTableId)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
