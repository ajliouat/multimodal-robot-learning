import torch
from src.core.sim2real.domain_adaptation import DomainAdapter

def test_domain_adapter():
    adapter = DomainAdapter()
    output = adapter.adapt(torch.randn(32, 512))
    assert output is not None

if __name__ == "__main__":
    test_domain_adapter()