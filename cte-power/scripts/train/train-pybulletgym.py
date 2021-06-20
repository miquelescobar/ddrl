import argparse
import json
import pickle
#
import ray
from ray import tune
import gym
#
from utils.config import read_tune_params


def train(env: str,
          run: str,
          stop: dict = None,
          config: dict = None,
          results_dir: str = None,
          verbose: int = 2,
          checkpoint_freq: int = 20,
          checkpoint_at_end: bool = True,
          num_samples: int = 1,
          restore: str = None):
    """
    """
    if not config:
        config = {"env": env}
    else:
        config["env"] = env
    #
    ray.shutdown()
    ray.init(ignore_reinit_error=True)
    #
    def make_env(env_config):
        import pybulletgym
        return gym.make(env)
    tune.register_env(env, make_env)
    #
    analysis = tune.run(
        run,
        config=config,
        stop=stop or {},
        local_dir = results_dir or (r'/home/bsc31/bsc31874/ray-results/' + env),
        verbose = verbose,
        checkpoint_freq = checkpoint_freq,
        checkpoint_at_end = checkpoint_at_end,
        num_samples= num_samples or 1,
        restore = restore
    )
    #
    ray.shutdown()


parser = argparse.ArgumentParser(description='Training script for PyBullet environments.')
parser.add_argument('--params-file', type=str, required=True, help='The JSON params file for PyBullet training.')
parser.add_argument('--results-dir', type=str, help='The directory to store the results.')
parser.add_argument('--verbose', type=str, default=2, help='')
parser.add_argument('--checkpoint-freq', type=str, default=20, help='')
parser.add_argument('--checkpoint-at-end', type=bool, default=True, help='')
parser.add_argument('--num-samples', type=int, help='')
parser.add_argument('--restore', type=str, help='')


if __name__ == '__main__':
    
    args = parser.parse_args()
    params = json.load(open(args.params_file, 'r'))
    print(params, flush=True)
    
    train(env=params['env'],
          run=params['run'],
          stop=params.get('stop'),
          config=params.get('config'),
          results_dir=args.results_dir,
          verbose=args.verbose,
          checkpoint_freq=args.checkpoint_freq,
          checkpoint_at_end=args.checkpoint_at_end,
          num_samples=args.num_samples,
          restore=args.restore)