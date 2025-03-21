import torch
from src.core.rl.policy import RLPolicy

def test_rl_policy():
    policy = RLPolicy()
    output = policy(torch.randn(32, 512))
    assert output.shape == (32, 8)

if __name__ == "__main__":
    test_rl_policy()