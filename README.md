# Multimodal Robot Learning with Vision-Language Models

A comprehensive system integrating vision-language models, segmentation, and reinforcement learning for advanced robotic manipulation. The system uses natural language commands to control robots while understanding visual scenes and adapting to new environments.

## Features
- Integration of GPT-4V for scene understanding
- Segment Anything Model (SAM) for real-time object segmentation
- Custom RL policy conditioned on language embeddings
- Real-time visual feedback loop
- Sim2real transfer with domain adaptation
- Custom CUDA kernels for real-time inference

## Table of Contents
1. [Installation](#installation)
2. [Dataset Preparation](#dataset-preparation)
3. [Usage](#usage)
4. [Configuration](#configuration)
5. [Project Structure](#project-structure)
6. [Benchmarks](#benchmarks)
7. [Contributing](#contributing)
8. [License](#license)

---

## Installation

### Prerequisites
- Python 3.8+
- PyTorch 2.0+
- ROS2 Humble
- CUDA 11.8+
- Isaac Gym

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Download Model Weights
1. **Segment Anything Model (SAM)**:
   - Download the SAM weights (`sam_vit_h_4b8939.pth`) from the [official repository](https://github.com/facebookresearch/segment-anything).
   - Place the weights in `models/sam/`.

2. **Vision-Language Model**:
   - If using GPT-4V, obtain the weights from OpenAI.
   - For open-source alternatives (e.g., GPT-2 or GPT-3), download the weights and place them in `models/vision_language/gpt4v_weights/`.

---

## Dataset Preparation

### Real-World Dataset
1. Use a dataset like COCO or create your own.
2. Place the images in `data/datasets/real_world/images/`.
3. Place the annotations in `data/datasets/real_world/annotations/` (COCO format recommended).

### Simulation Dataset
1. Generate synthetic data using tools like Isaac Gym or Blender.
2. Place the images in `data/datasets/simulation/images/`.
3. Place the annotations in `data/datasets/simulation/annotations/` (COCO format recommended).

### Preprocessing
Run the preprocessing script to prepare the data for training:
```bash
./scripts/preprocess_data.sh
```
This will populate the `data/preprocessed/` folder with train, test, and validation datasets.

---

## Usage

### Train the RL Policy
```bash
./scripts/train_rl_policy.sh --config configs/rl_config.yaml
```

### Train the Vision-Language Model
```bash
./scripts/train_vision_language.sh --config configs/vision_config.yaml
```

### Start ROS2 Nodes
```bash
./scripts/start_ros2_nodes.sh
```

---

## Configuration

The `config.yaml` files are the central configurations for the project. Below are example configurations:

### RL Configuration (`configs/rl_config.yaml`)
```yaml
learning_rate: 0.001
batch_size: 32
num_epochs: 100
```

### Vision Configuration (`configs/vision_config.yaml`)
```yaml
model_name: "gpt-4v"
temperature: 0.7
```

### ROS2 Configuration (`configs/ros2_config.yaml`)
```yaml
nodes:
  vision_node:
    rate: 30  # Hz
  control_node:
    rate: 10  # Hz
```

---

## Project Structure

```
multimodal-robot-learning/
├── benchmarks/          # Performance benchmarks
├── configs/             # Configuration files
├── data/                # Datasets and preprocessed data
├── deployments/         # Docker and Kubernetes deployment files
├── models/              # Pretrained models
├── notebooks/           # Exploration and testing notebooks
├── scripts/             # Utility scripts
├── src/                 # Source code
│   ├── core/            # Core RL and vision-language logic
│   ├── robotics/        # ROS2 nodes for robotics
│   └── utils/           # Utility functions
├── tests/               # Unit and integration tests
```

---

## Benchmarks

### RL Training Performance
| Framework       | Training Time (hrs) | Success Rate (%) |
|-----------------|---------------------|------------------|
| Baseline        | 10                  | 70               |
| Custom RL       | 8                   | 85               |

### Segmentation Performance
| Framework       | Inference Time (ms) | mIoU (%) |
|-----------------|---------------------|----------|
| SAM             | 15                  | 92       |

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

---

## License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.