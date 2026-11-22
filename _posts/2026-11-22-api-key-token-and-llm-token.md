---
title: "API Keys and Tokens: Separate Identity from Units"
title_zh: "API Key 与 Token：先分清身份，再分清单位"
date: 2026-11-22
categories: [tech]
tags: [API, LLM, Learning Notes]
summary: "API Key, Access Token and the token inside a language model are often mixed together. One table separates credentials from text units, then walks through the shape of an API call."
deck_zh: "API Key、Access Token 和大模型里的 Token 常被混在一起。用一张表分清身份凭证与文本单位，再理解一次 API 调用的基本结构。"
---

<div class="seg">
<p class="en">When you learn / about APIs / and large language models, / three ideas / are easy to mix up: / an API Key, / an Access Token, / and the token / a model uses / when it reads text. //</p>
<p class="zh" lang="zh-Hans">学习 API 和大模型时，有三个概念很容易被混在一起：API Key、Access Token，以及模型处理文本时所说的 Token。</p>
</div>

<div class="seg">
<p class="en">The first two / are about / identity and permission; // the third / is about / how text gets split up. // Mixing them / makes many tutorials / look harder / than they really are. //</p>
<p class="zh" lang="zh-Hans">前两者和「身份、权限」有关，后者和「文本如何被切分」有关。把它们混在一起，会让很多教程看起来比实际更复杂。</p>
</div>

<h2>1. What an API is<span class="h-zh" lang="zh-Hans">1. API 是什么</span></h2>

<div class="seg">
<p class="en">Think of an API / as an agreed service window / between two systems. //</p>
<p class="zh" lang="zh-Hans">可以把 API 理解成系统之间约定好的服务窗口。</p>
</div>

<div class="seg">
<p class="en">The caller / does not need / to know / every internal detail. // It only has to follow / the agreed request method, / address, / parameters / and credential, / and it gets back / a structured result. // For a business system, / that result / might be customer data, / an order status, / or a piece of model-generated text. //</p>
<p class="zh" lang="zh-Hans">调用方不需要知道对方内部所有实现，只要按照约定提供请求方式、地址、参数和身份凭证，就能得到结构化结果。对业务系统来说，这个「结果」可能是客户资料、订单状态，也可能是一段模型生成的文本。</p>
</div>

<div class="seg">
<p class="en">A typical call / usually contains / these parts. //</p>
<p class="zh" lang="zh-Hans">一次典型调用通常包含以下几部分。</p>
</div>

<ul class="seg-list">
<li><span class="en">URL — / which resource / you want to reach. //</span><span class="zh" lang="zh-Hans">URL：要访问哪个资源。</span></li>
<li><span class="en">Method — / what you want to do, / such as GET to read / or POST to create. //</span><span class="zh" lang="zh-Hans">Method：要做什么，例如 GET 查询、POST 创建。</span></li>
<li><span class="en">Headers — / extra information / like identity / and content type. //</span><span class="zh" lang="zh-Hans">Headers：身份、内容类型等附加信息。</span></li>
<li><span class="en">Body — / the data / you submit. //</span><span class="zh" lang="zh-Hans">Body：需要提交的数据。</span></li>
<li><span class="en">Response — / the returned data / and a status code. //</span><span class="zh" lang="zh-Hans">Response：对方返回的数据和状态码。</span></li>
</ul>

<div class="seg">
<p class="en">JSON / is a common data format, / because objects, / fields / and arrays / can express / structured information. //</p>
<p class="zh" lang="zh-Hans">JSON 是常见的数据格式，因为它能用对象、字段和数组表达结构化信息。</p>
</div>

<h2>2. How an API Key differs from an Access Token<span class="h-zh" lang="zh-Hans">2. API Key 与 Access Token 有什么不同</span></h2>

<table class="seg-table">
<thead><tr><th>Concept<span class="h-zh" lang="zh-Hans">概念</span></th><th>Nature<span class="h-zh" lang="zh-Hans">本质</span></th><th>Common traits<span class="h-zh" lang="zh-Hans">常见特点</span></th><th>Main use<span class="h-zh" lang="zh-Hans">主要用途</span></th></tr></thead>
<tbody>
<tr><td><span class="en">API Key</span><span class="zh" lang="zh-Hans">API Key</span></td><td><span class="en">An application identity</span><span class="zh" lang="zh-Hans">应用身份标识</span></td><td><span class="en">Usually long-lived / and fixed</span><span class="zh" lang="zh-Hans">通常较长期、固定</span></td><td><span class="en">Identify which application / is calling</span><span class="zh" lang="zh-Hans">识别哪个应用在调用服务</span></td></tr>
<tr><td><span class="en">Access Token</span><span class="zh" lang="zh-Hans">Access Token</span></td><td><span class="en">A temporary credential / from one authorisation</span><span class="zh" lang="zh-Hans">一次授权得到的临时凭证</span></td><td><span class="en">Usually has an expiry / and a permission scope</span><span class="zh" lang="zh-Hans">通常有时效，可带权限范围</span></td><td><span class="en">Access resources / as a user / or an authorised context</span><span class="zh" lang="zh-Hans">代表某个用户或授权上下文访问资源</span></td></tr>
</tbody>
</table>

<div class="seg">
<p class="en">An API Key / is like / a building access card / for an application: // it tells the service / “which application has arrived”. //</p>
<p class="zh" lang="zh-Hans">API Key 更像一张应用门禁卡：它告诉服务方「哪个应用来了」。</p>
</div>

<div class="seg">
<p class="en">An Access Token / is like / a temporary visitor pass: // it not only proves identity, / but may also limit / what you can access, / what you can do, / and when it expires. //</p>
<p class="zh" lang="zh-Hans">Access Token 更像一张临时通行证：它不仅证明身份，还可能限定「能访问什么、能做什么、什么时候过期」。</p>
</div>

<div class="seg">
<p class="en">Real systems / may combine both, / or use fuller mechanisms / such as OAuth / or signed requests. // The key / is not memorising names — / it is asking: / who does this credential represent, / what permission does it carry, / and when does it stop working? //</p>
<p class="zh" lang="zh-Hans">实际系统可能组合使用两者，也可能采用 OAuth、签名请求等更完整的机制。关键不是背名词，而是先问：这个凭证代表谁，拥有什么权限，何时失效？</p>
</div>

<h2>3. The model token is a different thing entirely<span class="h-zh" lang="zh-Hans">3. 大模型里的 Token 是另一回事</span></h2>

<div class="seg">
<p class="en">With large language models, / a token / usually means / the basic unit / after text is split up. // It can be / a word, / a character, / a word fragment, / or even punctuation, / depending on / the tokenisation method / the model uses. //</p>
<p class="zh" lang="zh-Hans">在大模型语境中，Token 通常指文本被模型切分后的基本单位。它可以是一个词、一个字、一个词片段，甚至标点，具体取决于模型使用的分词方式。</p>
</div>

<div class="seg">
<p class="en">So: / an authentication token / is about / whether you can call; // a text token / is about / how the model handles input / and how usage is counted. //</p>
<p class="zh" lang="zh-Hans">所以：认证 Token 关系到「你能不能调用」；文本 Token 关系到「模型怎样处理输入，以及用量怎样计算」。</p>
</div>

<div class="seg">
<p class="en">When a document / says “token count”, / decide / whether it means / quota and text length, / or an identity credential. // The security implications / are completely different. //</p>
<p class="zh" lang="zh-Hans">看到文档写「token 数量」时，要判断它说的是额度与文本长度，还是身份凭证。两者的安全含义完全不同。</p>
</div>

<h2>4. What a request roughly looks like<span class="h-zh" lang="zh-Hans">4. 一个请求大致长什么样</span></h2>

<div class="seg">
<p class="en">Below / is only / a structural example — / it does not / correspond to / a real service. //</p>
<p class="zh" lang="zh-Hans">下面只是结构示例，不对应真实服务。</p>
</div>

<pre><code>GET /v1/weather?city=Hong%20Kong HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
Accept: application/json</code></pre>

<div class="seg">
<p class="en">A returned result / might look / like this. //</p>
<p class="zh" lang="zh-Hans">返回结果可能是这样。</p>
</div>

<pre><code>{
  "city": "Hong Kong",
  "temperature": 26,
  "unit": "celsius"
}</code></pre>

<div class="seg">
<p class="en">When reading a result like this, / look first / at the top-level fields, / then go / one layer at a time / into objects or arrays. // For a beginner, / being able to map / request fields / to response fields / matters more / than rushing / to memorise / the full syntax. //</p>
<p class="zh" lang="zh-Hans">阅读这类结果时，先看最外层有哪些字段，再逐层进入对象或数组。对初学者来说，能在请求字段和返回字段之间建立对应关系，比急着背完整语法更重要。</p>
</div>

<h2>5. What multimodality adds<span class="h-zh" lang="zh-Hans">5. 多模态又增加了什么</span></h2>

<div class="seg">
<p class="en">A traditional API / may send / only text / or structured fields. // A multimodal application / may handle / images, / speech, / video / and text / all at once. //</p>
<p class="zh" lang="zh-Hans">传统 API 可以只传文本或结构化字段，多模态应用则可能同时处理图像、语音、视频和文本。</p>
</div>

<div class="seg">
<p class="en">The value / is complementary information: / a photo gives visual content, / words add business context, / and structured rules / constrain / the output format. // But once / input types multiply, / you need / clearer validation, / error handling / and human review — / you cannot assume / the result is correct / just because / the model “understood it”. //</p>
<p class="zh" lang="zh-Hans">它的价值在于信息互补：一张照片提供视觉内容，文字说明补充业务背景，结构化规则再约束输出格式。但输入类型增多后，也要更明确地设计校验、错误处理和人工复核，不能因为模型「看懂了」就默认结果一定正确。</p>
</div>

<h2>6. Credential safety is a basic discipline<span class="h-zh" lang="zh-Hans">6. 凭证安全是基本功</span></h2>

<div class="seg">
<p class="en">Whichever key / or token you use, / keep a few hard rules in mind. //</p>
<p class="zh" lang="zh-Hans">无论使用哪种 Key 或 Token，都应遵守几条底线。</p>
</div>

<ol class="seg-list">
<li><span class="en">Never put / a real credential / into public notes, / screenshots, / code repositories / or front-end pages. //</span><span class="zh" lang="zh-Hans">不把真实凭证写进公开笔记、截图、代码仓库或前端页面。</span></li>
<li><span class="en">Use placeholders / such as YOUR_API_KEY / in examples. //</span><span class="zh" lang="zh-Hans">示例统一使用 YOUR_API_KEY 等占位符。</span></li>
<li><span class="en">Read credentials / from environment variables / or a secure secret store / in local projects. //</span><span class="zh" lang="zh-Hans">本地项目通过环境变量或安全的密钥管理方式读取。</span></li>
<li><span class="en">If one leaks, / revoke or rotate it / immediately — / do not just / delete the public file. //</span><span class="zh" lang="zh-Hans">一旦泄露，立即撤销或轮换，而不是只删除公开文件。</span></li>
<li><span class="en">Grant / only the minimum permission / the task needs. //</span><span class="zh" lang="zh-Hans">只授予完成任务所需的最小权限。</span></li>
</ol>

<div class="seg">
<p class="en">One line / to summarise. //</p>
<p class="zh" lang="zh-Hans">一句话总结。</p>
</div>

<blockquote><div class="seg">
<p class="en">API Keys and Access Tokens / answer / “who is calling / and what can they do”; // the model’s text token / answers / “how content is split / and measured”. // Separate the questions first, / then choose the concept. //</p>
<p class="zh" lang="zh-Hans">API Key 和 Access Token 解决「谁在调用、能做什么」；大模型的文本 Token 解决「内容怎样被切分和计量」。先分清问题，再选择概念。</p>
</div></blockquote>
