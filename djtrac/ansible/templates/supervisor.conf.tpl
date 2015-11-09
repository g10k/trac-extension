[program:trac_extra_webserver]
directory = {{ repo_path }}
user = trac_extra
command = {{ virtualenv_python }} {{ repo_path }}/djtrac/manage.py runfcgi method=prefork minspare=2 maxspare=3 host=127.0.0.1 port=8885 daemonize=false
stdout_logfile = /var/log/trac_extra.log
stderr_logfile = /var/log/trac_extra.log

[program:trac_extra_send_milestone_changes]
directory = {{ repo_path }}
user = trac_extra
command = {{ virtualenv_python }} {{ repo_path }}/djtrac/manage.py send_milestone_changes --infinity
stdout_logfile = /var/log/trac_extra_send_milestone_changes.log
stderr_logfile = /var/log/trac_extra_send_milestone_changes.log

