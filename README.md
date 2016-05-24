Static site generation for Wasatch Photonics devices and software.


### Setup and configuration:

Clone this repository into:
~/projects/DeviceDocumentation

Clone the pelican-themes repository into:
~/projects/pelican-themes

conda create --name pelican_env pelican
export PATH=~/miniconda2/bin:$PATH
source activate pelican_env
pip install pelican
pip install ghp-import

In one window, setup auto-reloader (excepting .conf files)
pelican --autoreload --theme ../pelican-themes/pelican-bootstrap3/ content

In another window, set the pelican webserver:
python -m pelican.server

