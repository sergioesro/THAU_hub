# README.md content

# Gradio URL Launcher

A Python project that implements a visually appealing Gradio interface with a title, a customizable placeholder logo, and buttons that redirect to specific URLs based on a common IP address with varying port numbers. This project is designed for future deployment as a service.

## Features

- Customizable Gradio interface
- Buttons that redirect to specific URLs
- Easy configuration of IP address and ports

## Project Structure

```
gradio-url-launcher
├── src
│   ├── main.py          # Entry point of the application
│   ├── config
│   │   └── settings.py  # Configuration settings
│   ├── static
│   │   └── styles.css    # CSS styles for the interface
│   └── utils
│       └── url_handler.py # Utility functions for URL operations
├── tests
│   └── test_url_handler.py # Unit tests for URL handling
├── requirements.txt       # Project dependencies
├── .gitignore             # Files to ignore in Git
└── README.md              # Project documentation
```

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