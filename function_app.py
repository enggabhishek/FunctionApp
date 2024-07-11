import azure.functions as func
import logging
import requests
import os
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_example")
def http_example(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    name = req.params.get('name')
    token = os.environ.get("Airflow_Token")
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