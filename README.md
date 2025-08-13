# 🤖 OpsAI: Intelligent IT Support Automation

[![GitHub stars](https://img.shields.io/github/stars/pheonix-19/OpsAI.svg?style=social&label=Star)](https://github.com/pheonix-19/OpsAI)
[![GitHub forks](https://img.shields.io/github/forks/pheonix-19/OpsAI.svg?style=social&label=Fork)](https://github.com/pheonix-19/OpsAI/fork)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)

<!--
    Author: Ayush
    GitHub: https://github.com/pheonix-19
    Project: OpsAI - Intelligent IT Support Automation
    Copyright (c) 2025 Ayush. All rights reserved.
-->

> **Transform your IT helpdesk with AI-powered ticket triage and resolution suggestions**

OpsAI is an advanced AI system that revolutionizes IT support operations by automatically categorizing tickets, suggesting solutions, and routing requests to the right teams. Using cutting-edge vector embeddings and fine-tuned language models, it learns from historical data to provide instant, contextual support recommendations.

## � **Live Screenshots**

**🖥️ Grafana Dashboard in Action:**
![Grafana OpsAI Dashboard](asset/grafana.png)
*Real-time monitoring dashboard showing API metrics, request rates, and system health*

**📊 Prometheus Metrics Collection:**
![Prometheus Metrics](asset/promethius1.png)
*Prometheus collecting and displaying OpsAI application metrics*

**⚙️ Prometheus Configuration & Targets:**
![Prometheus Targets](asset/promethius2.png)
*Prometheus monitoring targets and service discovery configuration*

## �📋 **Table of Contents**

- [📸 Live Screenshots](#-live-screenshots)
- [🏗️ System Architecture](#️-system-architecture--components)
- [🎯 What Problem Does OpsAI Solve?](#-what-problem-does-opsai-solve)
- [✨ Core Features](#-core-features)
- [🚀 Quick Demo](#-quick-demo)
- [📋 Prerequisites](#-prerequisites)
- [⚡ Installation & Setup](#-installation--setup)
- [🎮 API Endpoints Reference](#-api-endpoints-reference)
- [📊 Monitoring & Observability](#-monitoring--observability)
- [📁 Project Structure](#-project-structure)
- [🔐 Security & Secrets Management](#-security--secrets-management)
- [🐳 Docker & Deployment](#-docker--deployment)
- [🔗 Enterprise Integrations](#-enterprise-integrations)
- [🧪 Testing & Development](#-testing--development)
- [🚨 Troubleshooting](#-troubleshooting)
- [🚀 Quick Start Guide](#-quick-start-guide)
- [📚 Additional Resources](#-additional-resources)
- [🤝 Contributing](#-contributing)
- [📄 License & Support](#-license--support)Intelligent IT Support Automation

<!--
    Author: Ayush
    GitHub: https://github.com/pheonix-19
    Project: OpsAI - Intelligent IT Support Automation
    Copyright (c) 2025 Ayush. All rights reserved.
-->

> **Transform your IT helpdesk with AI-powered ticket triage and resolution suggestions**

OpsAI is an ad## 🔐 **Security & Secrets Management**anced AI system that revolutionizes IT support operations by automatically categorizing tickets, suggesting solutions, and routing requests to the right teams. Using cutting-edge vector embeddings and fine-tuned language models, it learns from historical data to provide instant, contextual support recommendations.

## 🏗️ **System Architecture & Components**

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           🤖 OpsAI System Architecture                              │
└─────────────────────────────────────────────────────────────────────────────────────┘

           👤 Users                     🔧 IT Teams                   📊 Stakeholders
             │                            │                            │
             ▼                            ▼                            ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                               🔗 Integration Layer                                  │
├────────────────┬────────────────┬────────────────┬────────────────────────────────┤
│   📋 Jira      │  💬 Slack Bot  │ 🎫 Freshdesk   │     🌐 Custom APIs             │
│   Webhooks     │  Real-time     │ Ticket Sync    │     REST Endpoints             │
│   Automation   │  Notifications │ Customer Mgmt   │     External Systems           │
└────────────────┴────────────────┴────────────────┴────────────────────────────────┘
             │                            │                            │
             └──────────────┬─────────────────────────┬─────────────────┘
                            ▼                         ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                            🚀 FastAPI Server (Port 8000)                           │
├─────────────────────────────────────────────────────────────────────────────────────┤
│  📍 Endpoints:  /classify  |  /resolve  |  /feedback  |  /metrics  |  /docs        │
│                      │           │           │           │           │              │
│                      ▼           ▼           ▼           ▼           ▼              │
└─────────────────────────────────────────────────────────────────────────────────────┘
                                        │
                                        ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                              🧠 AI/ML Processing Core                               │
├──────────────────────┬──────────────────────┬──────────────────────┬──────────────┤
│   🔍 Vector Search   │   🤖 Language Model   │  🎯 Classification   │ 🔄 Learning  │
│                      │                      │                      │              │
│  📊 Embeddings:      │  🧬 Model:           │ 🏷️ Labels:           │ 📈 Training: │
│  • sentence-trans    │  • GPT-Neo-125M      │ • auth, network      │ • LoRA       │
│  • all-MiniLM-L6-v2  │  • LoRA Fine-tuned   │ • performance, mail  │ • Adaptation │
│  • Vector Similarity │  • Context-aware     │ • Team Routing       │ • Feedback   │
│                      │                      │                      │              │
│  🗂️ FAISS Index:     │  💭 Generation:      │ 🎯 Mapping:          │ 🔄 Updates:  │
│  • Fast Search       │  • Solution Suggest  │ • IT Helpdesk        │ • Continuous │
│  • Metadata Store    │  • Context Tickets   │ • Engineering        │ • Improvement│
└──────────────────────┴──────────────────────┴──────────────────────┴──────────────┘
                                        │
                                        ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                               💾 Data Storage Layer                                 │
├──────────────────────┬──────────────────────┬──────────────────────┬──────────────┤
│    📁 Raw Data       │   ⚙️ Processed       │   🗂️ Vector Index    │ 🎓 Models    │
│                      │                      │                      │              │
│  📄 tickets.csv      │  📋 Normalized:      │  🔍 FAISS Database:  │ 🧬 Weights:  │
│  📄 tickets.json     │  • ticket_0.json     │  • ticket_index      │ • LoRA       │
│  📊 Historical Data  │  • ticket_1.json     │  • ticket_meta.pkl   │ • Adapters   │
│  🔄 Continuous Feed  │  • Clean Format      │  • Fast Retrieval    │ • Fine-tuned │
│                      │  • Standardized      │  • Similarity Search │ • Checkpoint │
└──────────────────────┴──────────────────────┴──────────────────────┴──────────────┘
                                        │
                                        ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                            📊 Monitoring & Observability                           │
├──────────────────────┬──────────────────────┬──────────────────────┬──────────────┤
│  📈 Prometheus       │   📊 Grafana         │   🚨 Alerting        │ 📝 Logging   │
│  (Port 9090)         │   (Port 3000)        │                      │              │
│                      │                      │                      │              │
│  📊 Metrics:         │  📋 Dashboards:      │  🚨 Alerts:          │ 🗂️ Logs:     │
│  • Request Count     │  • Performance       │  • High Error Rate   │ • API Calls  │
│  • Response Time     │  • Error Rates       │  • Slow Response     │ • Model Inf. │
│  • AI Performance   │  • Business KPIs     │  • System Down       │ • Debug Info │
│  • System Health    │  • Real-time Charts  │  • Auto-notification │ • Audit Trail│
└──────────────────────┴──────────────────────┴──────────────────────┴──────────────┘
                                        │
                                        ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                              🐳 Infrastructure Layer                                │
├──────────────────────┬──────────────────────┬──────────────────────┬──────────────┤
│   🐳 Docker Setup    │   🐍 Python Env     │   🔥 Hardware        │ ⚙️ CI/CD     │
│                      │                      │                      │              │
│  📋 Services:        │  📦 Dependencies:    │  💻 Requirements:    │ 🔄 Pipeline: │
│  • API Container     │  • transformers      │  • Python 3.11+     │ • GitHub     │
│  • Prometheus        │  • fastapi           │  • 8GB+ RAM          │ • Actions    │
│  • Grafana           │  • torch             │  • CUDA GPU (opt)    │ • Testing    │
│  • Auto-scaling      │  • faiss-cpu         │  • 4GB Disk          │ • Deploy     │
└──────────────────────┴──────────────────────┴──────────────────────┴──────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────┐
│                              📈 Data Flow Direction                                 │
│                                                                                     │
│  Tickets → Integration → API → AI Processing → Data Storage → Monitoring            │
│     ↑                                          ↓                     ↓             │
│  Feedback ←── Solutions ←── Intelligence ←── Training ←── Analytics ←── Metrics     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

## 🎯 **What Problem Does OpsAI Solve?**

### **Before OpsAI (Traditional IT Support):**
```
User reports issue → Manual ticket review → Search past solutions → Assign to team → Resolution
⏱️ Hours/Days        💰 High cost        🔍 Time-intensive   👥 Manual routing
```

### **With OpsAI (AI-Powered Support):**
```
User reports issue → AI instant analysis → Auto-suggested solution → Smart team routing → Fast resolution
⚡ Seconds           💰 Cost efficient   🧠 AI-powered      🎯 Accurate routing
```

## ✨ **Core Features**

| Feature | Description | Business Impact |
|---------|-------------|-----------------|
| 🎯 **Smart Classification** | AI categorizes tickets by type (auth, network, performance) | Automatic team routing |
| 🧠 **Resolution Suggestions** | Generates solutions based on similar past cases | Faster problem solving |
| 🔍 **Semantic Search** | Finds relevant tickets using AI understanding, not just keywords | Better context matching |
| 📊 **Real-time Monitoring** | Prometheus metrics + Grafana dashboards | System health visibility |
| 🔗 **Enterprise Integration** | Connects with Jira, Slack, Freshdesk | Seamless workflow integration |
| 🎓 **Continuous Learning** | LoRA fine-tuning adapts to your organization | Improving accuracy over time |

## 🚀 **Quick Demo**

### **Example 1: Ticket Classification**
```bash
curl -X POST "http://localhost:8000/classify" \
  -H "Content-Type: application/json" \
  -d '{"text": "Cannot access email, getting authentication errors"}'
```
**Response:**
```json
{
  "tags": ["auth", "mail", "user"],
  "teams": ["IT Helpdesk"]
}
```

### **Example 2: AI Resolution Suggestion**
```bash
curl -X POST "http://localhost:8000/resolve" \
  -H "Content-Type: application/json" \
  -d '{"text": "Database connection timeout in production"}'
```
**Response:**
```json
{
  "suggestion": "Check database connection pool settings and increase timeout values...",
  "context_tickets": [{"title": "Similar DB issue", "resolution": "..."}]
}
```

## 📋 **Prerequisites**

- **Python 3.11+** (tested with 3.12.3)
- **8GB+ RAM** (for AI model inference)
- **Docker & Docker Compose** (for full stack deployment)
- **CUDA-compatible GPU** (optional, for faster inference)
- **4GB disk space** (for models and vector index)

## ⚡ **Installation & Setup**

### **Method 1: Local Development (Recommended for Testing)**

1. **Clone and Setup Environment:**
```bash
git clone https://github.com/pheonix-19/OpsAI.git
cd OpsAI

# Create virtual environment
python3 -m venv env
source env/bin/activate  # Linux/macOS
# env\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
pip install -e .
```

2. **Process Sample Data and Build AI Index:**
```bash
# Process the included sample tickets
PYTHONPATH=. python -m src.ingestion.ingest data/raw data/processed

# Build vector embeddings index for semantic search
PYTHONPATH=. python -m src.embeddings.build_index --input-dir data/processed --output-dir data/index
```

3. **Start the API Server:**
```bash
PYTHONPATH=. uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload
```

4. **Access the System:**
- **API Documentation**: http://localhost:8000/docs
- **Metrics Endpoint**: http://localhost:8000/metrics

### **Method 2: Full Production Stack (Docker)**

```bash
# Start complete monitoring stack
docker-compose up --build

# Access services:
# - OpsAI API: http://localhost:8000
# - Prometheus: http://localhost:9090  
# - Grafana: http://localhost:3000 (admin/admin)
```

## 🎮 **API Endpoints Reference**

| Endpoint | Method | Purpose | Example Use Case |
|----------|--------|---------|------------------|
| `/` | GET | Health check | Service monitoring |
| `/classify` | POST | Categorize tickets | Auto-route to teams |
| `/resolve` | POST | Get AI suggestions | Provide solutions |
| `/feedback` | POST | Submit user ratings | Improve AI accuracy |
| `/metrics` | GET | Prometheus metrics | System monitoring |

### **Detailed API Usage:**

#### **🎯 Classify Tickets**
```bash
curl -X POST "http://localhost:8000/classify" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Server not responding to ping requests",
    "top_k": 3
  }'
```

#### **🧠 Get AI Resolutions**
```bash
curl -X POST "http://localhost:8000/resolve" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Application crashes when uploading large files", 
    "top_k": 5
  }'
```

#### **📝 Submit Feedback**
```bash
curl -X POST "http://localhost:8000/feedback" \
  -H "Content-Type: application/json" \
  -d '{
    "ticket": {"title": "Login issue", "description": "Cannot access system"},
    "suggestion": "Reset password and clear browser cache",
    "rating": 5,
    "comment": "Perfect solution, worked immediately!"
  }'
```

## 📊 **Monitoring & Observability**

### **🔍 Prometheus Metrics**
OpsAI automatically tracks comprehensive performance metrics:

```bash
# View current metrics
curl http://localhost:8000/metrics | grep opsai

# Example metrics output:
opsai_requests_total{endpoint="/classify",method="POST"} 5.0
opsai_request_latency_seconds_sum{endpoint="/resolve"} 2.28
```

**Key Metrics Tracked:**
- **Request Volume**: API calls per endpoint per second
- **Response Times**: Latency percentiles (50th, 90th, 99th)
- **Error Rates**: Failed requests and status codes
- **AI Performance**: Model inference times
- **Business KPIs**: Total tickets processed

### **📈 Grafana Dashboards** ✅ **CONFIGURED & WORKING**

**✅ Active Dashboards:**
1. **OpsAI Monitoring Dashboard** - Real-time API metrics
2. **Prometheus 2.0 Stats** - System performance monitoring  
3. **Prometheus Stats** - Infrastructure metrics

**📊 Access:** http://localhost:3000 (admin/admin)

**Dashboard Features:**
- 📊 **Total API Requests**: Live request tracking
- ⏱️ **Request Rate**: Real-time requests per minute
- 🚨 **HTTP Status Codes**: Success vs Error monitoring
- 📈 **Endpoint Breakdown**: Usage analytics by endpoint
- 🥧 **Visual Analytics**: Interactive charts and tables

### **� Live Screenshots**

**🖥️ Grafana Dashboard in Action:**
![Grafana OpsAI Dashboard](asset/grafana.png)
*Real-time monitoring dashboard showing API metrics, request rates, and system health*

**📊 Prometheus Metrics Collection:**
![Prometheus Metrics](asset/promethius1.png)
*Prometheus collecting and displaying OpsAI application metrics*

**⚙️ Prometheus Configuration & Targets:**
![Prometheus Targets](asset/promethius2.png)
*Prometheus monitoring targets and service discovery configuration*

### **�🔍 Prometheus Query Examples**
Essential queries for monitoring (see `PROMETHEUS_QUERIES.md` for complete reference):

```promql
# Basic metrics
sum(opsai_requests_total) by (endpoint)          # Total requests by endpoint
rate(opsai_requests_total[5m])                   # Request rate per second

# Performance monitoring  
avg(opsai_request_latency_seconds) by (endpoint) # Average response time
histogram_quantile(0.95, rate(opsai_request_latency_seconds_bucket[5m])) # 95th percentile
```

## 📁 **Project Structure**
```
opsai/
├── src/                     # Core application code
│   ├── api/                 # FastAPI endpoints
│   ├── embeddings/          # Vector search & FAISS
│   ├── ingestion/           # Data processing 
│   ├── integrations/        # External APIs (Jira, Slack)
│   ├── model_training/      # AI model fine-tuning
│   └── monitoring/          # Prometheus metrics
├── data/                    # Training data & indexes
├── models/                  # LoRA adapters & weights
├── tests/                   # Test suite
└── infra/                   # Docker & monitoring configs
```

## � **Security & Secrets Management**

### **🚨 Important: Managing Secrets in Public Repositories**

⚠️ **NEVER commit actual secrets to your repository!** This guide shows you how to securely manage environment variables and API keys for both local development and CI/CD.

#### **📋 Required vs Optional Credentials**

| **Credential** | **Required For** | **Default Behavior** |
|---------------|------------------|---------------------|
| `DATABASE_URL` | Database connection | ✅ Defaults to local SQLite |
| `OPENAI_API_KEY` | OpenAI features | ⚠️ Optional - features disabled if missing |
| `HUGGINGFACE_API_TOKEN` | Model downloads | ⚠️ Optional - uses cached/local models |
| `JIRA_API_TOKEN` | JIRA integration | ⚠️ Only if using JIRA |
| `SLACK_BOT_TOKEN` | Slack bot | ⚠️ Only if using Slack |
| `FRESHDESK_API_KEY` | Freshdesk integration | ⚠️ Only if using Freshdesk |
| `DOCKERHUB_USER/TOKEN` | CI/CD deployment | ⚠️ Only for Docker Hub publishing |

#### **🛡️ Local Development Setup**

1. **Copy environment template:**
```bash
cp .env.example .env
```

2. **Edit `.env` with your actual values (NEVER commit this file):**
```bash
# Required only if using specific integrations
JIRA_URL="https://your-company.atlassian.net"
JIRA_USER="your-email@company.com"
JIRA_API_TOKEN="your_new_jira_token_here"

SLACK_BOT_TOKEN="xoxb-your-slack-bot-token-here"
SLACK_APP_TOKEN="xapp-your-slack-app-token-here"

# Optional - for enhanced AI features
OPENAI_API_KEY="sk-your-openai-key-here"
HUGGINGFACE_API_TOKEN="hf_your-token-here"
```

3. **The `.env` file is automatically ignored by git** (included in `.gitignore`)

#### **🔑 GitHub Secrets for CI/CD**

For GitHub Actions to work with your secrets:

1. **Go to GitHub Repository Settings**
2. **Navigate to:** Settings → Secrets and variables → Actions
3. **Add these secrets** (only the ones you need):

```
# Docker deployment (required for CI/CD)
DOCKERHUB_USER=your_dockerhub_username
DOCKERHUB_TOKEN=your_dockerhub_access_token

# Integration secrets (optional)
JIRA_API_TOKEN=your_jira_token
SLACK_BOT_TOKEN=your_slack_token
FRESHDESK_API_KEY=your_freshdesk_key
```

#### **✅ Security Best Practices Implemented**

- ✅ **No secrets in source code** - All credentials from environment variables
- ✅ **Secure config validation** - `src/config.py` handles missing secrets gracefully
- ✅ **Environment isolation** - Production vs development detection
- ✅ **CI/CD ready** - GitHub Actions configured with proper secret injection
- ✅ **Optional integrations** - Core functionality works without external APIs

#### **🔧 Security Configuration Files**

**Key files for security:**
- `.env.example` - Template with placeholder values (safe to commit)
- `src/config.py` - Secure configuration management 
- `.gitignore` - Ensures `.env` files are never committed
- `SECURITY.md` - Complete security guidelines

### **🚨 Token Security Checklist**

- [ ] All real tokens removed from version control
- [ ] `.env` file exists locally with actual values
- [ ] GitHub secrets configured for CI/CD
- [ ] Old/exposed tokens revoked and regenerated
- [ ] Team members trained on security practices

## 🐳 **Docker & Deployment**

### **🛠️ Fixed Docker Build Issues**

**Common Docker problems and solutions implemented:**

#### **❌ Problem: Package Version Conflicts**
```
ERROR: Could not find a version that satisfies the requirement tokenizers==0.21.2
ERROR: No matching distribution found for SQLAlchemy==2.0.23
```

#### **✅ Solution: Flexible Version Ranges**
Updated `requirements.txt` to use compatible version ranges instead of pinned versions:

```python
# Before (problematic)
tokenizers==0.21.2
SQLAlchemy==2.0.23

# After (working)
tokenizers>=0.13.0,<1.0.0
SQLAlchemy>=1.4.0,<3.0.0
```

#### **❌ Problem: Network Timeouts During Build**
```
pip._vendor.urllib3.exceptions.ReadTimeoutError: HTTPSConnectionPool: Read timed out
```

#### **✅ Solution: Enhanced Dockerfile**
```dockerfile
# Install with increased timeout and retries
RUN pip install --no-cache-dir \
    --timeout 1000 \
    --retries 5 \
    --default-timeout=1000 \
    -r requirements.txt
```

### **🚀 Deployment Options**

#### **Option 1: Quick Development Setup**
```bash
# Minimal setup for development
cp requirements-minimal.txt requirements.txt
docker-compose up --build
```

#### **Option 2: Full Production Stack**
```bash
# Complete setup with all features
docker-compose up --build
```

#### **Option 3: Retry Script (Handles Network Issues)**
```bash
# Automated retry with fallback to minimal setup
./docker-build.sh
```

### **📦 Docker Services Overview**

| **Service** | **Port** | **Purpose** | **Health Check** |
|-------------|----------|-------------|------------------|
| `opsai-api` | 8000 | Main application | `curl localhost:8000/` |
| `prometheus` | 9090 | Metrics collection | `curl localhost:9090/-/healthy` |
| `grafana` | 3000 | Monitoring dashboards | `curl localhost:3000/api/health` |

### **🔧 Docker Troubleshooting**

**Check service status:**
```bash
docker-compose ps
docker-compose logs api
```

**Restart specific service:**
```bash
docker-compose restart api
docker-compose restart prometheus
```

**Clean rebuild:**
```bash
docker-compose down
docker system prune -f
docker-compose up --build --no-cache
```

## 📊 **Monitoring & Metrics - Complete Setup Guide**

### **🎯 Prometheus Configuration**

**✅ Working Prometheus Setup:**

```yaml
# infra/prometheus/prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'prometheus'      # Self-monitoring
    static_configs:
      - targets: ['localhost:9090']
    
  - job_name: 'opsai_api'       # Application monitoring
    static_configs:
      - targets: ['api:8000']
```

### **📈 Grafana Dashboard Setup**

**✅ Auto-configured Grafana features:**

1. **Data Source**: Prometheus auto-configured at `http://prometheus:9090`
2. **Dashboards**: Pre-built OpsAI monitoring dashboard
3. **Provisioning**: Automatic setup via configuration files

**Access:** http://localhost:3000 (admin/admin)

### **📊 Available Metrics & Queries**

#### **🚀 OpsAI Application Metrics**

**✅ Confirmed Working Queries:**

```promql
# Instant metrics (always show data)
opsai_requests_total                              # Total API requests
process_resident_memory_bytes{job="opsai_api"}   # Memory usage
time() - process_start_time_seconds{job="opsai_api"}  # Uptime
up{job="opsai_api"}                              # Service availability
python_gc_objects_collected_total{job="opsai_api"}    # Python metrics

# Aggregated metrics
sum by (endpoint) (opsai_requests_total)         # Requests by endpoint  
sum by (http_status) (opsai_requests_total)      # Requests by status code
```

#### **📈 Rate-based Metrics (Need Traffic)**

```promql
# Generate traffic first: ./generate-traffic.sh
rate(opsai_requests_total[5m])                   # Request rate
rate(process_cpu_seconds_total{job="opsai_api"}[5m]) * 100  # CPU usage
histogram_quantile(0.95, rate(opsai_request_latency_seconds_bucket[5m]))  # 95th percentile latency
```

### **🔍 Testing Metrics**

**Generate test traffic:**
```bash
# Continuous traffic generation
./generate-traffic.sh

# Or manual testing
for i in {1..20}; do 
  curl -s http://localhost:8000/ > /dev/null
  curl -s http://localhost:8000/docs > /dev/null
  sleep 1
done
```

**Verify metrics in Prometheus:**
```bash
# Check if metrics are being collected
curl -s "http://localhost:9090/api/v1/query?query=opsai_requests_total" | jq '.data.result | length'

# Test specific queries
curl -s "http://localhost:9090/api/v1/query?query=up{job=\"opsai_api\"}"
```

### **📋 Grafana Dashboard Features**

**Working dashboard panels:**
- 📊 **Total API Requests**: Real-time request count
- ⏱️ **Request Rate**: Requests per minute over time
- 🥧 **HTTP Status Codes**: Success vs error breakdown  
- 📈 **Request Latency**: Response time percentiles
- 💾 **Memory Usage**: RAM consumption tracking
- ⏰ **Service Uptime**: Time since last restart

### **🚨 Monitoring Troubleshooting**

**If Grafana shows "No Data":**

1. **Check Prometheus targets:**
   ```bash
   curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | {job: .labels.job, health: .health}'
   ```

2. **Verify data source in Grafana:**
   - URL should be: `http://prometheus:9090`
   - Click "Save & Test" - should show green "Data source is working"

3. **Test simple queries in Grafana:**
   - Start with: `opsai_requests_total`
   - Set time range to "Last 15 minutes"
   - Enable auto-refresh (5s)

4. **Generate traffic if needed:**
   ```bash
   ./generate-traffic.sh
   ```

### **📈 Custom Dashboard Creation**

**Manual dashboard setup:**
1. Go to Grafana → "+" → Dashboard → Add new panel
2. Enter query: `opsai_requests_total`
3. Set visualization type (Time series, Stat, etc.)
4. Configure time range and refresh interval
5. Save dashboard

### **🔧 Monitoring Best Practices**

- ✅ **Start simple**: Use instant metrics first (`opsai_requests_total`)
- ✅ **Generate traffic**: Use `./generate-traffic.sh` for rate metrics
- ✅ **Check time ranges**: Use "Last 15 minutes" for recent data
- ✅ **Verify targets**: Ensure Prometheus is scraping successfully
- ✅ **Test queries**: Use Prometheus UI to validate queries before Grafana

## 📚 **Step-by-Step Setup Walkthrough**

### **🚀 Complete Setup from Scratch**

#### **1. Repository Setup**
```bash
git clone https://github.com/pheonix-19/OpsAI.git
cd OpsAI
```

#### **2. Security Configuration**
```bash
# Copy environment template
cp .env.example .env

# Edit .env with your actual credentials (optional)
nano .env

# Verify .env is in .gitignore
grep -q "^\.env$" .gitignore && echo "✅ .env properly ignored"
```

#### **3. Docker Build (with retry logic)**
```bash
# Method 1: Automated retry script
chmod +x docker-build.sh
./docker-build.sh

# Method 2: Manual build
docker-compose up --build

# Method 3: Minimal build (if having issues)
cp requirements-minimal.txt requirements.txt
docker-compose up --build
```

#### **4. Verify Services**
```bash
# Check all services are running
docker-compose ps

# Test API
curl http://localhost:8000/

# Test metrics endpoint
curl http://localhost:8000/metrics | head -10

# Check Prometheus targets
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[].health'
```

#### **5. Setup Monitoring**
```bash
# Generate test traffic
./generate-traffic.sh &

# Open Grafana (admin/admin)
open http://localhost:3000

# Open Prometheus
open http://localhost:9090
```

#### **6. Test AI Features**
```bash
# Test classification
curl -X POST "http://localhost:8000/classify" \
  -H "Content-Type: application/json" \
  -d '{"text": "Cannot login to email account"}'

# Test resolution suggestions  
curl -X POST "http://localhost:8000/resolve" \
  -H "Content-Type: application/json" \
  -d '{"text": "Database connection timeout error"}'
```

### **🔧 CI/CD Setup**

#### **GitHub Actions Configuration**

Your repository includes automated CI/CD with these workflows:

**`.github/workflows/ci.yml`** - Tests and builds on every push:
```yaml
# Automatically runs:
- Python linting with flake8
- Test suite with pytest  
- Docker image build
- Deployment to Docker Hub (if secrets configured)
```

**`.github/workflows/retrain.yml`** - Scheduled model retraining:
```yaml
# Runs weekly to:
- Retrain AI models with new data
- Update LoRA adapters
- Upload new model artifacts
```

#### **Required GitHub Secrets for CI/CD**

**Minimal setup (for basic CI/CD):**
```
DOCKERHUB_USER=your_dockerhub_username
DOCKERHUB_TOKEN=your_dockerhub_access_token
```

**Full setup (for all integrations):**
```
JIRA_API_TOKEN=your_jira_token
SLACK_BOT_TOKEN=your_slack_token  
FRESHDESK_API_KEY=your_freshdesk_key
```

### **📝 Configuration Files Reference**

| **File** | **Purpose** | **When to Edit** |
|----------|-------------|------------------|
| `.env.example` | Template for environment variables | Never (contains placeholders) |
| `.env` | Your actual secrets (not in git) | Add your real credentials |
| `src/config.py` | Configuration management | Customize app settings |
| `requirements.txt` | Python dependencies | Add new packages |
| `docker-compose.yml` | Service orchestration | Modify ports/volumes |
| `infra/prometheus/prometheus.yml` | Metrics collection | Add monitoring targets |

### **🎯 Quick Validation Checklist**

- [ ] Services start: `docker-compose ps` shows all running
- [ ] API responds: `curl http://localhost:8000/` returns JSON
- [ ] Metrics work: `curl http://localhost:8000/metrics` shows data
- [ ] Prometheus scraping: Targets page shows "UP" status
- [ ] Grafana connected: Data source test succeeds
- [ ] Dashboards show data: Generate traffic and verify graphs
- [ ] AI features work: Classification and resolution endpoints respond
- [ ] Security configured: No real secrets in git, `.env` properly ignored

This comprehensive setup ensures your OpsAI deployment is secure, monitored, and production-ready! 🎉

## 🔗 **Enterprise Integrations**

### **📋 Jira Integration**
```bash
# Environment variables for Jira
JIRA_URL=https://your-domain.atlassian.net
JIRA_USER=your-email@company.com
JIRA_API_TOKEN=your-api-token

# Auto-process tickets from Jira webhooks
# POST /jira/webhook - Receives ticket updates
```

### **💬 Slack Bot Integration**
```bash
# Slack bot configuration
SLACK_BOT_TOKEN=xoxb-your-bot-token
SLACK_APP_TOKEN=xapp-your-app-token

# Start the Slack bot
python src/integrations/slack_bot.py
```

## 🧪 **Testing & Development**

### **Run Test Suite:**
```bash
# Run all tests
pytest

# Run specific modules
pytest tests/test_api.py        # API endpoint tests
pytest tests/test_embeddings.py # Vector search tests
pytest tests/test_ingestion.py  # Data processing tests
```

### **Development Workflow:**
```bash
# Hot reload during development
uvicorn src.api.main:app --reload --port 8000

# Process new training data
python src/ingestion/ingest.py --input data/raw/new_tickets.csv

# Rebuild search index
python src/embeddings/build_index.py --input-dir data/processed --output-dir data/index
```

## 🚨 **Troubleshooting**

### **Common Issues & Solutions**

**🔧 Device Mismatch Error:**
```
RuntimeError: Expected all tensors to be on the same device
```
**Solution:** ✅ Fixed in latest version - tensors automatically moved to correct device

**🔧 Import Errors:**
```
ImportError: attempted relative import with no known parent package
```
**Solution:** Use `PYTHONPATH=. python -m src.module.script`

**🔧 Port Already in Use:**
```
OSError: [Errno 98] Address already in use
```
**Solution:** Use different port: `--port 8001` or kill existing process

### **Debugging Commands**
```bash
# Check API health
curl http://localhost:8000/

# View current metrics
curl http://localhost:8000/metrics | grep opsai

# Check Docker services
docker-compose ps
```

## 🚀 **Quick Start Guide**

**1. Test Basic Classification:**
```bash
curl -X POST "http://localhost:8000/classify" \
  -H "Content-Type: application/json" \
  -d '{"text": "Password reset needed for user account"}'
```

**2. Get AI-Powered Solutions:**
```bash
curl -X POST "http://localhost:8000/resolve" \
  -H "Content-Type: application/json" \
  -d '{"text": "Email server connection timeout"}'
```

**3. Provide Feedback for Learning:**
```bash
curl -X POST "http://localhost:8000/feedback" \
  -H "Content-Type: application/json" \
  -d '{
    "ticket": {"title": "Login issue"},
    "suggestion": "Reset password", 
    "rating": 5,
    "comment": "Perfect solution!"
  }'
```

## 📚 **Additional Resources**

### **🔗 Useful Links**
- **📖 API Documentation**: http://localhost:8000/docs (when running)
- **📊 Monitoring**: http://localhost:3000 (Grafana dashboards)  
- **🔍 Metrics**: http://localhost:9090 (Prometheus)
- **📋 Query Reference**: See `PROMETHEUS_QUERIES.md` for complete monitoring guide
- **🐛 Issues**: https://github.com/pheonix-19/OpsAI/issues
- **💬 Discussions**: https://github.com/pheonix-19/OpsAI/discussions

### **📖 Technical Stack**
- **Vector Embeddings**: `sentence-transformers/all-MiniLM-L6-v2`
- **Language Model**: `EleutherAI/gpt-neo-125M` with LoRA fine-tuning
- **Search Index**: FAISS (Facebook AI Similarity Search)
- **Monitoring**: Prometheus + Grafana stack
- **API Framework**: FastAPI with automatic OpenAPI docs

## 🤝 **Contributing**

We welcome contributions! Here's how to get started:

### **🛠️ Development Setup**
```bash
# Fork the repository
git clone https://github.com/your-username/OpsAI.git
cd OpsAI

# Create feature branch
git checkout -b feature/amazing-improvement

# Make changes and test
pytest
pre-commit run --all-files

# Submit pull request
git push origin feature/amazing-improvement
```

### **🎯 Contribution Areas**
- 🐛 **Bug Fixes**: Fix issues and improve stability
- ✨ **New Features**: Add integrations, UI improvements, ML enhancements
- 📚 **Documentation**: Improve guides, examples, and API docs
- 🧪 **Testing**: Add test coverage and performance benchmarks

## 📄 **License & Support**

### **📜 License**
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### **🆘 Getting Help**

**For Questions:**
1. 📖 Check this README and API documentation first
2. 🔍 Search existing [GitHub issues](https://github.com/pheonix-19/OpsAI/issues)
3. 💬 Start a [GitHub discussion](https://github.com/pheonix-19/OpsAI/discussions)
4. 🐛 Create a new issue with detailed information

**For Bugs:**
Include in your issue:
- Python version and OS
- Complete error message and stack trace  
- Steps to reproduce the problem
- Expected vs actual behavior

### **🙏 Acknowledgments**

- **Hugging Face**: For transformer models and libraries
- **FastAPI**: For the excellent web framework
- **Prometheus & Grafana**: For monitoring and observability
- **FAISS**: For efficient vector similarity search
- **OpenAI/EleutherAI**: For foundation language models

---

## 🎉 **Ready to Transform Your IT Support?**

OpsAI is production-ready and has been tested with real-world IT scenarios. Start with the sample data, then gradually add your organization's historical tickets to improve accuracy.

**Get started in 5 minutes:**
```bash
git clone https://github.com/pheonix-19/OpsAI.git
cd OpsAI
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
pip install -e .
PYTHONPATH=. uvicorn src.api.main:app --reload
```

