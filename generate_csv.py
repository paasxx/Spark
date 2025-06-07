import pandas as pd
import os
import random
from datetime import datetime, timedelta
from tqdm import tqdm

def generate_gps_data(
        
        num_vehicles=100,
        rows_per_vehicle=100_000,
        start_time_str="2025-01-01 00:00:00",
        output_file="csv_data/gps_data.csv"

):
    if os.path.exists(output_file):
        print(f"Arquivo já existe: {output_file}. Pulando geração.")
        return
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    
    start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
    data = []

    for vehicle_id in tqdm(range(1,num_vehicles + 1), desc="Generating data"):
        timestamp = start_time
        for _ in range(rows_per_vehicle):
            data.append({
                "vehicle_id": f"V{vehicle_id}",
                "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                "latitude": round(random.uniform(-23.7, -23.4),6),
                "longitude": round(random.uniform(-46.8, -46.5), 6),
                "speed_kmh": random.randint(0,180)

            })
            timestamp += timedelta(seconds=1)

    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
    print(f"\nCSV com {len(df)} linhas salvo em: {output_file}")

if __name__ == "__main__":
    generate_gps_data(
        num_vehicles=100,
        rows_per_vehicle=100_000,
        output_file="csv_data/gps_data.csv"
    
    )