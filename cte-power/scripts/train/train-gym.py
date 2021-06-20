import argparse
import json
import ray
from ray import tune
import gym


def train(env: str,
          run: str,
          stop: dict = None,
          config: dict = None,
          results_dir: str = None,
          verbose: int = 2,
          checkpoint_freq: int = 20,
          checkpoint_at_end: bool = True):
    """
    """
    #
    ray.shutdown()
    ray.init(ignore_reinit_error=True)
    #
    def make_env(env_config):
        return gym.make(env)
    tune.register_env(env, make_env)
    #
    if not config:
        config = {"env": env}
    else:
        config["env"] = env
    if not stop:
        stop = {}
    analysis = tune.run(
        run,
        config=config,
        stop=stop,
        local_dir = results_dir or (r'/home/bsc31/bsc31874/ray-results/' + env),
        verbose = verbose,
        checkpoint_freq = checkpoint_freq,
        checkpoint_at_end = checkpoint_at_end
    )
    #
    ray.shutdown()


parser = argparse.ArgumentParser(description='Training script for PyBullet environments.')
parser.add_argument('--params-file', type=str, required=True, help='The JSON params file for PyBullet training.')
parser.add_argument('--results-dir', type=str, help='The directory to store the results.')
parser.add_argument('--verbose', type=str, default=2, help='')
parser.add_argument('--checkpoint-freq', type=str, default=20, help='')
parser.add_argument('--checkpoint-at-end', type=bool, default=True, help='')


if __name__ == '__main__':
    args = parser.parse_args()
    params = json.load(open(args.params_file, 'r'))
    train(env=params['env'],
          run=params['run'],
          stop=params.get('stop'),
          config=params.get('config'),
          results_dir=args.results_dir,
          verbose=args.verbose,
          checkpoint_freq=args.checkpoint_freq,
          checkpoint_at_end=args.checkpoint_at_end)