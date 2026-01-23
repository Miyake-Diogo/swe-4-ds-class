# scripts/test_volume.py
"""Script para testar acesso a volumes."""
from pathlib import Path
import sys

data_dir = Path("/app/data")
print(f"Diretório de dados existe: {data_dir.exists()}")

if data_dir.exists():
    print("\nConteúdo:")
    for item in data_dir.rglob("*"):
        print(f"  {item}")
else:
    print("Diretório /app/data não encontrado!")
    print("Monte um volume com -v")
    sys.exit(1)