import ray
from ray import tune
from ray.tune.registry import register_env
from ray.rllib.env.wrappers.unity3d_env import Unity3DEnv
#
import argparse
import json
import gym



def train(env_file: str,
          env_name: str,
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
        config = {"env": "unity3d"}
    else:
        config["env"] = "unity3d"
    print(f'train-bullet-envs.train : DEBUG : config = {config}', flush=True)
    #
    print(f'train-bullet-envs.train : DEBUG : ray.is_initialized() = {ray.is_initialized()}', flush=True)
    ray.shutdown()
    print('train-bullet-envs.train : INFO : Starting Ray...', flush=True)
    ray.init(ignore_reinit_error=True)
    print(f'train-bullet-envs.train : DEBUG : ray.is_initialized() = {ray.is_initialized()}', flush=True)
    #
    print(f'train-bullet-envs.train : INFO : Environment definition (name = unity3d).', flush=True)
    tune.register_env(
        "unity3d",
        lambda c: Unity3DEnv(
            file_name=env_file,
            no_graphics=True,
            episode_horizon=c["episode_horizon"],
    ))
    print(f'train-bullet-envs.train : INFO : Environment registration completed.', flush=True)
    #
    print(f'train-bullet-envs.train : INFO : Starting tune.run execution.', flush=True)
    print(f'train-bullet-envs.train : DEBUG : config = {config}', flush=True)
    print(f'train-bullet-envs.train : DEBUG : stop = {stop}', flush=True)
    analysis = tune.run(
        run,
        config=config,
        stop=stop or {},
        local_dir = results_dir or (r'/home/bsc31/bsc31874/ray-results/' + env_name),
        verbose = verbose,
        checkpoint_freq = checkpoint_freq,
        checkpoint_at_end = checkpoint_at_end,
        num_samples= num_samples or 1,
        restore = restore
    )
    #
    ray.shutdown()


parser = argparse.ArgumentParser(description='Training script for PyBullet environments.')
parser.add_argument('--env-file', type=str, default="unity_env", help='The binary file of the Unity environment.')
parser.add_argument('--env-name', type=str, required=True, help='The name of the environment.')
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
    print(f'train-bullet-envs.main : DEBUG : params = {params}', flush=True)
    
    train(env_file=args.env_file,
          env_name=args.env_name,
          run=params['run'],
          stop=params.get('stop'),
          config=params.get('config'),
          results_dir=args.results_dir,
          verbose=args.verbose,
          checkpoint_freq=args.checkpoint_freq,
          checkpoint_at_end=args.checkpoint_at_end,
          num_samples=args.num_samples,
          restore=args.restore)
