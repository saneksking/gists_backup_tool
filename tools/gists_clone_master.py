# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
import os
import shutil


class GistsCloneMaster:
    choice = ''

    @classmethod
    def clone_gist(cls, gists=None, auto=False):
        if gists is None:
            gists = []

        home_directory = os.path.expanduser('~')
        clone_path = os.path.join(home_directory, 'github_gists')
        num_of_gist = len(gists)
        for n, repo in enumerate(gists, 1):
            gists_name = repo['id']
            gist_ssh_url = repo['git_pull_url']
            gist_path = os.path.join(clone_path, gists_name)
            if auto:
                pass
            else:
                cls.choice = input(f'Download gist {gists_name}? (y/n): ')
            if cls.choice == 'y' or auto:
                if os.path.exists(gist_path):
                    shutil.rmtree(gist_path)

                os.makedirs(gist_path, exist_ok=True)
                os.system(f'git clone {gist_ssh_url} {gist_path}')
                print('-' * 30)
                msg = f'{n}/{num_of_gist}. Cloned {gists_name} successfully! [ok]'
                length = len(msg)
                print('-' * length)
                print(msg)
                print('-' * length)
            elif cls.choice == 'n':
                continue
