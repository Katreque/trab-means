from sklearn.cluster import KMeans
from random import randint
import numpy as np
import csv
import matplotlib.pyplot as plt

matriz = []

with open('dataset_iris.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        largPetala = (row['larguraPetala'])
        compSepala = (row['comprimentoSepala'])
        matriz.append([float(largPetala), float(compSepala)])

matriz = np.array(matriz)

def criacaoCentroideRandom():
    array = [[randint(0, 9), randint(0, 9)], [randint(0, 9), randint(0, 9)], [randint(0, 9), randint(0, 9)]]
    array = np.array(array)
    return array

def avaliacaoAcertos(arrayAnalise):
    return

for i in range(1, 4):
    if (i != 3):
        #Minha geração de centroides;
        trabmeans = KMeans(n_clusters=3, init=criacaoCentroideRandom(), n_init=1).fit(matriz)
    else:
        #Geração de centroides otimizada da própria lib;
        trabmeans = KMeans(n_clusters=3).fit(matriz)

    plt.figure(i)
    plt.scatter(matriz[:, 0], matriz[:, 1], s = 100, c = trabmeans.labels_)
    plt.scatter(trabmeans.cluster_centers_[:, 0], trabmeans.cluster_centers_[:, 1], s = 100, c = 'red', label = 'Centroides')
    plt.xlabel('Largura da Petala')
    plt.ylabel('Comprimento da Sepala')
    plt.legend()
    print(avaliacaoAcertos(trabmeans.labels_))

#plt.show()