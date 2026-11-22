---
title: "How a Software Project Actually Moves, Stage by Stage"
title_zh: "一个软件项目，实际上是怎么往前走的"
date: 2026-11-22
categories: [projects]
tags: [ERP, Delivery, Requirements]
summary: "The same six stages, but with what each one looks like on a real ERP project — the one-sentence requirement, the field that meant two things, and the report nobody printed the same way twice."
deck_zh: "还是那六个阶段，但换成真实 ERP 项目里的样子：一句需求、一个有两种意思的字段、一份谁也打不出一致格式的报表。"
---

<div class="seg">
<p class="en">Every article about project delivery / has the same diagram. / Opportunity, / requirements, / solution, / build, / go-live, / operations. // The diagram is correct. // It is also useless / until you know what each box / looks like on a Tuesday. //</p>
<p class="zh" lang="zh-Hans">讲项目交付的文章都有同一张图：商机、需求、方案、实施、上线、运营。图是对的，但在你知道每个格子在一个普通的星期二长什么样之前，它没什么用。</p>
</div>

<div class="seg">
<p class="en">So this is the same six stages, / with one concrete example each, / taken from ERP work. //</p>
<p class="zh" lang="zh-Hans">所以还是这六个阶段，但每个配一个 ERP 项目里的具体例子。</p>
</div>

<h2>The three-part view<span class="h-zh" lang="zh-Hans">先分三段看</span></h2>

<table class="seg-table">
<thead><tr><th>Stage<span class="h-zh" lang="zh-Hans">阶段</span></th><th>The question it answers<span class="h-zh" lang="zh-Hans">要回答的问题</span></th><th>What you should be able to hand over<span class="h-zh" lang="zh-Hans">应该能交出去的东西</span></th></tr></thead>
<tbody>
<tr><td><span class="en">Before signing</span><span class="zh" lang="zh-Hans">签约前</span></td><td><span class="en">Is this worth doing, / and can we actually do it?</span><span class="zh" lang="zh-Hans">值不值得做，我们真的做得了吗？</span></td><td><span class="en">A scope list, / a price, / and the parts / we are not promising</span><span class="zh" lang="zh-Hans">范围清单、价格，以及我们没承诺的部分</span></td></tr>
<tr><td><span class="en">Signing to go-live</span><span class="zh" lang="zh-Hans">签约到上线</span></td><td><span class="en">How exactly, / and how do we prove it works?</span><span class="zh" lang="zh-Hans">具体怎么做，怎么证明做成了？</span></td><td><span class="en">Confirmed rules, / test results, / and a cutover plan</span><span class="zh" lang="zh-Hans">确认过的规则、测试结果、切换方案</span></td></tr>
<tr><td><span class="en">After go-live</span><span class="zh" lang="zh-Hans">上线后</span></td><td><span class="en">Is anyone actually using it?</span><span class="zh" lang="zh-Hans">到底有没有人在用？</span></td><td><span class="en">Usage numbers, / a closed issue list, / and the next change</span><span class="zh" lang="zh-Hans">使用数据、已闭环的问题清单、下一步改动</span></td></tr>
</tbody>
</table>

<div class="seg">
<p class="en">That is the whole structure. // What follows is what fills it. //</p>
<p class="zh" lang="zh-Hans">结构就这些。下面说每个格子里装的是什么。</p>
</div>

<h2>1. Before signing: from one sentence to a price<span class="h-zh" lang="zh-Hans">一、签约前：从一句话到一份报价</span></h2>

<div class="seg">
<p class="en">The first version of a requirement / is usually one sentence. // On this project it was: / “we need to see stock.” // Six words, / and about four different meanings. //</p>
<p class="zh" lang="zh-Hans">需求的第一版通常只有一句话。这个项目里是：「我们要能看到库存。」六个字，大约有四种意思。</p>
</div>

<div class="seg">
<p class="en">Stock where — / one warehouse, or all of them? // Does it include goods on the way? // Does it include stock already reserved / for someone else? // Can a shop see the main warehouse / or only its own shelf? //</p>
<p class="zh" lang="zh-Hans">哪个仓的库存——一个仓还是全部？在途的算不算？已经被别人订走的算不算？门店能看到总仓，还是只看到自己货架上的？</p>
</div>

<div class="seg">
<p class="en">None of those questions / are technical. // All of them change the price. // “See stock” can be one screen / or three weeks / and an integration. //</p>
<p class="zh" lang="zh-Hans">这些问题一个都不技术，但每一个都会改变报价。「看库存」可能只是一个页面，也可能是三周工作量加一个接口。</p>
</div>

<div class="seg">
<p class="en">The other thing that happens here / is the quiet promise. // A demo shows something impressive, / the client remembers it, / and it never appears / in the scope list. // Six months later / someone finds it in a meeting minute / and asks why it is missing. //</p>
<p class="zh" lang="zh-Hans">这个阶段还会发生另一件事：悄悄许下的承诺。演示里展示了某个很亮眼的功能，客户记住了，但它从来没出现在范围清单里。六个月后有人在会议纪要里翻到，问为什么没做。</p>
</div>

<div class="seg">
<p class="en">The fix is unglamorous. // Anything shown in a demo / gets written into the scope list, / marked as included, / extra, / or not available. // Three words next to a line / saves an argument later. //</p>
<p class="zh" lang="zh-Hans">解决办法很朴素：演示里出现过的每一项，都写进范围清单，标成「包含」「额外收费」或「不支持」。在一行后面加三个字，能省掉后面一场争论。</p>
</div>

<h2>2. Delivery: turning words into rules<span class="h-zh" lang="zh-Hans">二、交付：把说法变成规则</span></h2>

<div class="seg">
<p class="en">“We need approval” / is enough to sign a contract. // It is not enough to configure anything. // Who starts it, / who approves, / at what amount, / how many levels, / what happens after a rejection, / and what to do with documents / created before the rule existed. //</p>
<p class="zh" lang="zh-Hans">「需要审批」足够签合同，但不够配置任何东西。谁发起、谁审批、多少钱以上、几级、驳回后怎么走、规则生效之前建的单据怎么办。</p>
</div>

<div class="seg">
<p class="en">The expensive one on this project / was a field. // “Available stock.” // Finance read it as / stock minus what is already sold. // The warehouse read it as / what is physically on the shelf, / including goods already promised. //</p>
<p class="zh" lang="zh-Hans">这个项目里最贵的是一个字段：「可用库存」。财务理解成「减掉已卖出的」，仓库理解成「货架上实际有的，包括已经答应给别人的」。</p>
</div>

<div class="seg">
<p class="en">Both were reasonable. // Both had been true / in the old spreadsheets, / in different columns, / maintained by different people. // We found out in testing, / two weeks before go-live, / when two reports / disagreed by a few hundred units. //</p>
<p class="zh" lang="zh-Hans">两边都合理。在旧的 Excel 里两种口径都成立，只是在不同列，由不同的人维护。我们是在测试阶段才发现的，离上线两周，两张报表差了几百件。</p>
</div>

<div class="seg">
<p class="en">The lesson was not / “define your fields”. // It was that / a word everyone uses daily / is the most dangerous word in the room, / because nobody thinks / it needs defining. //</p>
<p class="zh" lang="zh-Hans">教训不是「要把字段定义清楚」。而是：一个大家每天都在用的词，是会议室里最危险的词，因为没人觉得它需要被定义。</p>
</div>

<div class="seg">
<p class="en">So now the blueprint has a page / that is only definitions. // Not the technical data dictionary — / a plain list: / this word, / what it means here, / and what it does not include. // It is the least interesting page / and the one that gets quoted / three months later. //</p>
<p class="zh" lang="zh-Hans">所以现在蓝图里有一页只写定义。不是技术数据字典，就是一张大白话清单：这个词、在这里是什么意思、不包括什么。这是全篇最无聊的一页，也是三个月后唯一会被引用的那一页。</p>
</div>

<h2>3. Testing: the part that decides whether people trust it<span class="h-zh" lang="zh-Hans">三、测试：决定用户信不信的那一段</span></h2>

<div class="seg">
<p class="en">A system that runs / is not a system people trust. // The difference is usually small: / a total that is off by two decimal places, / a printout that wraps onto a second page, / a search that is one second slower / than the old one. //</p>
<p class="zh" lang="zh-Hans">系统能跑，不等于用户信它。差别通常很小：合计差两位小数、打印单多出一页、搜索比旧的慢一秒。</p>
</div>

<div class="seg">
<p class="en">On this project / the finance team ran three days of real documents / through the system, / then compared totals with the old one. // Two matched. // One was off by 0.02, / every time, / on the same kind of order. //</p>
<p class="zh" lang="zh-Hans">这个项目里，财务用三天真实单据跑了一遍系统，再和旧系统对总数。两张对上了，第三张每次都差 0.02，而且只出现在同一类订单上。</p>
</div>

<div class="seg">
<p class="en">It was a rounding rule. // Nobody would have written it down. // Someone would have found it / in month two, / and by then / every number in the system / would have been slightly suspect. //</p>
<p class="zh" lang="zh-Hans">是一个舍入规则。没有人会主动把它写下来。等到第二个月才有人发现，到那时候系统里每个数字都会显得有点可疑。</p>
</div>

<div class="seg">
<p class="en">That is what UAT is really for. // Not proving the software works — / we can test that ourselves. // It is letting the people who own the numbers / find the thing / we would never have thought to check. //</p>
<p class="zh" lang="zh-Hans">这才是 UAT 真正的用处。不是证明软件能跑——那个我们自己能测。而是让对那些数字负责的人，找出我们根本想不到要去检查的地方。</p>
</div>

<h2>4. After go-live: the quiet failure<span class="h-zh" lang="zh-Hans">四、上线后：安静的失败</span></h2>

<div class="seg">
<p class="en">Go-live went fine. // Two weeks later / we looked at who was logging in. // Three people. // Out of about twenty / who were supposed to use it daily. //</p>
<p class="zh" lang="zh-Hans">上线很顺利。两周后我们看了一下登录记录：三个人。而本来应该每天用它的，大约有二十个。</p>
</div>

<div class="seg">
<p class="en">The reason was not resistance. // The picking list printed / in a different layout / from the old one, / and the warehouse staff / had a routine built around that layout / for eleven years. // They were not refusing the system. // They were printing from the system, / then retyping it / into an old template. //</p>
<p class="zh" lang="zh-Hans">原因不是抵触。拣货单打印出来的版式和旧的不一样，而仓库同事围绕那个版式形成了十一年的习惯。他们不是拒绝系统，而是从系统里打印出来，再手抄回旧模板。</p>
</div>

<div class="seg">
<p class="en">Nobody complains about that. // They just quietly do the work twice. // Which is why “is it live?” / is a much weaker question / than “who did what they used to do, / and why?” //</p>
<p class="zh" lang="zh-Hans">这种事没人投诉。他们只是安静地把活干两遍。所以「上线了吗」这个问题，比「谁还在按老办法做，为什么」要弱得多。</p>
</div>

<div class="seg">
<p class="en">We changed the layout. // It took half a day. // It would have taken ten minutes / if we had asked / before go-live. //</p>
<p class="zh" lang="zh-Hans">我们改了版式，花了半天。如果在上线前问过一句，本来只要十分钟。</p>
</div>

<h2>Two things I would tell someone starting<span class="h-zh" lang="zh-Hans">如果重来，我会先说两句</span></h2>

<div class="seg">
<p class="en">First: the work is not / writing documents. // It is getting a specific person / to say a specific sentence / in front of other people, / so it cannot quietly change later. //</p>
<p class="zh" lang="zh-Hans">第一：这份活不是写文档，而是让某个具体的人，在其他人在场的时候，把某句具体的话说出来，这样它后面就没法悄悄改掉。</p>
</div>

<div class="seg">
<p class="en">Second: every stage ends / when the next person can move / without asking you anything. // Not when the file is finished. // When you are no longer needed. //</p>
<p class="zh" lang="zh-Hans">第二：每个阶段的结束点，是下一个人不需要问你任何事就能继续。不是文件写完，而是你不再被需要。</p>
</div>

<div class="seg">
<p class="en">That is a low bar / and most projects / do not reach it. // Which is why the same diagram / keeps getting drawn. //</p>
<p class="zh" lang="zh-Hans">这个标准不高，但多数项目达不到。这也是为什么同一张图一直被重新画一遍。</p>
</div>
