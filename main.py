from fastapi import FastAPI, Query
from math import radians, sin, cos, sqrt, atan2

app = FastAPI(title="Distance Checker API")


def haversine(lat1, lon1, lat2, lon2):
    """
    Calcula a distância em km entre dois pontos usando a fórmula de Haversine.
    """
    R = 6371.0  # Raio da Terra em km

    # Converte graus para radianos
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


@app.get("/check_distance")
def check_distance(
    lat_a: float = Query(..., description="Latitude do ponto A"),
    lon_a: float = Query(..., description="Longitude do ponto A"),
    lat_b: float = Query(..., description="Latitude do ponto B"),
    lon_b: float = Query(..., description="Longitude do ponto B")
):
    distance = haversine(lat_a, lon_a, lat_b, lon_b)
    is_within_2km = distance <= 2

    return {
        "Distancia em Km": round(distance, 3),
        "Dentro de 2km": is_within_2km
    }
