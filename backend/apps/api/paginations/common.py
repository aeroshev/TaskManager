from collections import OrderedDict
from typing import List, MutableMapping

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.utils.urls import remove_query_param


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data: List[MutableMapping]) -> Response:
        url = self.request.build_absolute_uri()
        page = self.request.query_params.get(self.page_query_param, 1)
        if page == 'last':
            page = self.page.paginator.num_pages
        return Response(OrderedDict([
            ('page', int(page)),
            ('count', self.page.paginator.count),
            ('base_url', remove_query_param(url, self.page_query_param)),
            ('result', data),
        ]))
