import logging
import os

from azure.data.tables import TableClient
from azure.data.tables import UpdateMode

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    ##Grab the entity the table
    connection_string = os.getenv("AzureWebJobsVisitorCounter")
    with TableClient.from_connection_string(connection_string, table_name="VisitorCounter") as table:
        count_entity = table.get_entity('0', '0')
        count_entity = updatecount(count_entity)
        table.update_entity(mode=UpdateMode.REPLACE, entity=count_entity)
    ##Return the Count
    return func.HttpResponse(f"{count_entity['Counter']}")

def updatecount(count_entity):
    count_entity['Counter'] += 3
    return count_entity
