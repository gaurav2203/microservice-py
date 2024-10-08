# Microservices Flask Application

This project is a simple microservices application built with Flask, Docker Compose, and Kubernetes. It consists of two main services:

- **Frontend Service**: A Flask application that serves the user interface.
- **Backend Service**: A Flask application that provides API endpoints and interacts with a PostgreSQL database.
- **Database Service**: A PostgreSQL database used by the backend service.

**Note**: This Project contains two branches master and v2. The master branch contains only one backend microservice but the v2 branch contains two backend services where the hello message is also configured as backend2 microservice and the backend microservice only contains the database connection.


## Table of Contents

- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Running with Docker Compose](#running-with-docker-compose)
  - [Configuration](#configuration)
  - [Deploying on Kubernetes](#deploying-on-kubernetes)
- [Application](#application)


## Architecture

The application follows a microservices architecture where each component is a separate service that can be developed, deployed, and scaled independently.

<!-- You can include an architecture diagram here if you have one. -->

## Project Structure

```plaintext
microservices-app/
├── backend/                -- contains the backend application files written in Python Flask
├── frontend/               -- contains the frontend application files along with HTML and CSS files
├── database/               -- contains the initial PostgreSQL table 
├── docker-compose.yml      -- deploys the application using docker-compose
├── kubernetes/             -- contains all the k8s manifests to deploy this application
└── README.md
```

## Getting Started

### Prerequisites

- **Docker** and **Docker Compose** installed on your local machine.
- **Python 3.x** installed to run the services locally.
- **Kubernetes** cluster (optional, for Kubernetes deployment). Here, I have used local k8s kubeadm cluster with untainted master node.

### Running with Docker Compose

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/microservices-app.git
   cd microservices-app
   ```
2. **Build and Run the services**

   ```bash
   docker-compose up --build
   ```
   This command will build the docker images and start all the services defined in docker-compose.yml.

3. **Access the Application**
  - Open your browser and navigate to ```http://localhost:5000``` to access the frontend services.

### Configuration

1. **ConfigMap:** I have created a configmap manifest with sample values. You can change the values according to your needs. Here, I have given all the values in plain text, for added security you can also create additional secrets and reference the values to the manifest file. 

### Deploying on Kubernetes
1. **Apply kubernetes manifests**
   ```bash
   kubectl apply -f k8s/
   ```
   This will create all the objects defined in the k8s manifest.

2. **Checking the status of the Application**
   ```bash
   kubectl get all
   ```
   It should display all the 3 pods in ```Running``` state, with 3 services, deployments and replicasets each.

3. **Accessing the Application**
   ```bash
   kubectl get svc
   ```
   Find the frontend service with type NodePort. All copy the port starting with 30000. Go on the browser and paste the following URL to access the application.
   ``` <node-ip>:<copied port>```

### Application
- **Endpoints**
    - ``` / ```: Main Page that displays 'Hello' message.
    - ``` /db ```: Displays the data from database via backend microservice.
