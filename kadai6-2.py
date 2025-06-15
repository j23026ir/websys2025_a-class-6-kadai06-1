import requests

# APIのエンドポイント
api_url = "https://api.open-meteo.com/v1/forecast"

# クエリパラメータの設定
params = {
    "latitude": 35.6895,  # 東京の緯度
    "longitude": 139.6917,  # 東京の経度
    "hourly": "temperature_2m",  # 1時間ごとの気温データ
    "timezone": "Asia/Tokyo"  # タイムゾーンを日本時間に設定
}

# APIリクエスト
response = requests.get(api_url, params=params)

# 結果の表示
if response.status_code == 200:
    data = response.json()
    print("東京の気温データ:")
    
    # 各時間帯の気温とその時刻を表示
    for time, temp in zip(data["hourly"]["time"], data["hourly"]["temperature_2m"]):
        print(f"{time}: {temp}°C")
else:
    print("APIリクエストに失敗しました:", response.status_code)
