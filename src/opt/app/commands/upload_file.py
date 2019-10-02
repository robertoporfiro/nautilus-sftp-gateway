from loguru import logger

import command
import config
from helpers import is_tmp


def upload_file(file_path):
    buckets = config.APP_GCS_BUCKETS.split(",")
    for bucket in buckets:
        upload_command = [
            "/usr/bin/gsutil",
            "mv",
            file_path,
            "gs://{}".format(bucket),
        ]
        if not is_tmp(file_path):
            command.run(upload_command, quiet=True)
        else:
            logger.info("Skipping temp file - {}", {"path": file_path})
