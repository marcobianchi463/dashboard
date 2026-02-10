FROM python:3.12-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
	STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

RUN apt-get update && apt-get install -y \
	build-essential \
	curl \
	git \
	&& rm -rf /var/lib/apt/lists/*

COPY app/ .

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
	CMD curl --fail http://localhost:8501/_stcore/health || exit 1

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
