Static site generation for Wasatch Photonics devices and software.


### CNAMEs, A-records and branches

    This is a project page, in a repository, owned by an organization.
    Therefore, the live content is in the gh-pages branch.
    The URL is WasatchPhotonics.github.io/DeviceDocumentation

    CNAME has to be in every branch. If you use ghp-import, you have to
    manually add the CNAME file to the branch.

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

### Setup and configuration:

    Clone this repository into:
    ~/projects/DeviceDocumentation

    Clone the pelican-themes repository into:
    ~/projects/pelican-themes
    
    conda create --name pelican_env pelican
    export PATH=~/miniconda2/bin:$PATH
    source activate pelican_env
    pip install pelican
  
    In one window, setup auto-reloader (excepting .conf files)
    pelican --autoreload --theme ../pelican-themes/pelican-bootstrap3/ content
    
    In another window, set the pelican webserver:
    python -m pelican.server


### Push to a github projects page

    pelican --theme ../pelican-themes/pelican-bootstrap3/ content
    git commit -a -m "documenation log message..."
    git push origin gh-pages

### Miscellaneous notes

    ghp-import looks good, sounds good, does what it says.
    It also removes the CNAME file which makes it unusable for
    organizational project pages. The solution adopted here is to do all
    the development in gh-pages directly. This makes sense for this
    project, as it is purely about documentation.


