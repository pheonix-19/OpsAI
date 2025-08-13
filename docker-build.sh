#!/bin/bash
# Docker build script with retry logic for network issues

echo "🐳 Building OpsAI Docker container with retry logic..."

MAX_ATTEMPTS=3
ATTEMPT=1

while [ $ATTEMPT -le $MAX_ATTEMPTS ]; do
    echo "🔄 Attempt $ATTEMPT of $MAX_ATTEMPTS"
    
    if docker-compose build --no-cache; then
        echo "✅ Build successful!"
        echo "🚀 Starting containers..."
        docker-compose up
        exit 0
    else
        echo "❌ Build failed on attempt $ATTEMPT"
        if [ $ATTEMPT -eq $MAX_ATTEMPTS ]; then
            echo "💥 All attempts failed. Trying with minimal requirements..."
            
            # Backup original requirements
            cp requirements.txt requirements-full.txt
            cp requirements-minimal.txt requirements.txt
            
            echo "📦 Building with minimal requirements..."
            if docker-compose build --no-cache; then
                echo "✅ Minimal build successful!"
                echo "ℹ️  You can install additional packages later if needed"
                docker-compose up
                exit 0
            else
                echo "💥 Even minimal build failed. Check your network connection."
                # Restore original requirements
                cp requirements-full.txt requirements.txt
                exit 1
            fi
        fi
        
        echo "⏳ Waiting 10 seconds before retry..."
        sleep 10
        ATTEMPT=$((ATTEMPT + 1))
    fi
done
