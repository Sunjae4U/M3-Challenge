# M3 Challenge — Gambling Loss Model

A mathematical modeling project built for the 2026 M3 Challenge. Simulates annual gambling losses across demographic groups using Monte Carlo methods, and estimates disposable income after tax for US and UK earners.

## Table of Contents
1. [About The Project](#about-the-project)
2. [Built With](#built-with)
3. [Getting Started](#getting-started)
4. [Usage](#usage)
5. [Roadmap](#roadmap)
6. [Contributing](#contributing)
7. [License](#license)
8. [Contact](#contact)
9. [Acknowledgments](#acknowledgments)

## About The Project

This project models the financial impact of gambling across age groups and risk profiles using two core components:

- Gambling Loss Simulator — runs 10,000 Monte Carlo simulations per demographic group (High Risk Male, Low Risk Male, High Risk Female, Low Risk Female) across four age brackets (18-29, 30-49, 50-64, 65+), using lognormal stake distributions and a house hold of ~10.16%
- Tax & Disposable Income Calculator — computes post-tax take-home pay and disposable income for US filers (single, jointly, head of household) and UK earners, using 2025 tax brackets and age-adjusted expenditure scalars

> Disclaimer: This model is built for academic purposes as part of the 2026 M3 Challenge. Results are not indicative of real-world financial advice.

([back to top](#m3-challenge--gambling-loss-model))

## Built With

- [Python](https://www.python.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

([back to top](#m3-challenge--gambling-loss-model))

## Getting Started

### Prerequisites

Make sure you have Python installed, then install the required packages:

```bash
pip install numpy matplotlib
```

### Installation

1. Clone the repo
```bash
git clone https://github.com/Sunjae4U/M3-Challenge.git
```

2. Navigate to the project directory
```bash
cd M3-Challenge
```

3. Run any simulation script
```bash
python high_risk_male.py
python low_risk_male.py
python high_risk_female.py
python low_risk_female.py
python tax_calculator.py
```

([back to top](#m3-challenge--gambling-loss-model))

## Usage

Each gambling simulation script runs 10,000 yearly simulations and plots a histogram of annual losses by age group with mean loss indicators. Parameters such as `BETS_PER_YEAR`, `AVG_STAKE`, `ODDS`, and `HOLD` can be adjusted at the top of each file to model different scenarios.

The tax calculator takes a gross income, filing status, and age as inputs and returns estimated disposable income after federal tax, FICA, and age-adjusted essential expenditures.

```python
# US example
print(us_disposable_income(94000, "jointly", 30))

# UK example
print(uk_disposable_income(40400, 25))
```

([back to top](#m3-challenge--gambling-loss-model))

## Roadmap

- [ ] Combine all simulations into a single unified script
- [ ] Add state-level tax support for US
- [ ] Export simulation results to CSV
- [ ] Add interactive visualizations (Plotly)

See the [open issues](https://github.com/Sunjae4U/M3-Challenge/issues) for a full list of proposed features and known issues.

([back to top](#m3-challenge--gambling-loss-model))

## Contributing

Contributions are welcome and greatly appreciated!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

([back to top](#m3-challenge--gambling-loss-model))

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

([back to top](#m3-challenge--gambling-loss-model))

## Contact

Sunjae4U — [GitHub](https://github.com/Sunjae4U)

Project Link: [https://github.com/Sunjae4U/M3-Challenge](https://github.com/Sunjae4U/M3-Challenge)

([back to top](#m3-challenge--gambling-loss-model))

## Acknowledgments

- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Choose an Open Source License](https://choosealicense.com)
- [2026 M3 Challenge](https://m3challenge.siam.org/)

([back to top](#m3-challenge--gambling-loss-model))
