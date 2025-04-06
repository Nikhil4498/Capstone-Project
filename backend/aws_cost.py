import boto3
import os
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv
from db.mongo_connection import cost_collection
from utils.standardize import standardize_cost

# Load environment variables from .env
load_dotenv()

# AWS credentials
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = "us-east-1"  # Change if needed

# Initialize AWS Cost Explorer client
client = boto3.client(
    "ce",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION,
)

# Fetch last month's cost data
response = client.get_cost_and_usage(
    TimePeriod={"Start": "2025-01-01", "End": "2025-01-31"},
    Granularity="MONTHLY",
    Metrics=["BlendedCost"],
)

print(response)

with open("aws_cost_log.json", "w") as file:
    json.dump(response, file, indent=4)

# Fetch AWS data here as `response`
# (Assuming 'response' contains necessary fields)

#standardized = standardize_cost(
    #provider="aws",
    #service="EC2",
    #date=str(datetime.now().date()),
    #cost=15.25,
    #usage={"cpu": "30%", "memory": "1GB"}
#)

#cost_collection.insert_one(record)
#print("AWS data inserted successfully.")

# Set date range for yesterday
    end = datetime.utcnow().date()
    start = end - timedelta(days=1)

    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': str(start),
            'End': str(end)
        },
        Granularity='DAILY',
        Metrics=['UnblendedCost'],
        GroupBy=[{'Type': 'DIMENSION', 'Key': 'SERVICE'}]
    )

    for item in response['ResultsByTime'][0]['Groups']:
        service = item['Keys'][0]
        amount = float(item['Metrics']['UnblendedCost']['Amount'])

        record = standardize_cost(
            provider="aws",
            service=service,
            date=str(start),
            cost=amount,
            usage={}  # You can enhance this with resource metrics later
        )

        cost_collection.insert_one(record)
        print(f"[AWS] Inserted {service} with cost ${amount} on {start}")


