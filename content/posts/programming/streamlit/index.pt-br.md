---
title: Streamlit
date: 2024-05-19T08:06:25+06:00
description: Sobre Streamlit
menu:
  sidebar:
    name: Streamlit
    identifier: programming-streamlit
    parent: programming
    weight: 21
author:
  name: Luciana Nobre
  image: /images/author/luciana.png
hero: images/datahub.png
tags: ["Data Lineage","Metadata Management","Data Governance","Data Discovery"]
categories: ["Basic"]
---

## Introdução



## Tópicos

https://github.com/topics/streamlit-deployment

https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app


Uma empresa está utilizando o AWS Glue para seus processos de ETL. Eles precisam garantir que os dados armazenados no AWS Glue Data Catalog estejam criptografados. Qual das seguintes opções deve ser usada para atender a esse requisito?


    A. Ativar a criptografia do lado do servidor com chaves gerenciadas pelo Amazon S3 (SSE-S3) para o AWS Glue Data Catalog.
    B. Usar chaves gerenciadas pelo cliente do AWS Key Management Service (KMS) para a criptografia do AWS Glue Data Catalog.
    C. Implementar a criptografia do lado do cliente antes de armazenar os metadados no AWS Glue Data Catalog.
    D. Aplicar configurações de segurança do AWS Glue para criptografar o tráfego da rede.



Uma empresa precisa armazenar e processar regularmente arquivos de log gerados por sua aplicação. Os logs estão em formato de texto e o processamento envolve operações de busca e filtragem. Qual combinação de serviços da AWS deve ser usada para armazenar e processar esses dados de forma eficiente?


    A. Amazon S3 e AWS Lambda
    B. Amazon EC2 e Amazon EBS
    C. Amazon Glacier e Amazon Redshift
    D. Amazon DynamoDB e AWS Glue



Uma empresa precisa armazenar dados relacionais com altas taxas de transação e requer consistência imediata. Os dados serão utilizados para processamento de transações online (OLTP). Qual serviço da AWS deve ser usado?


    A. Amazon DynamoDB
    B. Amazon RDS
    C. Amazon S3
    D. Amazon Redshift


Sua empresa requer uma solução de armazenamento para dados não estruturados em grande escala que possam ser acessados globalmente com baixa latência. Os dados são acessados com frequência e requerem alta durabilidade. Qual solução de armazenamento da AWS é a mais adequada?


    A. Amazon S3
    B. Amazon RDS
    C. Amazon EBS
    D. Amazon Redshift


Uma plataforma de e-commerce precisa ingerir dados de atividade do usuário de seu site no final de cada dia, processar os dados e, em seguida, carregá-los no Amazon Redshift para análise. Qual combinação de serviços da AWS é a mais apropriada para essa ingestão e processamento de dados em lote?


    A. AWS Glue e Amazon Redshift
    B. Amazon EC2 e AWS Lambda
    C. Amazon S3 e Amazon Kinesis Data Streams
    D. AWS Data Pipeline e Amazon Redshift


Um engenheiro de dados está trabalhando em um projeto que requer a execução de scripts personalizados para processamento de dados. Eles precisam de um serviço que aceite scripts para tarefas como transformação e análise de dados. Qual serviço da AWS eles devem escolher para esse propósito?


    A. Amazon S3
    B. AWS Glue
    C. Amazon Redshift
    D. AWS Lambda

Para impor governança de dados e controle de acesso granular em um data lake armazenado no Amazon S3, permitindo que engenheiros e cientistas de dados tenham acesso seletivo com base em seus papéis, qual serviço da AWS deve ser utilizado principalmente?


    A. Amazon S3 Access Points
    B. AWS Lake Formation
    C. AWS Identity and Access Management (IAM)
    D. Amazon Macie


Em um ambiente de computação distribuída onde um engenheiro de dados precisa processar conjuntos de dados em larga escala usando Apache Spark, qual serviço da AWS oferece um ambiente gerenciado para Spark?


    A. Amazon RDS
    B. Amazon EC2
    C. Amazon EMR
    D. AWS Lambda


Quando projetando um processo de validação de dados para garantir a completude e a precisão dos dados em um trabalho ETL do AWS Glue, qual recurso um engenheiro de dados deve usar para automatizar as verificações de qualidade dos dados?



    A. Glue Workflow
    B. Glue Data Catalog
    C. Glue Job Bookmark
    D. Glue Schema Registry


Em um projeto que requer a otimização de um data warehouse Amazon Redshift para consultas complexas sobre grandes conjuntos de dados, qual recurso o engenheiro de dados deve utilizar para melhorar o desempenho das consultas?


    A. Redshift Concurrency Scaling
    B. Elastic Resize
    C. Materialized Views
    D. Query Editor


Qual serviço da AWS permite que um engenheiro de dados defina e aplique controles de acesso granulares para bancos de dados e tabelas em um ambiente de data lake?


    A. Amazon Macie
    B. AWS Lake Formation
    C. AWS IAM
    D. Amazon Cognito


Para gerenciar requisitos de dados quentes e frios de forma eficiente, permitindo que os dados se movam entre camadas de acesso frequente e armazenamento de longo prazo com base nos padrões de acesso, qual recurso do Amazon S3 deve ser utilizado?


    A. S3 Intelligent-Tiering
    B. S3 One Zone-Infrequent Access
    C. S3 Standard-Infrequent Access
    D. S3 Glacier

Para um pipeline de dados que integra dados de múltiplas fontes no Amazon Redshift, qual serviço ou recurso da AWS deve ser utilizado para lidar com a transformação de dados antes do carregamento?


    A. Amazon Redshift Spectrum
    B. AWS Data Pipeline
    C. Amazon Redshift Stored Procedures
    D. AWS Glue ETL


Uma equipe de analistas de dados frequentemente realiza consultas idênticas em grandes conjuntos de dados armazenados no Amazon S3, utilizando o Athena para análise. Eles notaram que os resultados de suas consultas geralmente permanecem relevantes e inalterados por cerca de 2 horas após a execução. Para otimizar a eficiência das consultas e reduzir custos, a equipe busca um método para evitar varreduras de dados redundantes durante esse período de 2 horas. Qual abordagem devem adotar para atender a essa necessidade, sem a necessidade de mudanças significativas em sua infraestrutura de consulta?


    A. Implementar uma função AWS Lambda personalizada para armazenar e buscar resultados de consultas por um período de 2 horas.
    B. Habilitar o recurso de reutilização de resultados de consultas do Athena e definir a idade máxima para reutilização dos resultados de consultas para 120 minutos.
    C. Configurar o Athena para reutilizar automaticamente os resultados de consultas, confiando na configuração padrão de idade máxima, que é de 120 minutos.
    D. Utilizar políticas de ciclo de vida do Amazon S3 para reter e reutilizar resultados de consultas por 2 horas.



A company is using AWS Glue for their ETL processes. They need to ensure that the data stored in the AWS Glue Data Catalog is encrypted. Which of the following options should be used to meet this requirement?

 
      A. Enable server-side encryption with Amazon S3-managed keys (SSE-S3) for the AWS Glue Data Catalog.
      B. Use AWS Key Management Service (KMS) customer-managed keys for the AWS Glue Data Catalog encryption.
      C. Implement client-side encryption before storing metadata in the AWS Glue Data Catalog.
    Apply AWS Glue security configurations to encrypt network traffic.


A company needs to store and regularly process log files generated by their application. The logs are in text format and the processing involves searching and filtering operations. Which combination of AWS services should be used to efficiently store and process this data?


    A Amazon S3 and AWS Lambda

    B Amazon EC2 and Amazon EBS

    C Amazon Glacier and Amazon Redshift


    D Amazon DynamoDB and AWS Glue


A company needs to store relational data with high transaction rates and requires immediate consistency. The data will be used for online transaction processing (OLTP). Which AWS service should be used?


    A Amazon DynamoDB


    B Amazon RDS

    c Amazon S3

    D Amazon Redshift

Pergunta 14Correto
Your company requires a storage solution for large-scale, unstructured data that can be accessed globally with low latency. The data is frequently accessed and requires high durability. Which AWS storage solution is most suitable?


    A Amazon S3

    B Amazon RDS

    C Amazon EBS

    D Amazon Redshift

Pergunta 15Correto
An e-commerce platform needs to ingest user activity data from its website at the end of each day, process the data, and then load it into Amazon Redshift for analysis. Which AWS service combination is most appropriate for this batch data ingestion and processing?


    A AWS Glue and Amazon Redshift

    B Amazon EC2 and AWS Lambda

    C Amazon S3 and Amazon Kinesis Data Streams

    D AWS Data Pipeline and Amazon Redshift


Pergunta 19
A data engineer is working on a project that requires running custom scripts for data processing. They need a service that accepts scripting for tasks like data transformation and analysis. Which AWS service should they choose for this purpose?

    A Amazon S3


    B AWS Glue

    C Amazon Redshift

    D AWS Lambda



Pergunta 2
To enforce data governance and fine-grained access control on a data lake stored in Amazon S3, allowing data engineers and scientists selective access based on their roles, which AWS service should be primarily utilized?

    Amazon S3 Access Points
    AWS Lake Formation
    AWS Identity and Access Management (IAM)
    Amazon Macie



Pergunta 4
In a distributed computing environment where a data engineer needs to process large-scale datasets using Apache Spark, which AWS service offers a managed Spark environment?

    Amazon RDS
    Amazon EC2
    Amazon EMR
    AWS Lambda


Pergunta 10

When designing a data validation process to ensure data completeness and accuracy in an AWS Glue ETL job, which feature should a data engineer use to automate data quality checks?

    Glue Workflow
    Glue Data Catalog
    Glue Job Bookmark
    Glue Schema Registry



Pergunta 12

In a project requiring the optimization of an Amazon Redshift data warehouse for complex queries over large datasets, which feature should the data engineer utilize to improve query performance?

    Redshift Concurrency Scaling
    Elastic Resize
    Materialized Views
    Query Editor



Pergunta 13
Which AWS service enables a data engineer to define and enforce fine-grained access controls for databases and tables in a data lake environment?

    Amazon Macie
    AWS Lake Formation
    AWS IAM
    Amazon Cognito



Pergunta 4
For managing hot and cold data requirements efficiently, allowing data to move between frequent access and long-term storage tiers based on access patterns, which Amazon S3 feature should be utilized?

    S3 Intelligent-Tiering
    S3 One Zone-Infrequent Access
    S3 Standard-Infrequent Access
    S3 Glacier



Pergunta 9

For a data pipeline that integrates data from multiple sources into Amazon Redshift, which AWS service or feature should be utilized to handle data transformation before loading?

    Amazon Redshift Spectrum

    AWS Data Pipeline

    Amazon Redshift Stored Procedures
    AWS Glue ETL



Pergunta 25
A team of data analysts frequently conducts identical queries on large datasets stored in Amazon S3, using Athena for analysis. They've noticed that their query results typically remain relevant and unchanged for about 2 hours after execution. To optimize query efficiency and reduce costs, the team seeks a method to avoid redundant data scans for this 2-hour period.
What approach should they adopt to meet this requirement without the need for significant changes to their query infrastructure?

    Implement a custom AWS Lambda function to store and fetch query results for a period of 2 hours.

    Enable Athena's query result reuse feature and set the maximum age for reusing query results to 120 minutes


    Configure Athena to automatically reuse query results, relying on the default maximum age setting, which is 120 minutes.


    Utilize Amazon S3 lifecycle policies to retain and reuse query results for 2 hours.


