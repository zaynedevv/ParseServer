

import requests

def populateFile(templatePath, data, outputName):

    json = {
    "outputName": outputName,
    "templateName": templatePath,
    "data": data,
    "outputFormat": "pdf;docx",
    "accessKey": "YzFiMmI0ZDQtMzIxYS00YTBiLWJlNjYtMDdkM2I4YjU4ODc3OjY0NjI1OTY3ODE"
    }

    headers = {'content-type': 'application/json'}

    response = requests.post('https://au1.dws4.docmosis.com/api/render', headers = headers, json=json)
    if response.status_code != 200:
        print(response.content)
    return response.content


