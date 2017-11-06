# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class SyncImagesRequest(Request):

    def __init__(self):
        super(SyncImagesRequest, self).__init__(
            'image', 'qcloudcliV1', 'SyncImages', 'image.api.qcloud.com')

    def get_DestinationRegions(self):
        return self.get_params().get('DestinationRegions')

    def set_DestinationRegions(self, DestinationRegions):
        self.add_param('DestinationRegions', DestinationRegions)

    def get_ImageIds(self):
        return self.get_params().get('ImageIds')

    def set_ImageIds(self, ImageIds):
        self.add_param('ImageIds', ImageIds)
