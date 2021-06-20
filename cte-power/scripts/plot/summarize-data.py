import os
import pandas as pd

from utils import (
    Progress,
    Params,
    Training
)


DATA_ROOT = '../../results/humanoid'
AVG_METRICS = ['episode_reward_min', 'episode_reward_max', 'episode_reward_mean']
LAST_METRICS = ['training_iteration', 'timesteps_total', 'time_this_iter_s', 'time_total_s']
PARAMS = ['num_workers', 'num_gpus', 'num_cpus_per_worker', 'num_gpus_per_worker']


def summarize_trainings(path: str,
                        avg_metrics: list = AVG_METRICS,
                        last_metrics: list = LAST_METRICS,
                        params: list = PARAMS):
    """
    """
    rows = []
    for training_dir in os.listdir(path):
        row = {}
        training = Training(path + '/' + training_dir)
        
        for avg_metric in avg_metrics:
            row[avg_metric] = training.progress.df[avg_metric].iloc[-1]#.mean()
        for last_metric in last_metrics:
            row[last_metric] = training.progress.df[last_metric].iloc[-1]
            
        if params == 'all':
            for key, val in training.params.params.items():
                row[key] = val
        else:
            for param in params:
                row[param] = training.params.get(param)
            
        rows.append(row)
    return pd.DataFrame(rows)


if __name__ == '__main__':
    
    for alg in ('sac', 'td3', 'ppo'):
    
        path = f'../../results/humanoid/{alg}-time'
        save_path = f'../../results/humanoid/{alg}-time.csv'
        df = summarize_trainings(path)
        df.to_csv(save_path, index=False)

        path = f'../../results/humanoid/{alg}-hyp'
        save_path = f'../../results/humanoid/{alg}-hyp.csv'
        df = summarize_trainings(path, params='all')
        df.to_csv(save_path, index=False)
