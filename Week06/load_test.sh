npm install -g artillery

artillery quick --count 10 -n 20 http://localhost:3001/courses

# ulimit -n 4096 # just in case if you need it

artillery run --output sync-flask-report.json sync-flask-config.yml
artillery report sync-flask-report.json

artillery run --output async-fastapi-report.json async-fastapi-config.yml
artillery report async-fastapi-report.json

artillery run --output async-fastapi-pg-report.json async-fastapi-pg-config.yml
artillery report async-fastapi-pg-report.json
