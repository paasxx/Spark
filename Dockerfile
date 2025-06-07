FROM bitnami/spark:latest

# Variáveis de ambiente
ENV JAVA_HOME=/opt/bitnami/java
ENV PATH="${JAVA_HOME}/bin:$PATH"

# ✅ Define HOME dentro de /opt/bitnami (onde o user 1001 tem permissão)
ENV HOME=/opt/bitnami/sparkuser

# ✅ Cria pasta e dá permissão para o user 1001 (agora dentro de /opt/bitnami)
USER root
RUN mkdir -p /opt/bitnami/sparkuser && chown -R 1001:1001 /opt/bitnami/sparkuser

# ✅ Instala pacotes Python com root
RUN pip install pandas tqdm

# ✅ Cria entrada no /etc/passwd para evitar o erro do whoami
RUN echo "sparkuser:x:1001:1001:sparkuser:/opt/bitnami/sparkuser:/bin/bash" >> /etc/passwd

# Troca pro user 1001
USER 1001

# Copia arquivos da aplicação
COPY --chmod=755 entrypoint.sh /entrypoint.sh
COPY . /app
WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]
