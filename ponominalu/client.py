# -*- coding: utf-8 -*-
"""
    ponominalu.client
    ~~~~~~~~~~~~~~~~~

    Implementation of client API for ponominalu.ru.

    :copyright: (c) 2015 by Rambler&Co.
"""

from base import BaseAPI


class PonominaluAPI(BaseAPI):
    host = 'https://api.cultserv.ru/jtransport/partner'

    def __init__(self, key=None):
        super(PonominaluAPI, self).__init__(key or '123')

    def categories(self, **kwargs):
        return self.request(
            path='get_categories',
            **kwargs
        )

    def events(self, **kwargs):
        return self.request(
            path='get_events',
            allowed_params=[
                'category',
                'limit',
                'offset',
                'min_date',
                'exclude',
                'title',
            ],
            **kwargs
        )

    def all_events(self, **kwargs):
        return self.request(
            path='get_all_events',
            allowed_params=[
                'alias',
                'limit',
                'offset',
            ],
            **kwargs
        )

    def event(self, **kwargs):
        return self.request(
            path='get_subevent',
            allowed_params=['id', 'alias'],
            **kwargs
        )

    def description(self, **kwargs):
        return self.request(
            path='get_description',
            allowed_params=['subevent_id'],
            **kwargs
        )

    def places(self, **kwargs):
        return self.request(
            path='get_venues',
            allowed_params=['title', 'limit', 'offset', 'exclude'],
            **kwargs
        )

    def place(self, **kwargs):
        return self.request(
            path='get_venue',
            allowed_params=['id'],
            **kwargs
        )
