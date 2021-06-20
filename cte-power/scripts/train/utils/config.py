from typing import (
    Union,
    Iterable
)
from ray import tune


STR_TO_TUNE = {
    "uniform": tune.uniform,  # Uniform float between -5 and -1
    "quniform": tune.quniform,  # Round to increments of 0.2
    "loguniform": tune.loguniform,  # Uniform float in log space
    "qloguniform": tune.qloguniform,  # Round to increments of 0.0005
    "randn": tune.randn,  # Normal distribution with mean 10 and sd 2
    "qrandn": tune.qrandn,  # Round to increments of 0.2
    "randint": tune.randint,  # Random integer between -9 and 15
    "qrandint": tune.qrandint,  # Round to increments of 3 (includes 12)
    "choice": tune.choice,  # Choose one of these options uniformly
    "grid": tune.grid_search  # Search over all these values
}


def read_tune_params(params: dict):
    """
    """
    for key, value in params.items():
        if type(value) == dict:
            for subkey, subvalue in value.items():
                if subkey in STR_TO_TUNE:
                    params[key] = str_to_tune(subkey, subvalue)
                elif type(subvalue) == dict:
                    for subsubkey, subsubvalue in value.items():
                        if subsubkey in STR_TO_TUNE:
                            params[key][subkey] = str_to_tune(subsubkey, subsubvalue)
    return params
            
            
def str_to_tune(search_space: str,
                values: Union[Iterable, dict]):
    """
    """
    tune_func = STR_TO_TUNE(search_space)
    if type(values) == dict:
            return tune_func(**values)
    if search_space in ("choice", "grid",):
        return tune_func(values)
    return tune_func(*values)
