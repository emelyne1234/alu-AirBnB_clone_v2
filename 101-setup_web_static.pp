#!/usr/bin/python3
"""using puppet"""

#installing nginx if not there
package { 'installing nginx':
  ensure   => 'present',
  provider => 'apt'
} ->

#creating said directories
file { '/data':
  ensure  => 'directory'
} ->

file { '/data/web_static':
  ensure => 'directory'
} ->


file { '/data/web_static/releases':
  ensure => 'directory'
} ->

file { '/data/web_static/releases/test':
  ensure => 'directory'
} ->

#creating html file and testing it
file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "Gorgeous Emelyne\n"
} ->

file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page\n"
} ->

#setting up configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => nginx_confifuration
} ->

#restarting nginx
exec {restart nginx':
  path => '/etc/init.d/'
}
