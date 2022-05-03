from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates/")


@app.get("/")
def read_root(request: Request):
    urls = ['https://google.co.in', 'https://stackoverflow.com']
    response_list = list()
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            status = 'Up'
        else:
            status = response.status_code
        response = requests.post(url)
        time_taken = response.elapsed.total_seconds()
        response_dict = {'URL': url, 'StatusCode': response.status_code, 'Status': status, 'ETA': time_taken}
        response_list.append(response_dict)
    return templates.TemplateResponse('index.html', context={'request': request, 'result': response_list})
