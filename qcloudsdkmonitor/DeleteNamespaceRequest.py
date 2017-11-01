# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteNamespaceRequest(Request):

    def __init__(self):
        super(DeleteNamespaceRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'DeleteNamespace', 'monitor.api.qcloud.com')

    def get_namespace(self):
        return self.get_params().get('namespace')

    def set_namespace(self, namespace):
        self.add_param('namespace', namespace)
