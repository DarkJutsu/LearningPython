class MyRoute:
    _instance=None
    route=None

    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
            cls._instance.route=None
        return cls._instance

    def set_route(self, str_route):
        self.route=str_route

    def get_route(self):
        return self.route