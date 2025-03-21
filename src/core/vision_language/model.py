import torch
from transformers import GPT2Model

class VisionLanguageModel:
    def __init__(self):
        self.model = GPT2Model.from_pretrained("gpt2")

    def forward(self, input_ids):
        return self.model(input_ids)