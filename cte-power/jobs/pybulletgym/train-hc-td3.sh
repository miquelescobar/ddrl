#!/bin/bash
#SBATCH --job-name job_name
#SBATCH -D /gpfs/home/bsc31/bsc31xxx/
#SBATCH --output /gpfs/home/bsc31/bsc31xxx/%j.out
#SBATCH --error /gpfs/home/bsc31/bsc31xxx/%j.err
#SBATCH --nodes 1                  
#SBATCH -c 32  
#SBATCH --gres='gpu:4'
#SBATCH --time 24:00:00
#SBATCH --exclusive
 
 
module purge; module load gcc/8.3.0 cuda/10.2 cudnn/7.6.4 nccl/2.4.8 tensorrt/6.0.1 openmpi/4.0.1 atlas/3.10.3 scalapack/2.0.2 fftw/3.3.8 szip/2.1.1 ffmpeg/4.2.1 opencv/4.1.1 python/3.7.4_ML ray/1.1.0

export PYTHONUNBUFFERED=1
python script.py
