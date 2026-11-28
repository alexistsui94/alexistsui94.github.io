---
title: "API Keys, Access Tokens, and Model Tokens: Three Different Things"
date: 2026-11-22
published: false
categories: [tech]
topic: ai
tags: [API, LLM, Learning Notes]
summary: "Same word, three meanings. Two are about who is calling; one is about how text gets chopped up and billed. With a worked tokenisation example and one story about a leaked key."
---

<div class="seg">
<p class="en">If you read enough docs / about APIs and language models, / you meet three things / that all get called a token / or a key, / and they have almost nothing to do with each other. //</p>
</div>

<div class="seg">
<p class="en">Two of them answer / “who is calling, and what are they allowed to do.” // The third answers / “how is this text cut up, / and how much do I pay for it.” //</p>
</div>

<div class="seg">
<p class="en">Mixing them up / is why a two-page quickstart / can feel unreadable. // So let us keep them apart, / one at a time. //</p>
</div>

<h2>1. An API is a service counter</h2>

<div class="seg">
<p class="en">Think of a bank counter. // You do not walk into the vault. // You go to the window, / hand over a form, / show your ID, / and get something back. //</p>
</div>

<div class="seg">
<p class="en">An API is that window, / between two pieces of software. // You send a request in an agreed shape, / and you get a structured answer back. // The answer might be a customer record, / an order status, / or a paragraph of generated text. //</p>
</div>

<div class="seg">
<p class="en">Every request has roughly the same five parts. // Once you can name them, / most API documentation / stops being intimidating. //</p>
</div>

<ul class="seg-list">
<li><span class="en">URL — / which counter you are walking up to. //</span></li>
<li><span class="en">Method — / read something, / create something, / change it, / or remove it. //</span></li>
<li><span class="en">Headers — / small print: who you are, / and what format you speak. //</span></li>
<li><span class="en">Body — / the form you filled in. //</span></li>
<li><span class="en">Response — / the receipt, / with a status code on top. //</span></li>
</ul>

<h2>2. A key is a door card; a token is a visitor pass</h2>

<table class="seg-table">
<thead><tr><th>Thing</th><th>What it represents</th><th>How long it lasts</th></tr></thead>
<tbody>
<tr><td><span class="en">API Key</span></td><td><span class="en">The application / that is calling</span></td><td><span class="en">Usually months or years, / until someone rotates it</span></td></tr>
<tr><td><span class="en">Access Token</span></td><td><span class="en">A user, / or one specific permission</span></td><td><span class="en">Often minutes to hours, / and limited in scope</span></td></tr>
<tr><td><span class="en">Model token</span></td><td><span class="en">A piece of text</span></td><td><span class="en">Not a credential at all — / it is a unit of measure</span></td></tr>
</tbody>
</table>

<div class="seg">
<p class="en">An API key is the card / that opens the staff entrance. // It says “this application belongs here.” // It does not know / which human is behind it. //</p>
</div>

<div class="seg">
<p class="en">An access token is the visitor badge / you get at reception. // It is printed for one visit, / it says which floors you can reach, / and it expires at the end of the day / whether you are finished or not. //</p>
</div>

<div class="seg">
<p class="en">That difference matters in practice. // If a key leaks, / every call looks like the application. // If a token leaks, / it usually stops working / in a few hours, / and you can see exactly / what it was allowed to touch. //</p>
</div>

<div class="seg">
<p class="en">Real systems often use both, / or a fuller mechanism / like OAuth / or signed requests. // The habit worth keeping / is not memorising names. // It is asking three questions / about any credential: / who does it represent, / what can it do, / when does it stop working. //</p>
</div>

<h2>3. The model token is a completely different thing</h2>

<div class="seg">
<p class="en">Before a language model reads text, / the text is cut into pieces. // A piece can be a whole word, / part of a word, / a single character, / or a punctuation mark. // Those pieces are tokens. //</p>
</div>

<div class="seg">
<p class="en">A concrete example. // The English word “unbelievable” / is usually three tokens: / “un”, / “believ”, / “able”. // Six characters of meaning / compressed into three pieces. //</p>
</div>

<div class="seg">
<p class="en">Chinese behaves differently. // One character is often one token, / sometimes two characters share one. // So the same sentence / can cost very different amounts / depending on language — / which surprises people / when they compare bills. //</p>
</div>

<div class="seg">
<p class="en">Rough rule of thumb / for planning, not for billing: / one thousand English words / is around 1,300 tokens. // A long meeting transcript / is a few thousand. // A short chat reply / is a few hundred. //</p>
</div>

<div class="seg">
<p class="en">This is why “token limit” and “token expiry” / are unrelated sentences / that look related. // One is about length and cost. // The other is about access. //</p>
</div>

<h2>4. What a request looks like</h2>

<div class="seg">
<p class="en">A small example, / not tied to any real service. //</p>
</div>

<pre><code>GET /v1/weather?city=Hong%20Kong HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
Accept: application/json</code></pre>

<div class="seg">
<p class="en">And the answer. //</p>
</div>

<pre><code>{
  "city": "Hong Kong",
  "temperature": 26,
  "unit": "celsius"
}</code></pre>

<div class="seg">
<p class="en">When you read a response for the first time, / do it in one order. // Look at the outermost fields, / then open one object at a time. // Do not try to hold the whole structure / in your head. //</p>
</div>

<div class="seg">
<p class="en">The skill that pays off / is matching a field you sent / to a field you got back. // Syntax you can look up. // That mapping is what tells you / whether the thing actually worked. //</p>
</div>

<h2>5. Images and audio change the arithmetic</h2>

<div class="seg">
<p class="en">A text-only API sends text. // A multimodal one / can take an image, / a recording, / a video / and text, / and answer across all of them. //</p>
</div>

<div class="seg">
<p class="en">The practical difference / is that images are expensive to read. // One photo of a label / can cost more tokens / than a page of text, / because the model is not reading words — / it is looking at a grid of pixels. //</p>
</div>

<div class="seg">
<p class="en">More input types also means / more ways to be wrong. // A photo is blurry, a recording has background noise, / a scanned form is slightly rotated. // None of that shows up as an error. // It shows up as a confident wrong answer. //</p>
</div>

<h2>6. The one rule about credentials</h2>

<div class="seg">
<p class="en">I once pasted a key / into a file / and pushed it to a public repository / without thinking. // Within minutes / a bot had opened an issue / telling me the key was exposed. //</p>
</div>

<div class="seg">
<p class="en">Nothing bad happened, / because it was a test key / and I deleted it immediately. // But the lesson was clear: / the file being deleted / does not delete the key. // It is in the commit history, / and in whatever already copied it. //</p>
</div>

<div class="seg">
<p class="en">So the rules are short. //</p>
</div>

<ol class="seg-list">
<li><span class="en">Never put a real key / in a note, a screenshot, / a repository, / or front-end code. //</span></li>
<li><span class="en">In examples, / always use a placeholder / like YOUR_API_KEY. //</span></li>
<li><span class="en">Read keys from environment variables, / not from code. //</span></li>
<li><span class="en">If one leaks, / revoke it first / and delete the file second. //</span></li>
<li><span class="en">Give it the smallest permission / that still does the job. //</span></li>
</ol>

<div class="seg">
<p class="en">And that is the whole topic, / really. // A key says which application is calling. // An access token says who is asking / and what they may touch. // A model token is a piece of text, / counted for length and price. //</p>
</div>

<div class="seg">
<p class="en">Three different questions. // Three different words / that happen to look the same. //</p>
</div>
