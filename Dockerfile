FROM itzg/minecraft-server
SHELL [ "/bin/bash", "-c" ]
COPY .env /.env
RUN export $(cat /.env | xargs)
ENTRYPOINT [ "/start" ]
HEALTHCHECK --start-period=1m CMD mc-health
