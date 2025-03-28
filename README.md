# MasterThesis
Repository containing data and scripts used in the making of my Master Thesis, to be used as supplementary information to the methods and data reported.

The repository follows the structure below:

- `BIOSCREEN/` -> Folder containing the version of BIOSCREEN used in the making of the thesis.
- `CW_SWAP_data/` -> Folder containing the redox potential data from the Constructed Wetland pilot study used in the making of the thesis.
- `CW_data_analysis_scripts/` -> Folder containing all Python scripts used to analyze the Constructed Wetland field sampling and redox potential data, and the scripts used for generating figures.
  + `BTEX_compound_plotting.py` -> Python script used to make the composite plots for BTEX concentrations over the length of the Constructed Wetland.
  + `acceptor_compound_plotting.py` -> Python script used to make the composite plots for electron acceptor concentrations over the length of the Constructed Wetland.
  + `redox_plotter.py` -> Python script used to make plots of the redox potential in the Constructed Wetland over time.
  + `sampling_plotter.py` -> Python script used to make single plots of the contaminant concentrations in the Constructed Wetland over time.
  + `single_compound_combi.py` -> Python script used to make a composite plot for a single contaminant.
  + `tools.py` -> Python module containing the functions used in the scripts for plotting and analysis.
- `CW_field_measurements/` -> Folder containing the raw Constructed Wetland field data as measured in the field campaigns.
  + `240120_Resultaten_ronde_T=0.xlsx` -> Excel file with the field measurements from first sampling in August.
  + `240120_Resultaten_ronde_T=1.xlsx` -> Excel file with the field measurements from first sampling in October.
  + `240120_Resultaten_ronde_T=2.xlsx` -> Excel file with the field measurements from first sampling in December.
- `CW_weather_data/` -> Folder containing the raw weather data from the Constrcuted Wetland pilot study used in the making of the thesis.
- `anatrans_example_plots/` -> Folder containing Python scripts used to generate the figures in the thesis, using anatrans (or mibitrans), as it is currently called.
  + `BIOSCREEN_default_data_comparison.py` -> Python script generating plots comparing anatrans to BIOSCREEN, using data from the Keesler Air Force base site.
  + `BIOSCREEN_example_data_comparison.py` -> Python script generating plots comparing anatrans to BIOSCREEN, using the example data build into BIOSCREEN.
  + `base_plots_example.py` -> Python script showing figures with the base capabilities of anatrans.
- `README.md` -> The file you are currently reading. Provides overview over the contents of this repository.

