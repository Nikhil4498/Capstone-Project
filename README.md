
# DevOps Dashboard for Resource and Cost Monitoring

## Overview

This project aims to create a centralized dashboard to monitor the usage and costs of cloud resources across multiple cloud platforms: AWS, Azure, and GCP. The dashboard will provide real-time and historical data, along with cost thresholds and alerts for inefficiencies. This project is designed for DevOps teams to optimize cloud resource usage and reduce unnecessary spending.

---

## Table of Contents

- [Project Setup and Cloud Integration](#sprint-1-project-setup-and-cloud-integration)
- [Data Aggregation and Storage](#sprint-2-data-aggregation-and-storage)
- [Real-Time Dashboard Development](#sprint-3-real-time-dashboard-development)

---

## Sprint 1: Project Setup and Cloud Integration

### Goal: Establish connectivity with AWS, Azure, and GCP & retrieve sample cost/resource data.

### Steps:

1. **Initialize the Project Repository**
   - Create a GitHub repository for the project.
   - Define the folder structure (`backend`, `frontend`, `database`, `docs`).
   - Add a `README.md` and `requirements.txt` for dependency management.

2. **Set Up Python Environment for Backend API**
   - Create a virtual environment and activate it:
     ```bash
     python -m venv venv
     source venv/bin/activate   # On Windows use: venv\Scripts\activate
     ```

3. **Install Dependencies**
   - Install the following dependencies:
     ```bash
     pip install boto3 azure-mgmt-costmanagement google-cloud-billing Flask python-dotenv
     ```

4. **Fetch Resource & Cost Data from AWS, Azure, and GCP**
   - Write Python scripts to authenticate and fetch sample cost data:
     - **AWS**: Use `boto3` for AWS Cost Explorer.
     - **Azure**: Use `azure-mgmt-costmanagement` for Azure.
     - **GCP**: Use `google-cloud-billing` for GCP.
   
   - Print the data in JSON format for verification.
   - Store credentials securely using environment variables (`.env` file).

---

## Sprint 2: Data Aggregation and Storage

### Goal: Aggregate data from cloud providers and store it in MongoDB for future analysis.

### Steps:

1. **Install MongoDB** (on your local machine or using a cloud service like MongoDB Atlas).

2. **Store Credentials Securely in `.env` File**
   - Store sensitive information such as MongoDB URI and cloud API keys in the `.env` file:
   ```env
   MONGODB_URI=mongodb://localhost:27017
   MONGODB_DB_NAME=devops_dashboard
   ```

3. **Write Data Aggregation Scripts**
   - Use Python to fetch resource data from AWS, Azure, and GCP using their APIs.
   - Format and standardize the data into a unified format.

4. **Set Up MongoDB Connection**
   - Use `pymongo` to connect to MongoDB and store the retrieved data:
   ```python
   from pymongo import MongoClient
   client = MongoClient(os.getenv("MONGODB_URI"))
   db = client[os.getenv("MONGODB_DB_NAME")]
   ```

5. **Store and Retrieve Data in MongoDB**
   - Ensure that historical data is stored in MongoDB for future trend analysis.
   - Test the data storage and retrieval process to ensure data integrity.

---

## Sprint 3: Real-Time Dashboard Development (with Grafana)

### Goal: Use **Grafana** for visualizing real-time data and trends.

### Steps:

1. **Install and Run Grafana Locally**
   - Follow the steps to install and run Grafana on your local machine.
   - Access Grafana at `http://localhost:3000`.

2. **Connect MongoDB as a Data Source**
   - Use a **Grafana Plugin** to connect to MongoDB.
   - Configure the plugin and define the MongoDB connection settings within Grafana.

3. **Create a Real-Time Dashboard**
   - Set up the Grafana dashboard:
     - Add panels for each cloud provider (AWS, Azure, GCP).
     - Use queries to pull data from MongoDB and visualize metrics.
   
4. **Customize Dashboard**
   - Customize the dashboard with:
     - **Cost over time**
     - **Resource usage**
     - **Trending data**

5. **Test the Dashboard**
   - Ensure that the data updates in real-time and that the Grafana panels show correct metrics.

---

## Dependencies

- **Python 3.8+**
- **Flask**: For creating the backend API.
- **boto3**: For AWS Cost Explorer API.
- **azure-mgmt-costmanagement**: For Azure Cost Management API.
- **google-cloud-billing**: For GCP Billing API.
- **MongoDB**: For storing historical data.
- **Grafana**: For real-time dashboard visualization.

### Install Python Dependencies
```bash
pip install boto3 azure-mgmt-costmanagement google-cloud-billing Flask pymongo python-dotenv
```

---

## `.env` Example

Here’s an example `.env` file for storing your environment variables securely:

```env
# AWS Credentials
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key

# Azure Credentials
AZURE_CLIENT_ID=your_azure_client_id
AZURE_SECRET=your_azure_secret
AZURE_TENANT_ID=your_azure_tenant_id
AZURE_SUBSCRIPTION_ID=your_azure_subscription_id

# GCP Credentials
GOOGLE_APPLICATION_CREDENTIALS=path_to_your_service_account_json
GCP_PROJECT_ID=your_gcp_project_id

# MongoDB Credentials
MONGODB_URI=mongodb://localhost:27017
MONGODB_DB_NAME=devops_dashboard
```

---

## Future Steps

- **Sprint 4**: Add Historical Data Analysis and Trend Visualizations in the Grafana Dashboard.
- **Sprint 5**: Set up Alerting and Notification System using **Prometheus Alertmanager**.
- **Sprint 6**: Final Testing, Documentation, and Deployment.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
