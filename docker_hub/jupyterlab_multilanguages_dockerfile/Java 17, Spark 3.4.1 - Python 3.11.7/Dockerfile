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

# Install Kafka
ARG VERSION_KAFKA_KERNEL=3.6.1
ARG VERSION_KAFKA=kafka_2.13-3.6.1
ARG KAFKA_HOME=/usr/local/kafka

RUN wget https://archive.apache.org/dist/kafka/${VERSION_KAFKA_KERNEL}/${VERSION_KAFKA}.tgz && \
    tar xvf ${VERSION_KAFKA}.tgz && \
    mv ${VERSION_KAFKA} ${KAFKA_HOME} && \
    ln -s ${KAFKA_HOME} /kafka && \
	mkdir -p ${KAFKA_HOME}/data/logs && \
	mkdir -p ${KAFKA_HOME}/data/zookeeper && \
    rm ${VERSION_KAFKA}.tgz

# Install JupyterLab and PySpark
RUN pip install install jupyterlab==4.0.10
RUN pip install jupyterlab-git==0.50.0
RUN pip install pyspark==3.4.1
RUN pip install pandas==1.5.3 
RUN pip install apache-beam[interactive]==2.48.0 
RUN pip install Faker==22.0.0 
RUN pip install itables==1.6.3 
RUN pip install panel==1.3.6
RUN pip install mysql-connector-python==8.2.0
RUN pip install psycopg2==2.9.9
RUN pip install pymongo==4.6.1
RUN pip install dbt-core==1.7.4
RUN pip install dbt-postgres==1.7.4
RUN pip install apache-airflow==2.8.0
RUN pip install pytest==7.4.3
RUN pip install scikit-learn==1.3.2
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
COPY ./jars/*.jar /usr/local/spark/jars
COPY ./airflow_files/*.py ./

# copia archivos kafka
COPY ./kafka_files /*.properties /usr/local/kafka/config

# crea los directorios para los logs de los brokers de kafka
RUN mkdir -p ${KAFKA_HOME}/data/logs/broker_1
RUN mkdir -p ${KAFKA_HOME}/data/logs/broker_2
RUN mkdir -p ${KAFKA_HOME}/data/logs/broker_3
RUN mkdir -p ${KAFKA_HOME}/data/logs/broker_4

# Expose ports for JupyterLab, Spark UI, PANEL, NodeJS, DBT, Airflow, Zookeeper, Brokers Kafka
EXPOSE 8888 4040 5006 3000 8080 8081 9091 9092 9093 9094

# Start Airflow when the container launches
# avoid loading all DAG examples
ENV AIRFLOW__CORE__LOAD_EXAMPLES=False 
RUN airflow db init
RUN airflow users create --role Admin --username admin --email admin@jorgecardona.com --firstname jorge --lastname cardona --password 12345678
RUN rm /usr/local/lib/python3.11/site-packages/airflow/example_dags/example_branch_operator_decorator.py
RUN rm /usr/local/lib/python3.11/site-packages/airflow/example_dags/example_branch_operator.py
RUN mkdir /root/airflow/dags
RUN mv ./dbt_airflow.py /root/airflow/dags

#RUN airflow scheduler
#RUN airflow webserver -p 8081

# Configurar variables de entorno
ENV SPARK_HOME=/usr/local/spark
ENV PATH=$PATH:$SPARK_HOME/bin
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

# Start JupyterLab when the container launches
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--LabApp.token=''"]

# docker run --name jorgecardona-multilanguage --rm -p 8888:8888 -p 4040:4040 -p 5006:5006 -p 3000:3000 -p 8080:8080 -p 8081:8081 -p 9091:9091 -p 9092:9092 -p 9093:9093  -p 9094:9094 jorgecardona/jupyterlabmultilanguagespython3117:latest

# docker build -t jorgecardona/jupyterlabmultilanguagespython3117:latest .
# docker push jorgecardona/jupyterlabmultilanguagespython3117:latest

######################################################################################################################################
########################################################## UTILIDADES ################################################################
######################################################################################################################################
# COPIA ARCHIVOS A LA IMAGEN
#COPY ./mongo-spark-connector_2.13-10.2.1.jar /usr/local/spark/jars
#COPY ./bson-4.11.1.jar /usr/local/spark/jars
#COPY ./mongodb-driver-core-4.11.1.jar /usr/local/spark/jars
#COPY ./mongodb-driver-sync-4.11.1.jar /usr/local/spark/jars
#COPY ./postgresql-42.7.1.jar /usr/local/spark/jars
#COPY ./mysql-connector-j-8.2.0.jar /usr/local/spark/jars
#COPY ./dbt_airflow.py ./
#COPY ./zookeeper.properties /usr/local/kafka/config
#COPY ./server1.properties /usr/local/kafka/config
#COPY ./server2.properties /usr/local/kafka/config
#COPY ./server3.properties /usr/local/kafka/config
#COPY ./server4.properties /usr/local/kafka/config

# Configurar variables de entorno, en la terminal
# export KAFKA_HOME=/usr/local/kafka
# export PATH=$PATH:$KAFKA_HOME/bin
# export PATH=$PATH:$KAFKA_HOME/config
# export SPARK_HOME=/usr/local/spark
# export PATH=$PATH:$SPARK_HOME/bin
# export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
# . ~/.bashrc

# EJECUTAR ZOOKEPER PAAR PODER INICIAR KAFKA
# /usr/local/kafka/bin/zookeeper-server-start.sh /usr/local/kafka/config/zookeeper.properties

# INICIAR BROKERS DE KAFKA
# /usr/local/kafka/bin/kafka-server-start.sh /usr/local/kafka/config/server1.properties
# /usr/local/kafka/bin/kafka-server-start.sh /usr/local/kafka/config/server2.properties
# /usr/local/kafka/bin/kafka-server-start.sh /usr/local/kafka/config/server3.properties
# /usr/local/kafka/bin/kafka-server-start.sh /usr/local/kafka/config/server4.properties

# LISTAR LOS BROKERS DISPONIBLES
# /usr/local/kafka/bin/zookeeper-shell.sh localhost:2181 ls /brokers/ids

# CREAR UN TOPIC
# /usr/local/kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 2 --partitions 3 --topic animals-topic-batch
# /usr/local/kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 2 --partitions 3 --topic animals-topic-streaming


# LISTAR LOS TOPICS
#/usr/local/kafka/bin/kafka-topics.sh --list --bootstrap-server localhost:9092

# ENVIAR UN MENSAJE AL TOPIC
# echo "Mensaje de ejemplo" | /usr/local/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic animals-topic-streaming

# VER TODOS LOS MENSAJES
# /usr/local/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic animals-topic-streaming --from-beginning

# ELIMINA UN TOPIC
# /usr/local/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic animals-topic-batch
# /usr/local/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic animals-topic-streaming

# VER LA VERSION DE KAFKA
#/usr/local/kafka/bin/kafka-topics.sh --version
