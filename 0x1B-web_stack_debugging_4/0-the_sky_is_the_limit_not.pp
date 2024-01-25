# fix nginx to accept and serve more requests

file { 'fix-for-nginx':
  ensure  => 'file',
  path    => '/etc/default/nginx',
  content => inline_template('<%= File.read("/etc/default/nginx").gsub(/15/, "4096") %>'),
}
exec {'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/',
}
