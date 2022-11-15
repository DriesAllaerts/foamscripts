#!/bin/bash

#sourcedir=/projects/mmc/dallaert/profile_assimilation_obs/run.internal.pat.obs.noT/postProcessing
#outputdir=/scratch/dallaert/profile_assimilation_obs/internal.ipa.obs.noT
#archive_all_output.sh $sourcedir $outputdir

#sourcedir=/projects/mmc/dallaert/profile_assimilation_obs/run.internal.pat.wrf/postProcessing
#outputdir=/scratch/dallaert/profile_assimilation_obs/internal.ipa.wrf
#archive_all_output.sh $sourcedir $outputdir

#sourcedir=/projects/mmc/equon/profile_assimilation_obs/run.internal.ipa.obs.allT/postProcessing
#outputdir=/scratch/dallaert/profile_assimilation_obs/internal.ipa.obs.allT
#archive_all_output.sh $sourcedir $outputdir

#sourcedir=/projects/mmc/equon/profile_assimilation_obs/run.internal.ipa.obs.Tassim/postProcessing
#outputdir=/scratch/dallaert/profile_assimilation_obs/internal.ipa.obs.Tassim
#archive_all_output.sh $sourcedir $outputdir

sourcedir=/projects/mmc/equon/profile_assimilation_obs/run.internal.dpa.obs.noT/postProcessing
outputdir=/scratch/dallaert/profile_assimilation_obs/internal.dpa.obs.noT
archive_all_output.sh $sourcedir $outputdir

sourcedir=/projects/mmc/equon/profile_assimilation_obs/run.internal.dpa.obs.Tassim/postProcessing
outputdir=/scratch/dallaert/profile_assimilation_obs/internal.dpa.obs.Tassim
archive_all_output.sh $sourcedir $outputdir

sourcedir=/projects/mmc/equon/profile_assimilation_obs/run.internal.dpa.obs.allT/postProcessing
outputdir=/scratch/dallaert/profile_assimilation_obs/internal.dpa.obs.allT
archive_all_output.sh $sourcedir $outputdir

sourcedir=/projects/mmc/dallaert/profile_assimilation_obs/run.internal.pat.obs.wrfT/postProcessing
outputdir=/scratch/dallaert/profile_assimilation_obs/internal.ipa.obs.wrfT
archive_all_output.sh $sourcedir $outputdir

sourcedir=/projects/mmc/dallaert/profile_assimilation_obs/run.internal.pat.obs.wrfTadv/postProcessing
outputdir=/scratch/dallaert/profile_assimilation_obs/internal.ipa.obs.wrfTadv
archive_all_output.sh $sourcedir $outputdir
