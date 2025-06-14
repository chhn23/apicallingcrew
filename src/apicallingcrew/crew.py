from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class Apicallingcrew():
    """Apicallingcrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def apiCaller(self) -> Agent:
        return Agent(
            config=self.agents_config['apiCaller'], # type: ignore[index]
            verbose=True
        )

    @agent
    def analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['analyst'], # type: ignore[index]
            verbose=True
        )

    @task
    def apiCall(self) -> Task:
        return Task(
            config=self.tasks_config['apiCall'], # type: ignore[index]
        )

    @task
    def analysis(self) -> Task:
        return Task(
            config=self.tasks_config['analysis'], # type: ignore[index]
        )    



    @crew
    def crew(self) -> Crew:
        """Creates the Apicallingcrew crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
