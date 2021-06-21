#!/bin/bash
#SBATCH --job-name train-humanoid-sac-gpu-all-dist8
#SBATCH -D /home/bsc31/bsc31874/ddrl/
#SBATCH --output /home/bsc31/bsc31874/ddrl/jobs/out/%j.out
#SBATCH --error /home/bsc31/bsc31874/ddrl/jobs/err/%j.err
#SBATCH --nodes 1                  
#SBATCH -c 120
#SBATCH --gres='gpu:3'
#SBATCH --time 24:00:00
 
 
module purge;
module load gcc/8.3.0 cuda/10.2 cudnn/7.6.4 nccl/2.4.8 tensorrt/6.0.1 openmpi/4.0.1 atlas/3.10.3 scalapack/2.0.2 fftw/3.3.8 szip/2.1.1 ffmpeg/4.2.1 opencv/4.1.1 python/3.7.4_ML ray/1.1.0;

echo starting

python train-pybulletgym.py --params-file "./trainings/humanoid-sac-gpu-all-dist8.json"