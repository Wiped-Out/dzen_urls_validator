import pytest

from dzen_urls_validator import validate_url


@pytest.mark.parametrize(
    ('input_url', 'expected_url'),
    (
            ('dzen.ru/id/5ce671035b6e3000b303d27a', 'https://dzen.ru/id/5ce671035b6e3000b303d27a'),
            ('http://dzen.ru/id/5ce671035b6e3000b303d27a', 'https://dzen.ru/id/5ce671035b6e3000b303d27a'),
            ('https://dzen.ru/id/5ce671035b6e3000b303d27a', 'https://dzen.ru/id/5ce671035b6e3000b303d27a'),
    )
)
def test_https_prefix(input_url: str, expected_url: str):
    assert validate_url(input_url) == expected_url


@pytest.mark.parametrize(
    ('input_url', 'expected_url'),
    (
            ('https://dzen.ru/id/5ce671035b6e3000b303d27a', 'https://dzen.ru/id/5ce671035b6e3000b303d27a'),
            ('https://zen.yandex.ru/id/5ce671035b6e3000b303d27a', 'https://dzen.ru/id/5ce671035b6e3000b303d27a'),
    )
)
def test_host_replacement(input_url: str, expected_url: str):
    assert validate_url(input_url) == expected_url
