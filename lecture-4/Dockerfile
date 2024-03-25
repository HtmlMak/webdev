FROM node:17 as frontend_builder
WORKDIR /app

COPY client/package.json .
COPY client/package-lock.json .

RUN npm install
COPY ./client .
RUN npm run build



FROM python
WORKDIR /app
COPY ./server/requiments.txt .
RUN pip install -r requiments.txt
RUN pip install gunicorn

ENV PORT 3000

EXPOSE $PORT
COPY ./server .
COPY --from=frontend_builder /app/dist /app/app/static

# CMD ["flask", "run", "--host=0.0.0.0", "--debug"]
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:3000", "app:create_app()"]