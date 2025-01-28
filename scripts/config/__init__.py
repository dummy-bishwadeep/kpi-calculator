from dotenv import load_dotenv
load_dotenv()

import pathlib
from pydantic import Field
from pydantic_settings import BaseSettings
from scripts.config.app_configurations import PathToStorage, ServiceConfig




class _Service(BaseSettings):
    PROXY: str = Field(default="/hack-repl")
    BACKEND_DIR: str = Field(default=".")


class _BasePathConf(BaseSettings):
    BASE_PATH: str = Field(default=PathToStorage.BASE_PATH, env="BASE_MOUNT")


class _PathConf:
    BASE_PATH: pathlib.Path = pathlib.Path(_BasePathConf().BASE_PATH)


Service = _Service()
PathConf = _PathConf()
