NAME="termServer"                                                     # Name of the application
DJANGODIR=/home/ubuntu/term-deposit-sample                  # Django project directory
SOCKFILE=/home/ubuntu/term-deposit-sample/term/run/gunicorn.sock  # we will communicte using this unix socket
USER=ubuntu                                                         # the user to run as
NUM_WORKERS=3                                                       # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=term.term.settings                            # which settings file should Django use
DJANGO_WSGI_MODULE=term.term.wsgi                                    # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
. /home/ubuntu/term-deposit-sample/server/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec server/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER  \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --access-logfile t \
  --error-logfile /var/log/gunicorn-error.log
  
