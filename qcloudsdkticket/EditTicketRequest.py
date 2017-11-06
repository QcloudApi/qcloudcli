# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class EditTicketRequest(Request):

    def __init__(self):
        super(EditTicketRequest, self).__init__(
            'ticket', 'qcloudcliV1', 'EditTicket', 'ticket.api.qcloud.com')

    def get_appraisal(self):
        return self.get_params().get('appraisal')

    def set_appraisal(self, appraisal):
        self.add_param('appraisal', appraisal)

    def get_content(self):
        return self.get_params().get('content')

    def set_content(self, content):
        self.add_param('content', content)

    def get_modUin(self):
        return self.get_params().get('modUin')

    def set_modUin(self, modUin):
        self.add_param('modUin', modUin)

    def get_ownerUin(self):
        return self.get_params().get('ownerUin')

    def set_ownerUin(self, ownerUin):
        self.add_param('ownerUin', ownerUin)

    def get_service_rate(self):
        return self.get_params().get('service_rate')

    def set_service_rate(self, service_rate):
        self.add_param('service_rate', service_rate)

    def get_ticketId(self):
        return self.get_params().get('ticketId')

    def set_ticketId(self, ticketId):
        self.add_param('ticketId', ticketId)
