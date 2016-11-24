# -*- coding: utf-8 -*-
import requests
import pendulum

DEVMAN_ATTEMPTS_URL = 'https://devman.org/api/challenges/solution_attempts/'
MIDNIGHT_END = 6


def load_attempts():
    response = requests.get(DEVMAN_ATTEMPTS_URL)
    for page in range(1, response.json()['number_of_pages']+1):
        page_items = requests.get(
            DEVMAN_ATTEMPTS_URL, params={'page': page}).json()['records']
        yield from page_items


def is_midnight(attempt):
    if attempt['timezone'] is None or attempt['timestamp'] is None:
        return None
    attempt_time = pendulum.from_timestamp(
        attempt['timestamp'], attempt['timezone'])
    return attempt_time.hour < MIDNIGHT_END


def get_midnighters_names():
    return sorted({attempt['username'] for attempt in load_attempts()
                   if is_midnight(attempt)})

if __name__ == '__main__':
    print('\nMidnight coders list:')
    print(', '.join(get_midnighters_names()))
