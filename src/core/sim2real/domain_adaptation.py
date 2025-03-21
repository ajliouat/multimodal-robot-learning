import torch
import torch.nn as nn

class DomainAdapter(nn.Module):
    def __init__(self, input_dim=512, hidden_dim=256):
        super(DomainAdapter, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, input_dim)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x