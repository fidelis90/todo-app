FROM python:latest

WORKDIR /app 

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY web/web.py .
COPY ../functions.py . 
COPY ../todo.txt . 

EXPOSE 8501

CMD ["streamlit", "run", "web.py"]