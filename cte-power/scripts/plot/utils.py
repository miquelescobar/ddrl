import matplotlib.pyplot as plt
import json
import pandas as pd
import numpy as np



class Training():
    
    def __init__(self,
                 path: str):
        self.progress = Progress(path + '/progress.csv')
        self.params = Params(path + '/params.json')
      

class Progress():
    
    def __init__(self,
                 filename: str,
                 env: str = None,
                 alg: str = None):
        """
        """
        self.env = env
        self.alg = alg
        self.df = pd.read_csv(filename)


class Params():
    
    def __init__(self,
                 filename: str, 
                 env: str = None,
                 alg: str = None):
        """
        """
        self.env = env
        self.alg = alg
        self._read_params_file(filename)
        
    def __get__(self, key):
        return getattr(self, key)
    
    def get(self, key):
        return getattr(self, key)
    
    def _read_params_file(self,
                          filename: str):
        """
        """
        self.params = json.load(open(filename, 'r'))
        self.num_gpus = 0
        self.num_workers = 1
        self.num_cpus_per_worker = 1
        self.num_gpus_per_worker = 0        
        for param, value in self.params.items():
            setattr(self, param, value)
            
    def get_num_cpus(self) -> float:
        """
        """
        return 1 + self.num_cpus_per_worker * self.num_workers
    
    def get_num_gpus(self) -> float:
        """
        """    
        return self.num_gpus + self.num_gpus_per_worker * self.num_workers
    
    
    
plt.style.use('seaborn')
    
def plot_time(env: str,
              alg: str,
              df: str,
              fig: list,
              ax: list,
              fit_line: bool = False):
    """
    """
        
    ys = df.time_this_iter_s
    x = df.num_workers
    
    ax.scatter(x, ys, marker='o', color='black')
    ax.set_ylim([0, max(ys)*1.25])

    if fit_line:
        try:
            p1, c = np.polyfit(x, ys, 1)
            x = np.arange(min(x), max(x), 1e-3)
            ax.plot(x, p1*x + c, 'r--')
    
        except Exception as e:
            print(e)


def configure_time_figs_and_axes(alg: str,
                                 gpu: bool = False):
    """
    """
    fig1 = plt.figure()

    ax1 = fig1.add_subplot(111)
    ax1.set_xlabel("Number of workers")
    ax1.set_ylabel("avg. time per iter")
    #ax1.set_title(f"Training time by number of workers ({alg})")
        
    ax1.set_ylim([0, 100])
    
    return (fig1), (ax1)