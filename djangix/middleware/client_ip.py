class ClientIPMiddleware:
    """ Добавляем IP клиента к request-у """

    def __init__(self, get_response):
        self.get_response = get_response

    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip

    def __call__(self, request):
        ip: str = self.get_client_ip(request)
        setattr(request, "ip", ip)

        response = self.get_response(request)

        return response
