import sagemaker
import boto3
import sys
import os
import glob
import re
import subprocess
import numpy as np
from IPython.display import HTML
import time
from time import gmtime, strftime
from common.docker_utils import (
    build_and_push_docker_image
)
from sagemaker.rl import (
    RLEstimator,
    RLToolkit,
    RLFramework
)


metric_definitions = RLEstimator.default_metric_definitions(RLToolkit.RAY)
int_regex = '[0-9]+'
float_regex = "[-+]?[0-9]*[.]?[0-9]+([eE][-+]?[0-9]+)?"  # noqa: W605, E501
metric_definitions.append( {"Name": "timesteps_total", "Regex": "timesteps_total: (%s)" % int_regex} )
metric_definitions.append( {"Name": "time_this_iter_s", "Regex": "time_this_iter_s: (%s)" % float_regex} )


def execute_training(job_name: str,
                     entry_point: str,
                     source_dir: str = "src",
                     dependencies: list = ["common/sagemaker_rl"],
                     instance_type: str =  "ml.c5.9xlarge",
                     instance_count: int = 1,
                     build_image: bool = False,
                     cpu_or_gpu: str = "cpu",
                     repository_name: str = "custom-image",
                     image_name: str = None,
                     wait: bool = False,
                     hyperparameters: dict = {}):
    """
    """
    
    sage_session = sagemaker.session.Session()
    s3_bucket = sage_session.default_bucket()
    s3_output_path = "s3://{}/".format(s3_bucket)
    print("S3 bucket path: {}".format(s3_output_path))
    try:
        role = sagemaker.get_execution_role()
    except:
        role = get_execution_role()
        
    if build_image:
        docker_build_args = {
            "CPU_OR_GPU": cpu_or_gpu,
            "AWS_REGION": boto3.Session().region_name,
        }
        image_name = build_and_push_docker_image(repository_name, build_args=docker_build_args)


    estimator = RLEstimator(
        entry_point=entry_point,
        source_dir=source_dir,
        dependencies=dependencies,
        image_uri=image_name if image_name else None,
        role=role,
        instance_type=instance_type,
        instance_count=instance_count,
        output_path=s3_output_path,
        base_job_name=job_name,
        metric_definitions=metric_definitions,
        hyperparameters=hyperparameters
    )

    estimator.fit(wait=wait)
    job_name = estimator.latest_training_job.job_name
    print("Training job: %s" % job_name)
    return job_name
    


if __name__ == '__main__':
    
    ALG = 'ppo'
    job_name = "rl-humanoid-bullet"
    image_name = "565870655207.dkr.ecr.us-west-2.amazonaws.com/sagemaker-bullet-ray-cpu:latest"
    entry_point = "train-%s.py" % f"humanoid-{ALG}"
    
    execute_training(job_name, entry_point, image_name)
