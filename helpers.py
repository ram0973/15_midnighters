# -*- coding: utf-8 -*-
import sys
import requests


def enable_win_unicode_console():
    """
    Включаем правильное отображение unicode в консоли под MS Windows
    """
    if sys.platform == 'win32':
        import win_unicode_console
        win_unicode_console.enable()


def handle_requests_exceptions(decorated):
    """
    Декоратор, обрабатывающий ошибки в requests
    :param decorated: Функция, в которой надо отловить requests exceptions
    :return: функция-декоратор
    """
    def decorator(*args, **kwargs):
        try:
            return decorated(*args, **kwargs)
        except requests.ConnectionError:
            print('Ошибка сетевого соединения')
            exit(1)
        except requests.HTTPError as e:
            print('Сервер вернул неудачный код статуса ответа: %s %i' %
                  (e.response.reason, e.response.status_code))
            exit(1)
        except requests.Timeout:
            print('Вышло время ожидания ответа от сервера')
            exit(1)
        except requests.TooManyRedirects:
            print('Слишком много редиректов')
            exit(1)

    return decorator