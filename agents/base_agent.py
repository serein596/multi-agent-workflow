from abc import ABC, abstractmethod
from state import WorkflowState

class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def run(self, state: WorkflowState) -> WorkflowState:
        """执行 Agent 逻辑，修改并返回状态"""
        pass