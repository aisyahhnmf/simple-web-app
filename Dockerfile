FROM python:3.10-slim
WORKDIR /flask
COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt
COPY . .
EXPOSE 5000
CMD ["python", "-m", "flask", "--app", "board", "run", "--host=0.0.0.0", "--debug"]

