# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import requests_mock
from .unittestsetup import test_generic, ReqMockTest
import saxo_openapi.endpoints.trading as tr
from parameterized import parameterized


class TestSaxo_Trading_Orders(ReqMockTest):
    """Tests for `trading-orders` endpoints."""

    def setUp(self):
        super(TestSaxo_Trading_Orders, self).setUp()

    @parameterized.expand([
        (tr.orders, "Order", {}),
        (tr.orders, "ChangeOrder", {}),
        (tr.orders, "CancelOrders", {'OrderIds': '6289286'}),
        (tr.orders, "PrecheckOrder", {})
      ])
    @requests_mock.Mocker(kw='mock')
    def test_all(self, _mod, clsNm, route, **kwargs):
        test_generic(self, _mod, clsNm, route, **kwargs)
