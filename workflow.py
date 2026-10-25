from state import WorkflowState
from agents.coder_agent import CoderAgent
from agents.reviewer_agent import ReviewerAgent
from agents.fixer_agent import FixerAgent

class CodeWorkflow:
    def __init__(self):
        self.coder = CoderAgent()
        self.reviewer = ReviewerAgent()
        self.fixer = FixerAgent()

    def run(self, requirement: str) -> WorkflowState:
        """执行整个工作流"""
        state = WorkflowState(requirement=requirement)
        
        # 1. 编码 Agent 出场
        state = self.coder.run(state)
        
        # 2. 进入循环：审查 -> 修复（这就是高级流程控制）
        while not state.is_passed and state.iteration_count < state.max_iterations:
            # 审查
            state = self.reviewer.run(state)
            
            # 如果审查不通过，且还没到达最大迭代次数，就召唤修复 Agent
            if not state.is_passed and state.iteration_count < state.max_iterations:
                state = self.fixer.run(state)
            else:
                break
                
        # 3. 收尾
        if state.is_passed:
            state.add_log("Workflow", "🎉 工作流结束：代码通过审查！")
        else:
            state.add_log("Workflow", "⚠️ 工作流结束：达到最大修复次数，仍未通过。")
            
        return state