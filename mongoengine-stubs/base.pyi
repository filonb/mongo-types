from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    NoReturn,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
)

from bson.son import SON

U = TypeVar("U", bound="BaseDocument")

class BaseDocument:
    def to_mongo(
        self, use_db_field: bool = ..., fields: List[str] = ...
    ) -> SON[Any, Any]: ...
    def validate(self, clean: bool = ...) -> None: ...
    def to_json(self, *args: Any, **kwargs: Any) -> str: ...
    @classmethod
    def from_json(
        cls: Type[U], json_data: Dict[str, Any], created: bool = ...
    ) -> U: ...
    def _delta(self) -> Tuple[Dict[str, Any], Dict[str, Any]]: ...
    @classmethod
    def _get_collection_name(cls) -> Optional[str]: ...
    @classmethod
    def _from_son(
        cls: Type[U],
        son: Dict[str, Any],
        _auto_dereference: bool = ...,
        only_fields: Optional[List[str]] = ...,
        created: bool = ...,
    ) -> U: ...
    def __getitem__(self, name) -> Any: ...

class BaseField:
    def __new__(
        cls,
        db_field: str = ...,
        name: Optional[str] = ...,
        required: bool = ...,
        default: Union[Any, None, Callable[[], Any]] = ...,
        unique: bool = ...,
        unique_with: Union[str, Iterable[str]] = ...,
        primary_key: bool = ...,
        choices: Optional[Iterable[Any]] = ...,
        null: bool = ...,
        verbose_name: Optional[str] = ...,
        help_text: Optional[str] = ...,
    ) -> BaseField: ...
    def __set__(self, instance: Any, value: Any) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> Any: ...
    def validate(self, value: Any, clean: bool = ...) -> None: ...
    def prepare_query_value(self, op: str, value: Any) -> Any: ...
    def error(
        self,
        message: str,
        errors: Union[Dict[str, Any], None] = ...,
        field_name: Union[str, None] = ...,
    ) -> NoReturn: ...
    def to_python(self, value: Any) -> Any: ...
    def to_mongo(self, value: Any) -> Any: ...

class ComplexBaseField(BaseField): ...
