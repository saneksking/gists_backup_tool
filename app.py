# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
import argparse
import os
from dotenv import load_dotenv

from tools.app_manager import AppManager
from tools.github_api_man import GitHubAPI


def main():
    app_manager = AppManager()

    load_dotenv()
    token = os.getenv("GITHUB_API_TOKEN")
    name = os.getenv("GITHUB_NAME")

    parser = argparse.ArgumentParser(description=app_manager.config.name)
    parser.add_argument('-a', action='store_true', help='Auto', default=False)
    args = parser.parse_args()
    auto = args.a

    app_manager.smart_printer.show_head(text='Gists Backup Tool')

    print('Please wait...')

    github_api_manager = GitHubAPI(
        name=name,
        token=token
    )

    gists = github_api_manager.get_gists_names()
    print(f'Name: {github_api_manager.name} | Gists: {len(gists)}')

    if auto:
        app_manager.gists_clone_master.clone_gist(gists=gists, auto=True)
    elif not auto:
        app_manager.gists_clone_master.clone_gist(gists=gists)

    app_manager.smart_printer.show_footer(url=app_manager.config.url, copyright_=app_manager.config.copyright_)


if __name__ == '__main__':
    main()
