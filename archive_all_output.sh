#!/bin/bash

sourcedir=$1
outputdir=$2

echo Processing probe data
echo ---------------------
echo $sourcedir
for probe in $(ls $sourcedir | egrep '^probe[0-9]$');
do
    echo Processing $probe
    if [ ! -f "$outputdir/$probe.nc" ]; then
        echo Converting data in $probe to netcdf
        archive_sowfa_probe.py $sourcedir/$probe $outputdir/$probe.nc
    fi
done

echo Processing planar average data
echo ------------------------------
if [ ! -f "$outputdir/planarAverages.nc" ]; then
    echo Converting data in planarAverages to netcdf
    archive_sowfa_planarAverages.py $sourcedir/planarAverages $outputdir/planarAverages.nc
fi

echo Processing source history data
echo ------------------------------
if [ ! -f "$outputdir/sourceHistory.nc" ]; then
    echo Converting data in sourceHistory to netcdf
    archive_sowfa_sourceHistory.py $sourcedir/sourceHistory $outputdir/sourceHistory.nc
fi

#echo Processing sliceDataInstantaneous
#echo ---------------------------------
##if [ ! -d "$outputdir/sliceDataInstantaneous" ]; then
#    echo Copying sliceDataIntantaneous files from src to dest
#    copy_vtk_series.py $sourcedir/sliceDataInstantaneous/ $outputdir/sliceDataInstantaneous
##fi
