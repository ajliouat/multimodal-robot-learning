#!/bin/bash

# Preprocess simulation data
python src/utils/data_loader.py --input_dir data/datasets/simulation --output_dir data/preprocessed/train

# Preprocess real-world data
python src/utils/data_loader.py --input_dir data/datasets/real_world --output_dir data/preprocessed/val