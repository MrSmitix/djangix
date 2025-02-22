from django.utils import timezone

from django.contrib.auth import SESSION_KEY
from django.contrib.sessions.models import Session


def get_all_sessions_from_user(user_pk: int) -> [(str, dict)]:
    """
    Возвращает все активные сессий пользователя в виде списка (session_key, session_data (decoded))

    :param user_pk: уникальный ID пользователя
    :return: список активных сессий
    """

    user_sessions = []

    for session in Session.objects.filter(expire_date__gte=timezone.now()):
        decoded_session_data = session.get_decoded()
        if decoded_session_data.get(SESSION_KEY, None) == str(user_pk):
            user_sessions.append((session.session_key, decoded_session_data))

    return user_sessions
