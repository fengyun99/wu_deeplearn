#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Dict, Any

from llama_index.llms import ChatMessage, OpenAILike, MessageRole

MAC_M1_LUNADEMO_CONSERVATIVE_TIMEOUT = 10 * 60  # sec

LOCALAI_IP = "192.168.2.103"
LOCALAI_PORT = 8001
LOCALAI_CONFIG: Dict[str, Any] = {
    "api_key": "localai_fake",
    "api_type": "localai_fake",
    "api_base": f"http://{LOCALAI_IP}:{LOCALAI_PORT}/v1",
}

model = OpenAILike(
    **LOCALAI_CONFIG,
    model="qwen14b",
    is_chat_model=True,
    timeout=MAC_M1_LUNADEMO_CONSERVATIVE_TIMEOUT,
)
# 对话
# response = model.chat(messages=[ChatMessage(role=MessageRole.USER, content="你好?")])

messages = [
    ChatMessage(role=MessageRole.SYSTEM, content="你是一位经历丰富多彩的海盗。"),
    ChatMessage(role=MessageRole.USER, content="给我讲一件你冒险的故事。")
]

resp = model.stream_chat(messages)
for r in resp:
    print(r.delta, end="")

# 续写
# response = model.complete("爱迪生发明了", max_tokens=100)
# 流式输出，流式输出传入的都是一个str
# response = model.stream_complete("帮我总结下面的内容:（一）住房公积金管理委员会：保定市住房公积金管理委员会有19名委员，2020年召开1次会议，审议通过的事项主要包括：《2019年住房公积金财务决算说明》、《2020年住房公积金财务收支预算编制说明》、《保定市住房公积金归集管理暂行办法》、《保定市住房公积金提取管理暂行办法》、《保定市住房公积金贷款管理暂行办法》、《灵活就业人员自愿缴存住房公积金管理办法（试行）》、《关于住房公积金个人住房贷款呆账核销的请示》。定州市住房公积金管理委员会有20名委员，2020年召开4次会议，审议通过的事项主要包括：《定州市2019年住房公积金管理工作报告》、《2019年住房公积金财务决算报告》、《2020年住房公积金财务收支预算编制说明》、市财政局《关于对市住房公积金管理中心2019年财务决算及2020年收支预算的审核报告》、《定州市住房公积金2019年年度报告》、《网络安全等级保护建设实施方案》和《综合服务提升项目建设实施方案》、《关于在华夏银行定州支行及河北银行定州支行设立账户的报告》、《定州市个人自愿缴存住房公积金管理暂行办法》、《关于落实〈河北省促进绿色建筑发展条例〉的报告》、《关于落实住房公积金异地个人住房贷款工作的通知》。东方物探住房公积金管理委员会有12名委员，2020年召开一次会议，审议通过的事项主要包括：听取2019年住房公积金管理工作汇报，审议通过了住房公积金2020年重点工作安排；审议通过了2020年住房公积金归集使用计划及管理经费预算计划；住房公积金管理委员会授权住房公积金管理中心批准缴存单位申请或降低缴存比例事项。（二）住房公积金管理中心：保定市住房公积金管理中心为直属市人民政府不以营利为目的的正县级自收自支事业单位，设11个处室，21个管理部，4个分中心。从业人员286人，其中，在编151人，非在编135人。定州市住房公积金管理中心为定州市人民政府不以营利为目的的财政性资金零补助事业单位，内设7个科室，下设住房公积金服务大厅。从业人员24人，其中在编24人。地方物探住房公积金管理中心为东方地球物理公司不以营利为目的的企业机关附属位，设3个科室，从业人员10人，其中，在编10人。")
#
# for r in response:
#     print(r.delta, end="")
