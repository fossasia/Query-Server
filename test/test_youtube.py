from bs4 import BeautifulSoup

from app.scrapers import Youtube


def test_parse_response():
    html_text = ('<a href="/channel/UCQprMsG-raCIMlBudm20iLQ" '
                 'class="yt-uix-sessionlink">mock_channel</a><a href='
                 '"/watch?v=mock" class="yt-uix-tile-link yt-ui-ellipsis '
                 'yt-ui-ellipsis-2 yt-uix-sessionlink" '
                 'title="mock_title">mock_title</a>')
    dummy_soup = BeautifulSoup(html_text, 'html.parser')
    expected_resp = [{
        'title': u'mock_title',
        'link': u'https://www.youtube.com/watch?v=mock'
    }]
    resp = Youtube().parse_response(dummy_soup)
    assert resp == expected_resp


def test_search_youtube_without_count():
    query = 'fossasia'
    expected_max_resp_count = 10
    resp_count = len(Youtube().search(query))
    assert resp_count == expected_max_resp_count


def test_search_youtube_with_small_count():
    query = 'fossasia'
    expected_resp_count = 2
    resp_count = len(Youtube().search(query, 2))
    assert resp_count == expected_resp_count


# Youtube search for "fossasia" returns 23 results
def test_search_youtube_with_large_count():
    query = 'fossasia'
    actual_resp_count = 23
    expected_max_resp_count = 27
    resp_count = len(Youtube().search(query, 27))
    assert (resp_count == actual_resp_count) and \
           (resp_count <= expected_max_resp_count)
