from fastapi import FastAPI, Query
from math import radians, sin, cos, sqrt, atan2

app = FastAPI(title="Distance Checker API")

def havesine(lat1,long1, lat2, long2):
    '''
    Aquii calcula a distancia em km entre os dois pontos usando a fórmula de Haversine.
    '''
    R = 6371.0 # Raio da Terra em km

    lat1, long1, lat2, long2 = map(radians, [lat1, long1, lat2, long2])

    dlat = lat2 - lat1
    dlong = long2 - long1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlong / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
