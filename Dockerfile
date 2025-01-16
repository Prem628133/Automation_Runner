# Use python version
FROM python:3.11

#file to save
WORKDIR /app

#copying requirements
COPY requirements.txt requirements.txt

#Running necessary requirements
RUN pip install --no-cache-dir -r requirements.txt

#Copying all files
COPY . .

#Declaring the port
EXPOSE 8000

#Commands
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]




