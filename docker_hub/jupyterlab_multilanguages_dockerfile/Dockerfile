# Base image
FROM python:3.11.4

# etiqueta creador de la imagen
LABEL maintainer="Jorge Cardona"


ARG VERSION_JAVA=openjdk-17-jdk
# Install OpenJDK 17
RUN apt-get update && apt-get install -y ${VERSION_JAVA}

	
ARG VERSION_SCALA=2.13.6
# Download and install Scala
RUN curl -O https://downloads.lightbend.com/scala/2.13.6/scala-2.13.6.tgz && \
    tar -xzf scala-2.13.6.tgz && \
    mv scala-2.13.6 /usr/local/share/scala && \
    ln -s /usr/local/share/scala/bin/scala /usr/local/bin/scala && \
    ln -s /usr/local/share/scala/bin/scalac /usr/local/bin/scalac && \
    rm scala-2.13.6.tgz
	

# Instala lenguaje R
RUN apt-get install r-base -y

# Instala R Jupyter Kernel
RUN echo 'install.packages(c("IRkernel"),repos="http://cran.us.r-project.org", dependencies=TRUE)' > /tmp/packages.R && Rscript /tmp/packages.R


# actualiza los repositorios para instalar NODEJS
RUN apt-get update

# INSTALA NODEJS y NPM
RUN apt-get install nodejs npm -y

# instala el paquete de nodejs para ejecutar aplicaciones que necesiten de la maquina virtual de nodejs
RUN npm install -g ijavascript 

	
ARG VERSION_SPARK_HADOOP=spark-3.4.0-bin-hadoop3-scala2.13

RUN wget https://downloads.apache.org/spark/spark-3.4.0/spark-3.4.0-bin-hadoop3-scala2.13.tgz && \
    tar xvf spark-3.4.0-bin-hadoop3-scala2.13.tgz && \
    mv spark-3.4.0-bin-hadoop3-scala2.13 /usr/local/spark && \
    ln -s /usr/local/spark /spark && \
    rm spark-3.4.0-bin-hadoop3-scala2.13.tgz
	
	
# Install JupyterLab and PySpark
RUN pip install jupyterlab==3.6.4
RUN pip install jupyterlab-git==0.41.0 
RUN pip install pyspark==3.4.0 
RUN pip install pandas==1.5.3 
RUN pip install apache-beam[interactive]==2.48.0 
RUN pip install Faker==18.11.1 
RUN pip install itables==1.5.3 
RUN pip install panel==1.1.1

ARG VERSION_JAVA_KERNEL=1.3.0
# Install kernel for Java in JupyterLab
RUN wget https://github.com/SpencerPark/IJava/releases/download/v1.3.0/ijava-${VERSION_JAVA_KERNEL}.zip && \
    unzip ijava-${VERSION_JAVA_KERNEL}.zip && \
    python3 install.py --sys-prefix && \
    rm ijava-${VERSION_JAVA_KERNEL}.zip
	
# Instala R kernel
RUN echo 'IRkernel::installspec()' > /tmp/temp.R && Rscript /tmp/temp.R

# Instala Kotlin kernel
RUN pip install kotlin-jupyter-kernel	
	
# Instala el kernel de JavaScript en Jupyter Notebook
RUN ijsinstall # jernel javaScript

# Instala el kernel de Scala en Jupyter Notebook
RUN curl -Lo coursier https://git.io/coursier-cli
RUN chmod +x coursier
RUN ./coursier launch --fork almond -- --install
RUN rm -f coursier

# Configurar variables de entorno
ENV SPARK_HOME=/usr/local/spark
ENV PATH=$PATH:$SPARK_HOME/bin
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64


# Set the working directory
WORKDIR /notebooks

# Expose ports for JupyterLab, Spark UI, PANEL, NodeJS
EXPOSE 8888 4040 5006 3000

# Start JupyterLab when the container launches
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--LabApp.token=''"]

# docker run --name labmultilanguage --rm -p 8888:8888 -p 4040:4040 -p 5006:5006 -p 3000:3000 jorgecardona/jupyterlabmultilanguages:v1

# docker build -t jorgecardona/jupyterlabmultilanguages:v1 .
# docker push jorgecardona/jupyterlabmultilanguages:v1