# Private GitHub setup notes

The ChatGPT GitHub connector available in this session can work with existing repositories, but it does not expose a create-new-private-repository action.

To publish this as a private GitHub repo:

1. Create a new private GitHub repository named:
   `chosen-company-ai-card-interaction-case-study`
2. Do not initialise it with a README, licence, or .gitignore if uploading this repo folder directly.
3. From your local machine, unzip this archive and run:

```bash
cd chosen-company-ai-card-interaction-case-study
git remote add origin git@github.com:ldandy/chosen-company-ai-card-interaction-case-study.git
git branch -M main
git push -u origin main
```

If using HTTPS instead of SSH:

```bash
git remote add origin https://github.com/ldandy/chosen-company-ai-card-interaction-case-study.git
git branch -M main
git push -u origin main
```

After pushing, keep the repo private and share the link only with people who message you.
