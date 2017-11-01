# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyInstanceInternetChargeTypeRequest(Request):

    def __init__(self):
        super(ModifyInstanceInternetChargeTypeRequest, self).__init__(
            'cvm', 'qcloudcliV1', 'ModifyInstanceInternetChargeType', 'cvm.api.qcloud.com')

    def get_InstanceId(self):
        return self.get_params().get('InstanceId')

    def set_InstanceId(self, InstanceId):
        self.add_param('InstanceId', InstanceId)

    def get_InternetAccessible(self):
        return self.get_params().get('InternetAccessible')

    def set_InternetAccessible(self, InternetAccessible):
        self.add_param('InternetAccessible', InternetAccessible)

    def get_StartTime(self):
        return self.get_params().get('StartTime')

    def set_StartTime(self, StartTime):
        self.add_param('StartTime', StartTime)

    def get_EndTime(self):
        return self.get_params().get('EndTime')

    def set_EndTime(self, EndTime):
        self.add_param('EndTime', EndTime)
