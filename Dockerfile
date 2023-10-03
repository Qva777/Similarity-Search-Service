FROM python:3.11

WORKDIR /app

COPY requirements.txt /app/
COPY server.py /app/
COPY similarity_search.proto /app/

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m grpc_tools.protoc -I/app --python_out=/app --grpc_python_out=/app similarity_search.proto

CMD ["python", "server.py"]
