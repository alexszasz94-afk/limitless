# Production image (built on the server by docker compose). One image, two
# containers: the dashboard (next start) and the scraper (scraper/scheduler.ts).
FROM node:22-alpine
WORKDIR /app

COPY package.json package-lock.json ./
# better-sqlite3 normally downloads a ready-made binary; build tools are
# installed only if that ever fails. Dev dependencies stay: tsx runs the scraper.
RUN npm ci --no-audit --no-fund \
  || (apk add --no-cache python3 make g++ && npm ci --no-audit --no-fund)

COPY . .
ENV NODE_ENV=production NEXT_TELEMETRY_DISABLED=1
RUN npm run build && chown -R node:node /app/.next

# The database lives on the server's disk (mounted at /data/db), never in the image.
ENV DATA_DIR=/data/db
USER node
EXPOSE 3100
HEALTHCHECK --interval=30s --timeout=5s --start-period=40s --retries=3 \
  CMD wget -qO /dev/null http://127.0.0.1:3100/login || exit 1
CMD ["node_modules/.bin/next", "start", "-p", "3100"]
