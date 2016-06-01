Static site generation for Wasatch Photonics devices and software.


### Setup and configuration:

    Clone this repository into:
    ~/projects/DeviceDocumentation
    
    Clone the wasatch pelican-themes fork into:
    git clone https://github.com/WasatchPhotonics/pelican-themes ~/projects/pelican-themes

    conda create --name pelican_env pip
    export PATH=~/miniconda2/bin:$PATH
    source activate pelican_env
    pip install pelican MarkDown ghp-import
    
    In one window, setup auto-reloader (excepting .conf files)
    source activate pelican_env
    cd ~/projects/DeviceDocumentation/
    pelican --autoreload --theme ../pelican-themes/wasatch-bootstrap3/ content
    
    In another window, set the pelican webserver:
    source activate pelican_env
    cd ~/projects/DeviceDocumentation/output
    python -m pelican.server
    
    Then in a web browser on the local machine, go to:
    http://localhost:8000



### CNAMEs, A-records and branches

    This is a project page, in a repository, owned by an organization.
    Therefore, the live content is in the gh-pages branch.
    The URL is WasatchPhotonics.github.io/DeviceDocumentation

    CNAME has to be in every branch. If you use ghp-import, you have to
    make sure the pelican configuration writes the CNAME file to the
    root of the gh-pages branch. The content of the CNAME file should
    be: devices.waspho.com

    The parent domain (for testing), is waspho.com.
    This content should appear at: devices.waspho.com
    The waspho.com domain is managed by hostway. Follow the instructions
    here:
    https://help.github.com/articles/troubleshooting-custom-domains/

    Create two A records that point to the github IP addresses:

    dig devices.waspho.com +nostats +nocmd +nocomments
    ; <<>> DiG 9.10.3-P4-RedHat-9.10.3-13.P4.fc23 <<>>
    devices.waspho.com +nostats +nocmd +nocomments
    ;; global options: +cmd
    ;devices.waspho.com.            IN      A
    devices.waspho.com.     14034   IN      A       192.30.252.154
    devices.waspho.com.     14034   IN      A       192.30.252.153

    When it's time to convert to production, the steps should be:
    add the github IP addresses to A records for wasatchphotonics.com
    change CNAME to from devices.waspho.com to
    devices.wasatchphotonics.com

    That's it, now devices.wasatchphotonics.com should point to this
    github gh-pages branch of the DeviceDocumentation repository.


### Push to a github projects page

    pelican --theme ../pelican-themes/wasatch-bootstrap3/ content
    git commit -a -m "documentation log message..."
    git push origin master

    ghp-import -p output
    (Checkout gh-pages, copy the content from master, save the output in
    the root of the gh-pages branch, upload to github)

    This way you stay in master, make all your changes, preview locally.
    When you are ready to go live, ghp-import is all you need.

