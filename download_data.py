import logging
logging.basicConfig(level=logging.DEBUG)
from datasets import load_dataset
dataset = load_dataset("imdb")