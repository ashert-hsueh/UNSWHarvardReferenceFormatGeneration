# UNSW Harvard Reference Generator

A desktop application built with PySide6 for converting BibTeX entries from Google Scholar to UNSW Harvard reference style.

## Features

- **Clean UI**: Modern interface following UNSW branding guidelines
- **BibTeX Input**: Paste BibTeX entries from Google Scholar
- **Harvard Output**: View formatted UNSW Harvard references
- **Copy Functionality**: Quick copy to clipboard
- **Responsive Design**: Centered window with minimum size constraints

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd UNSWHarvardReferenceFormatGeneration
   ```

2. **Activate the virtual environment**:
   ```bash
   # Windows
   .venv\Scripts\activate

   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r UI/requirements.txt
   ```

## Usage

1. **Run the application**:
   ```bash
   # Windows
   .venv\Scripts\python UI\main.py

   # macOS/Linux
   .venv/bin/python UI/main.py
   ```

2. **Paste BibTeX content** into the left text area

3. **Click "Convert"** (conversion logic coming soon)

4. **Copy the generated Harvard reference** using the Copy button

## UI Layout

- **Left Panel**: BibTeX input area with placeholder text
- **Right Panel**: Read-only Harvard reference output with Copy button
- **Bottom Center**: Prominent Convert button
- **Status Bar**: Feedback messages

## Branding

Uses official UNSW colors:
- Primary: UNSW Blue (#00338D)
- Secondary: UNSW Gold (#FFB81C)
- Light Blue: #E6EDF6 (for read-only areas)

## Technical Stack

- **Python 3.12+**
- **PySide6** - Qt UI framework
- **Qt Designer** - UI layout design

## Development

To modify the UI:
1. Edit `UI/main.ui` using Qt Designer
2. Regenerate Python code: `pyside6-uic UI/main.ui -o UI/myui.py`
3. Update functionality in `UI/main.py`

## License

MIT