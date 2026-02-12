# OpenCLAW Installation Tips

This document provides tips and methods for installing OpenCLAW in various environments.

## Installation Methods for Hugging Face Spaces

### Method 1: Using Tarball URL
```
https://github.com/TigerResearch/OpenCLAW/archive/refs/heads/master.tar.gz
```

**Pros:**
- Direct installation from GitHub archive
- No git dependency required
- Fast download

**Cons:**
- Requires specific branch name in URL
- URL may become outdated if default branch changes

### Method 2: Using git+ Protocol (Recommended)
```
git+https://github.com/TigerResearch/OpenCLAW.git@master
```

**Pros:**
- More flexible version control
- Easier to specify branches, tags, or commits
- Standard pip format

**Cons:**
- Requires git to be available during installation

### Method 3: Specific Branch or Tag
```
git+https://github.com/TigerResearch/OpenCLAW.git@v1.0.0
git+https://github.com/TigerResearch/OpenCLAW.git@main
```

**Use Cases:**
- Production deployments requiring stable versions
- Testing specific release versions
- Ensuring consistency across environments

### Method 4: Private Repository (with token)
```
git+https://${GITHUB_TOKEN}@github.com/TigerResearch/OpenCLAW.git@master
```

**Requirements:**
- GitHub personal access token
- Token configured as environment variable or secret
- Appropriate repository permissions

**Setup Steps:**
1. Create a GitHub personal access token with repo access
2. Configure token in your deployment environment
3. Use the token in the installation URL

## Local Testing

Before deploying to production, test the installation locally:

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
```

## Important Notes

⚠️ **Repository Verification:**
- Ensure the repository URL exists and is accessible
- Check that the repository has a valid `setup.py` or `pyproject.toml` file
- Verify the package name matches what you'll import in your code

⚠️ **Branch Names:**
- Use `main` instead of `master` for newer repositories
- Check the repository's default branch before installation

⚠️ **Installation Package Name:**
- The installed package name may differ from the repository name
- Check the repository's `setup.py` to confirm the actual package name
