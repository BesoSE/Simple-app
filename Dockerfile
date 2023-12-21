FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN python3 -m venv myenv
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . .
CMD . myenv/bin/activate
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
