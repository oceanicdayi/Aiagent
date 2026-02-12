# OpenCLAW Deployment Tips for Hugging Face Spaces

This document provides tips for deploying applications that use OpenCLAW to Hugging Face Spaces.

## Deployment Methods

### Method 1: Web Interface Deployment

**Steps:**
1. Visit https://huggingface.co/spaces
2. Click "New Space" button
3. Configure your Space:
   - **Owner**: Your username or organization
   - **Space name**: e.g., openclaw-demo
   - **License**: apache-2.0 or mit recommended
   - **SDK**: Select "Gradio"
   - **Hardware**: "CPU basic" (free) or as needed
   - **Visibility**: Public or Private

4. Upload files:
   - `app.py` - Your Gradio application
   - `requirements.txt` - Including OpenCLAW dependency
   - `README.md` - Documentation (optional)

5. Wait for automatic build

**Advantages:**
- User-friendly interface
- No command-line knowledge required
- Quick for small projects

### Method 2: Git Push Deployment

**Steps:**
1. Clone your Space repository:
   ```bash
   git clone https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
   cd YOUR_SPACE_NAME
   ```

2. Configure Git LFS (if needed):
   ```bash
   git lfs install
   ```

3. Copy project files:
   ```bash
   cp /path/to/Aiagent/app.py .
   cp /path/to/Aiagent/requirements.txt .
   cp /path/to/Aiagent/README.md .
   ```

4. Commit and push:
   ```bash
   git add .
   git commit -m "Initial deployment"
   git push
   ```

**Advantages:**
- Better for version control
- Easier batch updates
- Supports large files via Git LFS

## Configuration Tips

### Requirements.txt Best Practices

1. **Use Specific Versions for Stability:**
   ```txt
   gradio==3.50.2  # Instead of gradio>=3.50.0
   ```

2. **Order Dependencies Logically:**
   ```txt
   # Core packages first
   git+https://github.com/TigerResearch/OpenCLAW.git@master
   
   # Framework packages
   gradio>=3.50.0
   
   # Utility packages
   # (other dependencies)
   ```

3. **Comment for Clarity:**
   ```txt
   # OpenCLAW package from GitHub
   git+https://github.com/TigerResearch/OpenCLAW.git@master
   
   # UI Framework
   gradio>=3.50.0
   ```

### Private Repository Setup

For private repositories:

1. Navigate to Space Settings
2. Add `GITHUB_TOKEN` in "Repository secrets" section
3. Update requirements.txt:
   ```txt
   git+https://${GITHUB_TOKEN}@github.com/TigerResearch/OpenCLAW.git@master
   ```

## Deployment Verification

After deployment:

1. **Check Space Status**: Should show "Running"
2. **Access Application**: Visit your Space URL
3. **Review Logs**: Check "Logs" tab for errors
4. **Test Functionality**: 
   - Test all features
   - Verify OpenCLAW is properly installed
   - Check system info tab

## Update Deployment

### Via Web Interface:
1. Go to Space page
2. Click "Files" tab
3. Select file to update
4. Click "Edit"
5. Save (auto-rebuilds)

### Via Git:
```bash
cd YOUR_SPACE_NAME
# Make changes
git add .
git commit -m "Update description"
git push
```

## Performance Tips

1. **Choose Appropriate Hardware:**
   - CPU basic: Simple applications
   - CPU upgrade: More concurrent users
   - GPU: Heavy computation tasks

2. **Optimize Dependencies:**
   - Only include necessary packages
   - Use specific versions to avoid conflicts
   - Consider package size for faster builds

3. **Handle Timeouts:**
   - Free Spaces sleep after inactivity
   - Visiting URL wakes them up
   - Consider paid plans for 24/7 availability

## Monitoring and Maintenance

1. **Regular Log Checks**: Monitor for errors or warnings
2. **Dependency Updates**: Keep packages current but test first
3. **Documentation**: Maintain clear README with usage instructions
4. **Graceful Degradation**: Handle missing dependencies gracefully

## Related Resources

- [Hugging Face Spaces Documentation](https://huggingface.co/docs/hub/spaces)
- [Gradio Documentation](https://gradio.app/docs/)
- [Python pip Installation Guide](https://pip.pypa.io/en/stable/cli/pip_install/)
