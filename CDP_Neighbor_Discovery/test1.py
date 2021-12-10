from pymongo import MongoClient

def run_query():
    """
    Mode Constructor.

    Metodo constructor.
    """
    with MongoClient("mongodb://localhost:27017/") as mongo_client:

        dblist = mongo_client.list_database_names()

        nameDatabase = "Devices"
        nameDatabaseCollection = "Devices"

        if nameDatabase not in dblist:
            # Connect to branchOffice Database.
            dbDevices = mongo_client[nameDatabase]
            # Connect to Branches Collection
            dbDevicesColl = dbDevices[nameDatabaseCollection]

        else:
            dbDevices = mongo_client[nameDatabase]
            dbDevicesColl = dbDevices[nameDatabaseCollection]

        # if len(arguments) == 0:
        #     result = dbDevicesColl.find(filter=query)
        # else:
        #    result = dbDevicesColl.find(
        #                            filter=query,
        #                            sort=arguments[0],
        #                            limit=arguments[1])

    # return result

def main():
    resultado = run_query()


if __name__ == "__main__":
    main()