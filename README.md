# dashboard

## install fish shell
sudo apt-get install fish
chsh -s /usr//bin/fish

## install miniconda
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
echo ". /home/<user>/miniconda3/etc/profile.d/conda.sh" >> ~/.bashrc
echo "conda activate" >> ~/.bashrc
bash ~/miniconda.sh -b -p $HOME/miniconda
[optional] conda init fish
[optional] conda update conda

## uninstall miniconda
rm -rf ~/miniconda
[optional] remove from ~/.bashrc
[optional] rm -rf ~/.condarc ~/.conda ~/.continuum

## conda bashrc and PATH
echo ". /home/<user>/miniconda3/etc/profile.d/conda.sh" >> ~/.bashrc export environment to yml

echo "conda activate" >> ~/.bashrc

## export environment to yml
conda env export --no-builds | grep -v "^prefix: " > webserver.yml

## create environment from yml
conda env create -f webserver.yml
