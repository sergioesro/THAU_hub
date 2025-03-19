import os
import gradio as gr
from dotenv import load_dotenv

from css.css import button_style, button_hover

# Load environment variables
load_dotenv()

theme = gr.themes.Soft(
    primary_hue="lime",
)

with gr.Blocks(theme=theme, css="body {background-color: #e8f5e9; text-align: center;} .button-container { display: flex; flex-direction: column; align-items: center; }") as demo:
    gr.Markdown("""
    # 🤖 GTHAU Hub
    """)
    
    gr.Image("assets/thau_logo.jpeg", elem_id="logo")
    
    gr.Markdown("""---""")
    
    with gr.Row():
        gr.HTML(f'<a href="{os.getenv("MACHINES_URL")}" target="_blank"><button style="{button_style}" {button_hover}>🖥️ Machines</button></a>')
        gr.HTML(f'<a href="{os.getenv("MODEL_REPO_URL")}" target="_blank"><button style="{button_style}" {button_hover}>🤗 Model Repository</button></a>')
    
    with gr.Row():
        gr.HTML(f'<a href="{os.getenv("GTHAU_URL")}" target="_blank"><button style="{button_style}" {button_hover}>🏠 GTHAU Website</button></a>')
        gr.HTML(f'<a href="{os.getenv("DESK_BOOK_URL")}" target="_blank"><button style="{button_style}" {button_hover}>🪑 DESK BOOKING</button></a>')
    
    gr.Markdown("""---""")
    
    gr.Markdown("GTHAU - 2025 ❤️ @Sergio Esteban-Romero & @Iván Martín-Fernández & @Jaime Bellver-Soler ")

demo.launch(server_name="0.0.0.0", server_port=7861)

