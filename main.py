import modal

app = modal.App("anthropic-computer-use")
image = modal.Image.from_dockerfile("Dockerfile", add_python="3.11").pip_install(
    "streamlit>=1.38.0",
    "anthropic[bedrock,vertex]>=0.39.0",
    "jsonschema==4.22.0",
    "boto3>=1.28.57",
    "google-auth<3,>=2"
).add_local_dir("image", "/home/computeruse").add_local_dir("computer_use_demo", "/home/computeruse/computer_use_demo")

@app.function(image=image)
def start_computer_use():
    import os
    import subprocess
    with modal.forward(8501) as streamlit_tunnel:
        with modal.forward(6080) as desktop_tunnel:
            print(f"streamlit_tunnel.url = {streamlit_tunnel.url}")
            print(f"desktop_tunnel.url = {desktop_tunnel.url}")
            subprocess.run(["./entrypoint.sh"], check=True)
