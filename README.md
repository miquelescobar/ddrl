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
One can find the complete report of the project in the ```report.pdf``` file in the root directory, as well as the thesis defense slides  in the ````slides.pdf``` file.

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
In order to understand the implementation, below there is a more detailed description of each one of the modules.

In this repository one can find an example for executing a complete training pipeline of [PyBullet](https://pybullet.org/) environments



#### Scripts

<br>

#### Jobs

<br>

#### Training

<br>

#### Results

<br>


### AWS SageMaker
[AWS SageMaker](https://aws.amazon.com/) is the selected tool in this project for implementing the RL training pipelines in the Cloud. It is an [AWS](https://aws.amazon.com/sagemaker/) service that provides higher-level modules for machine learning functionalities in the AWS environment.



<br>

### Figures

#### Plots

#### Images

#### Videos


<br>


## Contact
For any inquiries please contact the author of this project at miquel.escobar@estudiantat.upc.edu or miquel.escobar@bsc.es.
