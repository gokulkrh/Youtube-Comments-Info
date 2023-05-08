import nltk
import pandas as pd
from sentence_transformers import SentenceTransformer
from nltk.cluster import KMeansClusterer
from scipy.spatial import distance_matrix
import numpy as np


def get_sentence_embeddings(sentence):
    model = SentenceTransformer('stsb-bert-base')
    embedding = model.encode([sentence])
    return embedding[0]


def distance_from_centroid(row):
    return distance_matrix([row['embeddings']], [row['centroid'].tolist()])[0][0]


def get_extractive_summ(comments):
    data = pd.DataFrame(comments)
    data.columns=['comments']
    data['embeddings']=data['comments'].apply(get_sentence_embeddings)
    NUM_CLUSTERS=20
    iterations=25
    X = np.array(data['embeddings'].tolist())
    kclusterer = KMeansClusterer(
        NUM_CLUSTERS, distance=nltk.cluster.util.cosine_distance,
        repeats=iterations,avoid_empty_clusters=True)
    assigned_clusters = kclusterer.cluster(X, assign_clusters=True)
    data['cluster']=pd.Series(assigned_clusters, index=data.index)
    data['centroid']=data['cluster'].apply(lambda x: kclusterer.means()[x])
    data['distance_from_centroid'] = data.apply(distance_from_centroid, axis=1)
    summary=' '.join(data.sort_values('distance_from_centroid',ascending = True).groupby('cluster').head(1).sort_index()['comments'].tolist())

    return summary
