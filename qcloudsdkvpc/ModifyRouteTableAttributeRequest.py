# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyRouteTableAttributeRequest(Request):

    def __init__(self):
        super(ModifyRouteTableAttributeRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'ModifyRouteTableAttribute', 'vpc.api.qcloud.com')

    def get_routeSet(self):
        return self.get_params().get('routeSet')

    def set_routeSet(self, routeSet):
        self.add_param('routeSet', routeSet)

    def get_routeTableId(self):
        return self.get_params().get('routeTableId')

    def set_routeTableId(self, routeTableId):
        self.add_param('routeTableId', routeTableId)

    def get_routeTableName(self):
        return self.get_params().get('routeTableName')

    def set_routeTableName(self, routeTableName):
        self.add_param('routeTableName', routeTableName)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
