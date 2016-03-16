from charms.reactive import when_not, set_state
from charmhelpers import fetch
import subprocess


@when_not('fluentd.installed')
def install_fluentd():

    # Add apt source for fluentd, using the source/key in config.yaml
    fetch.configure_sources()
    fetch.apt_update()

    # Install ruby, fluentd
    packages = ['ruby', 'td-agent']
    fetch.apt_install(fetch.filter_installed_packages(packages))

    # Configure fluentd

    set_state('fluentd.installed')
