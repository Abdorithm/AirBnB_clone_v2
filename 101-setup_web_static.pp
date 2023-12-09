# Installs a Nginx server with custom HTTP header

package { 'nginx':
  ensure    => 'installed',
}

# Create directory structure
file { '/data/web_static/shared/':
  ensure    => 'directory',
}

file { '/data/web_static/releases/test/':
  ensure    => 'directory',
}

# Create HTML content
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => '
<html>
<head>
</head>
<body>
Holberton School
</body>
</html>
',
}

# Create symbolic link
file { '/data/web_static/current/':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
  force  => true,
}

# Change ownership
file { '/data/':
  recurse => true,
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Restart Nginx
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
