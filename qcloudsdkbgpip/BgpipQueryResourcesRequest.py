# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class BgpipQueryResourcesRequest(Request):

    def __init__(self):
        super(BgpipQueryResourcesRequest, self).__init__(
            'bgpip', 'qcloudcliV1', 'BgpipQueryResources', 'bgpip.api.qcloud.com')

    def get_region(self):
        return self.get_params().get('region')

    def set_region(self, region):
        self.add_param('region', region)

    def get_resourceIds(self):
        return self.get_params().get('resourceIds')

    def set_resourceIds(self, resourceIds):
        self.add_param('resourceIds', resourceIds)
