"""
Hugging Face Spaces App with OpenCLAW
This is a sample application demonstrating how to use OpenCLAW in Hugging Face Spaces.

This app serves as a template for deploying Python packages from GitHub 
in Hugging Face Spaces.
"""

import gradio as gr
import sys

def check_installation():
    """Check if OpenCLAW is installed and return system information."""
    info = []
    info.append(f"Python version: {sys.version}")
    info.append(f"Python executable: {sys.executable}")
    info.append("\nInstalled packages:")
    
    try:
        import pkg_resources
        installed_packages = [(d.project_name, d.version) for d in pkg_resources.working_set]
        installed_packages = sorted(installed_packages, key=lambda x: x[0].lower())
        
        # Look for OpenCLAW
        openclaw_found = False
        for name, version in installed_packages:
            if 'openclaw' in name.lower():
                info.append(f"✓ {name} ({version}) - INSTALLED")
                openclaw_found = True
        
        if not openclaw_found:
            info.append("⚠ OpenCLAW not found in installed packages")
            info.append("\nPlease verify:")
            info.append("1. The GitHub repository URL is correct")
            info.append("2. The repository has a valid setup.py or pyproject.toml")
            info.append("3. The package name matches what you're trying to import")
    except Exception as e:
        info.append(f"Error checking packages: {str(e)}")
    
    return "\n".join(info)

def greet(name):
    """Simple greeting function for demonstration."""
    if not name:
        name = "User"
    
    greeting = f"Hello {name}! 👋\n\n"
    greeting += "This Hugging Face Space demonstrates how to install Python packages from GitHub.\n\n"
    
    # Try to check if OpenCLAW or similar package is available
    try:
        # This is a placeholder - replace with actual OpenCLAW import when available
        greeting += "Status: Ready to use OpenCLAW (once the correct repository is configured)\n"
    except ImportError:
        greeting += "Status: OpenCLAW installation pending (repository URL needs verification)\n"
    
    return greeting

def system_info():
    """Return detailed system information."""
    return check_installation()

# Create Gradio interface with tabs
with gr.Blocks(title="OpenCLAW Installation Demo") as demo:
    gr.Markdown("""
    # OpenCLAW Installation Demo
    
    This Space demonstrates how to install Python packages from GitHub in Hugging Face Spaces.
    
    ## How it works:
    
    1. Add the GitHub package URL to `requirements.txt`
    2. Hugging Face Spaces automatically installs it during deployment
    3. Import and use the package in your app
    
    ## Supported formats:
    
    - Direct tarball: `https://github.com/user/repo/archive/branch.tar.gz`
    - Git protocol: `git+https://github.com/user/repo.git@branch`
    - With tag: `git+https://github.com/user/repo.git@v1.0.0`
    """)
    
    with gr.Tab("Demo"):
        with gr.Row():
            name_input = gr.Textbox(
                label="Enter your name", 
                placeholder="Your name here...",
                value="User"
            )
        with gr.Row():
            greet_btn = gr.Button("Greet Me!", variant="primary")
        with gr.Row():
            output = gr.Textbox(label="Greeting", lines=6)
        
        greet_btn.click(fn=greet, inputs=name_input, outputs=output)
    
    with gr.Tab("System Info"):
        gr.Markdown("### Check installed packages and system information")
        check_btn = gr.Button("Check Installation", variant="primary")
        sys_output = gr.Textbox(label="System Information", lines=20)
        
        check_btn.click(fn=system_info, inputs=None, outputs=sys_output)
        
        # Auto-load on tab open
        demo.load(fn=system_info, inputs=None, outputs=sys_output)

if __name__ == "__main__":
    demo.launch()
