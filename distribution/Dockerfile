# Production image for the server (built there by docker compose).
FROM node:22-alpine
WORKDIR /app

COPY package.json package-lock.json ./
# better-sqlite3 normally downloads a ready-made binary; build tools are
# installed only if that ever fails.
RUN npm ci --no-audit --no-fund \
  || (apk add --no-cache python3 make g++ && npm ci --no-audit --no-fund)

COPY . .
ENV NODE_ENV=production NEXT_TELEMETRY_DISABLED=1
RUN npm run build && chown -R node:node /app/.next

# The database and the videos live on the server's disks (mounted at /data),
# never inside the image.
ENV DATA_DIR=/data/db CONTENT_DIR=/data/content
USER node
EXPOSE 3000
HEALTHCHECK --interval=30s --timeout=5s --start-period=40s --retries=3 \
  CMD wget -qO /dev/null http://127.0.0.1:3000/ || exit 1
CMD ["npx", "next", "start", "-p", "3000"]
