class MethodNotImplemented(Exception):
    pass


class IArray:

    def put(self, item: int, index: int = None) -> None:
        raise MethodNotImplemented

    def get(self, index: int) -> int:
        raise MethodNotImplemented

    def add(self, item: int) -> None:
        raise MethodNotImplemented

    def remove(self, index: int) -> int:
        raise MethodNotImplemented

