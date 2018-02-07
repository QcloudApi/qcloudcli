# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DataManipulationRequest(Request):

    def __init__(self):
        super(DataManipulationRequest, self).__init__(
            'yunsou', 'qcloudcliV1', 'DataManipulation', 'yunsou.api.qcloud.com')

    def get_Timestamp(self):
        return self.get_params().get('Timestamp')

    def set_Timestamp(self, Timestamp):
        self.add_param('Timestamp', Timestamp)

    def get_appId(self):
        return self.get_params().get('appId')

    def set_appId(self, appId):
        self.add_param('appId', appId)

    def get_contents(self):
        return self.get_params().get('contents')

    def set_contents(self, contents):
        self.add_param('contents', contents)

    def get_encoding(self):
        return self.get_params().get('encoding')

    def set_encoding(self, encoding):
        self.add_param('encoding', encoding)

    def get_op_type(self):
        return self.get_params().get('op_type')

    def set_op_type(self, op_type):
        self.add_param('op_type', op_type)
