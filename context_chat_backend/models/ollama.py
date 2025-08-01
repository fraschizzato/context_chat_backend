#
# SPDX-FileCopyrightText: 2024 Nextcloud GmbH and Nextcloud contributors
# SPDX-License-Identifier: AGPL-3.0-or-later
#
import logging

from langchain_community.llms.ollama import Ollama

logger = logging.getLogger('ccb.models')


def get_model_for(model_type: str, model_config: dict):
    if model_type == 'llm':
        base_url = model_config.pop('base_url', None)
        if base_url is None:
            protocol = model_config.pop('protocol', 'http')
            host = model_config.pop('host', 'localhost')
            port = model_config.pop('port', 11434)
            base_url = f'{protocol}://{host}:{port}'
        logger.info(f'Loading ollama model from {base_url}')
        return Ollama(base_url=base_url, **model_config)
    return None
