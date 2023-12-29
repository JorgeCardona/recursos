# Base image
FROM python:3.11.7

# etiqueta creador de la imagen
LABEL maintainer="Jorge Cardona"

# Instala Java
ARG VERSION_JAVA=openjdk-17-jdk
# Install OpenJDK 17
RUN apt-get update && apt-get install -y ${VERSION_JAVA}

# Download and install Scala
ARG VERSION_SCALA=2.13.10
ARG VERSION_SCALA_KERNEL=scala-${VERSION_SCALA}
RUN curl -O https://downloads.lightbend.com/scala/${VERSION_SCALA}/${VERSION_SCALA_KERNEL}.tgz && \
    tar -xzf ${VERSION_SCALA_KERNEL}.tgz && \
    mv ${VERSION_SCALA_KERNEL} /usr/local/share/scala && \
    ln -s /usr/local/share/scala/bin/scala /usr/local/bin/scala && \
    ln -s /usr/local/share/scala/bin/scalac /usr/local/bin/scalac && \
    rm ${VERSION_SCALA_KERNEL}.tgz
	
# Instala lenguaje R
RUN apt-get install r-base -y

# Instala IRkernel usando los paquetes de R
#RUN echo 'install.packages(c("IRkernel"), repos="http://cran.us.r-project.org", dependencies=TRUE)' > /tmp/packages.R && Rscript /tmp/packages.R
RUN echo "install.packages(c('IRkernel'), repos='http://cran.rstudio.com/', dependencies=TRUE)"  > /tmp/packages.R && Rscript /tmp/packages.R

# actualiza los repositorios para instalar NODEJS
RUN apt-get update

# INSTALA NODEJS y NPM
RUN apt-get install nodejs npm -y

# instala el paquete de nodejs para ejecutar aplicaciones que necesiten de la maquina virtual de nodejs
RUN npm install -g ijavascript 

# Install Spark
ARG VERSION_SPARK_KERNEL=spark-3.4.1
ARG VERSION_SCALA_KERNEL_SPARK=scala2.13
ARG VERSION_SPARK_HADOOP=${VERSION_SPARK_KERNEL}-bin-hadoop3-${VERSION_SCALA_KERNEL_SPARK}
RUN wget https://archive.apache.org/dist/spark/${VERSION_SPARK_KERNEL}/${VERSION_SPARK_HADOOP}.tgz && \
    tar xvf ${VERSION_SPARK_HADOOP}.tgz && \
    mv ${VERSION_SPARK_HADOOP} /usr/local/spark && \
    ln -s /usr/local/spark /spark && \
    rm ${VERSION_SPARK_HADOOP}.tgz

# Install JupyterLab and PySpark
RUN pip install install jupyterlab==4.0.9
RUN pip install jupyterlab-git==0.50.0
RUN pip install pyspark==3.4.1
RUN pip install pandas==1.5.3 
RUN pip install apache-beam[interactive]==2.48.0 
RUN pip install Faker==21.0.0 
RUN pip install itables==1.6.3 
RUN pip install panel==1.3.5
RUN pip install mysql-connector-python==8.2.0
RUN pip install psycopg2==2.9.9
RUN pip install pymongo==4.6.1
RUN pip install dbt-core==1.7.4
RUN pip install dbt-postgres==1.7.4
RUN pip install apache-airflow==2.8.0
RUN pip install pytest==7.4.3
RUN pip install --upgrade pip

ARG VERSION_JAVA_KERNEL=1.3.0
# Install kernel for Java in JupyterLab
RUN wget https://github.com/SpencerPark/IJava/releases/download/v1.3.0/ijava-${VERSION_JAVA_KERNEL}.zip && \
    unzip ijava-${VERSION_JAVA_KERNEL}.zip && \
    python3 install.py --sys-prefix && \
    rm ijava-${VERSION_JAVA_KERNEL}.zip
	
# Instala el kernel de R en JupyterLab
RUN echo 'IRkernel::installspec()' > /tmp/temp.R && Rscript /tmp/temp.R

# Instala el kernel de Kotlin en JupyterLab
RUN pip install kotlin-jupyter-kernel	
	
# Instala el kernel de JavaScript en JupyterLab
RUN ijsinstall # jernel javaScript

# Instala el kernel de Scala en Jupyter Notebook
# https://almond.sh/docs/quick-start-install
RUN curl -Lo coursier https://git.io/coursier-cli
RUN chmod +x coursier
RUN ./coursier launch --fork almond -- --install
RUN rm -f coursier

# Set the working directory
WORKDIR /notebooks

# COPIA LOS CONECTORES DE MONGO, POSTGRES Y MySQL para usar con SPARK
COPY ./mongo-spark-connector_2.13-10.2.1.jar /usr/local/spark/jars
COPY ./bson-4.11.1.jar /usr/local/spark/jars
COPY ./mongodb-driver-core-4.11.1.jar /usr/local/spark/jars
COPY ./mongodb-driver-sync-4.11.1.jar /usr/local/spark/jars
COPY ./postgresql-42.7.1.jar /usr/local/spark/jars
COPY ./mysql-connector-j-8.2.0.jar /usr/local/spark/jars

# Configurar variables de entorno
ENV SPARK_HOME=/usr/local/spark
ENV PATH=$PATH:$SPARK_HOME/bin
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

# Expose ports for JupyterLab, Spark UI, PANEL, NodeJS, DBT, Airflow
EXPOSE 8888 4040 5006 3000 8080 8081

# Start Airflow when the container launches
RUN airflow db init
RUN airflow users create --role Admin --username admin --email admin@jorgecardona.com --firstname jorge --lastname cardona --password 12345678
#RUN airflow webserver -p 8081
#RUN airflow scheduler

# Start JupyterLab when the container launches
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--LabApp.token=''"]

# docker run --name jorgecardona-multilanguage --rm -p 8888:8888 -p 4040:4040 -p 5006:5006 -p 3000:3000 -p 8080:8080 -p 8081:8081 jorgecardona/jupyterlabmultilanguagespython3117:v1

# docker build -t jorgecardona/jupyterlabmultilanguagespython3117:v1 .
# docker push jorgecardona/jupyterlabmultilanguagespython3117:v1