FROM nogil/python

WORKDIR /usr/src/app

#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./VarPartageeLecture.py" ]