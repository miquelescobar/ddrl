import sys
import time

import argparse
import subprocess


template_file =  "distributed-template.sh"
JOB_NAME = "${JOB_NAME}"
NUM_NODES = "${NUM_NODES}"
NUM_GPUS_PER_NODE = "${NUM_GPUS_PER_NODE}"
PARTITION_OPTION = "${PARTITION_OPTION}"
COMMAND_PLACEHOLDER = "${COMMAND_PLACEHOLDER}"
GIVEN_NODE = "${GIVEN_NODE}"
LOAD_ENV = "${LOAD_ENV}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--exp-name", type=str, required=True, help="The job name and path to logging file (exp_name.log).")
    parser.add_argument("--num-nodes", "-n", type=int, default=1, help="Number of nodes to use.")
    parser.add_argument("--node", "-w", type=str, help="The specified nodes to use. Same format as the return of 'sinfo'. Default: ''.")
    parser.add_argument("--num-gpus", type=int, default=0, help="Number of GPUs to use in each node. (Default: 0)")
    parser.add_argument("--partition", "-p", type=str)
    parser.add_argument("--load-env", type=str, help="The script to load your environment ('module load cuda/10.1')")
    parser.add_argument("--command", type=str, required=True, help="The command you wish to execute. For example: 'python train.py'.")
    args = parser.parse_args()

    if args.node:
        node_info = "#SBATCH -w {}".format(args.node)
    else:
        node_info = ""

    job_name = "{}_{}".format(args.exp_name,
                              time.strftime("%m%d-%H%M", time.localtime()))

    partition_option = "#SBATCH --partition={}".format(
        args.partition) if args.partition else ""

    # Modified the template script
    with open(template_file, "r") as f:
        text = f.read()
    text = text.replace(JOB_NAME, job_name)
    text = text.replace(NUM_NODES, str(args.num_nodes))
    text = text.replace(NUM_GPUS_PER_NODE, str(args.num_gpus))
    text = text.replace(PARTITION_OPTION, partition_option)
    text = text.replace(COMMAND_PLACEHOLDER, str(args.command))
    text = text.replace(LOAD_ENV, str(args.load_env))
    text = text.replace(GIVEN_NODE, node_info)

    # Save the script
    script_file = "{}.sh".format(job_name)
    with open(script_file, "w") as f:
        f.write(text)

    # Submit the job
    print("Starting to submit job!")
    subprocess.Popen(["sbatch", script_file])
    print(f"Job submitted! Script file is at: <{script_file}>. Log file is at: <{job_name}.log>")
    sys.exit(0)