import schedule
import time
from aws.aws_cost import fetch_aws_cost
from azure.azure_cost import fetch_azure_cost
from gcp.gcp_cost import fetch_gcp_cost

schedule.every().day.at("00:00").do(fetch_aws_cost)
schedule.every().day.at("00:10").do(fetch_azure_cost)
schedule.every().day.at("00:20").do(fetch_gcp_cost)

while True:
    schedule.run_pending()
    time.sleep(1)
