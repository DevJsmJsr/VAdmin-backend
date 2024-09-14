FROM public.ecr.aws/lambda/python:3.11

# Install python module needed for gdal and rasterio
RUN yum update -y && \
    yum install -y gcc python3-devel unzip curl gettext &&\
    yum clean all

# Install poetry https://python-poetry.org/docs/#installing-with-the-official-installer
# IMPORTANT: upgrade poetry periodically
RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.8.2

# Install AWS CLI v2
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf awscliv2.zip aws

# Set up .bashrc
COPY ./.bashrc /root/

# create project directory
RUN mkdir -p /opt/project
WORKDIR /opt/project

COPY ./VAdmin/pyproject.toml .
COPY ./VAdmin/poetry.lock .
RUN /root/.local/bin/poetry install

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod u+x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]