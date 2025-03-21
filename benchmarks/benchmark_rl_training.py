import time
from src.core.rl.trainer import RLPolicyTrainer

def benchmark_rl_training():
    trainer = RLPolicyTrainer()
    start_time = time.time()
    trainer.train(num_epochs=100)
    end_time = time.time()
    print(f"Training time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    benchmark_rl_training()