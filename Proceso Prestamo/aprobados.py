import pickle

aprobados = []

try:
    with open('aprobados.pkl', 'rb') as f:
        aprobados = pickle.load(f)
except FileNotFoundError:
    aprobados = []
