import schedule
import time

def scheduled_job():
    print("Automated pin posting job executed")

# Schedule the job every hour
schedule.every().hour.do(scheduled_job)

while True:
    schedule.run_pending()
    time.sleep(1)