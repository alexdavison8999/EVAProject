#!/bin/bash

POSTGRES_USER="evadb"
POSTGRES_PASSWORD="evadb100"
DATABASE_NAME="evadb"
MY_FILES="database/migrations/*.sql"

export PGPASSWORD=$POSTGRES_PASSWORD

echo "MAKE SURE YOU HAVE POSTGRES INSTALLED AND CAN LOGIN AS "postgres""

psql -U postgres < database/createUser.sql

echo "Created user '$POSTGRES_USER' and database '$DATABASE_NAME'."

psql -U evadb < database/database.sql

echo "Database initialized, running migrations from $MY_FILES..."

for f in $MY_FILES
do
 echo "Processing $f" # always double quote "$f" filename
 # do something on $f
 psql -U $POSTGRES_USER -d $DATABASE_NAME < $f
done