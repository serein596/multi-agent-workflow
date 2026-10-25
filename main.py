from workflow import CodeWorkflow

if __name__ == "__main__":
    print("=== 多 Agent 协作代码生成与修复工作流 ===")
    req = input("请输入你的代码需求（例如：写一个除法函数，要求处理除零异常）：\n")
    
    workflow = CodeWorkflow()
    final_state = workflow.run(req)
    
    print("\n" + "="*50)
    print(f"最终代码：\n{final_state.current_code}")
    print("\n" + "="*50)
    print(f"流转日志：")
    for log in final_state.history_logs:
        print(f"[迭代 {log['iteration']}] {log['agent']}: {log['message']}")