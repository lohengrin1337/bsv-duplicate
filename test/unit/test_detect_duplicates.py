import pytest
from unittest.mock import patch, MagicMock
from src.util.detector import detect_duplicates

pytestmark = pytest.mark.unit

# @pytest.fixture
# @patch('src.util.detector.parse', autospec=True)
# @patch('src.util.detector.Article', autospec=True)
# def sut_one_entry(mock_article, mock_parse):
#     mock_article.return_value = None
#     mock_parse.return_value = [mock_article]
#     return detect_duplicates

@pytest.fixture
def sut():
    def _sut(parse_return_val):
        with patch('src.util.detector.parse', autospec=True) as mock_parse:
            mock_parse.return_value = parse_return_val
            return detect_duplicates(data=None)
    return _sut

# TC 1
def test_1(sut):
    with pytest.raises(ValueError):
        sut(["one bibtex entry"])



# @pytest.fixture
# @patch('src.util.detector.parse', autospec=True)
# @patch('src.util.detector.Article', autospec=True)
# def sut_two_entries(mock_article, mock_parse):
#     mock_article.return_value = None
#     mock_parse.return_value = [mock_article, mock_article]
#     return detect_duplicates

# TC 1
# def test_one_entry(sut_one_entry):
#     """ Should raise ValueError """
#     with pytest.raises(ValueError):
#         result = sut_one_entry(data=None)

# @patch('src.util.detector.parse', autospec=True)
# @patch('src.util.detector.Article', autospec=True)
# def test_one_entry(mock_article, mock_parse):
#     """ Should raise ValueError """
#     mock_article.return_value = None
#     mock_parse.return_value = [mock_article]
#     with pytest.raises(ValueError):
#         result = detect_duplicates(data=None)


# TC 2
