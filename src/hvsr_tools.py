#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 13:12:39 2024

@author: Charity
"""
# Function: get_stations
    # Inputs: netcode, all_stations, channels, minlat, maxlat, minlon, maxlon
    # Outputs: station_inventory
    # Loop to iterate through list of station codes in all_stations
        # for each station_code in all_stations list:
            # get inputs about corresponding station and add to sta_inventory list


# Function: get_events
    # Inputs: stime, etime, central_lat, central_lon, min_radius, max_radius, min_mag
    # Outputs: eq_catalog
    # Call client to get_events:
        # get_events that match inputs and store results in eq_catalog

# Function: Loop processing to extract position of stations
    # Inputs: sta_inventory, network
    # Outputs: st_net, st_lons, st_lats, st_stas, st_start_year
    # Loop through each network and station
        # for each network in sta_inventory list:
            # for each station in network:
                # get outputs for each station and append to correlating attribute lists
                
#%% Create dictionary to store station attribute lists

# Function: Construct a dictionary (stdict) for inputs
    # Inputs: st_net, st_lons, st_lats, st_stas, st_start_year
    # Outputs: stdict       # station attribute dictionary
    # stdict = {[column name(s)]:input(s)}
    
#%% Convert station attribute dictionary to DataFrame

# Function: Convert stdict to a Pandas DataFrame (stdf)
    # Inputs: stdict
    # Outputs: stdf         # station dataframe
    # stdf = pd.DataFrame(stdict)
    
#%% Save DatFrame as CSV station inventory file

# Function: Save stdf in meta_dir as [station_inventory_name] without indexing
    # Inputs: stdf, meta_dir
    # Outputs: [station_inventory_name] CSV file    # Choose station inventory file name to save as
    # stdf.to_csv(meta_dir + [station_inventory_name], index = False)
    
#%% Extract event information

# Initiate attribute lists for event information
    # ev_lons = []      # event longitudes
    # ev_lats = []      # event latitudes
    # ev_depth = []     # event depths
    # ev_origint = []   # event origin times
    # ev_mag = []       # event magnitudes

# %%
def extract_eventinfo_from_catalog(eq_catalog):
    '''
    Extract attributes for each event in eq_catalog and append to respective lists
    
    Parameters
    ----------
    eq_catalog : Obspy earthquake catalog inventory
        Earthquake catalog containing downloaded event information.

    Returns
    -------
    ev_lons :    List with the event longitudes
    ev_lats:     List with the event latitudes
    ev_depth:    List with the event depths, positive down
    ev_origint:  List with the origin time of the event as UTCDateTime objects
    ev_mag:      List with the event magnitudes (ML or M)
    '''
    
    
    # Loop through event in eq_catalog list
        # for each event in eq_catalog:
            # access inputs for each event and append results to respective lists  
    
    return ev_lons, ev_lats, ev_depth, ev_origint, ev_mag

            
#%% Creat dictionary to store event attribute lists

# Function: Construct a dictionary (evdict) for inputs
    # Inputs: ev_lons, ev_lats, ev_depth, ev_mag, ev_origint
    # Outputs: evdict       # event attribute dictionary
    # evdict = {[column name(s)]:input(s)}

#%% Convert event attribute dictionary to DataFrame

# Function: Convert evdict to a Pandas DataFrame (evdict)
    # Inputs: evdict
    # Outputs: evdf         # event dataframe
    # evdf = pd.DataFrame(evdict)

#%% Save DatFrame as CSV event inventory file

# Function: Save evdf in meta_dir as [event_catalog_name] without indexing
    # Inputs: evdf, meta_dir
    # Outputs: [event_catalog_name] CSV file    # Choose event catalog file name to save as
    # evdf.to_csv(meta_dir + [event_catalog_name], index = False)
    

    
#%% Read station inventory CSV file 

# Function: Read the station inventory CSV file into Pandas DataFrame
    # Inputs: meta_dir, [station_inventory_name]    # where station_inventory_name is the file name
    # Outputs: station_inventory_df
    # station_inventory_df = pd.read_csv(meta_dir + [station_inventory_name])
    
#%% Create dictionary to map station names to network codes

# Function: Create a dictionary mapping stName to stNet
    # Inputs: station_inventory_df, stName, stNet
    # Outputs: station_network_map
    # station_network_map = dict(zip(station_inventory_df['stName'], station_inventory_df['stNet']))
    
#%% 
    
    
    
    
    
    
    
    
    
    
    
    
    
    

