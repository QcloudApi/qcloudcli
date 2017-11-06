# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeImagesRequest(Request):

    def __init__(self):
        super(DescribeImagesRequest, self).__init__(
            'image', 'qcloudcliV1', 'DescribeImages', 'image.api.qcloud.com')

    def get_Filters(self):
        return self.get_params().get('Filters')

    def set_Filters(self, Filters):
        self.add_param('Filters', Filters)

    def get_ImageIds(self):
        return self.get_params().get('ImageIds')

    def set_ImageIds(self, ImageIds):
        self.add_param('ImageIds', ImageIds)

    def get_InstanceType(self):
        return self.get_params().get('InstanceType')

    def set_InstanceType(self, InstanceType):
        self.add_param('InstanceType', InstanceType)

    def get_IsInner(self):
        return self.get_params().get('IsInner')

    def set_IsInner(self, IsInner):
        self.add_param('IsInner', IsInner)

    def get_Language(self):
        return self.get_params().get('Language')

    def set_Language(self, Language):
        self.add_param('Language', Language)

    def get_Limit(self):
        return self.get_params().get('Limit')

    def set_Limit(self, Limit):
        self.add_param('Limit', Limit)

    def get_Offset(self):
        return self.get_params().get('Offset')

    def set_Offset(self, Offset):
        self.add_param('Offset', Offset)
