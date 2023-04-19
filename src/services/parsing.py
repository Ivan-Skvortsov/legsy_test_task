import requests
import logging

from src.schemas.request_models.product import ProductRequest

CARD_DETAIL_URL = (
    "https://card.wb.ru/cards/detail"
    "?appType=1&curr=rub&dest=-1257786"
    "&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,48,110,31,22,71,114"  # noqa
    "&spp=0&nm={nm_id}"
)


def __request_product_data(url: str) -> requests.Response:
    try:
        response = requests.get(url)
        response.encoding = "utf-8"
    except requests.RequestException as err:
        logging.exception(f"Error requesting data: {err}")
        raise
    return response


def __parse_product_data(response: requests.Response) -> dict:
    try:
        response_data = response.json()
        product_data = response_data["data"]["products"][0]
    except requests.RequestException as err:
        logging.exception(f"Error decoding response: {err}")
        raise
    except (KeyError, IndexError) as err:
        logging.exception(f"Invalid response schema: {err}")
        raise
    product_data["quantity"] = __extract_quantity(product_data)
    return product_data


def __extract_quantity(product_data: dict) -> int:
    quantity = 0
    try:
        for size in product_data["sizes"]:
            for stock in size["stocks"]:
                quantity += stock["qty"]
    except KeyError as err:
        logging.exception(f"Error while trying to extract product quantity: {err}")
        raise
    return quantity


def get_product_data(nm_id: int) -> ProductRequest:
    response = __request_product_data(CARD_DETAIL_URL.format(nm_id=nm_id))
    parsed_data = __parse_product_data(response)
    return ProductRequest(**parsed_data)
