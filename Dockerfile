FROM python
LABEL authors="fasadar"
LABEL description="Telegram Bot for VeloBrotherhood"
LABEL homepage="https://github.com/fasadar2/veloGameBot.git"
LABEL license="MIT"
LABEL maintainer="fasadar"
LABEL version="1.0a"

WORKDIR /app
COPY . .
COPY PyBuilder/builder.py ./
COPY PyBuilder/builder.xml ./
COPY migrations/migration.py ./
RUN python builder.py
RUN python migration.py
ENTRYPOINT ["python"]
CMD ["./main.py"]