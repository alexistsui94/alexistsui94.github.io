---
title: "How I Actually Use AI Tools at Work"
title_zh: "我实际上怎么用 AI 工具"
date: 2026-03-12
categories: [tech]
topic: ai
tags: [AI, Python, Automation]
summary: "Four tasks I really hand to AI — meeting notes, spreadsheet formulas, emails, error messages — with what it got wrong each time and the one habit that keeps it useful."
deck_zh: "四个我真的会交给 AI 的任务：会议记录、表格公式、邮件、报错信息。每次都写清它错在哪里，以及我一直保留的那个习惯。"
---

<div class="seg">
<p class="en">A lot of people say / they use AI every day. // I say it too. // But when I actually write the list down, / it is shorter / and more boring / than it sounds. //</p>
<p class="zh" lang="zh-Hans">很多人说自己每天都在用 AI。我也这么说。但真的把清单写下来，其实没那么夸张，甚至有点无聊。</p>
</div>

<div class="seg">
<p class="en">Here are the four things / I really hand over, / and how much checking / each one still needs. //</p>
<p class="zh" lang="zh-Hans">下面四件事，是我真的会交出去的，以及每件事之后我还要花多少时间检查。</p>
</div>

<h2>1. Meeting notes into an action list<span class="h-zh" lang="zh-Hans">一、会议记录变成行动清单</span></h2>

<div class="seg">
<p class="en">A one-hour meeting / with eight people / has maybe forty minutes / worth keeping. // The rest is finding the right screen, / repeating a question, / and waiting for someone to come back from lunch. //</p>
<p class="zh" lang="zh-Hans">八个人开一小时的会，真正值得留下的内容大概四十分钟。其余时间在找画面、重复问同一个问题、等人吃完午饭回来。</p>
</div>

<div class="seg">
<p class="en">So I record it, / let the tool summarise, / and ask for one thing only: / a table of actions / with an owner / and a date. // I do not ask for a beautiful summary. // Summaries read nice / and change nothing. //</p>
<p class="zh" lang="zh-Hans">所以我会录音，让工具做摘要，但只提一个要求：把行动项列成表，每条带负责人和期限。我不要漂亮的摘要——摘要读起来舒服，但什么都不会改变。</p>
</div>

<div class="seg">
<p class="en">It gets the topics right / almost every time. // It gets the owners wrong / once or twice per meeting, / usually when two people / talk over each other. //</p>
<p class="zh" lang="zh-Hans">议题几乎每次都抓得对。负责人每场会错一两个，通常发生在两个人抢话的时候。</p>
</div>

<div class="seg">
<p class="en">So I read the list / and fix the names myself. // Five minutes / to save about thirty. // That trade is worth it, / but only because I read it. //</p>
<p class="zh" lang="zh-Hans">所以我会读一遍，自己改名字。花五分钟，省半小时。这笔交易划算——但前提是我真的读了。</p>
</div>

<h2>2. Formulas and small scripts<span class="h-zh" lang="zh-Hans">二、公式和小脚本</span></h2>

<div class="seg">
<p class="en">I am not a programmer. // I can read code / and roughly follow it, / but I cannot write it from nothing. // That is exactly the gap / where these tools help me most. //</p>
<p class="zh" lang="zh-Hans">我不是程序员。我能读代码、大致跟得上逻辑，但没法从零写出来。这正好是这类工具最帮得上忙的地方。</p>
</div>

<div class="seg">
<p class="en">Last month / I had to match two product lists / that used different item codes — / one from an old system, / one from the new one. // I described the columns / and what I wanted, / in plain language. // A working Python script came back / in about a minute. //</p>
<p class="zh" lang="zh-Hans">上个月，我要比对两份产品清单，两边的物料编码规则不一样——一份来自旧系统，一份来自新系统。我用大白话描述了有哪些列、想要什么结果，一分钟左右就拿到一个能跑的 Python 脚本。</p>
</div>

<div class="seg">
<p class="en">The first version / compared the wrong column. // It matched on the product name / instead of the code. // I noticed / because the match rate came back at 97% / on data that should have been about 60%. //</p>
<p class="zh" lang="zh-Hans">第一版比错了列——它拿品名去匹配，而不是编码。我会发现，是因为它给出的匹配率是 97%，而这批数据按理只该在 60% 左右。</p>
</div>

<div class="seg">
<p class="en">That number is the reason / I still check output. // Not because I distrust the tool, / but because 97% looked too good, / and too good is usually wrong. //</p>
<p class="zh" lang="zh-Hans">正是这个数字让我仍然会核对结果。不是不信任工具，而是 97% 好得不对劲，而好得不对劲通常就是错的。</p>
</div>

<h2>3. Emails and documents<span class="h-zh" lang="zh-Hans">三、邮件和文档</span></h2>

<div class="seg">
<p class="en">For emails, / I write the point first, / badly, / in Chinese or English. // Then I ask the tool / to make it calmer / and shorter. //</p>
<p class="zh" lang="zh-Hans">写邮件时，我先用中文或英文把要点写下来，写得很难看也没关系。然后让工具把它改得平和一点、短一点。</p>
</div>

<div class="seg">
<p class="en">I almost never send the first draft. // And the useful part / is not the wording — / it is that I had to say / what I actually wanted / in one sentence / before asking. //</p>
<p class="zh" lang="zh-Hans">我几乎从不直接发出第一版。真正有用的也不是措辞，而是在提要求之前，我必须先想清楚自己到底想要什么，并且用一句话讲出来。</p>
</div>

<div class="seg">
<p class="en">The same goes for long documents. // Ask for a rewrite / and it tidies the language. // Ask for “what is missing here?” / and it is suddenly useful, / because it lists the gaps / I stopped seeing / after the third read. //</p>
<p class="zh" lang="zh-Hans">长文档也一样。让它改写，它只是把文字理顺；但问它「这里还缺什么」，它突然就有用了——它会列出我读到第三遍已经看不见的那些缺口。</p>
</div>

<h2>4. Error messages<span class="h-zh" lang="zh-Hans">四、报错信息</span></h2>

<div class="seg">
<p class="en">When something breaks, / I paste the error / and ask two things: / what does this mean, / and what should I check first. //</p>
<p class="zh" lang="zh-Hans">出问题的时候，我会把报错贴过去，问两件事：这是什么意思，我应该先查哪里。</p>
</div>

<div class="seg">
<p class="en">Nine times out of ten / the answer is enough / to tell me one useful thing: / whether the problem is mine, / the data, / or the system. // That alone saves / a round of messages / with someone else. //</p>
<p class="zh" lang="zh-Hans">十次里有九次，答案足够告诉我一件有用的事：问题出在我这边、数据，还是系统。光这一点，就省掉一轮跟别人来回问的时间。</p>
</div>

<h2>Where it goes wrong<span class="h-zh" lang="zh-Hans">它在哪里出错</span></h2>

<div class="seg">
<p class="en">The failure I see most / is confident invention. // Ask about a table / and it will describe a column / that does not exist, / in exactly the same tone / it uses for the columns that do. //</p>
<p class="zh" lang="zh-Hans">我见得最多的失误，是「自信地编」。问它一张表的结构，它会描述一个根本不存在的字段，而语气跟描述真字段时一模一样。</p>
</div>

<div class="seg">
<p class="en">It is not lying. // It is filling a gap / because a gap looks like a mistake. // Which means / every field name, / every number / and every date / has to come from somewhere / I can point at. //</p>
<p class="zh" lang="zh-Hans">它不是在撒谎，它是在填空，因为留空看起来像错误。所以每一个字段名、每一个数字、每一个日期，都必须来自一个我能指出来的地方。</p>
</div>

<div class="seg">
<p class="en">The second failure / is length. // Hand it a forty-page document / and it reads the beginning well, / the middle roughly, / and the end / not at all. //</p>
<p class="zh" lang="zh-Hans">第二个失误是长度。给它一份四十页的文档，开头读得仔细，中间读个大概，结尾基本没读。</p>
</div>

<h2>The one habit I keep<span class="h-zh" lang="zh-Hans">我保留的那一个习惯</span></h2>

<div class="seg">
<p class="en">Before I automate anything, / I write three lines: / what goes in, / what rule applies, / what should come out. // If I cannot write those three lines, / the tool will not help me. // It will only make the confusion / arrive faster. //</p>
<p class="zh" lang="zh-Hans">在自动化任何事之前，我会先写三行：输入是什么、按什么规则、应该产出什么。如果这三行写不出来，工具帮不了我，它只会让混乱更快地到达。</p>
</div>

<div class="seg">
<p class="en">So the honest summary is this. // These tools save typing time / and searching time. // They do not save judgement time. // That part / is still mine, / and it is still the slow part. //</p>
<p class="zh" lang="zh-Hans">所以老实说：这类工具省的是打字和查找的时间，不是判断的时间。判断那一段仍然是我的，也仍然是慢的那一段。</p>
</div>
