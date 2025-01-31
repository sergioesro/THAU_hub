# README.md content

# Gradio URL Launcher

A Python project that implements a visually appealing Gradio interface with a title, a customizable placeholder logo, and buttons that redirect to specific URLs based on a common IP address with varying port numbers. This project is designed for future deployment as a service.

## Features

- Customizable Gradio interface
- Buttons that redirect to specific URLs
- Easy configuration of IP address and ports

## Project Structure

```
thau_hub
THAU_hub/ 
├── assets/ 
│ └── thau_logo.jpeg 
├── src/ 
│ 
└── main.py 
├── config/ 
│ └── .env 
├── services/ 
│ └── gthau-hub.service 
├── requirements.txt 
├── README.md 
└── .gitignore
```
You may need a .env file containing the IP Adress of your services.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/sergioesro/THAU_hub.git
   cd THAU_hub
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

Open your web browser and navigate to the specified IP address and port to access the Gradio interface.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.