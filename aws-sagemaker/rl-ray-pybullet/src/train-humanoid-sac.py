import json
import os

import gym
import ray
import pybullet_envs
from ray.tune import run_experiments
from ray.tune.registry import register_env
from sagemaker_rl.ray_launcher import SageMakerRayLauncher


def create_environment(env_config):
    # This import must happen inside the method so that worker processes import this code
    import roboschool

    return gym.make("HumanoidBulletEnv-v0")


class MyLauncher(SageMakerRayLauncher):
    def register_env_creator(self):
        register_env("HumanoidBulletEnv-v0", create_environment)

    def get_experiment_config(self):
        return {
            "training": {
                "env": "HumanoidBulletEnv-v0",
                "run": "SAC",
                "stop": {
                    "episode_reward_mean": 2500,
                },
                "config": {
                    "gamma": 0.99,
                    "lr": 0.0001,
                    "monitor": True, 
                    
                    "num_workers": (self.num_cpus - 1),
                    "num_gpus": self.num_gpus,
                },
            }
        }


if __name__ == "__main__":
    MyLauncher().train_main()
