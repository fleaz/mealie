import json
from pathlib import Path

from mealie.core.root_logger import get_logger
from mealie.db.data_access_layer.access_model_factory import Database

CWD = Path(__file__).parent
logger = get_logger(__name__)


def get_default_foods():
    with open(CWD.joinpath("resources", "foods", "en-us.json"), "r") as f:
        foods = json.loads(f.read())
    return foods


def get_default_units():
    with open(CWD.joinpath("resources", "units", "en-us.json"), "r") as f:
        units = json.loads(f.read())
    return units


def default_recipe_unit_init(db: Database) -> None:
    for unit in get_default_units():
        try:
            db.ingredient_units.create(unit)
        except Exception as e:
            logger.error(e)

    for food in get_default_foods():
        try:
            db.ingredient_foods.create(food)
        except Exception as e:
            logger.error(e)
