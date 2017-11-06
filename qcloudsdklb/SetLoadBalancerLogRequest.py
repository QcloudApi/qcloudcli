# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class SetLoadBalancerLogRequest(Request):

    def __init__(self):
        super(SetLoadBalancerLogRequest, self).__init__(
            'lb', 'qcloudcliV1', 'SetLoadBalancerLog', 'lb.api.qcloud.com')

    def get_bucketName(self):
        return self.get_params().get('bucketName')

    def set_bucketName(self, bucketName):
        self.add_param('bucketName', bucketName)

    def get_loadBalancerId(self):
        return self.get_params().get('loadBalancerId')

    def set_loadBalancerId(self, loadBalancerId):
        self.add_param('loadBalancerId', loadBalancerId)

    def get_operate(self):
        return self.get_params().get('operate')

    def set_operate(self, operate):
        self.add_param('operate', operate)

    def get_period(self):
        return self.get_params().get('period')

    def set_period(self, period):
        self.add_param('period', period)

    def get_switch(self):
        return self.get_params().get('switch')

    def set_switch(self, switch):
        self.add_param('switch', switch)
