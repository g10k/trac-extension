# docker build -t registry.service.mm.consul:5000/till .

FROM g10k/filebeat
MAINTAINER telminov <telminov@soft-way.biz>

EXPOSE 8080

VOLUME /data/
VOLUME /conf/
VOLUME /static/
VOLUME /node_modules/
VOLUME /logs/
VOLUME /tls/

RUN apt-get update && \
    apt-get install -y \
                    vim \
                    supervisor \
                    curl \
                    build-essential

RUN curl -sL https://deb.nodesource.com/setup | sudo bash -
RUN apt-get install -y nodejs

RUN mkdir /var/log/trac_extra

# copy source
COPY . /opt/trac_extra
WORKDIR /opt/trac_extra

RUN pip3 install -r requirements.txt
RUN cp project/local_settings.sample.py project/local_settings.py

COPY supervisord.conf /etc/supervisor/conf.d/trac_extra.conf

CMD test "$(ls /conf/local_settings.py)" || cp project/local_settings.sample.py /conf/local_settings.py; \
    test "$(ls /conf/filebeat.yml)" || cp /etc/filebeat/filebeat.yml /conf/filebeat.yml; \
    rm project/local_settings.py;  ln -s /conf/local_settings.py project/local_settings.py; \
    rm /etc/filebeat/filebeat.yml; ln -s /conf/filebeat.yml /etc/filebeat/filebeat.yml; \
    rm -rf static; ln -s /static static; \
    rm -rf node_modules; ln -s /node_modules node_modules; \
    service filebeat start; \
    npm install; \
    python3 ./manage.py migrate; \
    python3 ./manage.py collectstatic --noinput; \
    /usr/bin/supervisord -c /etc/supervisor/supervisord.conf --nodaemon