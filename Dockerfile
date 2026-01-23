

FROM python:3.12-slim

# Metadados da imagem
LABEL maintainer="seu-email@exemplo.com"
LABEL version="1.0"
LABEL description="API de predição de inadimplência de cartão de crédito"


# Variáveis de ambiente Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Diretório de trabalho
WORKDIR /app


# Instalar dependências do sistema (necessárias para algumas libs Python)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copiar apenas requirements primeiro (para cache de camadas)
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt


# Copiar código fonte
COPY src/ ./src/

# Copiar outros arquivos necessários
COPY pyproject.toml .

# Criar usuário não-root para segurança
RUN useradd --create-home --shell /bin/bash appuser
RUN chown -R appuser:appuser /app
USER appuser

# Porta que a aplicação vai usar (documentação)
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Comando padrão (será sobrescrito quando tivermos FastAPI)
CMD ["python", "-c", "print('Container swe4ds-credit-api iniciado!')"]