# Deployment

## Environments

| Environment | Purpose | URL/App Target | Notes |
| --- | --- | --- | --- |
| Local | Dev/test/migration validation | Local apps/services | Must have local dev DB; do not use production data for seed/test/migration trials |
| Production | MVP production | Domain/app store targets assigned during release setup | Current decision: one production environment, direct RDS production connection |
| Staging | Optional/future | Future environment | Not required for MVP if keeping simple, but risk must be managed |

## Build / Release

- Cloud: AWS.
- Backend API: EC2 simple deployment.
- Database: AWS RDS PostgreSQL + PostGIS.
- Redis: ElastiCache Redis.
- File/evidence storage: S3.
- Logs/metrics: CloudWatch minimum baseline; Sentry/OpenTelemetry not required for MVP start.
- Secrets: AWS Secrets Manager or SSM Parameter Store.
- Queue: BullMQ on Redis.
- CI/CD: GitHub Actions.
- CI minimum: lint, typecheck, unit test, build.
- CD minimum: deploy to EC2 via SSH or artifact copy, run controlled migration, restart service, health check.
- Rollback minimum: keep previous release and restart if health check fails.
- EC2 runtime: PM2 or systemd, reverse proxy via Nginx/Caddy.
- TLS: ACM + Load Balancer if ALB exists, otherwise Let's Encrypt for direct EC2 path.
- Backup/restore: RDS automated backup, point-in-time recovery if cost acceptable, test restore before true production.
- Mobile release: TestFlight for iOS, Google Play Internal Testing for Android before production; backend exposes min-version/force-update config.
- Web/Admin release can deploy independently from mobile after scaffold; Landing/Admin build artifacts can use GitHub Actions.
