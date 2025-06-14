# Apicallingcrew Crew

Welcome to the Apicallingcrew Crew project,. This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. The goal of this project is to make you familiar with the world of agentic AI. This project will you to setup your first crew so that they can make an API call and analyse the request and response sent and received by the client .

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:

```bash
crewai install
```

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/apicallingcrew/config/agents.yaml` to define your agents
- Modify `src/apicallingcrew/config/tasks.yaml` to define your tasks
- Modify `src/apicallingcrew/crew.py` to add your own logic, tools and specific args
- Modify `src/apicallingcrew/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the apiCallingCrew Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The apiCallingCrew Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

Let's create wonders together with the power and simplicity of crewAI.
