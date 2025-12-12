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

## Dependencies

Ocean Guard is built in [Python][5] `3.13`. It uses [uv][6] for dependency
installation and management.

To download the dependencies locally, run:
```bash
uv sync
```
`uv` will install all dependencies locally in the directory `.venv`.

To manage dependencies using [uv][6], run the following commands:

| Command                          | Description                    |
|----------------------------------|--------------------------------|
| `uv add <dependency-name>`       | Add new production dependency  |
| `uv add --dev <dependency-name>` | Add new development dependency |

## Development

We recommend using [PyCharm][7] as the integrated development environment (IDE).
The project contains configurations to make it easier to execute.

To set up [PyCharm][7] on **Linux** to use these dependencies:
1. Access `Settings` (top-left corner)
2. Select `Python` then `Interpreter` (left sidebar)
3. Select `Add Interpreter` then `Add Local Interpreter` (right-side dropdown)
4. Select the options `Generate new` (environment) and `uv` (type)
5. If a red box appears, click `Override existing environment`
6. Click `OK`

To set up [PyCharm][7] on **Windows** to use these dependencies:
1. Access `Remote Development > WSL`
2. Open the project in WSL Projects
3. Follow the instructions described for **Linux**

If you have already installed the dependencies locally, [Pycharm][7] will
synchronise the environment, making them accessible via the IDE.

## Linting

The project uses [ruff][8] for code analysis and formatting.

| Command       | Description                  |
|---------------|------------------------------|
| `make check`  | Check the code using `ruff`  |
| `make format` | Format the code using `ruff` |

## Testing

The project uses [PyCharm][7] [HTTP Client][9] for end-to-end testing,
which can be run via the IDE or in the command line.

To test the API, run the following commands:

| Command               | Description                  |
|-----------------------|------------------------------|
| `make api-e2e-tests`  | Run the API end-to-end tests |


[1]: https://github.com/ocean-guard/
[2]: https://github.com/ocean-guard/pirate-guard
[3]: https://docs.docker.com
[4]: https://www.gnu.org/software/make/
[5]: https://www.python.org/
[6]: https://docs.astral.sh/uv/
[7]: https://www.jetbrains.com/pycharm
[8]: https://docs.astral.sh/ruff/formatter/
[9]: https://www.jetbrains.com/help/pycharm/http-client-in-product-code-editor.html
