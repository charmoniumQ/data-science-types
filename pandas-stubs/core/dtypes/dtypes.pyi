from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    MutableMapping,
    Optional,
    Tuple,
    Type,
    Union,
    cast,
)

from .base import ExtensionDtype

str_type = str

class PandasExtensionDtype(ExtensionDtype):
    type: Any
    kind: Any
    # The Any type annotations above are here only because mypy seems to have a
    # problem dealing with with multiple inheritance from PandasExtensionDtype
    # and ExtensionDtype's @properties in the subclasses below. The kind and
    # type variables in those subclasses are explicitly typed below.
    subdtype = None
    str: str_type
    num = 100
    shape: Tuple[int, ...] = tuple()
    itemsize = 8
    base = None
    isbuiltin = 0
    isnative = 0

    def __str__(self) -> str_type: ...

    def __repr__(self) -> str_type: ...

    def __hash__(self) -> int: ...

    def __getstate__(self) -> Dict[str_type, Any]: ...

    @classmethod
    def reset_cache(cls) -> None: ...


class CategoricalDtypeType(type):
    ...


class CategoricalDtype(PandasExtensionDtype, ExtensionDtype):
    name: str
    type: Type[CategoricalDtypeType]
    kind: str_type
    str: str
    # base:  = np.dtype("O")

    def __init__(self, categories: Optional[Any]=None, ordered: Ordered = False):
        ...

    @classmethod
    def _from_fastpath(
        cls, categories: Optional[Any]=None, ordered: Optional[bool] = None
    ) -> CategoricalDtype:
        ...

    @classmethod
    def _from_categorical_dtype(
        cls, dtype: CategoricalDtype, categories: Optional[Any]=None, ordered: Ordered = None
    ) -> CategoricalDtype: ...

    @classmethod
    def _from_values_or_dtype(
        cls,
        values: Optional[Any]=None,
        categories: Optional[Any]=None,
        ordered: Optional[bool] = None,
        dtype: Optional[CategoricalDtype] = None,
    ) -> CategoricalDtype: ...

    @classmethod
    def construct_from_string(cls, string: str_type) -> CategoricalDtype:
        ...

    def _finalize(self, categories: Any, ordered: Ordered, fastpath: bool = False) -> None: ...

    def __setstate__(self, state: MutableMapping[str_type, Any]) -> None: ...

    def __hash__(self) -> int: ...

    def __eq__(self, other: Any) -> bool: ...

    def __repr__(self) -> str_type: ...

    @staticmethod
    def _hash_categories(categories, ordered: Ordered = True) -> int: ...

    @classmethod
    def construct_array_type(cls) -> Type[Categorical]: ...

    @staticmethod
    def validate_ordered(ordered: Ordered) -> None: ...

    @staticmethod
    def validate_categories(categories, fastpath: bool = False): ...

    def update_dtype(
        self, dtype: Union[str_type, "CategoricalDtype"]
    ) -> "CategoricalDtype": ...

    @property
    def categories(self): ...

    @property
    def ordered(self) -> Ordered: ...

    @property
    def _is_boolean(self) -> bool: ...

    def _get_common_dtype(self, dtypes: List[DtypeObj]) -> Optional[DtypeObj]: ...
