import pytest
from unittest.mock import patch, MagicMock
from src.util.detector import detect_duplicates

pytestmark = pytest.mark.unit

@pytest.fixture
def sut():
    def _sut(articles):
        with patch('src.util.detector.parse', autospec=True) as mock_parse:
            mock_parse.return_value = articles
            return detect_duplicates(data=None)
    return _sut

@pytest.fixture
def article():
    def _article(key, doi):
        mock = MagicMock()
        mock.key.return_value = key
        mock.doi.return_value = doi
        return mock
    return _article

# TC 1
def test_1(sut):
    with pytest.raises(ValueError):
        sut(["one article"])


# TC 2-3
@pytest.mark.parametrize(
    "keys, dois",
    [
        (["key1", "key2"], ["doi1", "doi2"]),
        (["key1", "key2", "key3"], ["doi1", "doi2", "doi3"])
    ]
)
def test_2_3(sut, article, keys, dois):
    articles = [article(key, doi) for key, doi in zip(keys, dois)]
    result = sut(articles)
    assert result == []

# TC 4-5
@pytest.mark.parametrize(
    "keys, dois",
    [
        (["key1", "key1"], ["doi1", "doi1"]),
        (["key1", "key1", "key2"], ["doi1", "doi1", "doi2"])
    ]
)
def test_4_5(sut, article, keys, dois):
    articles = [article(key, doi) for key, doi in zip(keys, dois)]
    print(articles)
    result = sut(articles)
    print(result)
    assert result[0] == articles[0]
