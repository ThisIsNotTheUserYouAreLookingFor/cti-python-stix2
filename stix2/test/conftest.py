import uuid

import pytest

import stix2

from .constants import (FAKE_TIME, INDICATOR_KWARGS, MALWARE_KWARGS,
                        RELATIONSHIP_KWARGS)


# Inspired by: http://stackoverflow.com/a/24006251
@pytest.fixture
def clock(monkeypatch):

    class mydatetime(stix2.utils.STIXdatetime):
        @classmethod
        def now(cls, tz=None):
            return FAKE_TIME

    monkeypatch.setattr(stix2.utils, 'STIXdatetime', mydatetime)


@pytest.fixture
def uuid4(monkeypatch):
    def wrapper():
        data = [0]

        def wrapped():
            data[0] += 1
            return "00000000-0000-0000-0000-00000000%04x" % data[0]

        return wrapped
    monkeypatch.setattr(uuid, "uuid4", wrapper())


@pytest.fixture
def indicator(uuid4, clock):
    return stix2.Indicator(**INDICATOR_KWARGS)


@pytest.fixture
def malware(uuid4, clock):
    return stix2.Malware(**MALWARE_KWARGS)


@pytest.fixture
def relationship(uuid4, clock):
    return stix2.Relationship(**RELATIONSHIP_KWARGS)


@pytest.fixture
def stix1_objs():
    ind1 = {
        "created": "2017-01-27T13:49:53.935Z",
        "id": "indicator--d81f86b9-975b-bc0b-775e-810c5ad45a4f",
        "labels": [
            "url-watchlist"
        ],
        "modified": "2017-01-27T13:49:53.935Z",
        "name": "Malicious site hosting downloader",
        "pattern": "[url:value = 'http://x4z9arb.cn/4712']",
        "type": "indicator",
        "valid_from": "2017-01-27T13:49:53.935382Z"
    }
    ind2 = {
        "created": "2017-01-27T13:49:53.935Z",
        "id": "indicator--d81f86b9-975b-bc0b-775e-810c5ad45a4f",
        "labels": [
            "url-watchlist"
        ],
        "modified": "2017-01-27T13:49:53.935Z",
        "name": "Malicious site hosting downloader",
        "pattern": "[url:value = 'http://x4z9arb.cn/4712']",
        "type": "indicator",
        "valid_from": "2017-01-27T13:49:53.935382Z"
    }
    ind3 = {
        "created": "2017-01-27T13:49:53.935Z",
        "id": "indicator--d81f86b9-975b-bc0b-775e-810c5ad45a4f",
        "labels": [
            "url-watchlist"
        ],
        "modified": "2017-01-27T13:49:53.936Z",
        "name": "Malicious site hosting downloader",
        "pattern": "[url:value = 'http://x4z9arb.cn/4712']",
        "type": "indicator",
        "valid_from": "2017-01-27T13:49:53.935382Z"
    }
    ind4 = {
        "created": "2017-01-27T13:49:53.935Z",
        "id": "indicator--d81f86b8-975b-bc0b-775e-810c5ad45a4f",
        "labels": [
            "url-watchlist"
        ],
        "modified": "2017-01-27T13:49:53.935Z",
        "name": "Malicious site hosting downloader",
        "pattern": "[url:value = 'http://x4z9arb.cn/4712']",
        "type": "indicator",
        "valid_from": "2017-01-27T13:49:53.935382Z"
    }
    ind5 = {
        "created": "2017-01-27T13:49:53.935Z",
        "id": "indicator--d81f86b8-975b-bc0b-775e-810c5ad45a4f",
        "labels": [
            "url-watchlist"
        ],
        "modified": "2017-01-27T13:49:53.935Z",
        "name": "Malicious site hosting downloader",
        "pattern": "[url:value = 'http://x4z9arb.cn/4712']",
        "type": "indicator",
        "valid_from": "2017-01-27T13:49:53.935382Z"
    }
    return [ind1, ind2, ind3, ind4, ind5]


@pytest.fixture
def stix2_objs():
    ind6 = {
        "created": "2017-01-27T13:49:53.935Z",
        "id": "indicator--d81f86b9-975b-bc0b-775e-810c5ad45a4f",
        "labels": [
            "url-watchlist"
        ],
        "modified": "2017-01-31T13:49:53.935Z",
        "name": "Malicious site hosting downloader",
        "pattern": "[url:value = 'http://x4z9arb.cn/4712']",
        "type": "indicator",
        "valid_from": "2017-01-27T13:49:53.935382Z"
    }
    ind7 = {
        "created": "2017-01-27T13:49:53.935Z",
        "id": "indicator--d81f86b8-975b-bc0b-775e-810c5ad45a4f",
        "labels": [
            "url-watchlist"
        ],
        "modified": "2017-01-27T13:49:53.935Z",
        "name": "Malicious site hosting downloader",
        "pattern": "[url:value = 'http://x4z9arb.cn/4712']",
        "type": "indicator",
        "valid_from": "2017-01-27T13:49:53.935382Z"
    }
    ind8 = {
        "created": "2017-01-27T13:49:53.935Z",
        "id": "indicator--d81f86b8-975b-bc0b-775e-810c5ad45a4f",
        "labels": [
            "url-watchlist"
        ],
        "modified": "2017-01-27T13:49:53.935Z",
        "name": "Malicious site hosting downloader",
        "pattern": "[url:value = 'http://x4z9arb.cn/4712']",
        "type": "indicator",
        "valid_from": "2017-01-27T13:49:53.935382Z"
    }
    return [ind6, ind7, ind8]
