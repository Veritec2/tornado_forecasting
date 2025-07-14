# Tornado Forecasting Model

A machine learning project for predicting tornadic events using meteorological data.

## Project Overview

This project aims to develop a predictive model for tornado forecasting by analyzing various meteorological parameters and historical tornado data. The goal is to improve early warning systems and enhance severe weather preparedness.

## Project Structure

```
tornado-forecasting/
├── data/
│   ├── raw/              # Original, unprocessed data
│   ├── processed/        # Cleaned and feature-engineered data
│   └── external/         # Third-party data sources
├── notebooks/            # Jupyter notebooks for exploration and analysis
├── src/                  # Source code for the project
│   ├── data/            # Scripts for data download and processing
│   ├── features/        # Feature engineering scripts
│   ├── models/          # Model training and prediction scripts
│   └── visualization/   # Visualization and plotting functions
├── models/              # Trained and serialized models
├── reports/             # Generated analysis and figures
│   └── figures/
├── tests/               # Unit tests
├── environment.yml      # Conda environment specification
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation (this file)
```

## Getting Started

### Prerequisites

- Python 3.11
- Anaconda or Miniconda
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/tornado-forecasting.git
   cd tornado-forecasting
   ```

2. **Create and activate the conda environment**
   ```bash
   conda env create -f environment.yml
   conda activate tornado-forecast
   ```

3. **Install additional dependencies (if any)**
   ```bash
   pip install -r requirements.txt
   ```

### Data Sources

- NOAA Storm Events Database
- NWS Radar Data
- Surface observation stations (ASOS/AWOS)
- Upper air soundings
- Satellite imagery
- ECM

*Note: Data files are not included in the repository due to size constraints. See `data/README.md` for download instructions.*

## Usage

### Data Processing
```bash
python src/data/download_noaa_data.py
python src/data/process_raw_data.py
```

### Model Training
```bash
python src/models/train_model.py --config configs/model_config.yaml
```

### Making Predictions
```bash
python src/models/predict.py --date 2024-05-15 --location "Oklahoma"
```

## Features

- **Data Pipeline**: Automated downloading and processing of meteorological data
- **Feature Engineering**: Extraction of relevant atmospheric parameters
- **Multiple Models**: Support for various ML algorithms (Random Forest, XGBoost, Neural Networks)
- **Visualization**: Interactive maps and charts for analysis
- **Real-time Capability**: Framework for operational forecasting

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Development Setup

### VS Code Configuration
This project includes VS Code settings for optimal Python development:
- Linting with pylint
- Formatting with black
- Integrated Jupyter notebook support

### Git Workflow
- Use feature branches for new development
- Follow conventional commit messages
- Run tests before pushing

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/
```

## Authors

- Your Name - Initial work - [YourGitHub](https://github.com/yourusername)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- NOAA/NWS for providing weather data
- MetPy developers for meteorological calculations
- Scikit-learn team for ML tools

## References

- [Storm Prediction Center](https://www.spc.noaa.gov/)
- [Tornado Climatology](https://www.ncdc.noaa.gov/climate-information/extreme-events/us-tornado-climatology)
- [ML in Meteorology Review](https://journals.ametsoc.org/)