from agents.base_agent import BaseAgent
from state import WorkflowState
from llm_client import call_llm

class FixerAgent(BaseAgent):
    def __init__(self):
        super().__init__("FixerAgent")

    def run(self, state: WorkflowState) -> WorkflowState:
        state.add_log(self.name, "收到审查意见，开始修复代码...")
        
        system_prompt = "你是一名资深 Python 开发工程师。请根据审查意见，修复代码中的问题。只输出修复后的完整代码，不要解释。"
        user_prompt = f"当前代码：\n{state.current_code}\n\n审查意见：\n{state.review_feedback}\n\n请输出修复后的代码："
        
        code = call_llm(system_prompt, user_prompt)
        code = code.replace("```python", "").replace("```", "").strip()
        
        state.current_code = code
        state.iteration_count += 1
        state.add_log(self.name, f"第 {state.iteration_count} 次修复完成。")
        return state