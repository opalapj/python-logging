import logging
import logging.config
import pathlib
import tomllib

import firstpackage
import firstpackage.module
import secondpackage
import secondpackage.module
import yaml


logger = logging.getLogger(__name__)


def do_basic_config():
    logging.basicConfig()


def do_dict_config_using_toml():
    with pathlib.Path("data/config.toml").open("rb") as file:
        content = tomllib.load(file)
    logging.config.dictConfig(config=content)
    return content


def do_basic_config_using_toml():
    with pathlib.Path("data/basic_config.toml").open("rb") as file:
        content = tomllib.load(file)
    logging.config.dictConfig(config=content)
    return content


def do_dict_config_using_yaml():
    with pathlib.Path("data/config.yaml").open("rb") as file:
        content = yaml.safe_load(file)
    logging.config.dictConfig(config=content)
    return content


def do_basic_config_using_yaml():
    with pathlib.Path("data/basic_config.yaml").open("rb") as file:
        content = yaml.safe_load(file)
    logging.config.dictConfig(config=content)
    return content


def function():
    hh = logger.hasHandlers()
    hs = logger.handlers
    logger.debug(f"debug from {__name__}, {hh}, {hs}")
    logger.info(f"info from {__name__}, {hh}, {hs}")
    logger.warning(f"warning from {__name__}, {hh}, {hs}")
    logger.error(f"error from {__name__}, {hh}, {hs}")
    logger.critical(f"critical from {__name__}, {hh}, {hs}")


def main():
    # Built-in basicConfig.
    # do_basic_config()

    # Basic config using config dicts.
    config_toml = do_basic_config_using_toml()
    config_yaml = do_basic_config_using_yaml()
    assert config_toml == config_yaml, "Different dicts!"

    # Custom config using config dicts.
    # config_toml = do_dict_config_using_toml()
    # config_yaml = do_dict_config_using_yaml()
    # assert config_toml == config_yaml, "Different dicts!"

    # Tests.
    function()
    firstpackage.function()
    firstpackage.module.function()
    secondpackage.function()
    secondpackage.module.function()


if __name__ == "__main__":
    main()
