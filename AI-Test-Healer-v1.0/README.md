# AI Test Healer v1.0

AI Test Healer is an intelligent assistant designed to analyze automated test results from Katalon, identify common failure causes such as XPath breaks, and suggest or apply fixes to the corresponding test scripts. This project aims to streamline the debugging process for automated tests, making it easier for developers to maintain and improve their test suites.

## Project Structure

```
AI-Test-Healer-v1.0
├── .devcontainer
│   ├── devcontainer.json
│   └── Dockerfile
├── .vscode
│   └── extensions.json
├── .gitignore
├── .env.example
├── README.md
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── healer.py
│   └── utils.py
├── data
│   ├── reports
│   │   └── sample_katalon_report.xml
│   └── groovy_scripts
│       └── sample_test.groovy
└── notebooks
    └── experiments.ipynb
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/AI-Test-Healer-v1.0.git
   cd AI-Test-Healer-v1.0
   ```

2. Set up a Python virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file based on the `.env.example` template to configure your environment variables.

## Usage

To run the application, execute the following command:
```
python src/main.py
```

This will initialize the AI Test Healer and print a confirmation message.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.