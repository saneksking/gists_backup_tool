# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
import os
from dotenv import load_dotenv
from tools.github_api_man import GitHubAPI
from tools.gists_clone_master import GistsCloneMaster


def main():
    load_dotenv()
    token = os.getenv("GITHUB_API_TOKEN")
    name = os.getenv("GITHUB_NAME")
    print('Please wait...')
    github_api_manager = GitHubAPI(
        name=name,
        token=token
    )
    gists = github_api_manager.get_gists_names()
    print(f'Name: {github_api_manager.name} | Repositories: {len(gists)}')
    clone_master = GistsCloneMaster()
    clone_master.clone_gist(gists=gists)


if __name__ == '__main__':
    main()
