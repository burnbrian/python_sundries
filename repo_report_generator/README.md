# Repository Report Generator

This Python script interacts with the GitHub API to retrieve information about specified repositories and generates Markdown reports based on a provided template. Here's a breakdown:

  - Token Retrieval: The get_private_token function fetches the GitHub access token from the environment variables.
  - GitHub API Request: The get_github_repo_info function performs a GET request to the GitHub API, retrieving information about a specified repository using the provided access token.
  - Reading URLs from File: The read_urls_from_file function reads a list of GitHub repository URLs from a file (repos.txt). It then extracts the owner and repository name, fetches information from the GitHub API, and saves both JSON and Markdown reports for each repository.
  - Markdown Templating: The script utilizes the Jinja2 template engine to create Markdown reports. The template file (template.md) is rendered with repository information.

Note: This script requires the requests, codecs, jinja2, and python-dotenv libraries. Additionally, it relies on environment variables for the GitHub access token and uses a file (repos.txt) to input repository URLs.
