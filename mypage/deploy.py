"""
デプロイ用スクリプト
`docker exec`についての説明
  >> https://unicorn.limited/jp/item/347
"""
import os

# docker container
os.system('docker-compose build')
os.system('docker-compose up -d')

# finally
print('`deploy.py`は終了しました。')
