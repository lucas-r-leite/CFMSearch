import requests
import os
from dotenv import load_dotenv

load_dotenv()


def getListaMedicos(page=1):
    url = "https://portal.cfm.org.br/api_rest_php/api/v1/medicos/buscar_medicos"

    payload = [
        {
            "useCaptchav2": True,
            "captcha": os.getenv("CAPTCHA"),
            "medico": {
                "nome": "",
                "ufMedico": "PB",
                "crmMedico": "",
                "municipioMedico": "4964",
                "tipoInscricaoMedico": "",
                "situacaoMedico": "A",
                "detalheSituacaoMedico": "",
                "especialidadeMedico": "",
                "areaAtuacaoMedico": "",
            },
            "page": page,
            "pageNumber": page,
            "pageSize": 10,
        }
    ]
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Connection": "keep-alive",
        "Referer": "https://portal.cfm.org.br/busca-medicos/",
        "Cookie": "__utmpk=0",
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    # print(response.text)
    return response


def getDoctorInfos(crm, hash):
    url = "https://portal.cfm.org.br/api_rest_php/api/v1/medicos/buscar_foto"

    payload = [{"securityHash": hash, "crm": crm, "uf": "PB"}]
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US",
        "Accept-Encoding": "gzip, deflate, br",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://portal.cfm.org.br",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": "https://portal.cfm.org.br/busca-medicos/",
        "Cookie": "__utmpk=0",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    return response
