import functools
from typing import TypeVar, Callable, Any, Generic, ParamSpec

from typing_extensions import Coroutine

T_Retval = TypeVar("T_Retval")
T_ParamSpec = ParamSpec("T_ParamSpec")
T = TypeVar("T")


class Paginator(Generic[T_Retval]):
    def __init__(
        self,
        func: Callable[[T_ParamSpec], Coroutine[Any, Any, T]],
        *args: T_ParamSpec,
        **kwargs: T_ParamSpec.kwargs,
    ):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.page = 1
        self.last_page = None

    def __aiter__(self):
        return self

    async def __anext__(self) -> T_Retval:
        if self.last_page is not None and self.page > self.last_page:
            raise StopAsyncIteration
        response = await self.func(*self.args, page=self.page, **self.kwargs)
        self.page += 1
        self.last_page = response.meta.total_pages
        return response

# FIXME: types drops in some cases (pycharm?)
# The type definition eventually stop introspect when input is too complicated
# it works well with simple function like paginate(sleep)(unexpected_argument=3)

def paginate(func: Callable[T_ParamSpec, Coroutine[Any, Any, T_Retval]]) -> Callable[T_ParamSpec, Paginator[T_Retval]]:
    @functools.wraps(func)
    def wrapper(*args: T_ParamSpec.args, **kwargs: T_ParamSpec.kwargs) -> Paginator[T_Retval]:
        return Paginator(func, *args, **kwargs)

    return wrapper
