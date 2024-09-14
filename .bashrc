export PS1="\[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ "
export PATH="$PATH:/root/.local/bin/"

# ALIASES

# testing
alias test="poetry run python manage.py test --parallel auto --keepdb"
alias retest="poetry run python manage.py test --parallel auto"

# migrations
alias makemigrations="poetry run python manage.py makemigrations"
alias migrate="poetry run python manage.py migrate"

# poetry virtual shell
alias shell="poetry shell"