# OpenCLAW Troubleshooting Tips

This document provides solutions to common issues when installing and using OpenCLAW.

## Installation Issues

### Issue: Installation Failed

**Symptoms:**
- Pip fails to install OpenCLAW
- Error messages during build process
- Dependencies cannot be resolved

**Solutions:**

1. **Verify Repository URL**
   ```bash
   # Test if repository is accessible
   curl -I https://github.com/TigerResearch/OpenCLAW
   ```
   - Ensure the repository exists
   - Check if it's public or private
   - Verify you have access permissions

2. **Check Branch Name**
   - Use `main` instead of `master` for newer repositories
   - List available branches on GitHub
   - Use correct branch in installation URL

3. **Private Repository Access**
   - Verify GitHub token has correct permissions
   - Check token hasn't expired
   - Ensure token is properly configured:
     ```txt
     git+https://${GITHUB_TOKEN}@github.com/TigerResearch/OpenCLAW.git@master
     ```

4. **Verify Package Structure**
   - Repository must have `setup.py` or `pyproject.toml`
   - Check package metadata is correct
   - Review installation instructions in repository README

### Issue: Module Not Found

**Symptoms:**
- `ImportError: No module named 'openclaw'`
- Package installed but cannot be imported

**Solutions:**

1. **Check Installed Package Name**
   ```python
   import pkg_resources
   installed_packages = [d.project_name for d in pkg_resources.working_set]
   print([p for p in installed_packages if 'claw' in p.lower()])
   ```

2. **Verify Import Name**
   - Package name ≠ Import name
   - Check repository's `setup.py` for actual module name
   - Review repository documentation

3. **Check Installation Success**
   ```bash
   pip list | grep -i claw
   ```

4. **Reinstall Package**
   ```bash
   pip uninstall openclaw
   pip install git+https://github.com/TigerResearch/OpenCLAW.git@master
   ```

### Issue: Dependency Conflicts

**Symptoms:**
- Version conflicts during installation
- Package installation succeeds but app fails to run
- Incompatible dependency versions

**Solutions:**

1. **Specify Compatible Versions**
   ```txt
   # In requirements.txt
   gradio==3.50.2
   numpy>=1.20.0,<2.0.0
   ```

2. **Use Virtual Environment**
   ```bash
   python -m venv clean_env
   source clean_env/bin/activate
   pip install -r requirements.txt
   ```

3. **Check Dependency Tree**
   ```bash
   pip install pipdeptree
   pipdeptree -p openclaw
   ```

4. **Update pip and setuptools**
   ```bash
   pip install --upgrade pip setuptools wheel
   ```

## Hugging Face Spaces Issues

### Issue: Build Error

**Symptoms:**
- Space shows "Build error" status
- Build process fails or times out
- Space stuck in building state

**Solutions:**

1. **Check Build Logs**
   - Navigate to "Logs" tab
   - Look for specific error messages
   - Identify failing step

2. **Common Build Issues:**
   
   **Timeout:**
   ```txt
   # Reduce dependencies or split builds
   # Use lighter-weight alternatives
   ```
   
   **Out of Memory:**
   - Upgrade to higher hardware tier
   - Reduce concurrent installations
   
   **Network Issues:**
   - Retry build
   - Check if GitHub is accessible
   - Verify URL format

3. **Verify requirements.txt Format**
   ```txt
   # Correct format
   git+https://github.com/TigerResearch/OpenCLAW.git@master
   gradio>=3.50.0
   
   # NOT like this (invalid)
   OpenCLAW  # Won't work if not on PyPI
   ```

### Issue: Runtime Error

**Symptoms:**
- Build succeeds but app doesn't start
- Application crashes on launch
- "Application error" message

**Solutions:**

1. **Check Runtime Logs**
   ```python
   # Add debugging in app.py
   import sys
   print(f"Python: {sys.version}")
   print(f"Path: {sys.path}")
   ```

2. **Test Import Statements**
   ```python
   try:
       import openclaw
       print("OpenCLAW imported successfully")
   except ImportError as e:
       print(f"Failed to import: {e}")
   ```

3. **Verify Gradio Configuration**
   ```python
   # Ensure proper launch configuration
   if __name__ == "__main__":
       demo.launch()  # No server_name or server_port needed
   ```

4. **Check for Missing Dependencies**
   - Review complete error stack trace
   - Add missing packages to requirements.txt
   - Test locally before redeploying

### Issue: Space Timeout/Sleeping

**Symptoms:**
- Space shows "Sleeping" status
- Application not responding
- "Space is building" but never completes

**Solutions:**

1. **Understand Space Lifecycle**
   - Free Spaces sleep after inactivity
   - Accessing URL wakes up Space
   - May take 1-2 minutes to wake

2. **Keep Space Alive**
   - Upgrade to persistent hardware
   - Use paid tier for 24/7 availability

3. **Handle Cold Starts**
   ```python
   # Add loading indicator in app
   gr.Markdown("Loading... Please wait")
   ```

## Development Issues

### Issue: Local Testing Fails

**Symptoms:**
- Works on Hugging Face but not locally
- Different behavior between environments

**Solutions:**

1. **Match Python Versions**
   ```bash
   # Check Python version
   python --version
   # Hugging Face uses Python 3.10+
   ```

2. **Use Same Dependencies**
   ```bash
   pip freeze > current_env.txt
   # Compare with requirements.txt
   ```

3. **Check Environment Variables**
   ```python
   import os
   print(os.environ.get('GITHUB_TOKEN'))
   ```

### Issue: Authentication Errors

**Symptoms:**
- "Authentication failed" for private repository
- Token not working
- Permission denied

**Solutions:**

1. **Verify Token Permissions**
   - Token needs `repo` scope for private repos
   - Check token hasn't expired
   - Regenerate if necessary

2. **Check Token Configuration**
   - Hugging Face: Add in Space Settings → Secrets
   - Local: Set environment variable:
     ```bash
     export GITHUB_TOKEN="your_token_here"
     ```

3. **Test Token**
   ```bash
   curl -H "Authorization: token YOUR_TOKEN" \
        https://api.github.com/repos/TigerResearch/OpenCLAW
   ```

## Getting Help

If issues persist:

1. **Check Repository Issues**: Look for similar problems
2. **Hugging Face Forum**: https://discuss.huggingface.co/
3. **GitHub Issues**: Report bugs to repository
4. **Review Documentation**: Check for updates or changes

## Debugging Checklist

- [ ] Repository URL is correct and accessible
- [ ] Branch/tag name is correct
- [ ] Package has valid setup.py or pyproject.toml
- [ ] All dependencies are listed in requirements.txt
- [ ] Python version is compatible
- [ ] Authentication is configured (for private repos)
- [ ] Import name matches installed package name
- [ ] Logs have been reviewed for specific errors
- [ ] Local testing completed successfully
