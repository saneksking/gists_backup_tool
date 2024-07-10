import os
import shutil


class GistsCloneMaster:

    @classmethod
    def clone_gist(cls, gists=None):
        if gists is None:
            gists = []

        home_directory = os.path.expanduser('~')
        clone_path = os.path.join(home_directory, 'github_gists')
        num_of_gist = len(gists)
        for n, repo in enumerate(gists, 1):
            gists_name = repo['id']
            gist_ssh_url = repo['git_pull_url']
            gist_path = os.path.join(clone_path, gists_name)

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
