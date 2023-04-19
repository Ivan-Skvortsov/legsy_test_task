import requests
import logging

from pydantic import ValidationError
from src.api.schemas.request_models import CreateOrUpdateProductRequest
from src.api.exceptions import ParsingError

PRODUCT_DETAIL_URL = (
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
        msg = f"Error accessing wildberries.ru: {err}"
        logging.exception(msg)
        raise ParsingError(msg)
    return response


def __parse_product_data(response: requests.Response) -> dict:
    try:
        response_data = response.json()
        product_data = response_data["dta"]["products"][0]
    except requests.RequestException as err:
        msg = f"Error decoding response from wildberries.ru: {err}"
        logging.exception(msg)
        raise ParsingError(msg)
    except KeyError as err:
        msg = (
            "Invalid response recieved from wildberries.ru. "
            "Check response structure."
        )
        logging.exception(f"{msg}: {err}")
        raise ParsingError(msg)
    except IndexError:
        raise ParsingError(
            "Product with given item number was not found on wildberries.ru."
        )
    product_data["quantity"] = __extract_quantity(product_data)
    return product_data


def __extract_quantity(product_data: dict) -> int:
    quantity = 0
    try:
        for size in product_data["sizes"]:
            for stock in size["stocks"]:
                quantity += stock["qty"]
    except KeyError as err:
        msg = (
            "Error when trying to retrieve product quantity. "
            "Check response structure from wilderries.ru."
        )
        logging.exception(f"{msg}: {err}")
        raise ParsingError(msg)
    return quantity


def get_product_data(nm_id: int) -> CreateOrUpdateProductRequest:
    response = __request_product_data(PRODUCT_DETAIL_URL.format(nm_id=nm_id))
    parsed_data = __parse_product_data(response)
    try:
        validated_data = CreateOrUpdateProductRequest(**parsed_data)
    except ValidationError as err:
        msg = (
            "Invalid data recieved from wilderries.ru. "
            "Check response structure."
        )
        logging.exception(f"{msg}: {err}")
        raise ParsingError(msg)
    return validated_data
