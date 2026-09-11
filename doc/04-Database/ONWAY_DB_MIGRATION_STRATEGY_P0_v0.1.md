# ONWAY - DB Migration & ORM Strategy P0

**Loai tai lieu:** Database Implementation Strategy  
**Phien ban:** 0.1  
**Trang thai:** Draft  
**Ngay cap nhat:** 11/09/2026  
**Stack decision:** Prisma + PostgreSQL/PostGIS + controlled raw SQL  

---

# 1. Decision

P0 uses:

- Prisma as the main database access layer.
- Prisma Migrate for normal relational schema migrations.
- Raw SQL migrations for PostgreSQL extensions, PostGIS geometry columns/indexes/functions, advanced partial indexes, and constraints Prisma cannot express cleanly.
- Repository/service wrappers for all raw SQL. No PostGIS raw SQL directly inside GraphQL resolvers.

Reason:

- Architecture ADR-037 already chooses Prisma.
- Prisma is strong for CRUD, transactions, generated TypeScript types, and normal migrations.
- Onway needs PostGIS; those parts must be handled with controlled SQL.

# 2. Repo structure recommendation

```txt
apps/api/
  prisma/
    schema.prisma
    migrations/
    seed.ts
    sql/
      postgis/
      indexes/
      views/
libs/
  database/
    prisma-client/
    repositories/
      region.repository.ts
      location.repository.ts
      matching.repository.ts
      catalog.repository.ts
```

If Nx layout chooses a shared Prisma package, keep one generated Prisma client consumed by API modules.

# 3. Prisma schema rules

## 3.1 Geometry fields

Use Prisma unsupported fields for PostGIS columns:

```prisma
model Region {
  id       String @id @default(uuid()) @db.Uuid
  boundary Unsupported("geometry(MultiPolygon,4326)")
}

model RestaurantOutlet {
  id       String @id @default(uuid()) @db.Uuid
  location Unsupported("geometry(Point,4326)")
}
```

Access geometry through repository methods using raw SQL:

- `containsPoint(regionId, point)`
- `resolveRegionByPoint(point, serviceType, vehicleType)`
- `findNearbyDrivers(point, radiusMeters, filters)`
- `validateOutletInsideRegion(outletId, regionId)`

## 3.2 Money fields

Use `BigInt` for `amountMinor` fields.

```prisma
amountMinor BigInt
currencyCode String @db.Char(3)
```

VND uses `minorUnitExponent = 0`, so `1.000.000 VND` is stored as `1000000`.

## 3.3 Status fields

P0 uses string status fields in Prisma plus DB-level `CHECK` constraints where useful.

Reason:

- Product states are still evolving.
- PostgreSQL enum migration is more rigid.
- Application-level enums still exist in TypeScript.

## 3.4 JSON fields

Use `Json` only for:

- policy config values;
- metadata;
- event payload snapshots;
- audit before/after summaries;
- external provider response snapshots.

Do not hide relational domain models in JSON.

# 4. Migration types

## 4.1 Prisma migrations

Use for:

- tables;
- normal columns;
- normal indexes/unique constraints Prisma supports;
- foreign keys;
- many-to-many join tables if explicit.

Command:

```bash
npx prisma migrate dev
npx prisma migrate deploy
```

## 4.2 Raw SQL inside Prisma migrations

Use for:

- `CREATE EXTENSION`.
- PostGIS geometry column transformations if needed.
- GIST indexes.
- Partial unique indexes.
- Complex check constraints.
- DB functions/views if needed.

Example migration SQL:

```sql
CREATE EXTENSION IF NOT EXISTS pgcrypto;
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS citext;

CREATE INDEX IF NOT EXISTS idx_regions_boundary_gist
ON regions USING GIST (boundary);
```

## 4.3 No silent destructive migrations

Production migration must not:

- drop columns/tables without explicit approved migration note;
- rewrite large tables without plan;
- delete production data;
- run test seeds.

# 5. Migration workflow

## 5.1 Local dev

1. Start local Postgres with PostGIS.
2. Run migrations.
3. Run seed for dev data only.
4. Run unit/integration tests.

## 5.2 CI

CI must:

- install dependencies;
- generate Prisma client;
- run migration validation on disposable database;
- run typecheck;
- run unit/integration tests;
- generate GraphQL schema;
- fail if generated schema has unexpected breaking changes.

## 5.3 Staging/production deploy

For production MVP:

1. Backup database or verify recent backup.
2. Deploy code artifact.
3. Run `prisma migrate deploy`.
4. Run post-migration verification SQL.
5. Restart app.
6. Run health check.
7. Roll back app release if health check fails.

DB rollback:

- Do not assume automatic down migration.
- Prefer forward fix migration.
- For high-risk migrations, prepare manual rollback script before deploy.

# 6. Seed data

P0 seed types:

- currencies: `VND`.
- country: Vietnam.
- initial city: TP. Ho Chi Minh.
- default policy configs.
- admin roles/permissions.
- development admin account placeholder.
- sample region only in local/dev, not production unless approved.

Production seed must not include fake drivers/customers/orders.

# 7. Repository rules for raw SQL

Allowed modules for raw SQL:

- `region`
- `location`
- `matching`
- `catalog`
- `analytics/admin reporting` if needed

Rules:

- Use parameterized queries only.
- Keep SQL in repository methods with tests.
- Do not concatenate user input.
- Return typed DTOs.
- Add integration tests for every PostGIS query.

Example:

```ts
await prisma.$queryRaw`
  SELECT id
  FROM regions
  WHERE status IN ('active', 'pilot')
    AND ST_Contains(boundary, ST_SetSRID(ST_Point(${lng}, ${lat}), 4326))
  LIMIT 1
`;
```

# 8. Transaction strategy

Use Prisma `$transaction` for:

- matching accept assignment;
- payment proof submission;
- Food order confirmation;
- catalog publishing;
- driver platform fee approval;
- complaint qualification and auto-lock;
- admin lock/unlock.

For atomic assignment:

- Use transaction.
- Lock session/offer rows where possible with raw SQL or safe conditional updates.
- Ensure only one accepted offer can assign entity.

# 9. Migration acceptance tests

- Fresh database can migrate from zero to latest.
- PostGIS extension exists.
- GIST indexes exist for region/outlet/ride/food location fields.
- Partial unique active records work: active menu per outlet, active override per outlet/item.
- VND currency seed has exponent `0`.
- Driver auto-lock index exists.
- Chat retention index exists.
- Prisma client generates successfully.

# 10. Open decisions

1. Exact local Postgres setup: Docker Compose or dev-managed DB.
2. Whether Prisma schema lives under `apps/api/prisma` or shared `libs/database`.
3. Exact migration approval policy before production.
4. Whether testcontainers are used for integration tests.

