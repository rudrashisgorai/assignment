
# FastAPI Brand-Company Matcher

## Overview
This project is a FastAPI application designed for matching brand and company names using fuzzy string matching. It leverages the `rapidfuzz` library for efficient string matching and integrates with a JSON dataset to provide accurate and fast brand-company associations.

## Features
- **Fuzzy String Matching**: Utilizes `rapidfuzz` for matching user-input brand and company names to a dataset.
- **FastAPI Framework**: Built using FastAPI for efficient and easy-to-use web API development.
- **Dynamic Dataset Integration**: Integrates with a JSON-based dataset for brands and companies, allowing dynamic data handling.
- **Customizable Thresholds**: Utilizes environment variables for customizable matching thresholds.

## Installation and Setup
1. **Clone the Repository**: 
   - Clone the repository from GitHub.
2. **Install Dependencies**:
   - Install required Python libraries: `fastapi`, `numpy`, `pandas`, `rapidfuzz`, `uvicorn`.
3. **Dataset Preparation**:
   - Place your `DatasetMapping.json` file in the project directory.
4. **Environment Variables**:
   - Set `THRESHOLD_COMPANY_MATCH` and `THRESHOLD_CONF_LEVEL` in your environment for customization.

## Running the Application
- Run the application using Uvicorn: `uvicorn main:app --reload`
- The application will be served at `http://127.0.0.1:8000/`.

## API Usage
- **Endpoint**: `GET /`
- **Parameters**:
  - `brand`: The brand name to match.
  - `company`: The company name to match.
- **Returns**: A JSON response with the best match and confidence level.

## Contributing
Contributions to enhance or expand the project are welcome. Please fork the repository and submit a pull request with your changes.

## Future Enhancements
- Adding more datasets for broader matching capabilities.
- Improving the matching algorithm for higher accuracy.
- Incorporating advanced data preprocessing techniques.
