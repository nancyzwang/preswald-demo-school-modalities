# School Learning Modalities Explorer

![Dashboard Demo](images/dashboard-demo.gif)

An interactive dashboard built with Preswald to visualize and analyze school learning modalities data from 2021-2022. This tool helps educators, administrators, and policymakers understand trends in school operations, learning approaches, and student distributions across different regions.

## Features
- **Comprehensive Analytics**: Analyze student counts, learning modalities, and operational schools across districts, cities, and states
- **Interactive Visualizations**: Explore 12 different interactive visualizations including:
  - Bar charts for district comparisons
  - Heatmaps for metric correlations
  - Violin plots for learning modality distributions
  - Treemaps for geographic insights
  - And more!
- **Key Metrics**: Track important statistics like:
  - Total and average student counts
  - Operational school numbers
  - Learning modality distributions
  - Student-to-school ratios

## Setup
1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install preswald>=0.1.0 plotly>=5.18.0 pandas>=2.1.4 numpy>=1.26.2
   ```
   
   Or install from requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your settings in `config.toml`
4. Run the dashboard:
   ```bash
   preswald run --port 9513 hello.py
   ```

## Data Format
The dashboard uses a CSV file with the following structure:
```csv
District NCES ID,District Name,Week,Learning Modality,Operational Schools,Student Count,City,State,ZIP Code
```

## Available Visualizations

1. **Student Count by District**: Compare student populations across top 20 districts
2. **Distribution of Student Counts**: View the frequency distribution of student counts
3. **Correlation Heatmap**: Explore relationships between key metrics
4. **Student Count by Learning Modality**: Analyze distribution of students across different learning approaches
5. **Top Districts Analysis**: Focus on the districts with highest student populations
6. **City and Learning Modality Distribution**: Understand how cities implement different learning approaches
7. **Student Count Variations**: View detailed distributions within districts
8. **Geographic Distribution**: Visualize student counts across cities
9. **Metric Relationships**: Explore correlations between different variables
10. **Learning Modality Patterns**: See how districts implement different learning approaches
11. **Hierarchical View**: Drill down from states to districts
12. **District Comparisons**: Compare key metrics across top districts

## Features
- **Comprehensive Analytics**: Analyze student counts, learning modalities, and operational schools across districts, cities, and states
- **Interactive Visualizations**: Explore 12 different interactive visualizations including:
  - Bar charts for district comparisons
  - Heatmaps for metric correlations
  - Violin plots for learning modality distributions
  - Treemaps for geographic insights
  - And more!
- **Key Metrics**: Track important statistics like:
  - Total and average student counts
  - Operational school numbers
  - Learning modality distributions
  - Student-to-school ratios

## Example Use Cases
- **Educational Planning**: Understand student distribution patterns to optimize resource allocation
- **Policy Analysis**: Compare learning modality adoption across different regions
- **Operational Insights**: Analyze the relationship between operational schools and student populations
- **Regional Comparisons**: Compare educational approaches across different cities and states

## Contributing
Feel free to submit issues and enhancement requests!

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---
Last updated: January 22, 2025
