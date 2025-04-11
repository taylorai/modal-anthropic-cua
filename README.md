# basic computer use on Modal

The `computer_use_demo` and `image` directories are copied directly from the Anthropic computer use demo [here](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo). The Dockerfile is modified to work with Modal. We use `modal.tunnel` to expose the Streamlit and noVNC ports (8501 and 6080) on Modal URLs. The side-by-side view on port 8080 doesn't work; you can just open each view in a separate window.

To run, just clone this repo, make sure your Modal credentials are set up and you have Modal installed, and then `modal run main.py`.
