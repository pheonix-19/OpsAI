#!/bin/bash
# Test all Prometheus queries for OpsAI

echo "🔍 Testing all Prometheus queries..."

PROMETHEUS_URL="http://localhost:9090"

queries=(
    "opsai_requests_total"
    "rate(opsai_requests_total[5m])"
    "sum by (endpoint) (opsai_requests_total)"
    "sum by (http_status) (opsai_requests_total)"
    "histogram_quantile(0.95, rate(opsai_request_latency_seconds_bucket[5m]))"
    "process_resident_memory_bytes{job=\"opsai_api\"}"
    "rate(process_cpu_seconds_total{job=\"opsai_api\"}[5m])"
    "time() - process_start_time_seconds{job=\"opsai_api\"}"
    "up{job=\"opsai_api\"}"
    "python_gc_objects_collected_total{job=\"opsai_api\"}"
)

for query in "${queries[@]}"; do
    echo "Testing: $query"
    result=$(curl -s "$PROMETHEUS_URL/api/v1/query?query=$(echo "$query" | sed 's/ /%20/g' | sed 's/{/%7B/g' | sed 's/}/%7D/g' | sed 's/=/%3D/g' | sed 's/"/%22/g')" | jq '.data.result | length')
    if [ "$result" -gt 0 ]; then
        echo "  ✅ Working ($result series)"
    else
        echo "  ❌ No data"
    fi
    echo
done

echo "🎉 Query testing complete!"
