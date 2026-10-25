from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class WorkflowState:
    requirement: str = ""           # 用户的初始需求
    current_code: str = ""          # 当前流转的代码
    review_feedback: str = ""       # 审查 Agent 的意见
    is_passed: bool = False         # 审查是否通过
    iteration_count: int = 0        # 当前迭代（修复）次数
    max_iterations: int = 2         # 最大允许修复次数
    history_logs: List[Dict] = field(default_factory=list)  # 执行日志

    def add_log(self, agent_name: str, message: str):
        self.history_logs.append({
            "agent": agent_name,
            "iteration": self.iteration_count,
            "message": message
        })