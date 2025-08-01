# 🤖 OpsAI: Intelligent IT Support Automation

<!--
    Author: Ayush
    GitHub: https://github.com/pheonix-19
    Project: OpsAI - Intelligent IT Support Automation
    Copyright (c) 2025 Ayush. All rights reserved.
-->

> **Transform your IT helpdesk with AI-powered ticket triage and resolution suggestions**

OpsAI is an advanced AI system that revolutionizes IT support operations by automatically categorizing tickets, suggesting solutions, and routing requests to the right teams. Using cutting-edge vector embeddings and fine-tuned language models, it learns from historical data to provide instant, contextual support recommendations.

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

### **🔍 Prometheus Query Examples**
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
source env/bin/activate
pip install -r requirements.txt
PYTHONPATH=. uvicorn src.api.main:app --reload
```

