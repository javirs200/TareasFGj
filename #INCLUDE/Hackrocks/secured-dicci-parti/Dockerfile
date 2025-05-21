FROM python:3.7.2-stretch

RUN useradd -U -m -s /bin/bash ctf

WORKDIR /home/ctf
COPY web.py ./ 
COPY flag.txt /flag.txt
RUN chmod 644 /flag.txt && pip install flask
RUN pip install datetime
RUN pip install werkzeug
RUN pip install pycryptodome

USER ctf

CMD [ "python", "/home/ctf/web.py" ]
