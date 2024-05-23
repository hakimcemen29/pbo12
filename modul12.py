import pytz
from datetime import datetime, timedelta

timezone = pytz.timezone('Asia/Jakarta')

current_time = datetime.now(timezone)

before_time = current_time - timedelta(minutes=1)
after_time = current_time + timedelta(minutes=1)

print("=====================")
print("Muhammad Hakim")
print("064002300027")
print("=====================")
print("Timzone : ",timezone)
print("Sebelumnya:", before_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]) 
print("Saat ini:", current_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]) 
print("Timzone : ",timezone)
print("Sesudahnya:", after_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]) 
