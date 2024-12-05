# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

from typing import List, Dict

from ..search import Search
from ..optimizers import EnsembleOptimizer as _EnsembleOptimizer


class EnsembleOptimizer(_EnsembleOptimizer, Search):
    def __init__(
        self,
        search_space: Dict[str, list],
        initialize: Dict[str, int] = {"grid": 4, "random": 2, "vertices": 4},
        constraints: List[Dict[str, callable]] = [],
        random_state: int = None,
        rand_rest_p: float = 0,
        nth_process: int = None,
        warm_start_smbo=None,
        max_sample_size: int = 10000000,
        sampling: dict = {"random": 1000000},
        replacement: bool = True,
    ):
        super().__init__(
            search_space=search_space,
            initialize=initialize,
            constraints=constraints,
            random_state=random_state,
            rand_rest_p=rand_rest_p,
            nth_process=nth_process,
            warm_start_smbo=warm_start_smbo,
            max_sample_size=max_sample_size,
            sampling=sampling,
            replacement=replacement,
        )
