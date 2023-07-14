from sqlalchemy import create_engine, inspect

def print_relationships(database_uri):
    engine = create_engine(database_uri)
    inspector = inspect(engine)

    table_names = inspector.get_table_names()

    for table_name in table_names:
        relationships = inspector.get_foreign_keys(table_name)
        print(f"Table: {table_name}")
        for relationship in relationships:
            print(f"Foreign Key: {relationship['constrained_columns']} "
                  f"References: {relationship['referred_table']}({relationship['referred_columns']})")
        print("---------------------------")

if __name__ == '__main__':
    database_uri = 'sqlite:///instance/dev.db'  # Replace with your database URI
    print_relationships(database_uri)
