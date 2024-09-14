import pickle

rechazados = []

try:
    with open('rechazados.pkl', 'rb') as f:
        rechazados = pickle.load(f)
except FileNotFoundError:
    rechazados = []
