# confidentiality: public-approved
from __future__ import annotations

import difflib
import hmac
import html
import io
import os
import tempfile
from datetime import datetime
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
import streamlit as st

from core import IngredientExtractor
from knowledge import KnowledgeBase
from script_checker import TraditionalChineseChecker

_APP_DIR = Path(__file__).resolve().parent
_NFH_LOGO_PATH = _APP_DIR / "assets" / "demo_logo.png"

st.set_page_config(
    page_title="食品標籤工具｜食品標籤助手",
    page_icon="🏷️",
    layout="wide",
    initial_sidebar_state="expanded",
)
load_dotenv(_APP_DIR / ".env")

_MAIN_APP_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;600&family=Noto+Serif+TC:wght@500;600;700&display=swap');
/* —— 食品標籤助手（標誌風格）：暖橙、金黃點綴、襯線標題 —— */
html, body, [data-testid="stAppViewContainer"], .stApp {
    font-family: 'Noto Sans TC', 'Microsoft JhengHei', sans-serif;
}
h1, h2, h3 {
    font-family: 'Noto Serif TC', 'Songti TC', 'PMingLiU', serif;
    color: #3D3329;
}
h1 { letter-spacing: 0.02em; font-weight: 700; }
h2, h3 { font-weight: 650; }
header[data-testid="stHeader"] {
    background: #FFFDFB;
    border-bottom: 3px solid #C86B2B;
}
.main .block-container {
    padding-top: 1rem;
    max-width: 1180px;
    padding-left: 2rem;
    padding-right: 2rem;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #FFFDFB 0%, #F5EBE0 100%);
    border-right: 2px solid #E8D4BC;
}
[data-testid="stSidebar"] .stMarkdown h3 { color: #A65A24; margin-bottom: 0.15rem; }
.stTabs [data-baseweb="tab-list"] {
    gap: 0.25rem;
    background: linear-gradient(180deg, #F3E6D8 0%, #EDE0D4 100%);
    padding: 0.35rem 0.5rem 0 0.5rem;
    border-radius: 10px 10px 0 0;
    border-bottom: 1px solid #D9C4A8;
    font-family: 'Noto Serif TC', 'Songti TC', serif;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 8px 8px 0 0;
    font-weight: 600;
    color: #6B5D52;
    padding: 0.5rem 1rem;
}
.stTabs [data-baseweb="tab"][aria-selected="true"] {
    color: #A65A24 !important;
    background: #FFFDFB !important;
    border-bottom: 3px solid #C86B2B !important;
}
[data-testid="stFileUploaderDropzone"],
[data-testid="stFileUploadDropzone"] {
    background: linear-gradient(180deg, #FFFCF8 0%, #FAF3EA 100%) !important;
    border: 2px dashed #D4A574 !important;
    border-radius: 12px !important;
    padding: 0.5rem !important;
}
[data-testid="stFileUploaderDropzone"]:hover,
[data-testid="stFileUploadDropzone"]:hover {
    border-color: #C86B2B !important;
    background: #FFF9F0 !important;
}
[data-testid="stFileUploaderDropzone"] button,
[data-testid="stFileUploadDropzone"] button {
    border-color: #C86B2B !important;
    color: #A65A24 !important;
}
.nfh-callout {
    display: flex;
    gap: 12px;
    align-items: flex-start;
    background: linear-gradient(90deg, #FBF5ED 0%, #FFF9F0 100%);
    border: 1px solid #E8D4BC;
    border-left: 4px solid #C86B2B;
    border-radius: 0 10px 10px 0;
    padding: 14px 16px;
    margin: 0.75rem 0 1rem 0;
    box-shadow: 0 1px 3px rgba(158, 84, 32, 0.08);
}
.nfh-callout-icon {
    flex-shrink: 0;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background: linear-gradient(145deg, #E8B84A 0%, #C86B2B 100%);
    color: #fff;
    font-size: 15px;
    font-weight: 700;
    line-height: 28px;
    text-align: center;
    font-family: 'Noto Serif TC', serif;
}
.nfh-callout-body { margin: 0; color: #4A423A; font-size: 0.95rem; line-height: 1.55; }
.nfh-callout-body strong { color: #3D3329; }
div[data-testid="stVerticalBlockBorderWrapper"]:has(h1) {
    background: linear-gradient(180deg, #FFFDFB 0%, #FAF3EA 100%) !important;
    border-color: #E8D4BC !important;
    box-shadow: 0 2px 10px rgba(158, 84, 32, 0.07);
}
.streamlit-expanderHeader {
    font-weight: 600 !important;
    color: #7A5A3E !important;
}
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #FFFDFB !important;
    border-color: #EAD8C4 !important;
    border-radius: 10px !important;
}
</style>
"""


def nfh_callout(text: str) -> None:
    """品牌風格提示（取代預設藍底 st.info）。"""
    st.markdown(
        f"""
        <div class="nfh-callout">
            <div class="nfh-callout-icon">i</div>
            <p class="nfh-callout-body">{html.escape(text)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


_LOGIN_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;600&family=Noto+Serif+TC:wght@600;700&display=swap');
[data-testid='stSidebar']{display:none;}
section.main [data-testid="stForm"] {
    max-width: 280px;
    margin: 0 auto;
}
section.main [data-testid="stForm"] .stTextInput [data-baseweb="input"],
section.main [data-testid="stForm"] .stTextInput input {
    min-height: 2.25rem !important;
    font-size: 0.9rem !important;
    line-height: 1.35 !important;
    padding: 0.3rem 0.55rem !important;
    border-width: 1.5px !important;
    border-color: #D4A574 !important;
    border-radius: 8px !important;
}
section.main [data-testid="stForm"] .stTextInput [data-baseweb="input"]:focus,
section.main [data-testid="stForm"] .stTextInput input:focus {
    border-color: #C86B2B !important;
    box-shadow: 0 0 0 1px #E8B84A !important;
}
section.main [data-testid="stForm"] label,
section.main [data-testid="stForm"] [data-testid="stWidgetLabel"] p {
    font-size: 0.88rem !important;
    color: #5C4E42 !important;
}
section.main [data-testid="stForm"] .stTextInput {
    margin-bottom: 0.35rem;
}
</style>
"""


def check_login() -> bool:
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        return True

    st.markdown(_LOGIN_CSS, unsafe_allow_html=True)
    st.markdown(
        """
        <div style="
            background:linear-gradient(100deg,#8B4A1F 0%,#C86B2B 28%,#E0AA3E 52%,#C86B2B 78%,#9E5420 100%);
            color:#fff;
            padding:18px 20px 16px 20px;
            margin:-1rem -4rem 1.25rem -4rem;
            text-align:center;
            box-shadow:0 3px 14px rgba(139,74,31,0.28);
        ">
            <div style="
                font-family:'Noto Serif TC','Songti TC','PMingLiU',serif;
                font-size:1.22rem;
                font-weight:700;
                letter-spacing:0.1em;
                text-shadow:0 1px 2px rgba(0,0,0,0.12);
            ">食品標籤助手 · 食品標籤工具</div>
            <div style="
                font-family:Georgia,'Times New Roman',serif;
                font-size:0.72rem;
                font-weight:600;
                letter-spacing:0.26em;
                opacity:0.94;
                margin-top:8px;
            ">FOOD LABEL ASSISTANT</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    _, col_mid, _ = st.columns([1, 1, 1])
    with col_mid:
        if _NFH_LOGO_PATH.exists():
            st.image(str(_NFH_LOGO_PATH), width=200)
        st.markdown(
            '<p style="font-family:\'Noto Serif TC\',serif;font-weight:600;color:#7A5A3E;margin:0 0 6px 0;">登入</p>',
            unsafe_allow_html=True,
        )
        st.caption("請輸入帳號及密碼")

        with st.form("login_form", clear_on_submit=False):
            username = st.text_input("帳號")
            password = st.text_input("密碼", type="password")
            submitted = st.form_submit_button("登入", use_container_width=True)

    if submitted:
        expected_user = os.getenv("APP_USERNAME", "")
        expected_pass = os.getenv("APP_PASSWORD", "")

        if not expected_user or not expected_pass:
            st.error("請先在本機 .env 設定 APP_USERNAME 與 APP_PASSWORD。")
            return False

        user_ok = hmac.compare_digest(username, expected_user)
        pass_ok = hmac.compare_digest(password, expected_pass)

        if user_ok and pass_ok:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("帳號或密碼不正確")

    return False


@st.cache_resource
def get_kb() -> KnowledgeBase:
    kb_path = Path(__file__).parent / "demo_knowledge.xlsx"
    if not kb_path.exists():
        raise FileNotFoundError(f"知識庫檔案不存在：{kb_path}")
    return KnowledgeBase(file_path=str(kb_path))


@st.cache_resource
def get_extractor() -> IngredientExtractor:
    return IngredientExtractor()


@st.cache_resource
def get_script_checker() -> TraditionalChineseChecker:
    return TraditionalChineseChecker(config="s2hk")


def format_match_type(match_type: str, score: float = 1.0) -> str:
    match_map = {
        "exact": "標準名稱匹配",
        "alias": "別名匹配",
        "e_number": "E編號匹配",
        "fuzzy": "近似匹配",
        "common_food": "普通配料",
    }
    text = match_map.get(match_type, match_type or "—")
    if match_type == "fuzzy":
        text += f"（相似度 {score:.2f}）"
    return text


def get_display_name(info) -> str:
    return info.name_zh_hk or info.name or info.name_zh_cn or "—"


def get_display_function(info) -> str:
    func_zh = info.func_zh_hk or info.func_zh or info.func_zh_cn or "—"
    func_en = info.func_en or ""
    return f"{func_zh} / {func_en}" if func_en else func_zh


def build_additive_results_export(ingredients: list[str], kb: KnowledgeBase) -> pd.DataFrame:
    """將識別成分與知識庫匹配結果整理為匯出用表格（含普通配料、未匹配列）。"""
    rows: list[dict] = []
    for idx, ingredient in enumerate(ingredients, start=1):
        info = kb.get_info(ingredient)
        base = {"序號": idx, "識別成分": ingredient}
        dash = "—"
        if info.is_common_food:
            rows.append(
                {
                    **base,
                    "項目類型": "普通配料",
                    "標準名稱_港": dash,
                    "英文名稱": dash,
                    "E編號": dash,
                    "功能_中文": dash,
                    "功能_英文": dash,
                    "匹配方式": dash,
                    "相似度": dash,
                    "備註": dash,
                }
            )
        elif info.found:
            func_zh = info.func_zh_hk or info.func_zh or info.func_zh_cn or ""
            func_en = info.func_en or ""
            score_txt = f"{info.score:.2f}" if info.match_type == "fuzzy" else dash
            rows.append(
                {
                    **base,
                    "項目類型": "已匹配添加劑",
                    "標準名稱_港": get_display_name(info),
                    "英文名稱": info.name_en or dash,
                    "E編號": info.e_code or dash,
                    "功能_中文": func_zh or dash,
                    "功能_英文": func_en or dash,
                    "匹配方式": format_match_type(info.match_type, info.score),
                    "相似度": score_txt,
                    "備註": info.notes or dash,
                }
            )
        else:
            rows.append(
                {
                    **base,
                    "項目類型": "未匹配",
                    "標準名稱_港": dash,
                    "英文名稱": dash,
                    "E編號": dash,
                    "功能_中文": dash,
                    "功能_英文": dash,
                    "匹配方式": dash,
                    "相似度": dash,
                    "備註": dash,
                }
            )

    columns = [
        "序號",
        "識別成分",
        "項目類型",
        "標準名稱_港",
        "英文名稱",
        "E編號",
        "功能_中文",
        "功能_英文",
        "匹配方式",
        "相似度",
        "備註",
    ]
    return pd.DataFrame(rows, columns=columns)


def dataframe_to_excel_bytes(df: pd.DataFrame, sheet_name: str = "識別結果") -> bytes:
    buf = io.BytesIO()
    with pd.ExcelWriter(buf, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name=sheet_name)
    return buf.getvalue()


def save_upload_to_temp(uploaded_file) -> str:
    suffix = Path(uploaded_file.name).suffix or ".jpg"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        return tmp_file.name


def render_changed_text_html(original: str, converted: str) -> str:
    """
    將 converted 中相對 original 的變更部分標紅。
    """
    original = original or ""
    converted = converted or ""

    matcher = difflib.SequenceMatcher(None, original, converted)
    parts = []

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        seg = converted[j1:j2]
        seg = html.escape(seg).replace("\n", "<br>")

        if tag == "equal":
            parts.append(f"<span>{seg}</span>")
        else:
            parts.append(
                "<span style='color:#A65128;font-weight:600;"
                "text-decoration:underline;text-decoration-color:#E8B84A;"
                "text-underline-offset:2px;background-color:#FFF5EB;border-radius:2px;'>"
                f"{seg}</span>"
            )

    return "".join(parts)


def render_layout_block(block) -> str:
    """
    根據 role 渲染「接近原圖排版」的香港繁體校對稿。
    變更部分會標紅。
    """
    role = block.role or "paragraph"

    if role == "field":
        label_orig = block.label_original or ""
        label_hk = block.label_hk or label_orig
        value_orig = block.value_original or ""
        value_hk = block.value_hk or value_orig

        label_html = render_changed_text_html(label_orig, label_hk)
        value_html = render_changed_text_html(value_orig, value_hk)

        return (
            "<div style='margin:10px 0; line-height:1.8;'>"
            f"<span style='font-weight:700;'>{label_html}</span>"
            f"<span>：{value_html}</span>"
            "</div>"
        )

    if role == "title_line":
        orig = block.original_text or ""
        hk = block.hk_text or orig
        content_html = render_changed_text_html(orig, hk)
        return (
            "<div style='margin:14px 0 10px 0; font-size:22px; font-weight:700; line-height:1.6;'>"
            f"{content_html}"
            "</div>"
        )

    if role == "footer":
        orig = block.original_text or ""
        hk = block.hk_text or orig
        content_html = render_changed_text_html(orig, hk)
        return (
            "<div style='margin:8px 0; font-size:14px; line-height:1.8; color:#6B5D52;'>"
            f"{content_html}"
            "</div>"
        )

    # 預設 paragraph
    orig = block.original_text or ""
    hk = block.hk_text or orig
    content_html = render_changed_text_html(orig, hk)
    return (
        "<div style='margin:10px 0; line-height:1.9;'>"
        f"{content_html}"
        "</div>"
    )


def build_full_text_from_blocks(blocks, use_hk: bool = False) -> str:
    lines = []

    for block in blocks:
        if block.role == "field":
            label = block.label_hk if use_hk else block.label_original
            value = block.value_hk if use_hk else block.value_original
            label = (label or "").strip()
            value = (value or "").strip()

            if label and value:
                lines.append(f"{label}：{value}")
            elif label:
                lines.append(label)
            elif value:
                lines.append(value)
        else:
            text = block.hk_text if use_hk else block.original_text
            text = (text or "").strip()
            if text:
                lines.append(text)

    return "\n".join(lines)


if not check_login():
    st.stop()

kb = get_kb()
extractor = get_extractor()
script_checker = get_script_checker()

dashscope_ready = bool(os.getenv("DASHSCOPE_API_KEY"))

st.markdown(_MAIN_APP_CSS, unsafe_allow_html=True)

with st.container(border=True):
    st.title("食品標籤工具")
    st.caption("公開示例版 · 圖片識別、知識匹配與香港繁體校對")
    st.warning("附帶知識庫僅含合成演示資料，不可用於真實食品判斷。圖片識別會將所選圖片發送至你配置的模型服務。")

with st.sidebar:
    if _NFH_LOGO_PATH.exists():
        st.image(str(_NFH_LOGO_PATH), use_container_width=True)
    else:
        st.markdown(
            '<p style="margin:0 0 4px 0;font-size:1.28rem;font-weight:700;'
            'font-family:\'Noto Serif TC\',serif;color:#A65A24;letter-spacing:0.12em;">食品標籤助手</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p style="margin:0;font-size:0.65rem;letter-spacing:0.2em;color:#8B7355;">FOOD LABEL ASSISTANT</p>',
            unsafe_allow_html=True,
        )
    st.caption("食品標籤工具 · 內部使用")
    st.divider()
    if dashscope_ready:
        st.success("DashScope API 已設定")
    else:
        st.warning("未設定 DASHSCOPE_API_KEY")
    st.divider()
    st.caption("已登入")
    if st.button("登出", use_container_width=True):
        st.session_state.logged_in = False
        st.rerun()

with st.expander("使用說明", expanded=False):
    st.markdown(
        "1. **添加劑識別**：上傳配料表圖片，系統會識別成分並查詢 E 編號及功能資訊；識別完成後可 **匯出 Excel**。\n"
        "2. **簡體檢查**：使用大模型直接理解整張標籤圖，生成接近原圖排版的香港繁體校對稿，修改部分會標紅。\n"
        "3. 本工具僅供內部資訊查詢，不構成專業食品安全或法規判斷。"
    )

if not dashscope_ready:
    st.warning("目前未檢測到 DASHSCOPE_API_KEY 環境變數，兩項 AI 功能將無法使用。")

tab1, tab2 = st.tabs(["添加劑識別", "簡體檢查"])


# =========================
# Tab 1: 添加劑識別
# =========================
with tab1:
    st.subheader("食品添加劑識別")
    st.caption("識別配料表中的食品添加劑，並顯示 E 編號及功能資訊")

    uploaded_ingredient_file = st.file_uploader(
        "上傳配料表圖片",
        type=["png", "jpg", "jpeg"],
        key="ingredient_uploader",
    )

    if uploaded_ingredient_file is None:
        nfh_callout(
            "請上傳配料表圖片（PNG／JPG）。上傳後左側為預覽，右側為識別結果。"
        )
    else:
        col_img, col_result = st.columns([1, 1], gap="large")
        with col_img:
            st.image(uploaded_ingredient_file, caption="已上傳圖片", use_container_width=True)

        with col_result:
            if not dashscope_ready:
                st.error("未設定 DASHSCOPE_API_KEY，無法進行添加劑識別。")
            else:
                with st.spinner("AI 正在識別配料表..."):
                    temp_file_path = save_upload_to_temp(uploaded_ingredient_file)
                    try:
                        result = extractor.extract(temp_file_path)
                    finally:
                        if os.path.exists(temp_file_path):
                            os.unlink(temp_file_path)

                if not result.success:
                    st.error(result.error or "AI 未能識別到有效成分")
                    if result.raw_text:
                        with st.expander("查看模型原始輸出"):
                            st.code(result.raw_text, language="json")
                else:
                    st.success(f"已識別 {len(result.ingredients)} 項成分")
                    st.write("識別結果：", "、".join(result.ingredients))
                    st.divider()

                    matched_count = 0
                    common_food_count = 0
                    unmatched = []

                    for ingredient in result.ingredients:
                        info = kb.get_info(ingredient)

                        if info.is_common_food:
                            common_food_count += 1
                            continue

                        if info.found:
                            matched_count += 1

                            with st.container(border=True):
                                st.subheader(f"🧪 {get_display_name(info)}")

                                c1, c2 = st.columns([1, 3])

                                with c1:
                                    st.markdown("**E編號**")
                                    st.markdown("**功能 / Function**")
                                    st.markdown("**匹配方式**")

                                with c2:
                                    st.markdown(info.e_code or "—")
                                    st.markdown(get_display_function(info))
                                    st.markdown(format_match_type(info.match_type, info.score))

                                if info.notes:
                                    st.caption(f"備註：{info.notes}")

                        else:
                            unmatched.append(ingredient)
                            st.warning(f"❓ {ingredient}（未在資料庫中找到）")

                    st.divider()

                    m1, m2, m3 = st.columns(3)
                    with m1:
                        st.metric("已匹配添加劑", matched_count)
                    with m2:
                        st.metric("普通配料", common_food_count)
                    with m3:
                        st.metric("未匹配項目", len(unmatched))

                    export_df = build_additive_results_export(result.ingredients, kb)
                    xlsx_bytes = dataframe_to_excel_bytes(export_df)
                    out_name = f"食品添加劑識別結果_{datetime.now():%Y%m%d_%H%M%S}.xlsx"
                    st.download_button(
                        "匯出識別結果（Excel）",
                        data=xlsx_bytes,
                        file_name=out_name,
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        key="export_additive_xlsx",
                        use_container_width=True,
                        help="工作表「識別結果」含序號、識別成分、項目類型、E 編號、功能與匹配方式等欄位",
                    )

                    if unmatched:
                        with st.expander("未匹配項目", expanded=True):
                            st.write("、".join(unmatched))


# =========================
# Tab 2: 簡體檢查（大模型整圖校對版）
# =========================
with tab2:
    st.subheader("簡體檢查")
    st.caption("使用大模型直接理解整張圖片，生成接近原圖排版的香港繁體校對稿，需修改部分會標紅")

    uploaded_script_file = st.file_uploader(
        "上傳標籤圖片",
        type=["png", "jpg", "jpeg"],
        key="script_uploader",
    )

    if uploaded_script_file is None:
        nfh_callout(
            "請上傳標籤圖片（PNG／JPG）。上傳後左側為預覽，右側為校對稿與原文。"
        )
    else:
        col_img, col_result = st.columns([1, 1], gap="large")
        with col_img:
            st.image(uploaded_script_file, caption="已上傳圖片", use_container_width=True)

        with col_result:
            if not dashscope_ready:
                st.error("未設定 DASHSCOPE_API_KEY，無法進行整圖文字理解。")
            else:
                with st.spinner("AI 正在理解整張圖片並生成校對稿..."):
                    temp_file_path = save_upload_to_temp(uploaded_script_file)
                    try:
                        layout_result = extractor.extract_layout_text(temp_file_path)
                    finally:
                        if os.path.exists(temp_file_path):
                            os.unlink(temp_file_path)

                if not layout_result.success:
                    st.error(layout_result.error or "未能生成版式文字稿")
                    if layout_result.raw_text:
                        with st.expander("查看模型原始輸出"):
                            st.code(layout_result.raw_text, language="json")
                else:
                    blocks = layout_result.blocks
                    original_full = build_full_text_from_blocks(blocks, use_hk=False)
                    full_check = script_checker.check_text(original_full)

                    if full_check.has_simplified:
                        st.warning("檢測到簡體字或內地用語，以下為香港繁體校對稿，修改部分已標紅。")
                    else:
                        st.success("未檢測到明顯簡體字。")

                    st.divider()

                    st.markdown("### 香港繁體校對稿（修改處標紅）")
                    rendered_blocks = [render_layout_block(block) for block in blocks]
                    st.markdown(
                        """
                        <div style="
                            background:#FFFDFB;
                            border:1px solid #EAD8C4;
                            border-radius:10px;
                            padding:18px 20px;
                            box-shadow:0 1px 3px rgba(158,84,32,0.07);
                        ">
                        """
                        + "".join(rendered_blocks)
                        + "</div>",
                        unsafe_allow_html=True,
                    )

                    with st.expander("查看原始完整文字", expanded=False):
                        st.text_area(
                            "原始完整文字",
                            value=original_full,
                            height=220,
                            key="layout_original_text",
                            label_visibility="collapsed",
                        )