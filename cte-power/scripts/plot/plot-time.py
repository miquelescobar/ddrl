import os
import pandas as pd
#
from utils import (
    plot_time,
    configure_time_figs_and_axes,
)


DATA_ROOT = '../../results/humanoid'
PLOT_DIR = '../../figures/plots'
ENV = 'humanoid'



if __name__ == '__main__':
    
    for alg in ('sac', 'td3', 'ppo'):
    
        time_file = DATA_ROOT + '/' + alg + '-time.csv'
        df = pd.read_csv(time_file)
        df_g = df[df.num_gpus > 0]
        df = df[df.num_gpus == 0]

        (fig), (ax) = configure_time_figs_and_axes(alg)
        plot_time(ENV, alg, df, fig, ax, fit_line=True)
        fig.savefig(f'{PLOT_DIR}/{ENV}-{alg}-time-nworkers.png')

        (fig), (ax) = configure_time_figs_and_axes(alg, gpu=True)
        plot_time(ENV, alg, df_g, fig, ax, fit_line=True)
        fig.savefig(f'{PLOT_DIR}/{ENV}-{alg}-time-nworkers-gpu.png')
