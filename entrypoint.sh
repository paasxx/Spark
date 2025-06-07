#!/bin/bash
set -e

echo "Python path:"
which python
which python3

echo "Python version:"
python --version

echo "PIP packages instalados:"
pip list

echo "Usuário atual:"
whoami || echo "Não foi possível identificar o usuário"

echo "Gerando CSV com pandas (se necessário)..."
python generate_csv.py

echo "Processando CSV com Spark..."
spark-submit spark_pipeline.py
