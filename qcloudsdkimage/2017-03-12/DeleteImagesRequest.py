# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteImagesRequest(Request):

    def __init__(self):
        super(DeleteImagesRequest, self).__init__(
            'image', 'qcloudcliV1', 'DeleteImages', 'image.api.qcloud.com')

    def get_ImageIds(self):
        return self.get_params().get('ImageIds')

    def set_ImageIds(self, ImageIds):
        self.add_param('ImageIds', ImageIds)
