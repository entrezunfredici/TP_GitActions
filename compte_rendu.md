# Compte Rendu TP GitHub actions

Etape 1 création du fichier [.github/workflows/github-actions-demo.yml](https://github.com/entrezunfredici/TP_GitActions/commit/77fe5818eaf456cdc6d27fd68ebd49121998493d#diff-9d37a6e95879cee8b9d03b296b3b32a3571b3846ada7430ff07df53d88a1e9e2 ".github/workflows/github-actions-demo.yml")

création, du dossiver .github/workflow avec la commande mkdir .github/workflow

```
name: GitHub Actions Demo
run-name: ${{ github.actor }} is testing out GitHub Actions 🚀
on: [push]
jobs:
  Explore-GitHub-Actions:
    runs-on: ubuntu-latest
    steps:
      - run: echo "🎉 The job was automatically triggered by a ${{ github.event_name }} event."
      - run: echo "🐧 This job is now running on a ${{ runner.os }} server hosted by GitHub!"
      - run: echo "🔎 The name of your branch is ${{ github.ref }} and your repository is ${{ github.repository }}."
      - name: Check out repository code
        uses: actions/checkout@v4
      - run: echo "💡 The ${{ github.repository }} repository has been cloned to the runner."
      - run: echo "🖥️ The workflow is now ready to test your code on the runner."
      - name: List files in the repository
        run: |
          ls ${{ github.workspace }}
      - run: echo "🍏 This job's status is ${{ job.status }}."
```

Etape 2 création du fichier [SimpleMath.py](https://github.com/entrezunfredici/TP_GitActions/commit/56a3abd9b3378c6cc786318443344146c7953c50#diff-71ade97337ef5a4622ada8feb0cb9ff1b1cc8a009c14a5d5f0aeb46193d9a838 "SimpleMath.py")

```
import math

class SimpleMath:
    print("=======================================")
    print("Welcome in SimpleMath class")
    a=int(input("entrez a ⇒ "))
    b=int(input("entrez b ⇒ "))
    def add(a, b):
        return a+b

    print(add(a, b))
    print("=======================================")
```
