import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils import (
    Training
)

plt.style.use('seaborn')


def read_data(data_paths: list):
    """
    """
    sample_times = []
    load_times = []
    learn_times = []
    update_times = []
    num_gpus = []
    index = []
    datas_gpu = {}
    datas = {}
    
    for data_path in data_paths:
        for training_dir in os.listdir(data_path):
            training = Training(data_path + '/' + training_dir)
            print(training_dir)
            print(training.params.num_workers)
            print(training.params.num_gpus)
            
            data = {'sample_times': [], 'load_times': [], 'learn_times': [], 'update_times': []}
            
            if 'info/sample_time_ms' in training.progress.df.columns:
                data['sample_times'].extend(list(training.progress.df['info/sample_time_ms']))
                data['load_times'].extend(list(training.progress.df['info/load_time_ms']))
                data['learn_times'].extend(list(training.progress.df['info/grad_time_ms']))
                data['update_times'].extend(list(training.progress.df['info/update_time_ms']))
            else:
                data['sample_times'].extend(list(training.progress.df['timers/sample_time_ms']))
                data['load_times'].extend(list(training.progress.df['timers/load_time_ms']))
                data['learn_times'].extend(list(training.progress.df['timers/learn_time_ms']))
                data['update_times'].extend(list(training.progress.df['timers/update_time_ms']))
            
            index = training.params.num_workers
            if training.params.num_gpus:       
                if index in datas_gpu:
                    datas_gpu[index]['sample_times'].extend(data['sample_times'])
                    datas_gpu[index]['load_times'].extend(data['load_times'])
                    datas_gpu[index]['learn_times'].extend(data['learn_times'])
                    datas_gpu[index]['update_times'].extend(data['update_times'])
                else:
                    datas_gpu[index] = data
            else:
                if index in datas:
                    datas[index]['sample_times'].extend(data['sample_times'])
                    datas[index]['load_times'].extend(data['load_times'])
                    datas[index]['learn_times'].extend(data['learn_times'])
                    datas[index]['update_times'].extend(data['update_times'])
                else:
                    datas[index] = data
                
            print(datas.keys(), datas_gpu.keys())
    
    
    datas = [ { 'index': k, 
                'sample_times': sum(v['sample_times'])/len(v['sample_times']),
                'load_times': sum(v['load_times'])/len(v['load_times']),
                'learn_times': sum(v['learn_times'])/len(v['learn_times']),
                'update_times': sum(v['update_times'])/len(v['update_times'])
              }  for k, v in datas.items() ]
    
    datas_gpu = [ { 'index': k, 
                'sample_times': sum(v['sample_times'])/len(v['sample_times']),
                'load_times': sum(v['load_times'])/len(v['load_times']),
                'learn_times': sum(v['learn_times'])/len(v['learn_times']),
                'update_times': sum(v['update_times'])/len(v['update_times'])
              }  for k, v in datas_gpu.items() ]
    
    
    return pd.DataFrame(datas), pd.DataFrame(datas_gpu)


def plot_time_breakdown(df: pd.DataFrame,
                        savepath: str):
    print(df)
    stacked_data = df.apply(lambda x: x*100/sum(x), axis=1)
    print(stacked_data)
    stacked_data.plot(kind="bar", stacked=True)

    plt.xlabel("Number of workers")
    plt.ylabel("Iteration time task breakdown (%)")
    lgd = plt.legend(title='Tasks', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.savefig(savepath, bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    
    save_path = '../../figures/plots/ppo-time-breakdown.png'
    save_path_g = '../../figures/plots/ppo-time-breakdown-gpu.png'
    data_paths = ['../../results/humanoid/ppo-hyp', '../../results/humanoid/ppo-time']
    # df, df_g = read_data(data_paths)
    
    # df.to_csv('../../results/humanoid/ppo-time-breakdown.csv', index=False)
    # df_g.to_csv('../../results/humanoid/ppo-time-breakdown-gpu.csv', index=False)
    
    df = pd.read_csv('../../results/humanoid/ppo-time-breakdown.csv')
    df = df.set_index('index').rename(columns={"sample_times":"sampling", "load_times":"loading", "learn_times":"learning", "update_times":"updating"})
    df_g = pd.read_csv('../../results/humanoid/ppo-time-breakdown-gpu.csv')
    df_g = df_g.set_index('index').rename(columns={"sample_times":"sampling", "load_times":"loading", "learn_times":"learning", "update_times":"updating"})
        
    plot_time_breakdown(df, save_path)
    plot_time_breakdown(df_g, save_path_g)
