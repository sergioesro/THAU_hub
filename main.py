import os
import webbrowser
import gradio as gr
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def open_url(url):
    webbrowser.open(url)

theme = gr.themes.Soft(
    primary_hue="lime",
)

with gr.Blocks(theme=theme) as demo:
    gr.Markdown("""
    # 🤖 GTHAU Hub
    """)
    
    gr.Image("assets/thau_logo.jpeg", elem_id="logo")
    
    gr.Markdown("""---""")
    
    with gr.Row():
        gr.Button("Machines", variant="primary").click(lambda: open_url(os.getenv('MACHINES_URL')))
        gr.Button("Model Repository", variant="secondary").click(lambda: open_url(os.getenv('MODEL_REPO_URL')))
    
    with gr.Row():
        gr.Button("GTHAU Website", variant="primary").click(lambda: open_url(os.getenv('GTHAU_URL')))
    
    gr.Markdown("""---""")
    
    gr.Markdown("GTHAU - 2025 | @Sergio Esteban-Romero & @Iván Martín-Fernández")

demo.launch(server_name="0.0.0.0", server_port=7861)

