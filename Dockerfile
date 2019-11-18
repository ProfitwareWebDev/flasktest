FROM alpine

RUN apk add --no-cache bash python3 npm curl \
	&& pip3 install --upgrade pip 

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app
COPY package.json /app
COPY package-lock.json /app

COPY app.py /app
COPY static /app/static
COPY templates /app/templates

EXPOSE 5000

RUN pip install -r requirements.txt
RUN npm install .

CMD ["flask", "run", "--host=0.0.0.0"]

