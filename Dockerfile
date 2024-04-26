FROM python
LABEL authors="fasadar"
LABEL description="Telegram Bot for VeloBrotherhood"
LABEL homepage="https://github.com/fasadar/telegram-bot"
LABEL license="MIT"
LABEL maintainer="fasadar"
LABEL version="1.0"

WORKDIR /app
COPY build.txt ./
RUN python -m pip install -r build.txt
COPY . .
ENTRYPOINT ["python"]
CMD ["./migrations/migration.py"]
ENTRYPOINT ["python"]
CMD ["./main.py"]