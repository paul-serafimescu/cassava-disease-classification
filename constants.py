import torch
import os

EPOCHS = 5
BATCH_SIZE = 32
N_EVAL = 30
SAVE_FILE = os.path.join(os.getcwd(), 'model')

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
