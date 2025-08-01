# 📊 OpsAI Prometheus Queries Reference

This document contains useful Prometheus queries for monitoring your OpsAI system.

## 🎯 Basic Metrics Queries

### Request Volume
```promql
# Total requests across all endpoints
sum(opsai_requests_total)

# Requests by endpoint
sum(opsai_requests_total) by (endpoint)

# Request rate (requests per second)
rate(opsai_requests_total[5m])

# Request rate by endpoint
rate(opsai_requests_total[5m]) by (endpoint)
```

### HTTP Status Monitoring
```promql
# Requests by status code
sum(opsai_requests_total) by (http_status)

# Success rate (2xx responses)
sum(rate(opsai_requests_total{http_status=~"2.."}[5m])) / sum(rate(opsai_requests_total[5m])) * 100

# Error rate (4xx + 5xx responses)
sum(rate(opsai_requests_total{http_status=~"[45].."}[5m])) / sum(rate(opsai_requests_total[5m])) * 100

# Client errors (4xx)
sum(rate(opsai_requests_total{http_status=~"4.."}[5m]))

# Server errors (5xx)
sum(rate(opsai_requests_total{http_status=~"5.."}[5m]))
```

## ⚡ Performance Queries

### Response Time Analysis
```promql
# Average response time
avg(opsai_request_latency_seconds) by (endpoint)

# 50th percentile (median) response time
histogram_quantile(0.50, rate(opsai_request_latency_seconds_bucket[5m]))

# 90th percentile response time
histogram_quantile(0.90, rate(opsai_request_latency_seconds_bucket[5m]))

# 95th percentile response time
histogram_quantile(0.95, rate(opsai_request_latency_seconds_bucket[5m]))

# 99th percentile response time
histogram_quantile(0.99, rate(opsai_request_latency_seconds_bucket[5m]))
```

### System Health
```promql
# Service uptime
up{job="opsai_api"}

# CPU usage (if node_exporter is configured)
100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# Memory usage (if node_exporter is configured)
(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100
```

## 💼 Business KPIs

### Ticket Processing
```promql
# Total tickets processed (classification + resolution)
sum(opsai_requests_total{endpoint=~"/classify|/resolve"})

# Classification requests only
sum(opsai_requests_total{endpoint="/classify"})

# Resolution requests only
sum(opsai_requests_total{endpoint="/resolve"})

# Feedback submissions
sum(opsai_requests_total{endpoint="/feedback"})
```

### Hourly/Daily Trends
```promql
# Requests per hour
rate(opsai_requests_total[1h]) * 3600

# Daily request increase
increase(opsai_requests_total[1d])

# Weekly trends
increase(opsai_requests_total[7d])

# Peak hour detection
topk(5, rate(opsai_requests_total[1h]) * 3600)
```

### AI Performance Metrics
```promql
# AI classification processing time
avg(opsai_request_latency_seconds{endpoint="/classify"})

# AI resolution processing time
avg(opsai_request_latency_seconds{endpoint="/resolve"})

# Classification vs Resolution performance comparison
avg(opsai_request_latency_seconds{endpoint="/classify"}) / avg(opsai_request_latency_seconds{endpoint="/resolve"})
```

## 🚨 Alerting Queries

### Critical Alerts
```promql
# Service is down (no requests for 5 minutes)
rate(opsai_requests_total[5m]) == 0

# High error rate (>5% for 2+ minutes)
(
  sum(rate(opsai_requests_total{http_status=~"5.."}[2m])) 
  / 
  sum(rate(opsai_requests_total[2m]))
) * 100 > 5

# High latency (95th percentile >2 seconds)
histogram_quantile(0.95, rate(opsai_request_latency_seconds_bucket[5m])) > 2
```

### Warning Alerts
```promql
# Elevated error rate (>1% for 5+ minutes)
(
  sum(rate(opsai_requests_total{http_status=~"[45].."}[5m])) 
  / 
  sum(rate(opsai_requests_total[5m]))
) * 100 > 1

# Slow response time (90th percentile >1 second)
histogram_quantile(0.90, rate(opsai_request_latency_seconds_bucket[5m])) > 1

# Low request volume (unusual drop)
rate(opsai_requests_total[5m]) < 0.1
```

## 📈 Capacity Planning

### Resource Utilization
```promql
# Request growth rate (week over week)
(rate(opsai_requests_total[7d]) / rate(opsai_requests_total[7d] offset 7d) - 1) * 100

# Peak requests per second
max_over_time(rate(opsai_requests_total[5m])[1d])

# Average daily load
avg_over_time(rate(opsai_requests_total[1h])[1d]) * 3600
```

### Forecasting
```promql
# Predict future load (linear prediction)
predict_linear(opsai_requests_total[24h], 24*3600)

# Request volume trend
deriv(rate(opsai_requests_total[1h])[12h])
```

## 🔧 Debugging Queries

### Troubleshooting
```promql
# Find endpoints with highest error rates
topk(10, 
  sum(rate(opsai_requests_total{http_status=~"[45].."}[5m])) by (endpoint)
  / 
  sum(rate(opsai_requests_total[5m])) by (endpoint)
)

# Slowest endpoints
topk(5, avg(opsai_request_latency_seconds) by (endpoint))

# Most active endpoints
topk(10, sum(rate(opsai_requests_total[5m])) by (endpoint))

# Recent errors
opsai_requests_total{http_status=~"[45].."}
```

### Status Validation
```promql
# Verify metrics are being collected
up{job="opsai_api"}

# Check scrape intervals
rate(prometheus_tsdb_head_samples_appended_total[5m])

# Validate endpoint availability
sum(opsai_requests_total{endpoint="/"}) > 0
```

## 📊 Dashboard Building

### Panel Queries for Grafana
```promql
# API Request Rate (Time Series)
rate(opsai_requests_total[5m])

# Total Requests (Stat Panel)
sum(opsai_requests_total)

# Error Rate (Gauge)
sum(rate(opsai_requests_total{http_status=~"5.."}[5m])) / sum(rate(opsai_requests_total[5m])) * 100

# Response Time Distribution (Heatmap)
rate(opsai_request_latency_seconds_bucket[5m])

# Top Endpoints (Table)
sort_desc(sum(rate(opsai_requests_total[5m])) by (endpoint))
```

## 🎯 Quick Reference Commands

### Test Queries in Prometheus
```bash
# Access Prometheus web UI
open http://localhost:9090

# Query via API
curl "http://localhost:9090/api/v1/query?query=sum(opsai_requests_total)"

# Query with time range
curl "http://localhost:9090/api/v1/query_range?query=rate(opsai_requests_total[5m])&start=2025-08-01T00:00:00Z&end=2025-08-01T23:59:59Z&step=5m"
```

### Validate Metrics Collection
```bash
# Check if OpsAI metrics are being scraped
curl -s http://localhost:9090/api/v1/label/__name__/values | jq '.data[]' | grep opsai

# View raw metrics from OpsAI
curl http://localhost:8000/metrics | grep opsai
```

---
**💡 Tip**: Use these queries in Grafana to create comprehensive dashboards for monitoring your OpsAI system performance and health!
