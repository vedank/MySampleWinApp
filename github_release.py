from datetime import datetime
import time
from github import Github

GITHUB_TOKEN = '318fdf050b663381890db398885baabd5cdcdbea'
user = 'vedank'

github = Github(GITHUB_TOKEN)

def github_create_tag_and_release(user, latest_tag):
  punchh_repo_url = "vedank/MySampleWinApp"
  gh_repo = github.get_repo(punchh_repo_url)
  head_ref = gh_repo.get_git_ref("heads/master")
  gh_repo.create_git_tag_and_release(
    tag = latest_tag,
    tag_message = "Deployed By %s" % user,
    release_name = latest_tag,
    release_message = "Deployed By %s" % user,
    object = head_ref.object.sha,
    type = 'commit'
  )

def tag_name():
  return "posdeploy-" + datetime.now().strftime("%Y%m%d_%H%M%S")

latest_tag = tag_name()
github_create_tag_and_release(user, latest_tag)
