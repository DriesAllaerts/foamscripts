#!/bin/bash

simulations=(
    internal.ipa.obs.noT
    internal.ipa.obs.Tassim
    internal.ipa.obs.allT
    internal.dpa.obs.noT
    internal.dpa.obs.Tassim
    internal.dpa.obs.allT
    internal.ipa.obs.wrfT
    internal.ipa.obs.wrfTadv
    internal.ipa.wrf
)

datadir=/scratch/dallaert/profile_assimilation_obs

for i in "${simulations[@]}"
do
    if [ ! -f "$datadir/$i/probe1_10min.nc" ]; then
        echo Processing $datadir/$i/probe1.nc
        probe_raw2stats.py $datadir/$i/probe1.nc $datadir/$i/probe1_10min.nc
    else
        echo File $datadir/$i/probe1_10min.nc already exists, skipping file.
    fi
done
