import subprocess
import os, shutil, requests
# from pygit2 import Repository,UserPass
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def clone_repo(repo_url, local_path):
    subprocess.run(['git', 'clone', repo_url, local_path])
    logger.info("Done")

def create_new_branch(branch_name, repo_path):
    subprocess.run(['git','init',repo_path])
    subprocess.run(['git', 'checkout', '-b', branch_name])

def add_files_to_branch(file1, file2, repo_path, local_path):
    file1_path = local_path+file1
    file2_path = local_path+file2
    shutil.copy(file1_path, repo_path)
    shutil.copy(file2_path, repo_path)
    subprocess.run(['git','init',repo_path])
    subprocess.run(['git', 'add', file1])
    subprocess.run(['git', 'add', file2])
    subprocess.run(['git', 'status'])


def commit_and_push_changes(commit_message, branch_name, repo_path):
    subprocess.run(['git', 'commit', '-m', commit_message])
    #subprocess.run(['git', 'push', 'origin', branch_name, '-f'])
    command = f"git push origin {branch_name} -f > push_output.txt | type push_output.txt"    
    # completed_process = subprocess.run(command, capture_output=True, text=True)
    # command_output = completed_process.stdout
    # print("Output: ",command_output)
    # process = subprocess.Popen(command, stdout=subprocess.PIPE, text=True)
    # command_output = process.stdout.read()
    # print("Output: ",command_output)
    url_output = subprocess.run(command, shell=True)
    with open("push_output.txt") as f:
        file_data = f.read()
    
    # logger.info("output:")
    # logger.info(file_data)

def pr_request_inputs(file1, file2, repo_url, target_dir, branch_name, commit_message):
# Replace these variables with your repository URL, local path, branch name, and files to add
    repo_url = repo_url
    local_path = "C:\\Semicolons\\"
    repo_path = target_dir
    branch_name = branch_name
    commit_message = commit_message
    repo_base_url = "https://github.com/anbublackop/codePropeller/pull/new/"
    os.chdir(repo_path)
    clone_repo(repo_url, repo_path)
    create_new_branch(branch_name, repo_path)
    add_files_to_branch(file1, file2, repo_path, local_path)
    commit_and_push_changes(commit_message, branch_name, repo_path)

    return f"Successfully pushed to the github! \n Create a pull request for '{branch_name}' on GitHub by visiting: \n {repo_base_url + branch_name}"

# pr_request_inputs("file1.txt", "file2.txt", "git@github.com:anbublackop/codePropeller.git", "C:\\Semicolons\\git_repo", "pr_automation_2", "Added files file1.txt and file2.txt")