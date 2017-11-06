# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class BgpipModifyResourceRequest(Request):

    def __init__(self):
        super(BgpipModifyResourceRequest, self).__init__(
            'bgpip', 'qcloudcliV1', 'BgpipModifyResource', 'bgpip.api.qcloud.com')

    def get_curDeadline(self):
        return self.get_params().get('curDeadline')

    def set_curDeadline(self, curDeadline):
        self.add_param('curDeadline', curDeadline)

    def get_newBandwidth(self):
        return self.get_params().get('newBandwidth')

    def set_newBandwidth(self, newBandwidth):
        self.add_param('newBandwidth', newBandwidth)

    def get_oldBandwidth(self):
        return self.get_params().get('oldBandwidth')

    def set_oldBandwidth(self, oldBandwidth):
        self.add_param('oldBandwidth', oldBandwidth)

    def get_region(self):
        return self.get_params().get('region')

    def set_region(self, region):
        self.add_param('region', region)

    def get_resourceId(self):
        return self.get_params().get('resourceId')

    def set_resourceId(self, resourceId):
        self.add_param('resourceId', resourceId)
