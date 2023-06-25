### How to use a Python env

Se por acaso ainda não tiver o pacote instalado, utilize o seguinte comando:

```python
pip install virtualenv
```

Logo após a instalação, no diretório do projeto python, execute:

```python
python -m venv env
```

Ative sua env:

  - In windows
    ```bash
    env/Scripts/activate.bat
    ```

  - In macOS/Linux
    ```bash
    source myenv/bin/activate
    ```

Instale os requesitos do projeto:

```bash
pip install -r requirements.txt
```

Para sair da env, basta usar o seguinte comando:

```bash
deactivate
```

## Instalar o Docker:

- **Instalação do Docker no Windows:**

  - Acesse o site oficial do Docker para Windows: https://www.docker.com/products/docker-desktop
  - Clique no botão "Download" para baixar o instalador do Docker para Windows.
  - Execute o instalador baixado e siga as instruções do assistente de instalação. Durante o processo de instalação, você pode ser solicitado a habilitar a virtualização do hardware em seu sistema.

  Após a conclusão da instalação, o Docker será iniciado automaticamente. Aguarde até que o ícone do Docker na bandeja do sistema indique que o Docker está em execução.

  Verifique a instalação do Docker executando o comando ```docker version``` em um terminal. Isso exibirá a versão do Docker instalada e confirmará que a instalação foi bem-sucedida.
  Verifique se o Docker não está instalado executando o comando docker version. Se não estiver instalado, siga as instruções apropriadas para o seu sistema operacional e instale o Docker.

- **Instalação do Docker no Linux:**

  - Abra um terminal no Linux. Execute os seguintes comandos, um por vez, para instalar o Docker:

    ```bash
    sudo apt update
    sudo apt install docker.io
    ```

  - Após a conclusão da instalação, inicie o serviço Docker executando o seguinte comando:

    ```bash
    sudo systemctl start docker
    ```

  - Adicione seu usuário ao grupo "docker" para que você possa executar comandos Docker sem precisar de privilégios de superusuário. Execute o seguinte comando:

    ```bash
    sudo usermod -aG docker $USER
    ```

  - Faça logout e login novamente para aplicar as alterações de grupo. Verifique a instalação do Docker executando o comando ```docker version``` em um terminal. Isso exibirá a versão do Docker instalada e confirmará que a instalação foi bem-sucedida.
  Instalar o k3d:

### Instalação do K3D
  O k3d é uma ferramenta para criar clusters Kubernetes em Docker. Para instalá-lo, siga as instruções apropriadas para o seu sistema operacional, disponíveis na documentação oficial do k3d: https://k3d.io/#installation.

- **Instalação do k3d no windows**
    - Abra um terminal do PowerShell ou do CMD e execute o seguinte comando para baixar o executável do k3d:
        ```bash
        curl -LO https://github.com/rancher/k3d/releases/latest/download/k3d-windows-amd64.exe
        ```

    - Renomeie o arquivo baixado para ```k3d.exe```
        ```bash
        ren k3d-windows-amd64.exe k3d.exe
        ```

    - Mova o arquivo ```k3d.exe``` para um diretório incluído no seu PATH de sistema, como ```C:\Windows``` ou ```C:\Windows\System32```.

    - Verifique a instalação do k3d executando o comando ```k3d version``` em um terminal. Isso exibirá a versão do k3d instalada e confirmará que a instalação foi bem-sucedida.

- **Instalação do k3d no Linux:**

    - Execute os seguintes comandos para baixar e instalar o k3d:
        ```bash
        curl -s https://raw.githubusercontent.com/rancher/k3d/main/install.sh | bash
        ```

    - Verifique a instalação do k3d executando o comando ```k3d version``` em um terminal. Isso exibirá a versão do k3d instalada e confirmará que a instalação foi bem-sucedida.

### Instalação do kubectl
O kubectl é uma ferramenta de linha de comando utilizada para interagir com o Kubernetes, um sistema de orquestração de contêineres amplamente utilizado. O Kubernetes é usado para gerenciar e coordenar aplicativos em contêineres em um ambiente de nuvem ou em um cluster local. O kubectl permite que os usuários executem várias operações no Kubernetes, como criar, atualizar e excluir recursos, implantar aplicativos, verificar o status dos pods e serviços, além de acessar e gerenciar logs e execuções de comandos dentro dos contêineres em execução.

- **Instalação do kubectl no Windows:**

    - Abra um navegador da web e acesse o seguinte link: https://dl.k8s.io/release/v1.26.0/bin/windows/amd64/kubectl.exe

    - Faça o download do arquivo ```kubectl.exe``` clicando com o botão direito do mouse no link e selecionando "Salvar link como". Escolha um local no seu sistema para salvar o arquivo.

    - Mova o arquivo ```kubectl.exe``` para um diretório incluído no seu PATH de sistema, como ```C:\Windows``` ou ```C:\Windows\System32```.

    - Abra um terminal do PowerShell ou do CMD.

    - Verifique a instalação do ```kubectl``` executando o comando ```kubectl version --client``` em um terminal. Isso exibirá a versão do ```kubectl``` instalada e confirmará que a instalação foi bem-sucedida.

    - Caso tenha dificuldade com a instalação, recomendo este conteúdo [Kubernetes Getting Started on Windows for beginners](https://www.youtube.com/watch?v=8h4FoWK7tIA)

- **Instalação do kubectl no Linux:**

    - Execute os seguintes comandos para baixar o kubectl e torná-lo executável:
        ```bash
        curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
        chmod +x kubectl
        ```

    - Mova o arquivo ```kubectl``` para um diretório incluído no seu PATH de sistema, como ```/usr/local/bin```:
        ```bash
        sudo mv kubectl /usr/local/bin
        ```

    - Verifique a instalação do `kubectl` executando o comando `kubectl version --client` em um terminal. Isso exibirá a versão do `kubectl` instalada e confirmará que a instalação foi bem-sucedida.

### Instalação do Helm
O Helm é uma ferramenta de gerenciamento de pacotes para Kubernetes. Ela permite que você defina, instale e atualize facilmente aplicativos complexos em um cluster Kubernetes. O Helm simplifica o processo de implantação de aplicativos em contêineres, fornecendo uma maneira de agrupar todos os recursos necessários, como pods, serviços, configurações e políticas, em um único pacote chamado "chart".

- **Instalação do Helm no Windows:**

    - Abra um navegador da web e acesse o seguinte link: https://get.helm.sh/helm-v3.7.0-windows-amd64.zip

    - Faça o download do arquivo ```helm-v3.7.0-windows-amd64.zip``` clicando no link. Escolha um local no seu sistema para salvar o arquivo.

    - Extraia o conteúdo do arquivo ZIP para um diretório de sua escolha.

    - Abra um terminal do PowerShell ou do CMD.

    - Navegue até o diretório onde você extraiu o arquivo ZIP do Helm.

    - Verifique se a instalação do Helm foi bem-sucedida executando o comando ```helm version``` em um terminal. Isso exibirá a versão do Helm instalada e confirmará que a instalação foi concluída com êxito.

- **Instalação do Helm no Linux:**

    - Execute os seguintes comandos para baixar e instalar o Helm:

        ```bash
        curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
        ```

    - Verifique se a instalação do Helm foi bem-sucedida executando o comando ```helm version``` em um terminal. Isso exibirá a versão do Helm instalada e confirmará que a instalação foi concluída com êxito.

### Criar um cluster Kubernetes com o k3d:

- Execute o seguinte comando para criar um cluster Kubernetes com o k3d:

    ```bash
    k3d cluster create --config k3d-simple-cluster.yaml
    ```

- Você terá um log parecido com isso:

    ```bash
    INFO[0000] Using config file k3d-simple-cluster.yaml (k3d.io/v1alpha2#simple) 
    WARN[0000] Default config apiVersion is 'k3d.io/v1alpha4', but you're using 'k3d.io/v1alpha2': consider migrating.
    INFO[0000] portmapping '80:80' targets the loadbalancer: defaulting to [servers:**:proxy agents:**:proxy]
    INFO[0000] Prep: Network
    INFO[0000] Created network 'k3d-my-cluster'
    INFO[0000] Created image volume k3d-my-cluster-images
    INFO[0000] Starting new tools node...
    INFO[0001] Starting Node 'k3d-my-cluster-tools'
    INFO[0001] Creating node 'k3d-my-cluster-server-0'
    INFO[0003] Creating node 'k3d-my-cluster-agent-0'
    INFO[0003] Creating node 'k3d-my-cluster-agent-1'
    INFO[0005] Creating node 'k3d-my-cluster-agent-2'
    INFO[0005] Creating LoadBalancer 'k3d-my-cluster-serverlb'
    INFO[0005] Using the k3d-tools node to gather environment information
    INFO[0007] Starting new tools node...
    INFO[0007] Starting Node 'k3d-my-cluster-tools'
    INFO[0009] Starting cluster 'my-cluster'
    INFO[0009] Starting servers...
    INFO[0009] Starting Node 'k3d-my-cluster-server-0'
    INFO[0015] Starting agents...
    INFO[0015] Starting Node 'k3d-my-cluster-agent-1'
    INFO[0015] Starting Node 'k3d-my-cluster-agent-0'
    INFO[0015] Starting Node 'k3d-my-cluster-agent-2'
    INFO[0027] Starting helpers...
    INFO[0027] Starting Node 'k3d-my-cluster-serverlb'      
    INFO[0038] Injecting records for hostAliases (incl. host.k3d.internal) and for 6 network members into CoreDNS configmap...
    INFO[0051] Cluster 'my-cluster' created successfully!   
    INFO[0051] You can now use it like this:
    kubectl cluster-info
    ```


    # Dockerizing an Apache Spark Standalone Cluster

### Check the article here:  <a href="https://medium.com/geekculture/dockerizing-an-apache-spark-standalone-cluster-eeb7d3f8efeb">Dockerizing an Apache Spark Standalone Cluster</a>

## Small Big Data ecosystem with In-Memory Processing

The aim of this repository is to show you the use of docker as a powerful tool to deploy applications that communicate with each other in a fast and stable way. In this case I present a small ecosystem of big data for in-memory processing, the ecosystem is based in different docker containers, it was considered to add Apache Hive and Hue as needed applications in a simple big data ecosystem with Apache Spark, this project will help you go directly to writing scala or pyspark code and get hands-on experience and not worry about the installation and implementation of the infrastructure, the installed applications and the reason for each one them are detailed below.

# Docker containers architecture
![architecture](https://user-images.githubusercontent.com/8701464/127952650-c71d6374-3cb0-40fc-8df5-01ffda530081.png)

## Apache Spark 
Apache Spark itself does not supply storage or any Resource Management. It is just a unified framework for in memory processing large amount of data near to real time.
checking the docker-compose.yml file you can see the detailed docker images for spark

- spark-master (wittline/spark-master:3.0.0)
- spark-worker-1 (wittline/spark-worker:3.0.0)
- spark-worker-2 (wittline/spark-worker:3.0.0)
 
you can check the details about the docker image here: <a  href="https://hub.docker.com/u/wittline"> wittline</a>

### What is a standalone cluster?
There are different ways to run an Apache Spark application: Local Mode, Standalone mode, Yarn, Kubernetes and Mesos, these are the way how Apache spark assigns resources to its drivers and executors, the last three mentioned are cluster managers, everything is based on who is the master node, let's see the table below:

![stdmode](https://user-images.githubusercontent.com/8701464/128092104-12c8c50c-992c-45d9-ba5e-27e47ab2af34.png)

The table above shows that one way to recognize a standalone configuration is by observing who is the master node, a standalone configuration can only run applications for apache spark and submit spark applications directly to the master node.

## JupyterLab
The pyspark code will be written using jupyter notebooks, we will submit the code to the standalone cluster using the SparkSession
checking the docker-compose.yml file you can see the detailed docker images for spark

- jupyterlab (wittline/jupyterlab:3.0.0-spark-3.0.0)

you can check the details about the docker image here: <a  href="https://hub.docker.com/u/wittline"> wittline</a>

## Hive
Apache Spark manages all the complexities of create and manage global and session-scoped views and SQL managed and unmanaged tables, in memory and disk, and SparkSQL is one the main components of Apache Spark, integrating relational procesing with spark functional programming. Apache Spark by default uses the Apache Hive metastore, located at user/hive/warehouse, to persist all the metadata about the tables created. Apache Spark does not need Hive, the idea of adding hive to this architecture is to have a metadata storage about tables and views that can be reused in a workload and thus avoid the use of re-creating queries for these tables. For example: A global temporary view is visible accross multiple SparkSessions, in this case we can conbine data from different SparkSessions that do not share the same hive metastore. Hive data warehouse facilitates reading, writing, and managing large datasets on HDFS storage using SQL

- hive-server (fjardim/fjardim/hive)
- hive-metastore (wittline/fjardim/hive)
- hive-metastore-postgresql (wittline/spark-worker:3.0.0)

you can check the details about the docker image here: <a href="https://hub.docker.com/u/fjardim">fjardim</a>


## Namenode and datanodes (HDFS)
The Namenode is the master node which persist metadata in HDFS and the datanode is the slave node which store the data. When you insert data or create objects into Hive tables, data will be stored in HDFS on Hadoop DataNodes and the NameNode will keep the tracking of which DataNode has the data.

- namenode (fjardim/namenode_sqoop)
- datanode1 (fjardim/datanode)
- datanode2 (fjardim/datanode)

you can check the details about the docker image here: <a href="https://hub.docker.com/u/fjardim">fjardim</a>

## Hue

Hue is an open source SQL Assistant for Databases & Data Warehouses, It is not necessary for a big data ecosystem, but it can help you visualize data in HDFS faster, and other notable features.

- namenode (fjardim/hue)
- database(fjardim/mysql)

you can check the details about the docker image here: <a href="https://hub.docker.com/u/fjardim">fjardim</a>

## How to run the docker environment
- Install Docker Desktop on Windows, it will install Docker Compose as well, Docker Compose will allow you to run multiple container applications
Install git-bash for windows, once installed , open git bash and download the below repository, this will download all the files needed.

``` 
ramse@DESKTOP-K6K6E5A MINGW64 /c
$ git clone https://github.com/Wittline/apache-spark-docker.git
```

- once inside the folder use the below comman, this will install all the images from the docker-compose file and will setup all the containers, This will take some time.

```
ramse@DESKTOP-K6K6E5A MINGW64 /c/apache-spark-docker/docker
$ winpty docker-compose up -d
```

- When everything is finished, you will see the name of all the containers with the status done
- Now go to jupyterlab, using the url: http://localhost:8889/, this will open a new tab, enjoy writing your pyspark code.
- Go to Hue using the url: http://localhost:8888/, and check your tables in HDFS

## Contributing and Feedback
Any ideas or feedback about this repository?. Help me to improve it.


## License
This project is licensed under the terms of the Apache License.
