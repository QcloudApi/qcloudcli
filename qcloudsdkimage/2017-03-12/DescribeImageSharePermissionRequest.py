# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeImageSharePermissionRequest(Request):

    def __init__(self):
        super(DescribeImageSharePermissionRequest, self).__init__(
            'image', 'qcloudcliV1', 'DescribeImageSharePermission', 'image.api.qcloud.com')

    def get_ImageId(self):
        return self.get_params().get('ImageId')

    def set_ImageId(self, ImageId):
        self.add_param('ImageId', ImageId)
