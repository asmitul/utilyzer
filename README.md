# 🎈 Python Package Template

A modern Python package template with comprehensive tooling and CI/CD setup.

## ✨ Features

- 📦 Package configuration with `pyproject.toml` built with `hatch`
- 🎨 Code formatting and linting with `ruff` and `black`
- 🐳 Ready-to-use `Dockerfile` with package installation
- 🔄 Git hooks with `pre-commit` configuration
- 💻 GitHub Codespaces support via `.devcontainer`
- 🚀 CI/CD Pipelines with GitHub Actions
- 🧪 Basic `pytest` setup for unit tests
- 📚 Auto-generated docs with `mkdocs` and `mkdocs-material`

## 🚀 Getting Started

### 1. Required Replacements

Replace the following placeholders in the codebase:

| Placeholder | Description | Example |
|------------|-------------|----------|
| `REPLACE_PACKAGE_NAME` | Package name (usually repository name) | `awesome_project` |
| `REPLACE_REPO_NAME` | GitHub repository name | `awesome-project` |
| `REPLACE_PACKAGE_DESCRIPTION` | Brief package description | `A tool for awesome things` |
| `REPLACE_FULL_NAME` | Your full name | `John Doe` |
| `REPLACE_EMAIL` | Your email address | `john@example.com` |
| `REPLACE_GITHUB_USERNAME` | Your GitHub username | `johndoe` |

### 2. GitHub Configuration

#### 2.1 PyPI Token Setup

Add your `PYPI_TOKEN` to repository secrets for package publishing.

#### 2.2 GitHub Actions Permissions

Enable write permissions for GITHUB_TOKEN:

1. Navigate to `Settings` > `Actions` > `General` in your repository
2. Under `Workflow permissions`, select `Read and write permissions`
3. Click `Save` to apply changes

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
