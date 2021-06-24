<h1 style="background-color:red;">README UNDER DEVELOPMENT</h1>

<p float="left">
<img src="https://www.upc.edu/comunicacio/ca/identitat/descarrega-arxius-grafics/fitxers-marca-principal/upc-positiu-p3005.png" height="75">
<img src="https://www.fib.upc.edu/sites/fib/files/images/logo-fib-lletres.png" height="85">
<img src="https://dse.upc.edu/ca/logosfooter-ca/fme/@@images/image" height="75">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="http://forumtelecos.upc.edu/wp-content/uploads/2019/03/logo_telecos-4-300x167.png" height="70">
</p>



# Distributed Deep Reinforcement Learning in an HPC system and deployment to the Cloud
<i>Bachelor's degree in Data Science and Engineering. Final Thesis</i>
<br>
<i>Defended on July 1, 2021</i>
<br>
<i>Miquel Escobar Castells, @miquelescobar, miquel.escobar@estudiantat.upc.edu</i>
<br>

<br>

## Table of Contents
1. [Abstract](#abstract)
2. [Repository structure](#repository-structure)
<br> 2.1. [CTE-POWER](#cte-power) 
<br> 2.1. [AWS SageMaker](#aws-sagemaker) 
<br> 2.1. [Figures](#figures) 
3. [Contact](#contact)

<br> 

## Abstract
Combining Reinforcement Learning and Deep Learning is the most challenging Artificial
Intelligence research and development area at present. Scaling these types of applications in
an HPC infrastructure available in the cloud will be crucial for advancing the massive use
of these technologies. The purpose of this project is to develop and test various implementations of Deep RL algorithms given a selected case study, using Barcelona Supercomputing
Center’s (BSC) CTE-POWER cluster, and make a deployment to the cloud of the training
pipeline to analyze its costs and viability in a production environment.

<br> 

## Repository structure
One can find the complete report of the project in the ```report.pdf``` file in the root directory, as well as the thesis defense slides  in the ```slides.pdf``` file.

The directory structure of this reposirory is shown below. In each of the subsections, more detailed documentation about its internal structure is provided, as well as instructions on dependencies installation and reproducibility.

```
├───cte-power
│   ├───jobs
│   │   ├───distributed
│   │   ├───err
│   │   ├───gym
│   │   ├───out
│   │   ├───pybullet-envs
│   │   ├───pybulletgym
│   │   └───unity
│   ├───scripts
│   │   ├───plot
│   │   ├───render
│   │   └───train
│   ├───trainings
│   │   ├───gym
│   │   ├───pybullet-envs
│   │   ├───pybulletgym
│   │   └───unity
│   └───results
│       └───humanoid
|
├───aws-sagemaker
│   └───rl-ray-pybullet
│       ├───common
│       │   ├───sagemaker_rl
│       └───src
|
└───figures
    ├───plots
    └───videos
```

### CTE-POWER
In the ```./cte-power/``` directory one can find all files and scripts required to execute the trainings and metrics evaluations in the [https://www.bsc.es/user-support/power.php](CTE-POWER) cluster. The scripts can be executed as-is, assuming that the compatibilities and the required dependencies are maintaned by the system operators at CTE, since the loading of environment are defined in the [jobs](#jobs) section scripts.

It is worth noting that some files might not be included in this repository due to their size.

In order to understand the implementation, below there is a more detailed description of each one of the modules.

#### Scripts
In the ```./cte-power/scripts/``` directory reside the necessary scripts for executing the training, renderization and evaluation plots of RLlib algorithms on different kinds of environments. Depending on the RL toolkit, different dependencies are required. 

There is an adapted script for the **training** of each of the following toolkits:

* [OpenAI Gym](https://gym.openai.com/): see ```./cte-power/scripts/train/train-gym.py``` script.
* [PyBullet](https://pybullet.org/): see ```./cte-power/scripts/train/train-bullet-envs.py``` script.
* [PyBullet Gymperium](https://github.com/benelot/pybullet-gym): see ```./cte-power/scripts/train/train-pybulletgym.py``` script.
* [Unity](https://github.com/Unity-Technologies/ml-agents): see ```./cte-power/scripts/train/train-unity.py``` script.

The ```./cte-power/scripts/render/``` directory also provides scripts for the **renderization** of the [OpenAI Gym](https://gym.openai.com/), [PyBullet](https://pybullet.org/) and [PyBullet Gymperium](https://github.com/benelot/pybullet-gym) toolkits.

Finally, the ```./cte-power/scripts/plot/``` directory containes the scripts used to analyze, slighlty transform and plot the data of the obtained training results.

<br>

#### Jobs
In this directory one can find the *bash* scripts used for the execuition of SLURM trainingjobs in the CTE-POWER cluster. There is the **output** and **error** directories, as well as a directory for each of the toolkits and the **distributed** directory that contains the distributed jobs definitions and launching script.

<br>

#### Trainings
The **trainings** directory contains the configurations used as input for the training jobs (hyperparameters, resource allocation, stopping conditions, etc.). They are organized by RL toolkit.


<br>

#### Results
In this directory the training results and metrics are stored. In the GitHub repository, only the summarized data extracted from the files with the raw training metrics at an iteration granularity level can be found, given that the latter occupy several MBs of space per file.

<br>


### AWS SageMaker
[AWS SageMaker](https://aws.amazon.com/) is the selected tool in this project for implementing the RL training pipelines in the Cloud. It is an [AWS](https://aws.amazon.com/sagemaker/) service that provides higher-level modules for machine learning functionalities in the AWS environment.

In this repository one can find an example for executing a complete training pipeline of [PyBullet](https://pybullet.org/) environments.


<br>

### Figures
In this directory, the figures corresponding to the generated plots from the training results, the drawn architectures and miscellaneous images as well as some videos of renderizations of interactions between trained agents and the environment can be found.



<br>


## Contact
For any inquiries please contact the author of this project at miquel.escobar@estudiantat.upc.edu or miquel.escobar@bsc.es.
