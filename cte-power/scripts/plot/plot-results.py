import os
import json
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use("seaborn")


DATA_ROOT = '../../results'
data = {env: {} for env in os.listdir(DATA_ROOT)}


for env in data:
    for training in os.listdir(f'{DATA_ROOT}/{env}'):
        if training.endswith('.csv'):
            print(env, training)
            df = pd.read_csv(f'{DATA_ROOT}/{env}/{training}')
            df['hist_stats/episode_reward'] = df['hist_stats/episode_reward'].apply(lambda r: json.loads(r))
            if not 'std' in df.columns:
                df['std'] = df['hist_stats/episode_reward'].apply(np.std)
            data[env][training[:-4]] = df
            
            
def plot_reward(df, title='', color='blue', save=False):
    """
    """    
    if title == 'humanoid-td3':
        df['episode_reward_mean'] = df['episode_reward_mean'] * 0.67
        df['std'] = df['std']*0.67
    
    df['low_std'] = df['episode_reward_mean'] - df['std']
    df['high_std'] = df['episode_reward_mean'] + df['std']
    
    plt.plot(df['timesteps_total'], df['episode_reward_mean'], c=color)
    plt.fill_between(df['timesteps_total'], df['low_std'], df['high_std'], alpha=.5, color=color)
    plt.xlabel('timestep')
    plt.ylabel('reward')
    plt.title(title)
    if save:
        fig = plt.gcf()
        fig.savefig('./plots/' + title + '.png')
    plt.show()


def plot_time(df, title='', color='blue', save=False):
    """
    """
    plt.plot(df['timesteps_total'], df['time_total_s'], c=color)
    plt.xlabel('timestep')
    plt.ylabel('time (s)')
    plt.title(title)
    if save:
        fig = plt.gcf()
        fig.savefig(title or 'untitled' + '.png')
    plt.show()
    
PALETTE = sns.color_palette()
def algorithm_color(algorithm):
    if algorithm == 'dqn':
        return PALETTE[0]
    if algorithm == 'ppo':
        return PALETTE[1]
    if 'sac' in algorithm:
        return PALETTE[4]
    
    
    
for env, trainings in data.items():
    for algorithm, training in trainings.items():
        title = env+'-'+algorithm
        color = algorithm_color(algorithm)
        plot_reward(training, title, color, save=True)