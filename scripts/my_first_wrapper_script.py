#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 13:18:17 2024

@author: Charity
"""

## Import  packages

import hvsr_tools as ht

#%% eHVSR SM Flowchart

# Import packages needed

# Define directory paths to store and retrieve data 
    # mseed_dir = directory to store miniseed data
    # fig_dir = directory to store figures
    # meta_dir = directory to store metadata
    
# Define min/max lat/lon search parameters
    # minlat = minimum latitude
    # maxlat = maximum latitude
    # minlon = minimum longitude
    # maxlon = maximum longitude
    
# Define central lat/lon search parameters
    # central_lat = central latitude
    # central_lon = central longitude
    
# Define min/max search radius parameters
    # min_radius = minimum search radius
    # max_radius = maximum search radius
    
# Define start/end time period search parameters
    # stime = start search time
    # etime = end search time
    
# Define min depth search parameter
    # min_depth = minimum depth of events to search for
    
# Define min magnitude search parameter
    # min_mag = minimum magnitude
    
# Define network/stations/channels/client search parameters
    # netcode = network code(s) to search for 
    # all_stations = station names to search for
    # channels = channel types to search for
    # client = client to retrieve data from
    
# Define TauPyModel to use
    # model = model choice


#%% Gather station inventory

# Initiate list to store inventory
    # sta_inventory = []
    
    
# %%  Convert earthquake catalog from obspy into pandas dataframe/lists

my_info = ht.extract_eventinfo_from_catalog()