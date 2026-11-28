---
title: "Vibe Coding, in Plain English: The Words That Change the Output"
date: 2026-11-28
categories: [tech]
topic: ai
tags: [AI, Vibe Coding, Agents, Context]
summary: "The vocabulary of AI coding, cut down to the terms that change what comes out — token, context window, prompt, agent, MCP, RAG — and the line where vibe coding stops being enough."
---

<div class="seg">
<p class="en">“Vibe coding” was coined in February 2025 / for something simple: / you describe what you want, / the model writes the code, / and you judge the result / by whether it runs. // Less than two years later / the phrase covers everything / from a weekend prototype / to a production release, / and most of the words around it / arrived faster than the practice did. //</p>
</div>

<div class="seg">
<p class="en">This is the short version. // Seven terms, / what each one actually means, / and what it changes / when you sit down to build something. //</p>
</div>

<h2>1. The model is the smallest part</h2>

<div class="seg">
<p class="en">A large language model / predicts the next token. // It reads what is in front of it / and continues. // That is the whole mechanism. // It does not know your system, / your data, / or your rules; / it has read a great many systems / that look like yours. //</p>
</div>

<div class="seg">
<p class="en">So the useful question / is never whether the model is smart enough. // It is whether it has enough to work with. //</p>
</div>

<table class="seg-table">
<thead><tr><th>Term</th><th>Plain meaning</th><th>What it changes in practice</th></tr></thead>
<tbody>
<tr><td><span class="en">LLM</span></td><td><span class="en">A model that continues text, one token at a time</span></td><td><span class="en">Ask for a shape you can check, not for truth</span></td></tr>
<tr><td><span class="en">Token</span></td><td><span class="en">The unit of text it reads, limits, and bills</span></td><td><span class="en">Long files cost money; identifiers get split</span></td></tr>
<tr><td><span class="en">Context window</span></td><td><span class="en">Everything the model can see in one call</span></td><td><span class="en">What you put in decides what comes out</span></td></tr>
<tr><td><span class="en">Prompt</span></td><td><span class="en">The instruction, plus any standing rules</span></td><td><span class="en">Examples beat adjectives</span></td></tr>
<tr><td><span class="en">Agent</span></td><td><span class="en">Model, tools, and a loop</span></td><td><span class="en">It can act, so actions need limits</span></td></tr>
<tr><td><span class="en">MCP</span></td><td><span class="en">A standard way to plug tools into an agent</span></td><td><span class="en">One integration, many clients</span></td></tr>
<tr><td><span class="en">RAG</span></td><td><span class="en">Retrieve your own documents, then answer</span></td><td><span class="en">Good for prose, poor for exact lookups</span></td></tr>
</tbody>
</table>

<h2>2. Token: the only unit that shows up on the invoice</h2>

<div class="seg">
<p class="en">A token / is not a word. // It is a fragment, / usually three or four characters / in English, / and the split does not follow meaning. // <code>RetailToSaleOrder</code> does not arrive as one thing; / it arrives as pieces, / and the pieces are what the model sees. //</p>
</div>

<div class="seg">
<p class="en">This matters twice. // Once on the bill, / because input and output are priced per token, / and cached input is cheaper than fresh input. // And once on the work: / an identifier the tokeniser chops in an awkward place / is harder for the model to copy correctly / than a short one. //</p>
</div>

<div class="seg">
<p class="en">Context windows are large now — / hundreds of thousands of tokens, / a million on some models. // Large is not the same as free. // A three-thousand-token rule file / is paid for on every single call, / and it also competes for attention / with the thing you actually asked. //</p>
</div>

<h2>3. Context is the skill</h2>

<div class="seg">
<p class="en">The definition worth keeping / comes from Andrej Karpathy: / context engineering is filling the window / with exactly the right information / for the next step. // Not more information. / The right information. //</p>
</div>

<div class="seg">
<p class="en">In practice it comes down to four moves. // Write: / put the stable rules somewhere the model reads every time, / such as an <code>AGENTS.md</code> file in the repository. // Select: / pull in only the files that matter for this task. // Compress: / summarise at the end of a long session, / before the early decisions drift out of view. // Isolate: / hand a messy sub-problem to a separate agent / so it cannot pollute the main thread. //</p>
</div>

<div class="seg">
<p class="en">A rule that has saved me more time than any prompt: / the rules file should contain only what the model cannot infer from the code itself. // Build commands, / boundaries, / the modules that must not change, / what “done” means. // Not coding style — / that is visible in the files. //</p>
</div>

<h2>4. Agent: model, tools, loop</h2>

<div class="seg">
<p class="en">An agent / is a model that can call tools / and keep going until it decides to stop. // Tool calling is the mechanism; / the loop is what makes it feel different / from a chat window. // It reads a file, / runs a test, / reads the failure, / edits again. //</p>
</div>

<div class="seg">
<p class="en">MCP — / the Model Context Protocol — / is the standard that lets those tools be plugged in once / and used by many clients. // In 2026 the protocol moved to a stateless core / and gained a skills extension / that loads instructions in stages, / metadata first, / full procedure only when it is needed. // The practical effect is smaller than the announcement: / fewer custom integrations, / and instructions that can live with the tool / instead of being pasted into a prompt. //</p>
</div>

<div class="seg">
<p class="en">Two rules I keep, / because every tool is also a way to break something. // Give the agent the fewest tools the task needs. // And make anything with a side effect — / a write, a deploy, a send — / require a confirmation. //</p>
</div>

<h2>5. Where vibe coding stops</h2>

<div class="seg">
<p class="en">Karpathy has since revised his own phrase / toward agentic engineering, / and the reason is practical. // Vibe coding judges output by whether it looks right. // A prototype can live with that. // Production cannot. //</p>
</div>

<div class="seg">
<p class="en">The dividing line is verification. // Tests cover the deterministic part: / given this input, / this output. // Evaluations cover the rest: / a set of cases, / a score, / a run you can repeat. // Without both, / whatever the prompt looks like, / you are still vibing. //</p>
</div>

<div class="seg">
<p class="en">The numbers in 2026 are large enough to be worth stating plainly. // A Google whitepaper on the new software lifecycle reports that / around 85% of professional developers now use AI coding agents daily, / and that 41% of new code is generated. // If that is the baseline, / the scarce skill is not writing prompts. // It is knowing how you would catch a wrong answer. //</p>
</div>

<h2>6. One example from my own work</h2>

<div class="seg">
<p class="en">I was fixing a script / that turns retail orders into sales orders / in an ERP system. // The model produced a mapping / that looked completely reasonable: / field to field, / one clean table. // It was wrong on units. // A carton is not a piece, / and the conversion sat in a different table / that I had not given it. //</p>
</div>

<div class="seg">
<p class="en">The fix was not a better prompt. // I gave it the two schemas, / two worked examples — / one carton case, one piece case — / and a check script that compares totals before and after. // Same model, / same week, / correct output. // What changed was the context, / and the fact that something could fail loudly. //</p>
</div>

<h2>7. What to remember</h2>

<div class="seg">
<p class="en">The vocabulary is small. // A model continues text. // It bills by token. // It can only use what is in the window. // An agent adds tools and a loop, / and tools need limits. // Retrieval helps with documents / and disappoints with exact lookups. //</p>
</div>

<div class="seg">
<p class="en">Everything else is fashion, / including the name. // What survives is the habit: / give it the right context, / ask for something checkable, / and keep a way to prove it wrong. //</p>
</div>
