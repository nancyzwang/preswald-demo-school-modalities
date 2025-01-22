from preswald import text, plotly
import pandas as pd
import plotly.express as px
import numpy as np

# Welcome message
text("# School Insights Explorer: Learning Modalities and Student Distribution")
text("Dive into the world of education insights! This analysis uncovers trends and patterns in school operations, learning modalities, and student distributions across districts, cities, and ZIP Codes. 📊\n")

# Load the data
data = pd.read_csv("School_Learning_Modalities__2021-2022_20250114.csv")

# Convert the Week column to datetime format
data['Week'] = pd.to_datetime(data['Week'])

# Filter out rows with zero values for key metrics
data_filtered = data[
    (data['Student Count'] > 0) & 
    (data['Operational Schools'] > 0)
].copy()

# Metrics calculations
total_students = data_filtered['Student Count'].sum()
average_students = data_filtered['Student Count'].mean()
max_students = data_filtered['Student Count'].max()
min_students = data_filtered['Student Count'].min()
total_operational_schools = data_filtered['Operational Schools'].sum()
average_operational_schools = data_filtered['Operational Schools'].mean()
students_per_school = total_students / total_operational_schools if total_operational_schools > 0 else 0

# Additional metrics
student_count_variance = data_filtered['Student Count'].var()
student_count_std_dev = data_filtered['Student Count'].std()
correlation_students_schools = data_filtered['Student Count'].corr(data_filtered['Operational Schools'])

# Learning modality insights
learning_modality_counts = data_filtered['Learning Modality'].value_counts()

# Display key metrics
text("## 📊 Key Metrics Overview")
text(f"""
- Total Students: **{total_students:,.0f}**
- Average Students per District: **{average_students:,.0f}**
- Maximum Students in a District: **{max_students:,.0f}**
- Minimum Students in a District: **{min_students:,.0f}**
- Total Operational Schools: **{total_operational_schools:,.0f}**
- Average Schools per District: **{average_operational_schools:.1f}**
- Average Students per School: **{students_per_school:.1f}**
""")

# Visualizations

# 1. Bar Chart: Student Count by District
text("## Student Count by District")
text("Each bar represents the total number of students in a district, providing a visual comparison of district populations.")
district_summary = data_filtered.groupby('District Name')['Student Count'].sum().nlargest(20).reset_index()
fig_students_bar = px.bar(
    district_summary,
    x='District Name', 
    y='Student Count', 
    title='Top 20 Districts by Student Count',
    color='Student Count',
    labels={'District Name': 'District', 'Student Count': 'Number of Students'},
    color_continuous_scale=px.colors.sequential.Viridis
)
fig_students_bar.update_layout(xaxis_tickangle=-45)
plotly(fig_students_bar)

# 2. Histogram: Distribution of Student Counts
text("## Distribution of Student Counts Across Districts")
text("This histogram shows the frequency distribution of student counts across districts, grouped into intervals for comparison.")
fig_histogram = px.histogram(
    data_filtered,
    x='Student Count',
    nbins=30,
    title='Distribution of Student Counts',
    labels={'Student Count': 'Number of Students'},
    color_discrete_sequence=['teal']
)
plotly(fig_histogram)

# 3. Heatmap: Correlation Between Metrics
text("## Correlation Heatmap")
text("This heatmap visualizes the correlation between key metrics, such as student count and operational schools, highlighting their relationships.")
correlation_matrix = data_filtered[['Student Count', 'Operational Schools']].corr()
fig_heatmap = px.imshow(
    correlation_matrix,
    title='Correlation Heatmap',
    labels={'color': 'Correlation'},
    text_auto=True,
    aspect='auto'
)
plotly(fig_heatmap)

# 4. Violin Plot: Student Count by Learning Modality
text("## Student Count by Learning Modality")
text("This violin plot shows the distribution and density of student counts for each learning modality, including any outliers.")
fig_violin = px.violin(
    data_filtered,
    y='Student Count',
    x='Learning Modality',
    color='Learning Modality',
    box=True,
    points="outliers",
    title='Student Count by Learning Modality',
    labels={'Learning Modality': 'Modality', 'Student Count': 'Number of Students'}
)
plotly(fig_violin)

# 5. Bar Chart: Top 5 Districts by Student Count
text("## Top 5 Districts by Student Count")
text("This bar chart highlights the districts with the highest student populations, showcasing the top five contributors.")
top_5_districts = data_filtered.groupby('District Name')['Student Count'].sum().nlargest(5).reset_index()
fig_top_districts = px.bar(
    top_5_districts,
    x='District Name',
    y='Student Count',
    title='Top 5 Districts by Student Count',
    color='Student Count',
    labels={'District Name': 'District', 'Student Count': 'Number of Students'},
    color_continuous_scale=px.colors.sequential.Plasma
)
plotly(fig_top_districts)

# 6. Parallel Categories Plot: City and Learning Modality
text("## City and Learning Modality Distribution")
text("This parallel categories chart explores the relationship between cities and the learning modalities their students engage in.")
top_cities = data_filtered.groupby('City')['Student Count'].sum().nlargest(10).index
city_modality_data = data_filtered[data_filtered['City'].isin(top_cities)]
fig_parallel = px.parallel_categories(
    city_modality_data,
    dimensions=['City', 'Learning Modality'],
    color='Student Count',
    title='Learning Modality Distribution in Top 10 Cities',
    color_continuous_scale=px.colors.sequential.Sunset
)
plotly(fig_parallel)

# 7. Box Plot: Student Count by District
text("## Student Count Variations by District")
text("This box plot highlights the distribution of student counts across top districts, including median values and outliers.")
top_districts = data_filtered.groupby('District Name')['Student Count'].sum().nlargest(15).index
district_data = data_filtered[data_filtered['District Name'].isin(top_districts)]
fig_box_district = px.box(
    district_data,
    x='District Name',
    y='Student Count',
    title='Student Count Distribution in Top 15 Districts',
    color='District Name',
    labels={'District Name': 'District', 'Student Count': 'Number of Students'}
)
fig_box_district.update_layout(xaxis_tickangle=-45)
plotly(fig_box_district)

# 8. Treemap: Student Count by City
text("## Treemap of Student Count by City")
text("This treemap shows the proportion of total students in each city, providing a hierarchical view of city contributions.")
city_students = data_filtered.groupby('City')['Student Count'].sum().reset_index()
city_students = city_students[city_students['Student Count'] > 0]  # Remove cities with zero students
fig_treemap_city = px.treemap(
    city_students,
    path=['City'],
    values='Student Count',
    title='Treemap of Student Count by City',
    color='Student Count',
    color_continuous_scale=px.colors.sequential.Mint
)
plotly(fig_treemap_city)

# 9. Scatter Matrix: Relationships Between Variables
text("## Scatter Matrix of Key Metrics")
text("This scatter matrix explores pairwise relationships between key variables such as student count and operational schools.")
fig_scatter_matrix = px.scatter_matrix(
    data_filtered,
    dimensions=['Student Count', 'Operational Schools'],
    title='Scatter Matrix of Key Metrics',
    labels={'Student Count': 'Number of Students', 'Operational Schools': 'Number of Schools'}
)
plotly(fig_scatter_matrix)

# 10. Bar Chart: Learning Modality Distribution by District
text("## Learning Modality Distribution by District")
text("This bar chart breaks down the distribution of learning modalities within top districts, showing how learning preferences vary.")
top_districts = data_filtered.groupby('District Name')['Student Count'].sum().nlargest(10).index
district_modality_data = data_filtered[data_filtered['District Name'].isin(top_districts)]
fig_bar_modality_district = px.bar(
    district_modality_data,
    x='District Name',
    y='Student Count',
    color='Learning Modality',
    title='Learning Modality Distribution in Top 10 Districts',
    barmode='stack',
    labels={'District Name': 'District', 'Student Count': 'Number of Students'}
)
fig_bar_modality_district.update_layout(xaxis_tickangle=-45)
plotly(fig_bar_modality_district)

# 11. Sunburst Chart: Student Count by State and District
text("## Sunburst Chart: Student Count by State and District")
text("This sunburst chart provides a hierarchical view of student counts, first by state and then by district.")
state_district_data = data_filtered.groupby(['State', 'District Name'])['Student Count'].sum().reset_index()
fig_sunburst = px.sunburst(
    state_district_data,
    path=['State', 'District Name'],
    values='Student Count',
    title='Student Count Distribution by State and District',
    color='Student Count',
    color_continuous_scale=px.colors.sequential.Turbo
)
plotly(fig_sunburst)

# 12. Radar Chart: Key Metrics by District
text("## Radar Chart: Key Metrics by District")
text("This radar chart compares key metrics such as student count and operational schools for the top districts.")
top_districts_metrics = data_filtered.groupby('District Name').agg({
    'Student Count': 'sum',
    'Operational Schools': 'sum'
}).nlargest(5, 'Student Count').reset_index()
fig_radar = px.line_polar(
    top_districts_metrics,
    r='Student Count',
    theta='District Name',
    title='Top 5 Districts by Student Count',
    line_close=True
)
plotly(fig_radar)