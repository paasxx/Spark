import pandas as pd
import random

data = []
for vehicle_id in range(1, 4):  # 3 veículos
    for i in range(1000):       # 1000 linhas por veículo
        data.append({
            "vehicle_id": f"V{vehicle_id}",
            "timestamp": f"2025-06-03 12:{i%60:02}:{i%60:02}",
            "latitude": round(random.uniform(-23.6, -23.5), 6),
            "longitude": round(random.uniform(-46.7, -46.6), 6),
            "speed_kmh": random.randint(0, 120)
        })

df = pd.DataFrame(data)
df.to_csv("gps_data.csv", index=False)
