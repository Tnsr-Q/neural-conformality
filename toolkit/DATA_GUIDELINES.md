# Data Submission Guidelines

To ensure that results are comparable and that the automated analysis in our toolkit functions correctly, all submitted data must adhere to the following format.

## The Golden Rule

The file must be a **CSV (Comma-Separated Values) file** where **rows represent time points** and **columns represent individual neural sources** (e.g., cortical vertices or ROIs).

## Pre-Processing Summary

The toolkit is designed to be the *final analysis step*. Before creating your CSV, you should have already performed the following pre-processing steps using a toolbox like MNE-Python:

1.  **Raw Data Acquisition:** Start with your raw MEG/EEG recording.
2.  **Band-Pass Filtering:** Filter the data into the specific frequency band of interest (e.g., gamma, 30-80 Hz).
3.  **Source Reconstruction:** Apply an inverse solution (e.g., MNE, dSPM) to project the sensor data onto a cortical surface model.
4.  **Hilbert Transform:** Apply the Hilbert transform to the time series of each source vertex to obtain the complex analytic signal.

## CSV File Format Specification

### 1. Filename
While not required, we recommend a descriptive filename, such as: `Subject01_Awake-Rest_2025-07-24.csv`

### 2. Header
Your CSV file **should have a header row** containing the names of the sources or ROIs. The toolkit will use this to determine the number of sources.

### 3. Column Structure
-   Each column should represent the time series of a single neural source.
-   The data in the columns should be the **real part** of the analytic signal. The toolkit will re-apply the Hilbert transform internally to reconstruct the complex signal `Z(t)`.
-   **Do not include a time column.** The time vector is handled by the "Sampling Frequency" input in the app.

### 4. Data Values
-   All values should be numerical (integer or float).
-   The values should represent the activity metric from your source reconstruction (e.g., current density in Amperes/meter).

### Example
For a small dataset with 3 ROIs over 4 time points, the CSV would look like this:

```csv
Frontal_L,Parietal_L,Occipital_L
0.003,0.001,-0.002
0.004,0.002,-0.001
0.005,0.001,0.000
0.004,-0.001,0.002
```

You can use the **[TEMPLATE.csv](TEMPLATE.csv)** file in this repository as a direct structural reference.

