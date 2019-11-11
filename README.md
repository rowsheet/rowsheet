
# RowSheet

> © 2019-present, Alexander Kleinhans
> All Rights Reserved



This is intended to be deployed in a highly automated fasion. Credentials should be placed in the `.env` file and kept out of commit history. Current setup deployes to three environments:

   1. Production
   2. Staging
   3. Local

Current setup allows multiple databases to be used with seamless migrations and in-between procedures.

### `Makefile` Summary

You can run with the following files (also running intermediary steps).

    #-------------------------------------------------------------------------------
    # PRODUCTION
    #-------------------------------------------------------------------------------
    set_prod_env: ; # Setting production env vars...
    deploy_production: set_prod_env ; # Running staging server...
    create_production_superuser: set_staging_env; # Creating super-user on production server...
    #-------------------------------------------------------------------------------
    # STAGING 
    #-------------------------------------------------------------------------------
    set_staging_env: ; # Setting staging env vars...
    deploy_staging: set_staging_env; # Running staging server...
    create_staging_superuser: set_staging_env; # Creating super-user on staging server...
    #-------------------------------------------------------------------------------
    # LOCAL
    #-------------------------------------------------------------------------------
    run_local: ; # Running local server...
    migrate_local_db: ; # Migrating local database...
    make_local_migrations: ; # Migrating local database...
    collect_static : ; # Collecting local static-files...
    create_local_superuser: ; # Creating super-user for local server...
    #-------------------------------------------------------------------------------
    # PSQL (Database Command Line) 
    #-------------------------------------------------------------------------------
    psql_stage: ; # Connecting to staging database...
    psql_prod: ; # Connecting to staging database...
    psql_local: ; # Connecting to local database...
    #-------------------------------------------------------------------------------
    # DUMP (Database Dump to File) 
    #-------------------------------------------------------------------------------
    dump_stage_db: ; # Dumping staging database to local file...
    dump_prod_db: ; # Dumping production database to local file...
    #-------------------------------------------------------------------------------
    # SYNC (Copy Database to Database)
    #-------------------------------------------------------------------------------
    sync_db_staging_from_prod: dump_prod_db ; # Syncing staging database with data from production...
    sync_db_local_from_stage: dump_stage_db ; # Syncing local database with data from staging...
    sync_db_local_from_prod: dump_prod_db ; # Syncing local database with data from production...

Note: Currently, all deployments (that use env vars) must be deployed through the makefile since credentials are stored in `.env`, but cannot be exported from that same file into local environments (i.e. what you would do with `source env.sh` or `export KEY=VAL`) because of the logic that must be placed in the `.env` file (which is **NOT** a `bash` file, but must be used to inject into local deployments at runtime through the `Makefile`. Overall it's a bit of a pain, but it's highly reproducable.

## By RowSheet, LLC

> Company:    RowSheet, LLC 
> Contact:    alex@rowsheet.com
> Website:  [rowsheet.com](https://rowsheet.com/)
> Address:    312 Cheyenne St. Denver, CO 80403
> [Github](https://github.com/rowsheet)
