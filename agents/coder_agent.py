from agents.base_agent import BaseAgent
from state import WorkflowState
from llm_client import call_llm

class CoderAgent(BaseAgent):
    def __init__(self):
        super().__init__("CoderAgent")

    def run(self, state: WorkflowState) -> WorkflowState:
        state.add_log(self.name, f"开始根据需求生成代码：{state.requirement}")
        
        system_prompt = "你是一名资深 Python 开发工程师。请根据需求编写高质量的 Python 代码。只输出代码，不要任何解释。"
        user_prompt = f"需求：{state.requirement}\n\n请写出代码："
        
        code = call_llm(system_prompt, user_prompt)
        # 清理大模型可能带出来的 markdown 标记
        code = code.replace("```python", "").replace("```", "").strip()
        
        state.current_code = code
        state.add_log(self.name, "初始代码生成完毕。")
        return state