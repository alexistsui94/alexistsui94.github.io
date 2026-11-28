---
title: "A Delivery Project, Reviewed Honestly"
title_zh: "一次交付复盘：三个当时没问清的问题"
date: 2026-03-12
categories: [projects]
topic: erp
tags: [ERP, Implementation]
summary: "Not a framework — three specific things that went wrong on one ERP delivery, what they cost, and the four checks I now run before calling a stage finished."
deck_zh: "不讲框架，讲一个 ERP 项目里真实出错的三个地方、各自付出了什么代价，以及我现在会在「算做完」之前先做的四项检查。"
---

<div class="seg">
<p class="en">This is not a methodology post. // It is one project, / with the parts / I would do differently. // Names and numbers are generalised, / but the shape of each problem / is exactly as it happened. //</p>
<p class="zh" lang="zh-Hans">这不是一篇方法论文章。就是一个项目，以及那些我会换个做法的地方。名字和数字做了模糊处理，但每个问题的形状都是原样。</p>
</div>

<div class="seg">
<p class="en">The client was a distributor / with five shops / and one warehouse. // Before the project / they ran on spreadsheets / and an old system / that only the warehouse team understood. //</p>
<p class="zh" lang="zh-Hans">客户是一个经销商，五个门店、一个仓库。项目之前主要靠 Excel，加一套只有仓库同事才弄得懂的旧系统。</p>
</div>

<div class="seg">
<p class="en">Six months, / five stages, / and one month after go-live / we were still fixing reports. // The system worked. // The rules were the problem. //</p>
<p class="zh" lang="zh-Hans">六个月，五个阶段，上线一个月后我们还在改报表。系统是能跑的，出问题的是规则。</p>
</div>

<h2>What the stages actually looked like<span class="h-zh" lang="zh-Hans">各阶段实际长什么样</span></h2>

<div class="seg">
<p class="en">The textbook version is clean: / requirements, / blueprint, / configuration, / testing, / go-live. // Here is the same list / with what actually happened. //</p>
<p class="zh" lang="zh-Hans">教科书版本很干净：需求、蓝图、配置、测试、上线。同样一份清单，换成实际发生的事是这样。</p>
</div>

<table class="seg-table">
<thead><tr><th>Stage<span class="h-zh" lang="zh-Hans">阶段</span></th><th>What it looked like<span class="h-zh" lang="zh-Hans">实际样子</span></th><th>What it cost<span class="h-zh" lang="zh-Hans">代价</span></th></tr></thead>
<tbody>
<tr><td><span class="en">Requirements</span><span class="zh" lang="zh-Hans">需求</span></td><td><span class="en">Four workshops, / each ending with / a list of “we will confirm later”</span><span class="zh" lang="zh-Hans">四场调研，每场都以「这个我们后面确认」收尾</span></td><td><span class="en">Three of those / came back in month five</span><span class="zh" lang="zh-Hans">其中三项在第五个月才回来</span></td></tr>
<tr><td><span class="en">Blueprint</span><span class="zh" lang="zh-Hans">蓝图</span></td><td><span class="en">A 40-page document / approved in a meeting / where two people read it</span><span class="zh" lang="zh-Hans">四十页文档，在一场只有两个人读过的会上通过</span></td><td><span class="en">Sign-off meant / less than we treated it</span><span class="zh" lang="zh-Hans">我们把签字的分量看得太重了</span></td></tr>
<tr><td><span class="en">Build and test</span><span class="zh" lang="zh-Hans">搭建与测试</span></td><td><span class="en">Working, / with a shared issue list / that kept growing</span><span class="zh" lang="zh-Hans">能跑，但共享问题清单一直在变长</span></td><td><span class="en">Two weeks lost / to one field meaning</span><span class="zh" lang="zh-Hans">为一个字段的含义丢掉两周</span></td></tr>
<tr><td><span class="en">Go-live</span><span class="zh" lang="zh-Hans">上线</span></td><td><span class="en">A weekend of imports / and three phone calls / after midnight</span><span class="zh" lang="zh-Hans">整个周末在导数据，半夜打了三通电话</span></td><td><span class="en">Old documents / matched about 90%</span><span class="zh" lang="zh-Hans">历史单据匹配率约 90%</span></td></tr>
<tr><td><span class="en">First month after</span><span class="zh" lang="zh-Hans">上线后第一个月</span></td><td><span class="en">Reports being rewritten / while people used them</span><span class="zh" lang="zh-Hans">边用边改报表</span></td><td><span class="en">Trust, mostly</span><span class="zh" lang="zh-Hans">主要是信任</span></td></tr>
</tbody>
</table>

<div class="seg">
<p class="en">Three of those rows / are really the same mistake, / made at three different times. // So let me take them one by one. //</p>
<p class="zh" lang="zh-Hans">这几行里其实有三处是同一个错误，只是在三个不同时间犯的。下面一件一件说。</p>
</div>

<h2>1. “We need approval” is not a requirement<span class="h-zh" lang="zh-Hans">一、「需要审批」不算需求</span></h2>

<div class="seg">
<p class="en">In the first workshop / the client said, / “when a purchase order is created, / it needs approval.” // Everyone nodded. // I wrote it down / exactly like that. //</p>
<p class="zh" lang="zh-Hans">第一场调研，客户说：「采购订单建好之后要审批。」所有人都点头。我就照这句话写进了文档。</p>
</div>

<div class="seg">
<p class="en">In month five / we found out what it meant. // Under 10,000 / one approver. // Over 10,000 / two. // Over 50,000 / three, / and the last one / was the finance director / who was often travelling. //</p>
<p class="zh" lang="zh-Hans">到第五个月才知道它的实际含义：一万以下一级审批，一万以上两级，五万以上三级，而最后一级是财务总监——他经常在出差。</p>
</div>

<div class="seg">
<p class="en">Return orders / did not need approval at all. // And there was one customer / whose orders always went by email, / then got entered the next morning, / which nobody had mentioned / because “everyone knows that”. //</p>
<p class="zh" lang="zh-Hans">退货单根本不走审批。还有一个客户，订单永远先走邮件，第二天早上再录进系统——这件事没人提，因为「大家都知道」。</p>
</div>

<div class="seg">
<p class="en">None of this was hidden. // It was just normal, / and normal things / do not get said out loud / unless someone asks / the boring questions. // Who starts it. / Who approves. / At what amount. / What happens after a rejection. / What about old documents. //</p>
<p class="zh" lang="zh-Hans">这些都不是秘密，只是太日常了。而太日常的事，除非有人问那些很笨的问题，否则不会有人说出来：谁发起、谁审批、多少钱以上、驳回之后怎么走、老单据怎么办。</p>
</div>

<div class="seg">
<p class="en">Now I ask those five questions / about every approval / before writing anything down. // It takes ten minutes / and it has never once / been a waste. //</p>
<p class="zh" lang="zh-Hans">现在每遇到一个审批，我都会先问这五个问题，再动笔写文档。花十分钟，从来没有一次是浪费。</p>
</div>

<h2>2. The demo promised something nobody built<span class="h-zh" lang="zh-Hans">二、演示承诺了没人做的东西</span></h2>

<div class="seg">
<p class="en">In the sales demo / there was a slide saying / “automatic reconciliation”. // It was true in a narrow sense: / the system could export both sides / in one format. //</p>
<p class="zh" lang="zh-Hans">售前演示里有一页写着「自动对账」。严格来说没错：系统可以把两边的数据导成同一种格式。</p>
</div>

<div class="seg">
<p class="en">The client heard “we click a button / and the difference is explained.” // That is not what the system does. // It shows you the difference / and waits for a human / to decide why. //</p>
<p class="zh" lang="zh-Hans">客户听到的是「点一下按钮，差异就解释清楚了」。系统并不是这样。它把差异摆出来，等人来判断原因。</p>
</div>

<div class="seg">
<p class="en">Nobody lied. // A slide got compressed, / a phrase travelled from sales / to the client / to the contract / to the blueprint, / and each step lost a little. // By the time it reached me / it was a promise. //</p>
<p class="zh" lang="zh-Hans">没有人撒谎。只是一页幻灯片被压缩，一句话从销售传到客户、传到合同、传到蓝图，每一步都掉一点。等传到我这里，它已经变成一个承诺了。</p>
</div>

<div class="seg">
<p class="en">What I would do differently / is small and unglamorous: / every phrase like that / gets rewritten / as a sentence with a subject and a verb / before it enters the blueprint. // “Automatic reconciliation” becomes / “the system lists unmatched items / and the finance team marks the reason.” //</p>
<p class="zh" lang="zh-Hans">我会改的地方很小，也不高级：凡是这种说法，在进入蓝图之前，都改写成一句有主语有动词的话。「自动对账」改写成「系统列出未匹配项，财务标注原因」。</p>
</div>

<div class="seg">
<p class="en">If the sentence sounds disappointing, / that is information. // It means the promise / was doing work / the product cannot do. //</p>
<p class="zh" lang="zh-Hans">如果改写后听起来让人失望，那本身就是信息：说明这个承诺在替产品做它做不到的事。</p>
</div>

<h2>3. The imports matched 90%, and 10% is a lot<span class="h-zh" lang="zh-Hans">三、历史数据匹配 90%，而 10% 很多</span></h2>

<div class="seg">
<p class="en">We migrated a few thousand / old documents. // About 90% matched cleanly. // Everyone relaxed. //</p>
<p class="zh" lang="zh-Hans">我们迁移了几千张历史单据，大约 90% 顺利匹配上。所有人都松了口气。</p>
</div>

<div class="seg">
<p class="en">But 10% of a few thousand / is a few hundred, / and each one of those / is a document someone has to open, / compare by hand, / and fix. // At two minutes each, / that is a working week. // It landed on one person. //</p>
<p class="zh" lang="zh-Hans">但几千的 10% 就是几百张，每一张都要有人打开、人工比对、修正。一张两分钟，加起来就是一整个工作周，全落在一个人身上。</p>
</div>

<div class="seg">
<p class="en">The cause was boring: / two systems used different item codes, / and the mapping table / had been maintained by hand / for years. // Some codes had been reused. / A few items had two codes. / One code pointed at a deleted item. //</p>
<p class="zh" lang="zh-Hans">原因很无聊：两个系统的物料编码规则不同，而映射表一直靠人手维护了好几年。有些编码被重复使用，有些物料有两个编码，还有一个编码指向一个已经删除的物料。</p>
</div>

<div class="seg">
<p class="en">The lesson is not / “test your data earlier”. // Everyone says that. // The lesson is that / 90% is not a passing grade / when the remaining 10% / becomes manual work / for one person / during the busiest week of their year. //</p>
<p class="zh" lang="zh-Hans">教训不是「要早点测数据」——每个人都会这么说。教训是：当剩下的 10% 会变成某个人一年里最忙那一周的手工活时，90% 不算及格。</p>
</div>

<h2>Four checks before I call a stage finished<span class="h-zh" lang="zh-Hans">说「做完了」之前，我先查四件事</span></h2>

<div class="seg">
<p class="en">I still use the same five stages. // What changed is the test / for whether one of them is done. //</p>
<p class="zh" lang="zh-Hans">阶段还是那五个，变的是「算不算做完」的判断标准。</p>
</div>

<ol class="seg-list">
<li><span class="en">Can the next person / start from a document, / without me explaining it in the corridor? //</span><span class="zh" lang="zh-Hans">下一个人能不能只看文档就开工，而不需要我在走廊上口头解释一遍？</span></li>
<li><span class="en">Is every “will confirm later” / written down / with a name / and a date? //</span><span class="zh" lang="zh-Hans">每一句「后面确认」，有没有写下来，并且带上名字和日期？</span></li>
<li><span class="en">Have I asked / who starts it, / who approves, / at what amount, / what happens after a rejection, / and what about old documents? //</span><span class="zh" lang="zh-Hans">有没有问过：谁发起、谁审批、多少钱以上、驳回后怎么走、老单据怎么办？</span></li>
<li><span class="en">If only 90% works, / who does the other 10% / and in which week? //</span><span class="zh" lang="zh-Hans">如果只有 90% 能用，剩下 10% 谁做，在哪一周做？</span></li>
</ol>

<div class="seg">
<p class="en">The project did go live, / and it is still running. // That is the normal ending. // Most projects are not saved by a clever idea; / they are saved by somebody / asking the boring question / one week earlier. //</p>
<p class="zh" lang="zh-Hans">这个项目确实上线了，现在也还在跑。这才是常见的结局。多数项目不是被什么巧妙的想法救回来的，而是被某个人提前一周问出那个很笨的问题救回来的。</p>
</div>
