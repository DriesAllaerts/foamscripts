#!/usr/bin/env python

import argparse
import pandas as pd
import xarray as xr
from datatools.SOWFA6.postProcessing.sourceHistory import SourceHistory

def reader(datadir,includeT=False):
    # Read in source history data and convert to pandas DataFrame
    varList = ['Momentum',]
    if includeT: varList.append('Temperature')
    df = SourceHistory(datadir,varList=varList,verbose=False).to_pandas()
    
    # Convert time in seconds to datetime
    df.reset_index(inplace=True)
    df['t'] = pd.to_timedelta(df['t'],unit='s') + pd.to_datetime('2013-11-08 00:00')
    
    # Rename columns
    column_names = ['datetime', 'height', 'Fx', 'Fy', 'Fz']
    if includeT: column_names.append('Ftheta')
    df.columns = column_names
    
    # Set multi-index with levels datetime and height
    df.set_index(['datetime','height'],inplace=True)

    # Convert to xarray
    xa = df.to_xarray()

    # Set metadata
    xa.height.attrs['units'] = "m"
    xa.height.attrs['long_name'] = "height above ground level"
    xa.Fx.attrs['units'] = "m/s**2"
    xa.Fx.attrs['long_name'] = "Large-scale forcing in the west-to-east direction"
    xa.Fy.attrs['units'] = "m/s**2"
    xa.Fy.attrs['long_name'] = "Large-scale forcing in the south-to-north direction"
    xa.Fz.attrs['units'] = "m/s**2"
    xa.Fz.attrs['long_name'] = "Large-scale forcing in the vertical direction"
    if includeT:
        xa.Ftheta.attrs['units'] = "K/s"
        xa.Ftheta.attrs['long_name'] = "Large-scale potential temperature forcing"

    return xa

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('datadir', type=str)
    parser.add_argument('outputfile', type=str)
    args = parser.parse_args()

    xa = reader(args.datadir).to_netcdf(args.outputfile)
