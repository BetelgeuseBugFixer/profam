#!/bin/bash
#SBATCH -p lrz-hgx-h100-94x4,lrz-hgx-a100-80x4,lrz-dgx-a100-80x8
#SBATCH --gres=gpu:1
#SBATCH -o slurm_out/foldtoken_test_std_output.out
#SBATCH -e slurm_out/foldtoken_test_std_err.err
#SBATCH --container-image="/dss/dsshome1/01/ge43vab3/fopra/container/fopra_container.sqsh"


# sbatch test_foldtoken.sbatch & tail -f slurm_out/foldtoken_test_std_output.out slurm_out/foldtoken_test_std_err.err
cd ~/fopra/profam
uv run python scratchpad/test.py
