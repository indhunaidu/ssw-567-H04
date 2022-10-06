import requests

def countCommits(user, repoName):
    commitRequest = requests.get(f'https://api.github.com/repos/{user}/{repoName}/commits').json()
    counter = 0
    for commit in commitRequest:
        counter += 1
    return counter

def getRepoNames(user):
    repoRequest = requests.get(f'https://api.github.com/users/{user}/repos').json()
    names = []
    for repo in repoRequest:
        for header in repo:
            if header == 'name':
                names.append(repo[header])
    return names

def displayRepos(user):
    repoNames = getRepoNames(user)
    print(repoNames)
    for name in repoNames:
        commits = countCommits(user, name)
        print(f'Repo: {name}, Number of commits: {commits}')

if __name__ == '__main__':
    print(getRepoNames('indhunaidu'))