# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetTicketListRequest(Request):

    def __init__(self):
        super(GetTicketListRequest, self).__init__(
            'ticket', 'qcloudcliV1', 'GetTicketList', 'ticket.api.qcloud.com')

    def get_end(self):
        return self.get_params().get('end')

    def set_end(self, end):
        self.add_param('end', end)

    def get_language(self):
        return self.get_params().get('language')

    def set_language(self, language):
        self.add_param('language', language)

    def get_order(self):
        return self.get_params().get('order')

    def set_order(self, order):
        self.add_param('order', order)

    def get_orderField(self):
        return self.get_params().get('orderField')

    def set_orderField(self, orderField):
        self.add_param('orderField', orderField)

    def get_ownerUin(self):
        return self.get_params().get('ownerUin')

    def set_ownerUin(self, ownerUin):
        self.add_param('ownerUin', ownerUin)

    def get_page(self):
        return self.get_params().get('page')

    def set_page(self, page):
        self.add_param('page', page)

    def get_rows(self):
        return self.get_params().get('rows')

    def set_rows(self, rows):
        self.add_param('rows', rows)

    def get_search(self):
        return self.get_params().get('search')

    def set_search(self, search):
        self.add_param('search', search)

    def get_start(self):
        return self.get_params().get('start')

    def set_start(self, start):
        self.add_param('start', start)

    def get_statusId(self):
        return self.get_params().get('statusId')

    def set_statusId(self, statusId):
        self.add_param('statusId', statusId)

    def get_statusIdList(self):
        return self.get_params().get('statusIdList')

    def set_statusIdList(self, statusIdList):
        self.add_param('statusIdList', statusIdList)
