# dashboardi

## export environment to yml
conda env export | grep -v "^prefix: " > webserver.yml

## create environment from yml
conda env create -f webserver.yml
