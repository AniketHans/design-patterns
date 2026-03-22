### Running Migrations

1. we will use Alembic for migrations
   1. `pip install alembic`
2. Run `alembic init migartions`. This will create a migrations table
3. Configure the env.py file in migrations folder.
4. After configurations, create migrations by running the command
   1. `alembic revision --autogenerate -m "<message>"` , this will generate a migartion file.
5. After revewing the migrations in the migartion file, we have to apply the changes, for that we have to run the following command:
   1. `alembic upgrade head`
