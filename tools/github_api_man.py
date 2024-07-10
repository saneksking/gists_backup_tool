# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
import requests
import os
from dotenv import load_dotenv


load_dotenv()


class GitHubAPI:
    def __init__(self, name, token, url=f'https://api.github.com/users/{os.getenv('GITHUB_NAME')}/gists'):
        self._name = name
        self._token = token
        self._url = url

    @property
    def name(self):
        return self._name

    def _get_headers(self):
        return {'Authorization': f'token {f"{self._token}"}'}

    def get_gists_names(self):
        repos = []
        page = 1
        per_page = 100

        while True:
            params = {'page': page, 'per_page': per_page}
            response = requests.get(self._url, headers=self._get_headers(), params=params)
            page_gists = response.json()

            if not page_gists:
                break

            repos.extend(page_gists)
            page += 1
        return repos
