
# 🚀 GPS Data Processing Pipeline com Apache Spark

Este projeto demonstra uma pipeline simples de engenharia de dados utilizando **Apache Spark** para processar dados simulados de GPS. Os dados são gerados com Python (Pandas) e processados com Spark para análises básicas.

---

## 🛠 Tecnologias Utilizadas

- **Python 3**
- **Pandas**
- **Apache Spark 3**
- **Docker + Docker Compose**
- **Bitnami Spark Image**
- **TQDM (barra de progresso)**
- **PySpark**

---

## 📦 Funcionalidades

- Geração de dados sintéticos de localização GPS com `generate_csv.py`:
  - 100 veículos simulados
  - 100.000 registros por veículo
  - Timestamps sequenciais com 1s de intervalo
- Processamento com Spark no `spark_pipeline.py`:
  - Filtro de dados por veículo
  - Cálculo de velocidade média por veículo
  - Salvamento em CSV dos resultados processados

---

## 📂 Estrutura do Projeto

```
.
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
├── generate_csv.py
├── spark_pipeline.py
├── csv_data/
│   └── gps_data.csv (gerado automaticamente)
└── output/
    └── avg_speed/ (resultados em CSV)
```

---

## 🧰 Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## 🚀 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

### 2. Construa a imagem Docker

```bash
docker compose build
```

### 3. Suba o container

```bash
docker compose up
```

Esse comando irá:

- Criar a pasta `/opt/bitnami/sparkuser` para armazenar arquivos temporários usados pelo Spark (configuração interna da imagem).
- Gerar o arquivo `csv_data/gps_data.csv` com 10 milhões de linhas (se ainda não existir).
- Processar esse CSV com Apache Spark.
- Mostrar no terminal:
  - Os dados do veículo `V1`
  - A média de velocidade de todos os veículos
- Salvar o resultado no diretório `output/avg_speed/`.

---

## 🧠 Expertise demonstrada

- Criação de dados sintéticos de larga escala com Python e Pandas
- Uso de PySpark para ETL (Extract, Transform, Load)
- Manipulação de grandes volumes de dados com Spark
- Empacotamento completo do projeto com Docker, respeitando permissões e segurança
- Organização modular de scripts e boas práticas de código
- Conhecimento de containers, volumes e automação com `entrypoint.sh`

---

## 📁 Observações importantes

- A imagem Bitnami Spark usa um usuário não-root com UID 1001 para rodar o Spark, por isso configuramos permissões e diretórios no Dockerfile para evitar erros de permissão.
- A variável de ambiente `HOME` foi redefinida para um caminho dentro de `/opt/bitnami` onde o usuário 1001 tem permissão de escrita. Isso evita erros comuns relacionados a diretórios home inexistentes ou sem permissão.
- O script `entrypoint.sh` automatiza o fluxo dentro do container, gerando o CSV e processando com Spark em sequência.
- O diretório `csv_data/` e `output/avg_speed/` são criados automaticamente e usados para entrada e saída de dados.

---

## 📬 Contato

Em caso de dúvidas ou sugestões, sinta-se à vontade para abrir uma [issue](https://github.com/seu-usuario/seu-repo/issues) ou enviar um pull request.
