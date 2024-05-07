import requests
def getListaMedicos(page = 1):
    url = "https://portal.cfm.org.br/api_rest_php/api/v1/medicos/buscar_medicos"

    payload = [
        {
            "useCaptchav2": True,
            "captcha": "03AFcWeA5iqADGa_MK2IAysNo931TsGmxrsSA3TH_Vx-7YgNqbu9dPQSxR7bdhY_59NW18bSfr0WHOnwPQSf0rx0nW0iBVugKZGcLq3gXijVZcMwX9ZwFuIuAonVRMSpcwIri3Sd0uqZ8jjI-WVd9L-KG7Edz1ermt01ipMO_l8fsOF6l_H0j8xyasK84Idy_tknq7BQZ-So8JDy4Gn4BMMPIpvz6Izqlc0Mx8fGv74wP5qh_yE61H9sLXh154dqCovs3Pk2zxfkFlrrnYiU7jWKoDRpLwIEHgLg1gMlwZw3UJAvNb4ng_JQ6PWnem2iGgEVmLAuUhfC9a1OMYdNYbS2ilXwzO2Aw23oMHTxp88BHw5Wdj8gadJmUd0RPnXPmDfNlni5qmVfTD5G5XQEf_XpmEvf5nTiJyWebA5ih8D6SXbomMSUbulqTaMTllobNI7uvq1vXo5bg7gr2lA74UnE-YcTuleiCRBn95RTf-nekofdmKkQFaEG9VJAfPJ-Fq6IYSqX_PQNw_h-QIXTQUop5Z7_z2hR3T_w0eZkODfca9rvnnCm7WR9J1puHm2rJwlD0Gp2qNCLB1SgAQR5n3Y7me7ylPmTxGfx3tsPgQZA9gt7bgUefBfz17QoXNVYZ9RasMS_aVymG7RCryltbF8PoeS3t3bei5WmP1lfdaohEu0ZILU5InIJyXsjHVnIo_74adVFBqGVaIFMx49jYyVhUgfv6VABYzkQ",
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

    #print(response.text)
    return response

def getDoctorInfos(crm, hash):
    url = "https://portal.cfm.org.br/api_rest_php/api/v1/medicos/buscar_foto"

    payload = [
        {
            "securityHash": "7f8f562649260bdf57d1e17dda6d8259",
            "crm": "4184",
            "uf": "PB"
        }
    ]
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
        "Sec-Fetch-Site": "same-origin"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)