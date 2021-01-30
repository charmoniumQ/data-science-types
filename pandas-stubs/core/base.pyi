"""
Base and utility classes for pandas objects.
"""

from typing import Any, Dict, FrozenSet, List, Optional, Union

from pandas.core.arrays import ExtensionArray

class PandasObject:

    def __repr__(self) -> str: ...

    def __sizeof__(self): ...


class NoNewAttributesMixin:
    def _freeze(self) -> None: ...

    def __setattr__(self, key: str, value) -> None: ...


class DataError(Exception):
    pass


class SpecificationError(Exception):
    pass


class SelectionMixin:
    def __getitem__(self, key): ...

    def aggregate(self, func, *args, **kwargs): ...

    agg = aggregate


class ShallowMixin:
    ...


class IndexOpsMixin:
    def transpose(self, *args, **kwargs): ...

    T = property(
        transpose,
        doc="""
        Return the transpose, which is by definition self.
        """,
    )

    @property
    def shape(self): ...

    def __len__(self) -> int: ...

    @property
    def ndim(self) -> int: ...

    def item(self): ...

    @property
    def nbytes(self) -> int: ...

    @property
    def size(self) -> int: ...

    @property
    def array(self) -> ExtensionArray: ...

    def to_numpy(self, dtype=None, copy=False, na_value=lib.no_default, **kwargs): ...

    @property
    def empty(self): ...

    def max(self, axis=None, skipna=True, *args, **kwargs): ...

    def argmax(self, axis=None, skipna=True, *args, **kwargs): ...

    def min(self, axis=None, skipna=True, *args, **kwargs): ...

    def argmin(self, axis=None, skipna=True, *args, **kwargs): ...

    def tolist(self): ...

    to_list = tolist

    def __iter__(self): ...

    def hasnans(self): ...


    def value_counts(
        self, normalize=False, sort=True, ascending=False, bins=None, dropna=True
    ): ...

    def unique(self): ...

    def nunique(self, dropna: bool = True) -> int: ...

    @property
    def is_unique(self) -> bool: ...

    @property
    def is_monotonic(self) -> bool: ...

    @property
    def is_monotonic_increasing(self) -> bool: ...

    @property
    def is_monotonic_decreasing(self) -> bool: ...

    def memory_usage(self, deep=False): ...

    def factorize(self, sort=False, na_sentinel=-1): ...
    def searchsorted(self, value, side="left", sorter=None) -> np.ndarray: ...

    def drop_duplicates(self, keep="first"): ...

    def duplicated(self, keep="first"): ...
