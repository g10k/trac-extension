FastCGIExternalServer /var/www/trac-extra/trac-extra.fcgi -host 127.0.0.1:8885

<VirtualHost {{ allowed_host }}:80>
    ServerName trac.extra.soft-way.biz
    DocumentRoot /var/www/trac-extra
    ServerAdmin support@soft-way.biz

    ErrorLog {{ log_path }}/www/error.log
    CustomLog {{ log_path }}/www/access.log common

    Alias /static {{ repo_path }}/djtrac/static
    Alias /npm {{ repo_path }}/djtrac/node_modules

    RewriteEngine On
    RewriteRule ^/(static.*)$ /$1 [QSA,L,PT]
    RewriteRule ^/(npm.*)$ /$1 [QSA,L,PT]
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^/(.*)$ /trac-extra.fcgi/$1 [QSA,L]
</VirtualHost>
