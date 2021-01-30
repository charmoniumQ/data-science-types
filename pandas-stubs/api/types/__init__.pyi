from typing import Iterable

from .core.arrays.categorical import Categorical

def union_categoricals(
        to_union: Iterable[Categorical],
        sort_categories: bool = ...,
        ignore_order: bool = ...):
    ...
