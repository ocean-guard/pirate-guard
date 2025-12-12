# Pirate Guard

[Ocean Guard][1] is a MLES that aims to detect anomalies in the maritime domain.

[Pirate Guard][2] is a simplified implementation of Ocean Guard which tries to demonstrate the software architecture practices demonstrated in the paper titled "Reusability in MLOps: Leveraging Ports and Adapters to Build a Microservices Architecture for the Maritime Domain".

- For more information about the system applications, please refer to
  [README.md](README.md).
- For more information about the developer setup, please refer to
  [CONTRIBUTING.md](CONTRIBUTING.md).


## Environment

To execute Pirate Guard in a system-agnostic way, please install [docker][3].
We also use [GNU Make][4] as an automation tool.

> Docker is a set of platform as a service (PaaS) products that use OS-level
> virtualization to deliver software in packages called containers.
>
> — **__Wikipedia__**

To generate the docker images, run the following commands:

| Command            | Description                                   |
|--------------------|-----------------------------------------------|
| `make build-dev`   | Create a development image (with live-reload) |
| `make build-prod`  | Create a production image (for deploy)        |

## Deploy

Ocean Guard uses [GitHub Actions][5] to automatically generate
docker images from any commits in the `main` git branch.

Check the directory `.github/workflows` for more details.

## PostgreSQL

Ocean Guard uses [PostgreSQL][6] with the [PostGIS][7] extension
as its database, in particular to implement its **data warehouse**.
Moreover, Ocean Guard uses [Alembic][8] to manage database migrations.

> PostGIS extends the capabilities of the PostgreSQL relational database
> by adding support for storing, indexing, and querying geospatial data.
>
> — **__PostGIS documentation__**

### Execution

To manage the postgresql service, run the following commands:

| Command           | Description                    |
|-------------------|--------------------------------|
| `make db-start`   | Start the postgresql service   |
| `make db-stop`    | Stop the postgresql service    |
| `make db-restart` | Restart the postgresql service |

### Utilities

To execute useful postgresql tasks, run the following commands:

| Command                   | Parameters             | Description                                         |
|---------------------------|------------------------|-----------------------------------------------------|
| `make db-cli`             |                        | Execute commands with postgresql console            |
| `make db-create-user`     | `USERNAME`, `PASSWORD` | Create user `USERNAME` with password `PASSWORD`     |
| `make db-remove-user`     | `USERNAME`             | Remove user `USERNAME`                              |
| `make db-create-database` | `USERNAME`, `DATABASE` | Create database `DATABASE` owned by user `USERNAME` |
| `make db-remove-database` | `DATABASE`             | Remove database `DATABASE`                          |

### Migrations

To manage migrations, start the database and run the following commands:

| Command                                     | Description                                      |
|---------------------------------------------|--------------------------------------------------|
| `make db-upgrade`                           | Execute all migrations                           |
| `make db-upgrade REVISION=<migration-id>`   | Execute all migrations until a specific revision |
| `make db-downgrade`                         | Revert all migrations                            |
| `make db-downgrade REVISION=<migration-id>` | Revert all migrations until a specific revision  |

## MinIO

Ocean Guard uses [MinIO][9] for large object storage,
in particular to implement its **data lake**.

> MinIO is a high-performance, S3-compatible object storage solution
> released under the GNU AGPL v3.0 license. Designed for speed
> and scalability, it powers AI/ML, analytics, and data-intensive
> workloads with industry-leading performance.
>
> — **__MinIO documentation__**

### Execution

To manage the minio service, run the following commands:

| Command              | Description               |
|----------------------|---------------------------|
| `make minio-start`   | Start the minio service   |
| `make minio-stop`    | Stop the minio service    |
| `make minio-restart` | Restart the minio service |

### Utilities

To execute useful minio tasks, run the following commands:

| Command                        | Parameters          | Description                                            |
|--------------------------------|---------------------|--------------------------------------------------------|
| `make minio-cli`               |                     | Execute commands with minio console                    |
| `make minio-register-server`   | `SERVER`, `ADDRESS` | Register address `ADDRESS` under server alias `SERVER` |
| `make minio-unregister-server` | `SERVER`            | Unregister server alias `SERVER`                       |
| `make minio-create-bucket`     | `SERVER`, `BUCKET`  | Create new bucket `BUCKET` in server alias `SERVER`    |
| `make minio-remove-bucket`     | `SERVER`, `BUCKET`  | Remove bucket `BUCKET` in server alias `SERVER`        |

## Kafka

Ocean Guard uses [Kafka][10] for near-real-time messaging,
in particular to implement its **model prediction**.

> Apache Kafka is an open-source distributed event streaming platform
> used by thousands of companies for high-performance data pipelines,
> streaming analytics, data integration, and mission-critical applications.
>
> — **__Kafka documentation__**

### Execution

To manage the kafka service, run the following commands:

| Command              | Description               |
|----------------------|---------------------------|
| `make kafka-start`   | Start the kafka service   |
| `make kafka-stop`    | Stop the kafka service    |
| `make kafka-restart` | Restart the kafka service |

### Utilities

To execute useful kafka tasks, run the following commands:

| Command                             | Parameters | Description                                           |
|-------------------------------------|------------|-------------------------------------------------------|
| `make kafka-create-topic`           | `TOPIC`    | Create topic named `TOPIC`                            |
| `make kafka-count-messages`         | `TOPIC`    | Count messages on topic `TOPIC`                       |
| `make kafka-produce`                | `TOPIC`    | Produces messages on topic `TOPIC`                    |
| `make kafka-consume`                | `TOPIC`    | Consumes messages on topic `TOPIC` from the execution |
| `make kafka-consume-from-beginning` | `TOPIC`    | Consumes messages on topic `TOPIC` from the beginning |

## MLFlow

Ocean Guard uses [MLFlow][11] for model registry and tracking.

> MLFlow is an open-source platform, purpose-built to assist machine learning
> practitioners and teams in handling the complexities of the machine learning
> process. MLFlow focuses on the full lifecycle for machine learning projects,
> ensuring that each phase is manageable, traceable, and reproducible.
>
> — **__MLFlow documentation__**

### Execution

To manage the mlflow service, run the following commands:

| Command               | Description                |
|-----------------------|----------------------------|
| `make mlflow-start`   | Start the mlflow service   |
| `make mlflow-stop`    | Stop the mlflow service    |
| `make mlflow-restart` | Restart the mlflow service |

### Utilities

To execute useful mlflow tasks, run the following commands:

| Command                      | Description                                     |
|------------------------------|-------------------------------------------------|
| `make mlflow-setup-db`       | Create user and database for mlflow             |
| `make mlflow-teardown-db`    | Remove user and database for mlflow             |
| `make mlflow-setup-minio`    | Register server and create bucket for minio     |
| `make mlflow-teardown-minio` | Unregister server and remove bucket for minio   |
| `make mlflow-setup`          | Run all the `setup` commands                    |
| `make mlflow-teardown`       | Run all the `teardown` commands                 |


[1]: https://github.com/ocean-guard/
[2]: https://github.com/ocean-guard/pirate-guard
[3]: https://docs.docker.com
[4]: https://www.gnu.org/software/make/
[5]: https://github.com/features/actions
[6]: https://www.postgresql.org/docs/
[7]: https://postgis.net/documentation/
[8]: https://alembic.sqlalchemy.org/
[9]: https://github.com/minio/minio
[10]: https://kafka.apache.org/
[11]: https://mlflow.org/
