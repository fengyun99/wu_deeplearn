#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/8/29 13:33
# @Author   : FengYun
# @File     : get_doc.py
# @Software : PyCharm
import re
from typing import List

from langchain.schema import Document

# 添加自己的数据内容
doc = '''住房公积金综合服务平台 建设导则\n为拓展住房公积金服务渠道，提高服务效率，向缴存单\n位和缴存职工提供高效便捷服务，充分发挥住房公积金作 用，规范各市住房公积金管理中心综合服务平台建设，制定 本导则。\n一、建设目标\n在进一步优化营业网点柜面服务的基础上，以“互联网 + ”为导向， 以互联网和移动终端为主要载体，拓展服务渠 道，加快建设功能齐全、使用便捷、服务高效、职工满意的 住房公积金综合服务平台。\n住房公积金综合服务平台主要由服务渠道、数据接口、 综合管理系统和安全保障体系四个部分组成，承担业务办 理、信息查询、信息发布和互动交流等四类服务功能，架构 图见附件 1。\n二、建设原则\n住房公积金综合服务平台的设计和建设，应符合住房公 积金基础数据标准、信息系统技术规范、信息化建设导则的 要求，并遵循以下原则。\n1、经济适用\n根据住房公积金业务办理特征，结合缴存单位和缴存职 工服务需求，操作简便快捷，按需建设，投入合理。以高频 简单业务线上自助办理为重点，提升缴存单位和缴存职工自 助业务办理能力。\n2、稳定可靠\n选用的产品和技术稳定可靠，系统配置和运行管理等环 节有严格保障措施，确保系统稳定运转、业务正常开展。\n3、安全高效\n安全保障措施完备，业务处理机制稳妥，在为用户提供 远程自助办理手段的同时，有效控制风险，保证资金和信息 安全。\n4、多样化\n服务渠道丰富，满足不同年龄结构、知识水平和使用习\n惯缴存职工的多样化服务需求。\n5、可扩展\n满足现阶段服务需求，同时也为未来新增服务渠道预留 空间，实现平滑升级和系统扩展。\n三、服务渠道\n住房公积金服务渠道除柜面业务办理系统外，还包括门 户网站、 网上业务大厅、自助终端、服务热线、手机短信 、 手机客户端、官方微信和官方微博等八种服务渠道。\n1、门户网站\n通过互联网为缴存单位、职工及社会公众提供综合性、 交互式信息服务，是最全面的对外信息发布交流窗口。\n2、网上业务大厅\n面向缴存单位、缴存职工及相关单位，覆盖归集、提取、 贷款等业务，实现业务在线办结和结算。\n3、自助终端\n通过中心自建服务终端或借助银行服务终端，向缴存单 位和缴存职工提供业务查询、证明打印、业务受理等服务。\n4、服务热线\n即 12329 全国住房公积金专用服务热线，提供政策咨询、 业务受理、投诉建议、回访调查等人工服务和自助服务。\n5、手机短信\n即 12329 全国住房公积金专用服务短信，提供政策宣传、 信息查询、业务通知、身份验证等服务。。\n6、手机客户端\n通过移动终端，向缴存单位和缴存职工提供综合性、交 互式服务，具有灵活便捷、高可定制性、用户体验佳等特点。\n7、官方微信\n通过跨通信运营商、跨操作系统平台，向缴存单位和缴 存职工快速发送住房公积金政策和业务文本、音频、视频和 图片，提供综合性和交互式服务。\n8、官方微博\n以主流运营商微博为载体，宣传住房公积金政策，了解\n收集社会公众意见，并及时予以反馈。\n上述八种渠道优缺点及可承载的服务功能，见附件 2。 各项住房公积金业务可采用的服务渠道， 见附件 3。\n根据业务办理频度、办理要素、资金流向等，可将住房 公积金业务部署到相应服务渠道上，业务分类和部署渠道见 附件 4。\n各城市住房公积金管理中心可以根据资金规模、业务流 程和管理能力，选择建设部分或全部服务渠道。\n四、数据接口\n住房公积金综合服务平台通过数据接口与服务渠道、内 部业务信息管理组件之间通讯。\n1、服务渠道接口。根据互联网、银行专线和中心专线 等不同接入方式，制定不同的接口标准和安全策略，确保综 合服务平台对外正常数据交换和业务办理。\n2、业务处理组件接口。根据不同请求内容对接相应的 内部业务处理组件，实现用户账务查询、提取、还款等业务 办理，实现发布信息的主动推送和用户交互服务，满足综合 服务平台服务要求。\n3、对外信息共享接口。要加强与公安、民政、房产、\n社保、税务、工商、人民银行以及受委托商业银行的沟通协 作，推动跨部门、跨行业信息互联互通。\n五、综合管理系统\n综合服务平台是住房公积金信息系统电子渠道业务的 延伸。综合管理系统是综合服务平台的核心，负责对各电子 渠道服务活动进行统一管理，统一进行安全控制和身份识 别，集中响应电子服务渠道的查询、咨询和业务办理请求， 采用松耦合方式对接业务信息管理组件，支持新渠道快速接 入、业务服务快速部署和渠道间相互协同，实现服务管理、 用户管理、渠道管理。\n1、部署和运行管理\n通过标准化的接口配置、业务组件调用，实现服务渠道 的快速部署。\n能够对某类服务在不同渠道上的启用、停用，进行审批 和控制。\n能够对某类服务的服务时间，进行参数化配置和管理。\n2、服务管理\n（1）业务办理\n统一控制各服务渠道端系统与核心业务系统的交互，保 证交易逻辑、业务处理流程、审核校验规则的一致性。\n对各渠道业务办理服务信息进行整合，实现同一交易过 程在不同渠道间的协同操作和处理。\n对用户的业务发起进行控制，同一用户同一时间同一业 务只能发起一次交易，避免在途业务冲突。\n（2）信息查询\n设计统一的查询交易逻辑和查询信息接口规范。针对不 同渠道特性，设计相应信息输入和输出形式。提供实时查询 服务。保证各渠道查询数据一致。\n缴存职工可自由选择信息查询渠道。\n（3）互动交流\n支持人工交流和自动应答。\n各渠道应使用统一的知识库和服务标准。\n建立用户互动交流日志。\n可保存和重新调用未完成互动交流状态。\n提供用户操作手册和引导帮助。\n（4）信息发布\n按统一流程编辑、审核和发布信息。\n支持在选定渠道应用文本、图片、音频、视频等格式发 布。\n支持在相应渠道实现批处理任务和实时任务。 支持在相应渠道手动发布和自动发布。\n3、渠道管理\n（1）接入管理\n具备开启或停止服务渠道接入功能。\n具备手动和自动两种控制方式。\n支持按照预设的控制逻辑，自动限制或停止接入请求。\n（2）流量控制\n设置渠道流量（访问量和业务量）阈值，对于超过阈值 的接入申请，能够实时控制。\n（3）限额控制\n设置用户在各渠道办理业务的单日交易限额和单笔交 易限额（上限和下限），对于超出限额的业务申请，能够返 回限额控制警示信息。\n4、用户管理\n（1）信息管理\n按照《住房公积金基础数据标准》（JGJ/T320-2014）， 为各渠道提供统一的用户信息。\n支持以用户为中心，整合、展示和使用登记、账务、交 易、交互等各类信息。\n（2）登录管理\n统一处理各渠道的用户注册、用户注销服务，实现一次 注册，多渠道使用。\n统一处理用户在各渠道的登录请求，校验用户名、密码、 验证码等。\n对用户退出应用后各项服务的关闭进行控制，对一定时 间无操作的用户，自动关闭其业务请求权限。\n（3）签约管理\n支持柜面签约信息同步。\n通过政府部门、商业银行等具有公信力的第三方，联网 验证用户身份，实现用户远程线上签约。\n实现各渠道签约流程统一、验证信息一致、签约信息共 享。\n六、安全保障体系\n安全保障体系是住房公积金综合服务平台必不可少的 组成部分，应严格执行国家信息系统安全规范，保障渠道设 施、终端设备、通讯线路和服务平台安全，实现线上业务、 资金和信息安全。\n1、平台安全\n按照相应等级保护要求，建立平台所处物理环境安全机 制和保护措施。\n建立网络结构安全、区域隔离、访问控制、安全审计、 边界完整性检查和网络设备防护等网络安全保护机制。\n建立业务信息的数字签名、数据加密机制和业务数据备 份机制，具备完善的数据保护能力。\n2、业务安全\n（1）身份认证\n建立可靠的身份认证机制，分为临柜认证、第三方协查 认证、用户名密码及手机短信验证码认证、数字证书认证、 生物特征认证等。\n（2）操作风险防控\n建立业务操作风险防控机制，包括重要线上业务开通管 理、交易权限控制、交易信息核查、账户变动情况提醒、异 常交易处置、交易日志记录和审计等，确保业务过程合规， 业务结果真实。\n（3）资金风险防控\n采取账户预留、防账户信息泄漏、防账户数据篡改和防 伪造转账指令、账户资金变动提醒、资金账户余额查询、资 金账户流水核对、业务流水核对等措施，防止资金非法流出 和资金业务差错，保障资金安全。\n（4）数据信息安全\n综合服务平台向第三方或通过第三方对社会提供住房 公积金数据信息服务，除法律法规有明确规定的，应当获得 缴存单位和缴存职工的同意。原则上不得向第三方直接提供 原始明细信息。\n七、运行绩效分析\n即采集和记载各服务渠道运行的数据，掌握系统运行状 况，发现异常交易，评价渠道运行效率和用户体验水平 。主 要指标包括：\n1、渠道运行指标\n渠道访问量：各渠道所提供栏目和服务的访问量\n渠道业务占比：单项业务在指定渠道的办理量与总办理 量之比\n业务办理成功率：各渠道办理成功数/业务办理请求数 异常交易率：各渠道异常交易业务数/业务办理总数\n栏目内容更新量：各渠道栏目内容的更新数量\n信息推送量：各渠道推送信息的数量\n渠道注册人数：各渠道当前注册人数、已关闭注册人数\n特定渠道活动用户占比：办理业务的活动用户数／注册 用户总数\n特定渠道用户注册率：渠道注册用户数／业务系统登记 用户总数\n2、用户体验评价指标\n用户满意度：（满意用户数＋基本满意用户数）/参与评 价用户数\n用户投诉率：投诉用户数/业务系统登记用户总数\n3、分析指标\n渠道运行信息：各渠道的访问数量、办理业务类型、访 问用户类型、访问时间段分布等。\n业务办理信息：各业务类型的办理数量、办理成功数、 办理失败数、办理时间、渠道分布情况(特定渠道业务办理 数/各渠道业务办理总数)、用户分布情况（特定渠道办理业 务用户数/各渠道办理业务用户总数）、办理时间段分布。\n用户信息：用户人数、年龄信息、性别信息、渠道访问 信息、业务办理信息、评价信息。\n咨询投诉热点排序：对知识库热点应自动统计，按照提 交日期、回复日期和访问频率等顺序进行筛选排列。\n附件 1：住房公积金综合服务平台架构图\n附件 2：渠道特点分析表\n附件 3: 业务与渠道分析表\n附件 4：渠道服务部署表\n附件1:\n住房公积金综合服务平台架构图\n附件 2：\n渠道特点分析表\n附件 3：\n业务分析与渠道选择表\n附件 4：\n渠道服务部署表\n注： ● 表示该渠道适合提供该服务；  ○ 表示暂不适合。\n'''


def under_non_alpha_ratio(text: str, threshold: float = 0.5):
    """Checks if the proportion of non-alpha characters in the text snippet exceeds a given
    threshold. This helps prevent text like "-----------BREAK---------" from being tagged
    as a title or narrative text. The ratio does not count spaces.

    Parameters
    ----------
    text
        The input string to test
    threshold
        If the proportion of non-alpha characters exceeds this threshold, the function
        returns False
    """
    if len(text) == 0:
        return False

    alpha_count = len([char for char in text if char.strip() and char.isalpha()])
    total_count = len([char for char in text if char.strip()])
    try:
        ratio = alpha_count / total_count
        return ratio < threshold
    except:
        return False


def is_possible_title(
        text: str,
        title_max_word_length: int = 25,
        non_alpha_threshold: float = 0.5,
) -> bool:
    """Checks to see if the text passes all of the checks for a valid title.

    Parameters
    ----------
    text
        The input text to check
    title_max_word_length
        The maximum number of words a title can contain
    non_alpha_threshold
        The minimum number of alpha characters the text needs to be considered a title
    """

    # 文本长度为0的话，肯定不是title
    if len(text) == 0:
        print("Not a title. Text is empty.")
        return False

    # 文本中有标点符号，就不是title
    ENDS_IN_PUNCT_PATTERN = r"[^\w\s]\Z"
    ENDS_IN_PUNCT_RE = re.compile(ENDS_IN_PUNCT_PATTERN)
    if ENDS_IN_PUNCT_RE.search(text) is not None:
        return False

    # 小标题不包含书名号《》
    HAS_BOOK_MARK = r"《|》"
    HAS_BOOK_MARK_RE = re.compile(HAS_BOOK_MARK)
    if HAS_BOOK_MARK_RE.search(text) is not None:
        return False

    # 标题不包含英文
    HAS_ENGLISH = r'[a-zA-Z]+'
    HAS_ENGLISH_RE = re.compile(HAS_ENGLISH)
    if HAS_ENGLISH_RE.search(text) is not None:
        return False

    # 文本长度不能超过设定值，默认20
    # NOTE(robinson) - splitting on spaces here instead of word tokenizing because it
    # is less expensive and actual tokenization doesn't add much value for the length check
    if len(text) > title_max_word_length:
        return False

    # 文本中数字的占比不能太高，否则不是title
    if under_non_alpha_ratio(text, threshold=non_alpha_threshold):
        return False

    # NOTE(robinson) - Prevent flagging salutations like "To My Dearest Friends," as titles
    if text.endswith((",", ".", "，", "。")):
        return False

    if text.isnumeric():
        print(f"Not a title. Text is all numeric:\n\n{text}")  # type: ignore
        return False

    # 开头的字符内应该有数字，默认5个字符内
    if len(text) < 5:
        text_5 = text
    else:
        text_5 = text[:5]
    alpha_in_text_5 = sum(list(map(lambda x: x.isnumeric(), list(text_5))))
    if not alpha_in_text_5:
        return False

    return True


def zh_title_enhance(docs: Document) -> Document:
    title = None
    if len(docs) > 0:
        for doc in docs:
            if is_possible_title(doc.page_content):
                doc.metadata['category'] = 'cn_Title'
                title = doc.page_content
            elif title:
                doc.page_content = f"下文与({title})有关。{doc.page_content}"
        return docs
    else:
        print("文件不存在")


def find_title(text: str):
    title = []
    text_list = text.split('\n')
    for i in text_list:
        if is_possible_title(i):
            title.append(i)

    print(title)


find_title(doc)
