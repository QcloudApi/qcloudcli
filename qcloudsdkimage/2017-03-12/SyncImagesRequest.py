# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class SyncImagesRequest(Request):

    def __init__(self):
        super(SyncImagesRequest, self).__init__(
            'image', 'qcloudcliV1', 'SyncImages', 'image.api.qcloud.com')

    def get_ImageIds(self):
        return self.get_params().get('ImageIds')

    def set_ImageIds(self, ImageIds):
        self.add_param('ImageIds', ImageIds)

    def get_DestinationRegionId(self):
        return self.get_params().get('DestinationRegionId')

    def set_DestinationRegionId(self, DestinationRegionId):
        self.add_param('DestinationRegionId', DestinationRegionId)
