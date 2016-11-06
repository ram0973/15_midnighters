# -*- coding: utf-8 -*-
import requests
from datetime import datetime
import pendulum
from helpers import enable_win_unicode_console, handle_requests_exceptions

DEVMAN_ATTEMPTS_URL = 'https://devman.org/api/challenges/solution_attempts/'
MIDNIGHT_END = 6


@handle_requests_exceptions
def load_attempts():
    """ Получаем json с данными по попыткам сдачи """
    response = requests.get(DEVMAN_ATTEMPTS_URL)
    response.raise_for_status()
    for page in range(1, response.json()['number_of_pages']+1):
        page_items = requests.get(
            DEVMAN_ATTEMPTS_URL, params={'page': page}).json()['records']
        yield from page_items


def is_midnight(attempt: dict) -> bool:
    """ Проверяем, полуночная ли была попытка
    :param attempt: словарь с данными попытки сдачи
    :return: True если попытка была полуночной
    """
    if attempt['timezone'] is None or attempt['timestamp'] is None:
        return None
    attempt_time = pendulum.timezone(attempt['timezone']).convert(
        datetime.fromtimestamp(attempt['timestamp']))
    return True if attempt_time.hour < MIDNIGHT_END else False


def get_midnighters() -> list:
    return sorted({attempt['username'] for attempt in load_attempts()
                   if is_midnight(attempt)})


def main():
    enable_win_unicode_console()
    print('\nСписок кодеров - полуночников:')
    print(', '.join(get_midnighters()))


if __name__ == '__main__':
    main()
