from pathlib import Path

from services.constants import PATH_TO_YAML
from ruamel.yaml import YAML

YAML_DICT = YAML(typ='rt').load(Path(PATH_TO_YAML))
