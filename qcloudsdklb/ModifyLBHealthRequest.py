# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyLBHealthRequest(Request):

    def __init__(self):
        super(ModifyLBHealthRequest, self).__init__(
            'lb', 'qcloudcliV1', 'ModifyLBHealth', 'lb.api.qcloud.com')

    def get_healthNum(self):
        return self.get_params().get('healthNum')

    def set_healthNum(self, healthNum):
        self.add_param('healthNum', healthNum)

    def get_intervalTime(self):
        return self.get_params().get('intervalTime')

    def set_intervalTime(self, intervalTime):
        self.add_param('intervalTime', intervalTime)

    def get_loadBalanceId(self):
        return self.get_params().get('loadBalanceId')

    def set_loadBalanceId(self, loadBalanceId):
        self.add_param('loadBalanceId', loadBalanceId)

    def get_switch(self):
        return self.get_params().get('switch')

    def set_switch(self, switch):
        self.add_param('switch', switch)

    def get_timeOut(self):
        return self.get_params().get('timeOut')

    def set_timeOut(self, timeOut):
        self.add_param('timeOut', timeOut)

    def get_unhealthNum(self):
        return self.get_params().get('unhealthNum')

    def set_unhealthNum(self, unhealthNum):
        self.add_param('unhealthNum', unhealthNum)
