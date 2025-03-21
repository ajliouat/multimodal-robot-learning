import torch
from torch.optim import Adam
from .policy import RLPolicy

class RLPolicyTrainer:
    def __init__(self):
        self.policy = RLPolicy()
        self.optimizer = Adam(self.policy.parameters(), lr=0.001)

    def train(self, num_epochs=100):
        for epoch in range(num_epochs):
            self.optimizer.zero_grad()
            output = self.policy(torch.randn(32, 512))
            loss = torch.mean(output)
            loss.backward()
            self.optimizer.step()
            print(f"Epoch {epoch + 1}/{num_epochs}, Loss: {loss.item():.4f}")