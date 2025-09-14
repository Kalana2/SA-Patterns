from abc import ABC, abstractmethod
from typing import Optional


# handler interface
class Handler(ABC):
    def __init__(self):
        self._next_handler: Handler | None = None

    @abstractmethod
    def set_next(self, handler: "Handler") -> "Handler":
        pass

    @abstractmethod
    def handle(self, request: str) -> None | str:
        pass


# concrete handler
class lowercaseHandler(Handler):
    _next_handler: Handler | None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, request: str) -> None | str:
        if request.islower():
            return f"lowercaseHandler handled the request: {request}"
        elif self._next_handler:
            return self._next_handler.handle(request)
        return None


class uppercaseHandler(Handler):
    _next_handler: Handler | None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, request: str) -> None | str:
        if request.isupper():
            return f"uppercaseHandler handled the request: {request}"
        elif self._next_handler:
            return self._next_handler.handle(request)
        return None


class numberHandler(Handler):
    _next_handler: Handler | None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, request: str) -> None | str:
        if request.isdigit():
            return f"numberHandler handled the request: {request}"
        elif self._next_handler:
            return self._next_handler.handle(request)
        return None


# client code
def client_code(handler: Handler) -> None:
    for request in ["hello", "WORLD", "12345", "MixedCase"]:
        print(f"\nClient: Who wants to handle the request '{request}'?")
        result = handler.handle(request)
        if result:
            print(f"  {result}")
        else:
            print(f"  {request} was left unhandled.")


if __name__ == "__main__":
    # create handlers
    lowercase_handler = lowercaseHandler()
    uppercase_handler = uppercaseHandler()
    number_handler = numberHandler()

    # set up the chain of responsibility
    lowercase_handler.set_next(uppercase_handler).set_next(number_handler)

    # start the client code with the first handler in the chain
    client_code(lowercase_handler)
