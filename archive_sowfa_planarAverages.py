#!/usr/bin/env python

import argparse
import pandas as pd
import xarray as xr
from datatools.SOWFA6.postProcessing.averaging import PlanarAverages

def reader(datadir):
    # Read in virtual tower data and convert to pandas DataFrame
    df = PlanarAverages(datadir,varList=['U','T','UU','TU','wUU'],verbose=True).to_pandas()
    
    # Convert time in seconds to datetime
    df.reset_index(inplace=True)
    df['t'] = pd.to_timedelta(df['t'],unit='s') + pd.to_datetime('2013-11-08 00:00')
    
    # Rename columns
    df.columns = ['datetime', 'height', 'u', 'v', 'w', 'theta','uu','uv','uw','vv','vw','ww',
        'utheta','vtheta','wtheta','wuu','wuv','wuw','wvv','wvw','www']
    
    # Set multi-index with levels datetime and height
    df.set_index(['datetime','height'],inplace=True)

    # Convert to xarray
    xa = df.to_xarray()

    # Set metadata
    xa.height.attrs['units'] = "m"
    xa.height.attrs['long_name'] = "height above ground level"
    xa.u.attrs['units'] = "m/s"
    xa.u.attrs['long_name'] = "west-to-east velocity component"
    xa.v.attrs['units'] = "m/s"
    xa.v.attrs['long_name'] = "south-to-north velocity component"
    xa.w.attrs['units'] = "m/s"
    xa.w.attrs['long_name'] = "vertical velocity component"
    xa.theta.attrs['units'] = "K"
    xa.theta.attrs['long_name'] = "potential temperature"
    xa.uu.attrs['units'] = "m**2/s**2"
    xa.uu.attrs['long_name'] = "uu Reynolds stress component"
    xa.uv.attrs['units'] = "m**2/s**2"
    xa.uv.attrs['long_name'] = "uv Reynolds stress component"
    xa.uw.attrs['units'] = "m**2/s**2"
    xa.uw.attrs['long_name'] = "uw Reynolds stress component"
    xa.vv.attrs['units'] = "m**2/s**2"
    xa.vv.attrs['long_name'] = "vv Reynolds stress component"
    xa.vw.attrs['units'] = "m**2/s**2"
    xa.vw.attrs['long_name'] = "vw Reynolds stress component"
    xa.ww.attrs['units'] = "m**2/s**2"
    xa.ww.attrs['long_name'] = "ww Reynolds stress component"
    xa.utheta.attrs['units'] = "K m/s"
    xa.utheta.attrs['long_name'] = "west-to-east component of the turbulent heat flux"
    xa.vtheta.attrs['units'] = "K m/s"
    xa.vtheta.attrs['long_name'] = "south-to-north component of the turbulent heat flux"
    xa.wtheta.attrs['units'] = "K m/s"
    xa.wtheta.attrs['long_name'] = "vertical component of the turbulent heat flux"
    xa.wuu.attrs['units'] = "m**3/s**3"
    xa.wuu.attrs['long_name'] = "wuu triple product"
    xa.wuv.attrs['units'] = "m**3/s**3"
    xa.wuv.attrs['long_name'] = "wuv triple product"
    xa.wuw.attrs['units'] = "m**3/s**3"
    xa.wuw.attrs['long_name'] = "wuw triple product"
    xa.wvv.attrs['units'] = "m**3/s**3"
    xa.wvv.attrs['long_name'] = "wvv triple product"
    xa.wvw.attrs['units'] = "m**3/s**3"
    xa.wvw.attrs['long_name'] = "wvw triple product"
    xa.www.attrs['units'] = "m**3/s**3"
    xa.www.attrs['long_name'] = "www triple product"

    return xa

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('datadir', type=str)
    parser.add_argument('outputfile', type=str)
    args = parser.parse_args()

    xa = reader(args.datadir).to_netcdf(args.outputfile)
