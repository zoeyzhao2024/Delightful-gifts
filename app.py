import streamlit as st
import random

# 设置页面标题
st.set_page_config(page_title="❤️ 专属情侣抽奖机", layout="centered")

st.title("🎁 我们的专属抽奖时间")
st.write("规则：选择你的档位，由命运（随机算法）决定奖品！")

# 1. 初始化奖品池（如果缓存中没有，则设置默认值）
if 'prizes' not in st.session_state:
    st.session_state.prizes = {
        "100元档": ["买束小花", "请喝奶茶", "清空购物车一件小物", "洗碗券一张"],
        "300元档": ["双人电影+大餐", "一套睡衣", "新款游戏/手办", "给TA买件衣服"],
        "500元档": ["周末近郊游", "星级自助餐", "护肤品套装", "情侣对戒"],
        "1000元档": ["周边短途旅行", "心仪已久的电子产品", "高级餐厅Date Night", "大牌香水"],
        "终极档 (Love+)": ["清空整个购物车", "国内双人游", "实现一个对方的愿望", "神秘奢华大礼"]
    }

# 2. 侧边栏：自定义奖品池
with st.sidebar:
    st.header("⚙️ 自定义奖品池")
    st.info("在这里修改属于你们的奖品，每行一个奖品。")
    
    for level in st.session_state.prizes.keys():
        current_prizes = "\n".join(st.session_state.prizes[level])
        new_prizes = st.text_area(f"修改 {level}", value=current_prizes, height=100)
        st.session_state.prizes[level] = [p.strip() for p in new_prizes.split("\n") if p.strip()]

# 3. 主界面：抽奖逻辑
selected_level = st.selectbox("🎯 请选择抽奖档位：", list(st.session_state.prizes.keys()))

if st.button("✨ 开启好运 ✨"):
    pool = st.session_state.prizes[selected_level]
    if pool:
        with st.spinner('正在抽取中...'):
            import time
            time.sleep(1) # 增加仪式感
            result = random.choice(pool)
            st.balloons()
            st.success(f"恭喜你！抽中了【{selected_level}】的奖品：")
            st.markdown(f"### 🏆 {result}")
    else:
        st.error("这个档位的奖品池是空的，快去左侧添加吧！")

# 4. 底部声明
st.markdown("---")
st.caption("💖 奖品有价，爱无价。抽中奖品后记得找对方兑现哦！")
