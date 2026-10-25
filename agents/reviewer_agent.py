from agents.base_agent import BaseAgent
from state import WorkflowState
from llm_client import call_llm

class ReviewerAgent(BaseAgent):
    def __init__(self):
        super().__init__("ReviewerAgent")

    def run(self, state: WorkflowState) -> WorkflowState:
        state.add_log(self.name, "开始审查代码...")
        
        system_prompt = """你是一名务实的代码审查专家。
请审查以下代码，重点检查是否会导致程序崩溃的 Bug（如除零、越界等）。
不要过度设计，如果代码已经解决了核心的崩溃问题，就让它通过。
最后必须输出一行结论：如果没有致命的运行时错误，输出 [PASS]；如果有，输出 [FAIL]。"""
        
        user_prompt = f"待审查代码：\n```python\n{state.current_code}\n```\n\n请给出审查报告："
        
        feedback = call_llm(system_prompt, user_prompt)
        state.review_feedback = feedback
        
        if "[PASS]" in feedback:
            state.is_passed = True
            state.add_log(self.name, "审查通过！未发现严重问题。")
        else:
            state.is_passed = False
            state.add_log(self.name, "审查未通过，发现潜在问题，需修复。")
            
        return state