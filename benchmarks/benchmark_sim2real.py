import time
from src.core.sim2real.domain_adaptation import DomainAdapter

def benchmark_sim2real():
    adapter = DomainAdapter()
    start_time = time.time()
    adapter.adapt(torch.randn(32, 512))
    end_time = time.time()
    print(f"Adaptation time: {(end_time - start_time) * 1000:.2f} ms")

if __name__ == "__main__":
    benchmark_sim2real()