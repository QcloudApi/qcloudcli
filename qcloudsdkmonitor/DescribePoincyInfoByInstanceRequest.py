# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribePoincyInfoByInstanceRequest(Request):

    def __init__(self):
        super(DescribePoincyInfoByInstanceRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'DescribePoincyInfoByInstance', 'monitor.api.qcloud.com')

    def get_dimension(self):
        return self.get_params().get('dimension')

    def set_dimension(self, dimension):
        self.add_param('dimension', dimension)

    def get_viewName(self):
        return self.get_params().get('viewName')

    def set_viewName(self, viewName):
        self.add_param('viewName', viewName)
