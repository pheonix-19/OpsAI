#!/bin/bash
# Generate continuous traffic for metrics testing

echo "🚀 Generating continuous API traffic for Grafana testing..."
echo "Press Ctrl+C to stop"

while true; do
    # Make requests to different endpoints
    curl -s http://localhost:8000/ > /dev/null
    curl -s http://localhost:8000/docs > /dev/null
    curl -s http://localhost:8000/metrics > /dev/null
    
    # Wait a bit
    sleep 2
    
    echo -n "."
done
