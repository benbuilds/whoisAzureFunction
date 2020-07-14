import logging
import whois
import datetime

import azure.functions as func

def getDomainInfo(name):
    print('Collecting whois info...')
    w = whois.whois(name)
    w.expiration_date  # dates converted to datetime object
    datetime.datetime(2013, 6, 26, 0, 0)
    w.text  # the content downloaded from whois server
    return w

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        w = getDomainInfo(name)
        return func.HttpResponse(f"Query triggered successfully. Update for {name}...{w.text}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a domainName in the query string or in the request body for a personalized response.",
             status_code=200
        )
