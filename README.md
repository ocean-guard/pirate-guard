# Pirate Guard

[Ocean Guard][1] is a MLES that aims to detect anomalies in the maritime domain.

[Pirate Guard][2] is a simplified implementation of Ocean Guard which tries to demonstrate the software architecture practices demonstrated in the paper titled "Reusability in MLOps: Leveraging Ports and Adapters to Build a Microservices Architecture for the Maritime Domain".

- For more information about the developer setup, please refer to
  [CONTRIBUTING.md](CONTRIBUTING.md).
- For more information about the system infrastructure, please refer to
  [INFRASTRUCTURE.md](INFRASTRUCTURE.md).

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

## API

The Ocean Guard API uses [FastAPI][5] as the main library to build an HTTP API.

> FastAPI is a modern, fast, high-performance, web framework for building APIs
> with Python based on standard Python type hints.
>
> — **__FastAPI documentation__**

To manage the API, run the following commands:

| Command            | Description             |
|--------------------|-------------------------|
| `make api-start`   | Start the API service   |
| `make api-stop`    | Stop the API service    |
| `make api-restart` | Restart the API service |

## Anomaly Detectors

Ocean Guard uses _anomaly detectors_ to run different anomaly detection machine
learning models:

> In data analysis, anomaly detection is generally understood to be
> the identification of rare items, events, or observations which deviate
> significantly from the majority of the data and do not conform to a well
> defined notion of normal behaviour.
>
> — **__Wikipedia__**

### Ship Anomaly Detector
This anomaly detector performs predictions on ships to determine if the ship is performing any abnormal activities.

## Data Loaders

Ocean Guard uses _data loaders_ to gather different data types inside its
database, creating a **data warehouse**:

> Data Warehouses are central repositories of data integrated from disparate
> sources. They store current and historical data organized in a way that is
> optimized for data analysis, generation of reports, and developing insights
> across the integrated data.
>
> — **__Wikipedia__**

### Ship Data Loader

This data loader gathers ship data in CSV format into the database.

To execute it, run the following commands:

| Command                                | Description                         |
|----------------------------------------|-------------------------------------|
| `make ship-csv-data-loader-start`   | Start the Ship CSV data loader   |
| `make ship-csv-data-loader-stop`    | Stop the Ship CSV data loader    |
| `make ship-csv-data-loader-restart` | Restart the Ship CSV data loader |

## Data Ingestors

Ocean Guard uses _data ingestors_ to ingest data from different sources into
the object storage, creating a **data lake**:

> A data lake is usually a single store of data including raw copies
> of source system data, sensor data, social data etc., and transformed
> data used for tasks such as reporting, visualization, advanced analytics,
> and machine learning.
>
> — **__Wikipedia__**

### Ship Data Ingestor

This data ingestor ingests Ship data from an example stream into the object storage.

To execute it, run the following commands:

| Command                                 | Description                          |
|-----------------------------------------|--------------------------------------|
| `make ship-stream-data-ingestor-start`   | Start the Ship Stream data ingestor   |
| `make ship-stream-data-ingestor-stop`    | Stop the Ship Stream data ingestor    |
| `make ship-stream-data-ingestor-restart` | Restart the Ship Stream data ingestor |


[1]: https://github.com/ocean-guard/
[2]: https://github.com/pirate-guard/
[3]: https://docs.docker.com
[4]: https://www.gnu.org/software/make/
[5]: https://fastapi.tiangolo.com/
