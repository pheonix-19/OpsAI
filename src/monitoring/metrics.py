#!/usr/bin/env python3
"""
Prometheus Metrics Module for OpsAI
Provides comprehensive monitoring and metrics collection for system performance.

Author: Ayush
GitHub: https://github.com/pheonix-19
Copyright (c) 2025
"""
# src/monitoring/metrics.py

import time
from fastapi import Request, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

# ─── Define metrics ─────────────────────────────────────────────────────
REQUEST_COUNT = Counter(
    "opsai_requests_total",
    "Total number of HTTP requests",
    ["method", "endpoint", "http_status"],
)
REQUEST_LATENCY = Histogram(
    "opsai_request_latency_seconds",
    "Request latency in seconds",
    ["method", "endpoint"],
)

def setup_metrics(app):
    @app.middleware("http")
    async def metrics_middleware(request: Request, call_next):
        start = time.time()
        response: Response = await call_next(request)
        duration = time.time() - start

        endpoint = request.url.path
        method   = request.method
        status   = response.status_code

        REQUEST_LATENCY.labels(method=method, endpoint=endpoint).observe(duration)
        REQUEST_COUNT.labels(method=method, endpoint=endpoint, http_status=status).inc()

        return response

    @app.get("/metrics")
    async def metrics():
        data = generate_latest()  # includes all registered metrics
        return Response(content=data, media_type=CONTENT_TYPE_LATEST)
