# Multi-Agent 协作代码生成与修复工作流

基于多智能体（Multi-Agent）协作的全自动代码闭环系统。系统包含 Coder、Reviewer 和 Fixer 三个智能体，通过共享状态进行通信，并支持条件循环（发现问题 -> 自动修复 -> 再次审查）。

## 功能特性

- **多 Agent 协作**：CoderAgent（编码）、ReviewerAgent（审查）、FixerAgent（修复）各司其职。
- **状态共享与流转**：通过 `WorkflowState` 传递需求、代码、审查意见和迭代次数。
- **条件循环控制**：审查不通过时触发 Fixer 修复，直到通过或达到最大迭代次数。
- **高度可扩展架构**：基于 `BaseAgent` 抽象类设计，新增 Agent 极其方便。
- **可视化 Web 界面**：使用 Streamlit 构建，提供极简现代风 UI，实时展示状态流转轨迹。

## 快速开始

### 1. 安装依赖
```bash
pip install -r requirements.txt