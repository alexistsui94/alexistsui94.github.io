---
title: "API Keys, Access Tokens, and Model Tokens: Three Different Things"
title_zh: "API Key、Access Token、模型 Token：三件不同的事"
date: 2026-11-22
categories: [tech]
topic: ai
tags: [API, LLM, Learning Notes]
summary: "Same word, three meanings. Two are about who is calling; one is about how text gets chopped up and billed. With a worked tokenisation example and one story about a leaked key."
deck_zh: "同一个词，三种意思。前两个讲「谁在调用」，第三个讲「文字怎么被切开、怎么计费」。附一个分词实例，和一个泄露 Key 的真实后果。"
---

<div class="seg">
<p class="en">If you read enough docs / about APIs and language models, / you meet three things / that all get called a token / or a key, / and they have almost nothing to do with each other. //</p>
<p class="zh" lang="zh-Hans">看多了 API 和大模型的文档，会碰到三样东西都被叫做 token 或 key，而它们彼此几乎没关系。</p>
</div>

<div class="seg">
<p class="en">Two of them answer / “who is calling, and what are they allowed to do.” // The third answers / “how is this text cut up, / and how much do I pay for it.” //</p>
<p class="zh" lang="zh-Hans">前两个回答「谁在调用、能做什么」，第三个回答「这段文字怎么被切开、我要付多少钱」。</p>
</div>

<div class="seg">
<p class="en">Mixing them up / is why a two-page quickstart / can feel unreadable. // So let us keep them apart, / one at a time. //</p>
<p class="zh" lang="zh-Hans">把这两类混在一起，是两页的快速上手文档读起来像天书的原因。所以一件一件分开说。</p>
</div>

<h2>1. An API is a service counter<span class="h-zh" lang="zh-Hans">一、API 是一个服务窗口</span></h2>

<div class="seg">
<p class="en">Think of a bank counter. // You do not walk into the vault. // You go to the window, / hand over a form, / show your ID, / and get something back. //</p>
<p class="zh" lang="zh-Hans">想象一个银行柜台。你不会走进金库，你到窗口前，递一张单子、出示证件，然后拿到一个结果。</p>
</div>

<div class="seg">
<p class="en">An API is that window, / between two pieces of software. // You send a request in an agreed shape, / and you get a structured answer back. // The answer might be a customer record, / an order status, / or a paragraph of generated text. //</p>
<p class="zh" lang="zh-Hans">API 就是两个软件之间的那个窗口。你按约定的格式递一个请求，拿回一个结构化的答复。答复可能是一条客户资料、一个订单状态，或者一段生成的文字。</p>
</div>

<div class="seg">
<p class="en">Every request has roughly the same five parts. // Once you can name them, / most API documentation / stops being intimidating. //</p>
<p class="zh" lang="zh-Hans">每个请求大致都由五个部分组成。能叫出这五个名字，多数 API 文档就不再吓人了。</p>
</div>

<ul class="seg-list">
<li><span class="en">URL — / which counter you are walking up to. //</span><span class="zh" lang="zh-Hans">URL：你走向哪个窗口。</span></li>
<li><span class="en">Method — / read something, / create something, / change it, / or remove it. //</span><span class="zh" lang="zh-Hans">Method：读取、创建、修改，还是删除。</span></li>
<li><span class="en">Headers — / small print: who you are, / and what format you speak. //</span><span class="zh" lang="zh-Hans">Headers：附加说明——你是谁、用什么格式。</span></li>
<li><span class="en">Body — / the form you filled in. //</span><span class="zh" lang="zh-Hans">Body：你填好的那张单子。</span></li>
<li><span class="en">Response — / the receipt, / with a status code on top. //</span><span class="zh" lang="zh-Hans">Response：回执，最上面有一个状态码。</span></li>
</ul>

<h2>2. A key is a door card; a token is a visitor pass<span class="h-zh" lang="zh-Hans">二、Key 是门禁卡，Token 是访客证</span></h2>

<table class="seg-table">
<thead><tr><th>Thing<span class="h-zh" lang="zh-Hans">概念</span></th><th>What it represents<span class="h-zh" lang="zh-Hans">代表什么</span></th><th>How long it lasts<span class="h-zh" lang="zh-Hans">有效期</span></th></tr></thead>
<tbody>
<tr><td><span class="en">API Key</span><span class="zh" lang="zh-Hans">API Key</span></td><td><span class="en">The application / that is calling</span><span class="zh" lang="zh-Hans">调用它的那个应用</span></td><td><span class="en">Usually months or years, / until someone rotates it</span><span class="zh" lang="zh-Hans">通常几个月到几年，直到有人主动更换</span></td></tr>
<tr><td><span class="en">Access Token</span><span class="zh" lang="zh-Hans">Access Token</span></td><td><span class="en">A user, / or one specific permission</span><span class="zh" lang="zh-Hans">某个用户，或某一项具体权限</span></td><td><span class="en">Often minutes to hours, / and limited in scope</span><span class="zh" lang="zh-Hans">常常只有几分钟到几小时，且权限受限</span></td></tr>
<tr><td><span class="en">Model token</span><span class="zh" lang="zh-Hans">模型 Token</span></td><td><span class="en">A piece of text</span><span class="zh" lang="zh-Hans">一段文字</span></td><td><span class="en">Not a credential at all — / it is a unit of measure</span><span class="zh" lang="zh-Hans">根本不是凭证，只是一个计量单位</span></td></tr>
</tbody>
</table>

<div class="seg">
<p class="en">An API key is the card / that opens the staff entrance. // It says “this application belongs here.” // It does not know / which human is behind it. //</p>
<p class="zh" lang="zh-Hans">API Key 是打开员工通道的那张卡。它说明「这个应用是自己人」，但它不知道背后是哪一个具体的人。</p>
</div>

<div class="seg">
<p class="en">An access token is the visitor badge / you get at reception. // It is printed for one visit, / it says which floors you can reach, / and it expires at the end of the day / whether you are finished or not. //</p>
<p class="zh" lang="zh-Hans">Access Token 是前台给你的访客证。它只为这一次来访打印，写明你能去哪些楼层，到下班时间就失效——不管你事情做没做完。</p>
</div>

<div class="seg">
<p class="en">That difference matters in practice. // If a key leaks, / every call looks like the application. // If a token leaks, / it usually stops working / in a few hours, / and you can see exactly / what it was allowed to touch. //</p>
<p class="zh" lang="zh-Hans">这个区别在实务上很重要。Key 泄露了，所有调用看起来都像那个应用；Token 泄露了，通常几小时后就失效，而且能查清它被允许碰哪些东西。</p>
</div>

<div class="seg">
<p class="en">Real systems often use both, / or a fuller mechanism / like OAuth / or signed requests. // The habit worth keeping / is not memorising names. // It is asking three questions / about any credential: / who does it represent, / what can it do, / when does it stop working. //</p>
<p class="zh" lang="zh-Hans">实际系统常常两者都用，或者用 OAuth、签名请求这类更完整的机制。值得养成的习惯不是背名词，而是对任何凭证都问三句：它代表谁、它能做什么、它什么时候失效。</p>
</div>

<h2>3. The model token is a completely different thing<span class="h-zh" lang="zh-Hans">三、模型 Token 完全是另一回事</span></h2>

<div class="seg">
<p class="en">Before a language model reads text, / the text is cut into pieces. // A piece can be a whole word, / part of a word, / a single character, / or a punctuation mark. // Those pieces are tokens. //</p>
<p class="zh" lang="zh-Hans">大模型读文字之前，会先把文字切成小块。一块可能是一个完整的词、词的一部分、一个字，或者一个标点。这些小块就是 token。</p>
</div>

<div class="seg">
<p class="en">A concrete example. // The English word “unbelievable” / is usually three tokens: / “un”, / “believ”, / “able”. // Six characters of meaning / compressed into three pieces. //</p>
<p class="zh" lang="zh-Hans">举个具体的例子。英文词 “unbelievable” 通常是三个 token：“un”、“believ”、“able”。三个片段合起来才是完整的意思。</p>
</div>

<div class="seg">
<p class="en">Chinese behaves differently. // One character is often one token, / sometimes two characters share one. // So the same sentence / can cost very different amounts / depending on language — / which surprises people / when they compare bills. //</p>
<p class="zh" lang="zh-Hans">中文的表现不一样。通常一个字就是一个 token，有时两个字合成一个。所以同一句话，用不同语言写，成本可能差很远——这也是对比账单时最让人意外的点。</p>
</div>

<div class="seg">
<p class="en">Rough rule of thumb / for planning, not for billing: / one thousand English words / is around 1,300 tokens. // A long meeting transcript / is a few thousand. // A short chat reply / is a few hundred. //</p>
<p class="zh" lang="zh-Hans">一个粗略的经验值，用来做预算而不是对账：一千个英文单词大约 1,300 个 token；一场长会议的文字记录是几千；一段简短的对话回复是几百。</p>
</div>

<div class="seg">
<p class="en">This is why “token limit” and “token expiry” / are unrelated sentences / that look related. // One is about length and cost. // The other is about access. //</p>
<p class="zh" lang="zh-Hans">这就是为什么「token 上限」和「token 过期」是两句毫无关系的话，却看起来像有关系。一个讲长度和成本，一个讲访问权限。</p>
</div>

<h2>4. What a request looks like<span class="h-zh" lang="zh-Hans">四、一个请求长什么样</span></h2>

<div class="seg">
<p class="en">A small example, / not tied to any real service. //</p>
<p class="zh" lang="zh-Hans">一个小例子，不对应任何真实服务。</p>
</div>

<pre><code>GET /v1/weather?city=Hong%20Kong HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
Accept: application/json</code></pre>

<div class="seg">
<p class="en">And the answer. //</p>
<p class="zh" lang="zh-Hans">返回是这样。</p>
</div>

<pre><code>{
  "city": "Hong Kong",
  "temperature": 26,
  "unit": "celsius"
}</code></pre>

<div class="seg">
<p class="en">When you read a response for the first time, / do it in one order. // Look at the outermost fields, / then open one object at a time. // Do not try to hold the whole structure / in your head. //</p>
<p class="zh" lang="zh-Hans">第一次读一个返回结果，按一个固定顺序来：先看最外层有哪些字段，然后一次打开一层。不要试图把整个结构一次装进脑子里。</p>
</div>

<div class="seg">
<p class="en">The skill that pays off / is matching a field you sent / to a field you got back. // Syntax you can look up. // That mapping is what tells you / whether the thing actually worked. //</p>
<p class="zh" lang="zh-Hans">真正有用的能力，是把你发出去的字段和收回来的字段对上。语法可以随时查，但这个对应关系才是判断「到底成不成」的依据。</p>
</div>

<h2>5. Images and audio change the arithmetic<span class="h-zh" lang="zh-Hans">五、图片和语音会改变算法</span></h2>

<div class="seg">
<p class="en">A text-only API sends text. // A multimodal one / can take an image, / a recording, / a video / and text, / and answer across all of them. //</p>
<p class="zh" lang="zh-Hans">纯文本的 API 只传文字。多模态的可以接收图片、录音、视频和文字，并综合起来回答。</p>
</div>

<div class="seg">
<p class="en">The practical difference / is that images are expensive to read. // One photo of a label / can cost more tokens / than a page of text, / because the model is not reading words — / it is looking at a grid of pixels. //</p>
<p class="zh" lang="zh-Hans">实务上的差别是：读图很贵。一张标签照片消耗的 token，可能比一整页文字还多，因为模型不是在看字，而是在看一片像素。</p>
</div>

<div class="seg">
<p class="en">More input types also means / more ways to be wrong. // A photo is blurry, a recording has background noise, / a scanned form is slightly rotated. // None of that shows up as an error. // It shows up as a confident wrong answer. //</p>
<p class="zh" lang="zh-Hans">输入类型变多，也意味着出错的方式变多。照片糊了、录音有背景噪音、扫描件歪了一点。这些都不会报错，只会变成一个自信的错误答案。</p>
</div>

<h2>6. The one rule about credentials<span class="h-zh" lang="zh-Hans">六、关于凭证，只有一条规矩</span></h2>

<div class="seg">
<p class="en">I once pasted a key / into a file / and pushed it to a public repository / without thinking. // Within minutes / a bot had opened an issue / telling me the key was exposed. //</p>
<p class="zh" lang="zh-Hans">我有一次把一个 key 贴进文件，然后没多想就推到了公开仓库。几分钟之内，就有机器人开了一个 issue 告诉我这个 key 暴露了。</p>
</div>

<div class="seg">
<p class="en">Nothing bad happened, / because it was a test key / and I deleted it immediately. // But the lesson was clear: / the file being deleted / does not delete the key. // It is in the commit history, / and in whatever already copied it. //</p>
<p class="zh" lang="zh-Hans">没出事，因为那是测试用的 key，我也立刻删掉了。但教训很清楚：删掉文件不等于删掉 key。它还在提交历史里，也在已经复制走它的地方。</p>
</div>

<div class="seg">
<p class="en">So the rules are short. //</p>
<p class="zh" lang="zh-Hans">所以规矩很短。</p>
</div>

<ol class="seg-list">
<li><span class="en">Never put a real key / in a note, a screenshot, / a repository, / or front-end code. //</span><span class="zh" lang="zh-Hans">真实 key 不写进笔记、截图、代码仓库或前端代码。</span></li>
<li><span class="en">In examples, / always use a placeholder / like YOUR_API_KEY. //</span><span class="zh" lang="zh-Hans">示例里一律用 YOUR_API_KEY 这样的占位符。</span></li>
<li><span class="en">Read keys from environment variables, / not from code. //</span><span class="zh" lang="zh-Hans">key 从环境变量读，不要写在代码里。</span></li>
<li><span class="en">If one leaks, / revoke it first / and delete the file second. //</span><span class="zh" lang="zh-Hans">一旦泄露，先撤销，再删文件——顺序不能反。</span></li>
<li><span class="en">Give it the smallest permission / that still does the job. //</span><span class="zh" lang="zh-Hans">只给完成这件事所需的最小权限。</span></li>
</ol>

<div class="seg">
<p class="en">And that is the whole topic, / really. // A key says which application is calling. // An access token says who is asking / and what they may touch. // A model token is a piece of text, / counted for length and price. //</p>
<p class="zh" lang="zh-Hans">这个题目其实就这些。Key 说明哪个应用在调用；Access Token 说明是谁在请求、可以碰什么；模型 Token 就是一段被切开并计价的文字。</p>
</div>

<div class="seg">
<p class="en">Three different questions. // Three different words / that happen to look the same. //</p>
<p class="zh" lang="zh-Hans">三个不同的问题，三个碰巧长得一样的词。</p>
</div>
