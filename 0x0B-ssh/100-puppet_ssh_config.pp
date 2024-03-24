#create ssh config file
#configuration must be configured to use the private key ~/.ssh/school
#configuration must be configured to refuse to authenticate using a password
$home_directory = $facts['home']

file_line { 'Disable password authentication':
  ensure => 'present',
  path   => "${home_directory}/.ssh/config",
  line   => '    PasswordAuthentication no',
}

file_line { 'Specify identity file':
  ensure => 'present',
  path   => "${home_directory}/.ssh/config",
  line   => '    IdentityFile ~/.ssh/school',
}
