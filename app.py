import streamlit as st
from workflow import CodeWorkflow
from state import WorkflowState

# ==========================================
# 1. 页面基础配置
# ==========================================
st.set_page_config(
    page_title="Mammut Workflow",
    page_icon="◼️",
    layout="wide",
    initial_sidebar_state="collapsed" 
)

# ==========================================
# 2. 注入高度定制的现代 Design Studio 风格 CSS
# ==========================================
st.markdown("""
<style>
    /* 引入极简无衬线字体 */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;900&display=swap');

    /* 全局背景：暖灰/米白色 */
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, sans-serif;
    }
    .stApp {
        background-color: #F2F1EC; 
        color: #111111;
    }

    /* 隐藏 Streamlit 默认元素 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* 顶部小胶囊 */
    .top-pill {
        display: inline-block;
        padding: 6px 14px;
        border: 1px solid #D1D5DB;
        border-radius: 30px;
        font-size: 0.8rem;
        font-weight: 500;
        color: #374151;
        margin-bottom: 2rem;
        background: transparent;
    }

    /* 主标题 */
    .hero-title {
        font-size: 5.5rem;
        font-weight: 900;
        line-height: 1.05;
        letter-spacing: -0.04em;
        color: #000000;
        text-align: center;
        margin-bottom: 1.5rem;
    }
    
    /* 副标题 */
    .hero-subtitle {
        font-size: 1.15rem;
        color: #6B7280;
        text-align: center;
        max-width: 600px;
        margin: 0 auto 4rem auto;
        line-height: 1.6;
    }

    /* 表单区白色卡片 */
    [data-testid="stForm"] {
        background-color: #FFFFFF;
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03);
        border: 1px solid #EAEAEA;
    }

    /* 输入框美化 */
    .stTextArea textarea {
        background: #F9FAFB !important;
        color: #111 !important;
        border: 1px solid #E5E7EB !important;
        border-radius: 12px !important;
        padding: 15px !important;
        font-size: 1rem !important;
        transition: all 0.2s ease;
    }
    .stTextArea textarea:focus {
        border-color: #111 !important;
        background: #FFFFFF !important;
    }

    /* 序号标签 */
    .input-label {
        font-size: 1.1rem;
        font-weight: 700;
        color: #111;
        margin-bottom: 1rem;
    }

    /* 按钮：纯黑极简 */
    .stButton>button {
        background-color: #111111;
        color: #FFFFFF;
        border: none;
        border-radius: 30px;
        padding: 0.8rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #333333;
        transform: scale(1.02);
    }

    /* 执行轨迹时间线卡片 */
    .timeline-card {
        background-color: #FFFFFF;
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.03);
        border-left: 6px solid #E5E7EB;
    }
    .timeline-card.coder { border-left-color: #3B82F6; }    /* 蓝 */
    .timeline-card.reviewer { border-left-color: #F59E0B; } /* 黄 */
    .timeline-card.fixer { border-left-color: #10B981; }    /* 绿 */
    .timeline-card.system { border-left-color: #111111; }   /* 黑 */
    
    .timeline-header {
        font-size: 0.9rem;
        font-weight: 700;
        color: #6B7280;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
    }
    .timeline-body {
        font-size: 1rem;
        color: #111111;
        line-height: 1.5;
    }

    /* 底部巨型水印文字 */
    .footer-massive {
        font-size: 10vw;
        font-weight: 900;
        color: #E5E5E5;
        text-align: center;
        line-height: 0.8;
        margin-top: 5rem;
        margin-bottom: -2rem;
        user-select: none;
        letter-spacing: -0.05em;
        pointer-events: none;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. 界面排版
# ==========================================
st.markdown("""
<div style="text-align: center; padding-top: 5rem;">
    <div class="top-pill">Multi-Agent System</div>
    <div class="hero-title">Built to code &<br>designed to fix</div>
    <div class="hero-subtitle">
        全自动代码生成与修复闭环。Coder 编写，Reviewer 审查，Fixer 修复，直到完美交付。
    </div>
</div>
""", unsafe_allow_html=True)

# 限制主内容宽度并居中
col1, col2, col3 = st.columns([1, 6, 1])

with col2:
    # 输入区
    with st.container():
        st.markdown('<div class="input-label">(01) 请输入你的开发需求</div>', unsafe_allow_html=True)
        
        with st.form("workflow_form"):
            req = st.text_area(
                "需求描述", 
                height=120, 
                value="写一个 Python 函数，接收两个参数 a 和 b，返回 a 除以 b 的结果。", 
                label_visibility="collapsed"
            )
            submitted = st.form_submit_button("🚀 启动 Agent 协作")

    if submitted:
        if not req.strip():
            st.warning("请输入需求！")
        else:
            workflow = CodeWorkflow()
            state = WorkflowState(requirement=req, max_iterations=2)
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<div class="input-label">(02) 执行日志与状态流转</div>', unsafe_allow_html=True)
            
            # 1. 编码
            with st.status("CoderAgent 正在编写代码...", expanded=True) as status:
                state = workflow.coder.run(state)
                st.code(state.current_code, language="python")
                status.update(label="CoderAgent 编码完成", state="complete", expanded=False)
                
            # 2. 循环：审查 -> 修复
            while not state.is_passed and state.iteration_count < state.max_iterations:
                with st.status(f"ReviewerAgent 正在进行第 {state.iteration_count + 1} 轮审查...", expanded=True) as status:
                    state = workflow.reviewer.run(state)
                    st.markdown(state.review_feedback)
                    if state.is_passed:
                        status.update(label="ReviewerAgent 审查通过！", state="complete", expanded=False)
                    else:
                        status.update(label="ReviewerAgent 发现问题，需要修复", state="error", expanded=False)
                
                if state.is_passed:
                    break
                    
                with st.status(f"FixerAgent 正在进行第 {state.iteration_count + 1} 次修复...", expanded=True) as status:
                    state = workflow.fixer.run(state)
                    st.code(state.current_code, language="python")
                    status.update(label=f"FixerAgent 修复完成（已迭代 {state.iteration_count} 次）", state="complete", expanded=False)

            # 3. 结束
            st.markdown("<br>", unsafe_allow_html=True)
            if state.is_passed:
                st.success("🎉 工作流结束：代码最终通过审查！")
            else:
                st.warning("⚠️ 工作流结束：达到最大修复次数，仍未通过。")
                
            st.markdown('<div class="input-label">(03) 最终交付代码</div>', unsafe_allow_html=True)
            st.code(state.current_code, language="python")
            
            st.markdown('<div class="input-label">(04) 执行轨迹</div>', unsafe_allow_html=True)
            
            for log in state.history_logs:
                agent_name = log['agent']
                iteration = log['iteration']
                message = log['message']
                
                card_class = "system"
                icon = "✨"
                if "Coder" in agent_name:
                    card_class = "coder"
                    icon = "💻"
                elif "Reviewer" in agent_name:
                    card_class = "reviewer"
                    icon = "🔍"
                elif "Fixer" in agent_name:
                    card_class = "fixer"
                    icon = "🔧"
                
                st.markdown(f"""
                <div class="timeline-card {card_class}">
                    <div class="timeline-header">{icon} {agent_name} (迭代 {iteration})</div>
                    <div class="timeline-body">{message}</div>
                </div>
                """, unsafe_allow_html=True)

# 底部巨型水印
st.markdown('<div class="footer-massive">CodeFlow</div>', unsafe_allow_html=True)