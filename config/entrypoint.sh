#!/bin/sh

python manage.py collectstatic --no-input

# auto create admin user
# echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@alsoapp.com', 'zhiming')" | python manage.py shell

exec "$@"
# 文件编码必须是unix; set ff=unix
