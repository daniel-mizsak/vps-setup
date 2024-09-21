# Set basic image data
FROM python:3.12-slim
LABEL org.opencontainers.image.source="https://github.com/daniel-mizsak/vps-setup"

ENV LANG=C.UTF-8
ENV TZ=Europe/Copenhagen

# Copy files
WORKDIR /workspace
COPY ./workspace/ ./

# Install python packages
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Run command
EXPOSE 80
CMD ["fastapi", "run", "fastapi_app/main.py", "--port", "80"]
