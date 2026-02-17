from backend_predictor import predict_parking_occupancy

# Example test
zone = "Z1"
day = 1
hour_24 = 18   # 6 PM

result = predict_parking_occupancy(zone, day, hour_24)

print("Predicted Occupancy:", result)
