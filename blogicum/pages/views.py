"""Статические страницы и обработчики ошибок проекта."""
from django.shortcuts import render


def page_not_found(request, exception):
    """Кастомная страница ошибки 404."""
    return render(request, 'pages/404.html', status=404)


def csrf_failure(request, reason=''):
    """Кастомная страница ошибки 403 (сбой проверки CSRF)."""
    return render(request, 'pages/403csrf.html', status=403)


def server_error(request):
    """Кастомная страница ошибки 500."""
    return render(request, 'pages/500.html', status=500)
