This project is a full-stack stock monitoring dashboard that integrates a FastAPI backend with a React frontend.
It demonstrates how to design, build, and connect scalable applications while also integrating AWS services and DevOps practices for deployment and automation.

🚀 Project Overview

The Stock Dashboard allows users to monitor stocks by fetching and displaying information such as:

Stock Alerts (e.g., “AAPL crossed above 170”)

Stock Prices with % Change (e.g., “TSLA – 250.40, -2.5%”)

The backend serves stock data as a REST API using FastAPI, while the frontend (built with React) consumes the API and presents it in a clean dashboard UI.

🛠️ Tech Stack

Frontend: React (JavaScript, Hooks, Fetch API, reusable components)

Backend: FastAPI (Python, lightweight REST APIs)

Data Format: JSON

Cloud (AWS):

S3 – Hosting React frontend as a static website.

EC2 – Running FastAPI backend on a virtual server.

API Gateway + Lambda (optional) – Alternative for a serverless backend.

DynamoDB (future scope) – Storing live stock data.

DevOps Tools:

Docker – Containerizing backend and frontend.

CI/CD (GitHub Actions / Jenkins) – Automating build, test, and deployment pipeline.

Terraform / CloudFormation – Infrastructure as Code for AWS setup.

Monitoring – CloudWatch for backend logs and health checks.

⚡ How It Works

Backend (FastAPI)

Provides stock data through REST endpoints.

Can be extended to fetch real-time data from stock APIs (e.g., Yahoo Finance, Alpha Vantage).

Frontend (React)

Fetches stock data from the FastAPI backend.

Displays it in a table (Alerts View or Price View).

Provides an interactive and responsive UI.

Cloud + DevOps Integration

Dockerized Application → Backend and frontend are containerized for portability.

CI/CD Pipeline → On every Git push, build & deploy are triggered automatically.

AWS Deployment:

Frontend hosted on S3 + CloudFront (CDN) for scalability.

Backend deployed on EC2 with Nginx/Gunicorn or as a serverless Lambda API.

Monitoring & Scaling → Auto Scaling Groups (EC2) or AWS Lambda scaling for handling variable loads.

🎯 Future Enhancements

Real-Time Data – Connect to live stock APIs for dynamic updates.

Charts & Visualization – Use Recharts or Chart.js for trend analysis.

Authentication – Add secure user login with AWS Cognito.

Database Integration – Store historical data in AWS DynamoDB or RDS.

Advanced DevOps – Kubernetes on EKS for production-grade orchestration.

💡 Learning Outcomes

This project covers:

Building and connecting frontend + backend in a full-stack architecture.

Designing REST APIs with Python’s FastAPI.

Deploying applications on AWS Cloud with best practices.

Implementing DevOps workflows: containerization, CI/CD, and monitoring.

Gaining hands-on experience in scalable cloud-native application development.
