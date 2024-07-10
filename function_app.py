import azure.functions as func
import logging
import requests
import os

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="HTTPExample")
def HTTPExample(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    name = req.params.get('name')
    token = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImNsb2Q0aGtqejAya3AwMWozdWNqbzJwOHIiLCJ0eXAiOiJKV1QifQ.eyJhcGlUb2tlbklkIjoiY2x4eXphNDN5MGttMTAxbnd2b2RseXF6eSIsImF1ZCI6ImFzdHJvbm9tZXItZWUiLCJpYXQiOjE3MTk1OTYzNzEsImlzQXN0cm9ub21lckdlbmVyYXRlZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6Ly9hcGkuYXN0cm9ub21lci5pbyIsImtpZCI6ImNsb2Q0aGtqejAya3AwMWozdWNqbzJwOHIiLCJwZXJtaXNzaW9ucyI6WyJhcGlUb2tlbklkOmNseHl6YTQzeTBrbTEwMW53dm9kbHlxenkiLCJkZXBsb3ltZW50SWQ6Y2x4eXcxMmZ4MGswbjAxbmNtenRrYXJscSIsIm9yZ2FuaXphdGlvbklkOmNseHl2cGpxcTBqeWowMW5jZzk1YmN6MTYiLCJvcmdTaG9ydE5hbWU6Y2x4eXZwanFxMGp5ajAxbmNnOTViY3oxNiIsIndvcmtzcGFjZUlkOmNseHl2cGxscDBqeXEwMW5jZWhoZXcybjAiXSwic2NvcGUiOiJhcGlUb2tlbklkOmNseHl6YTQzeTBrbTEwMW53dm9kbHlxenkgZGVwbG95bWVudElkOmNseHl3MTJmeDBrMG4wMW5jbXp0a2FybHEgb3JnYW5pemF0aW9uSWQ6Y2x4eXZwanFxMGp5ajAxbmNnOTViY3oxNiBvcmdTaG9ydE5hbWU6Y2x4eXZwanFxMGp5ajAxbmNnOTViY3oxNiIsInN1YiI6ImNseHl2bzg5dTBqeTcwMW5jOGV4MDZkdWMiLCJ2ZXJzaW9uIjoiY2x4eXphNDN5MGttMDAxbnc1Ym5xZHoxbyJ9.Ak1P0YQLg9dLki0k149His66MrjNC8QMG_WopMrV-9Gv6J-kOxebR7GWO1gZL3Hd80q8Zw9fA1jYbBJelS993FUNED5EZ_wvDXudTzTFsNVQRJZV54biuFForFV8J7xrwS4WWiCyvHLATH11BydUdsIbiSr3OI9eNH4RjbuqzRP7iNg5MgC9wbNeiKHrRZtmDyjgBhMqN6gPXMpcDDdAS_x6__COyi52rOEiW72iWr7pSKuysU8_3VNl8ZkTwbsB1B5mbZ3mls6N5O1-gwbg1Vchf1MpB3U0RkCsSzOyzYZTRGWNtrqaiDZyaB5ghsj1z9fYQ_VqJJS1KqIO6zLuLw"
    deployment_url = "https://clxyvpjqq0jyj01ncg95bcz16.astronomer.run/dztkarlq"
    dag_id = "virtual_operator"
    
    response = requests.post(
                url=f"{deployment_url}/api/v1/dags/{dag_id}/dagRuns",
                headers={"Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        },
        data='{}'
    )
    # logging.info(f"Python EventGrid triggered DAG pipelin: {response.json()}")
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             f"This HTTP triggered function executed successfully. Python EventGrid triggered DAG pipelin: {response.json()}",
             status_code=200
        )