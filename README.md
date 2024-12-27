# AverageRating
# Geographic Analysis of Restaurant Locations

This project performs a geographic analysis of restaurant locations, clustering them based on latitude and longitude data using the DBSCAN algorithm. The project includes the generation of interactive maps and visualizations.

---

## Features
- **Clustering with DBSCAN:**
  - Clusters restaurants based on proximity using the Haversine metric.
  - Differentiates between clustered points and noise.
- **Interactive Map Visualization:**
  - Plots restaurant locations on a Folium map.
  - Visualizes clusters using different colors for each cluster.
- **Static Scatter Plot Visualization:**
  - Displays clusters on a 2D scatter plot with longitude and latitude.

---

## Requirements

### Python Libraries
- `pandas`
- `numpy`
- `matplotlib`
- `folium`
- `scikit-learn`

Install all required libraries using the following command:
```bash
pip install pandas numpy matplotlib folium scikit-learn
```

---

## Usage

1. **Prepare the Dataset:**
   - Save your restaurant data in a CSV file named `Dataset.csv`.
   - Ensure the file includes the following columns:
     - `Latitude`
     - `Longitude`
     - `Restaurant name` (optional, for popups on the map).

2. **Run the Script:**
   - Execute the Python script to:
     - Clean the data.
     - Perform clustering using DBSCAN.
     - Generate interactive and static visualizations.

3. **View the Results:**
   - Open `cluster_map.html` in a web browser to explore the interactive map.
   - View the scatter plot to analyze the clustering visually.

---

## Code Explanation

### 1. Data Cleaning
Removes rows with missing latitude or longitude values:
```python
data_cleaned = data.dropna(subset=['Latitude', 'Longitude'])
```

### 2. DBSCAN Clustering
Clusters restaurant locations using the Haversine metric for geographic distance:
```python
coords = data_cleaned[['Latitude', 'Longitude']].values
db = DBSCAN(eps=0.01, min_samples=5, metric='haversine').fit(np.radians(coords))
data_cleaned['Cluster'] = db.labels_
```

### 3. Map Visualization
Plots each restaurant's location and colors it based on cluster membership:
```python
for _, row in data_cleaned.iterrows():
    cluster_color = 'red' if row['Cluster'] == -1 else 'blue'
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=5,
        color=cluster_color,
        fill=True,
        fill_opacity=0.7,
    ).add_to(cluster_map)
```

### 4. Scatter Plot
Displays clusters in a 2D scatter plot:
```python
plt.scatter(
    data_cleaned['Longitude'],
    data_cleaned['Latitude'],
    c=data_cleaned['Cluster'],
    cmap='viridis',
    marker='o'
)
plt.title("Restaurant Clusters")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.colorbar(label="Cluster ID")
plt.show()
```
## Example Output

### 1. Interactive Map
- `cluster_map.html`: View the clustered restaurant locations on an interactive map.

### 2. Scatter Plot
A 2D scatter plot showing clusters:

![Cluster Plot Example](example_cluster_plot.png)

---

## Notes
- Ensure your dataset is properly formatted and includes latitude and longitude values.
- Adjust the `eps` parameter in DBSCAN to tune clustering sensitivity.

---

## License
This project is licensed under the MIT License.
