---
title: "Vibe Coding, Term by Term: The Whole Vocabulary, Explained"
date: 2026-11-28
categories: [tech]
topic: ai
tags: [AI, Vibe Coding, Agents, Glossary]
summary: "Eighty-two terms in the order they are usually taught. Each one gets a definition, why it matters in practice, the mechanism underneath, and the terms it connects to — so the vocabulary reads as a system rather than a list."
---

<div class="seg">
<p class="en">Every field grows a vocabulary / faster than it grows a practice. // AI coding is two years old / and already carries eighty words for itself, / most of them borrowed, / several of them meaning something else by now. //</p>
</div>

<div class="seg">
<p class="en">This page keeps all of them, in the order they are usually taught, / and gives each one four things: / what it means, / why it matters when you are actually working, / the mechanism underneath, / and which other terms it leans on. // A word you cannot connect to anything else / is a word you will forget by Friday. //</p>
</div>

<div class="seg">
<p class="en">Definitions are short on purpose. // The connections are the point. //</p>
</div>

<p class="term-toc"><a href="#model">1 · The model</a> · <a href="#prompt">2 · The prompt</a> · <a href="#modes">3 · The modes</a> · <a href="#context">4 · The context</a> · <a href="#output">5 · The output</a> · <a href="#tools">6 · The tools</a> · <a href="#project">7 · The project words</a> · <a href="#stack">8 · Front end, back end</a></p>

<p class="level-key"><span class="lv lv1">L1</span>daily use<span class="lv lv2">L2</span>once you start building<span class="lv lv3">L3</span>specialist, still moving. Grades are mine, not the dictionary's.</p>

<h2 id="model">1. The model</h2>

<p class="term-lead">Everything else in this page sits on top of one mechanism: a network that predicts the next token. This layer explains the constraints that never go away — why text is counted, why knowledge is frozen, why the window matters.</p>

<h3 class="term">Artificial intelligence<span class="lv lv1">L1</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>The umbrella term for systems doing tasks we associate with human judgement.</dd></div>
  <div><dt>Why</dt><dd>It describes an ambition, not a mechanism — so it explains nothing about behaviour, cost or failure.</dd></div>
  <div><dt>Logic</dt><dd>A label applied after the fact. Every system under it still has a concrete architecture you can inspect.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Large language model · Agentic coding · Vibe coding</dd></div>
</dl>

<h3 class="term">Large language model<span class="lv lv1">L1</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>A model trained to predict the next token across a very large body of text.</dd></div>
  <div><dt>Why</dt><dd>Everything it does — answering, translating, writing code — is that prediction repeated. It has patterns, not knowledge of your system.</dd></div>
  <div><dt>Logic</dt><dd>Prompt tokens → probability distribution → sample one → append → repeat, until a stop condition.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Token · Context window · Temperature · Hallucination</dd></div>
</dl>

<h3 class="term">Token<span class="lv lv1">L1</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>The unit a model reads and writes; about four characters of English on average.</dd></div>
  <div><dt>Why</dt><dd>Cost, limits and speed are all counted in tokens, so length is a budget rather than a style choice.</dd></div>
  <div><dt>Logic</dt><dd>A tokeniser splits text into numbered pieces, ignoring meaning. <code>RetailToSaleOrder</code> arrives in fragments.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Input and output tokens · Token caching · Context window · Embeddings</dd></div>
</dl>

<h3 class="term">Input and output tokens<span class="lv lv1">L1</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>What you send is input; what comes back is output. They are priced and limited separately.</dd></div>
  <div><dt>Why</dt><dd>Output usually costs several times more than input, so a long answer is expensive in a way a long paste is not.</dd></div>
  <div><dt>Logic</dt><dd>Input is charged once per call; output is charged per token generated, which also sets how long you wait.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Token · Token caching · Streaming · Temperature</dd></div>
</dl>

<h3 class="term">Token caching<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>The provider keeps a prefix of your prompt in memory, so the next call does not pay full price to re-read it.</dd></div>
  <div><dt>Why</dt><dd>It rewards stable material at the top of the prompt — rules, schemas, documentation — and punishes reshuffling it.</dd></div>
  <div><dt>Logic</dt><dd>Prefix is hashed and stored; a matching prefix bills at a fraction of fresh input; the entry expires after minutes.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Token · Context window · Rules file · AGENTS.md</dd></div>
</dl>

<h3 class="term">Model parameters<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>The weights learned during training, counted in billions.</dd></div>
  <div><dt>Why</dt><dd>More parameters usually mean more capability and more cost, but the number says nothing about fit for your task.</dd></div>
  <div><dt>Logic</dt><dd>Set once by the provider, frozen afterwards. Nothing you type changes them.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Training and inference · Fine-tuning · Distillation</dd></div>
</dl>

<h3 class="term">Training and inference<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Training produces the weights; inference uses them.</dd></div>
  <div><dt>Why</dt><dd>It explains the central fact of working with models: the knowledge is frozen, so everything live has to arrive through the context.</dd></div>
  <div><dt>Logic</dt><dd>Training is gradient updates over a huge corpus, done once. Inference is one forward pass per request, done every time.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Model parameters · Fine-tuning · Context · Distillation</dd></div>
</dl>

<h3 class="term">Fine-tuning<span class="lv lv3">L3</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Further training of a finished model on your own examples.</dd></div>
  <div><dt>Why</dt><dd>It reliably shapes format, tone and narrow behaviour. It does not reliably add facts — for facts, put them in the context.</dd></div>
  <div><dt>Logic</dt><dd>Supervised pairs → weight updates → a new checkpoint you host or rent.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Training and inference · Few-shot · Distillation · Context</dd></div>
</dl>

<h3 class="term">Distillation<span class="lv lv3">L3</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Training a small model on the outputs of a large one.</dd></div>
  <div><dt>Why</dt><dd>It explains why cheap models feel like expensive ones on narrow, well-worn tasks — and why they fall apart on the unfamiliar ones.</dd></div>
  <div><dt>Logic</dt><dd>Teacher generates answers at scale; student learns to imitate the distribution, not the reasoning.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Model parameters · Fine-tuning · System-1 models</dd></div>
</dl>

<h3 class="term">Context window<span class="lv lv1">L1</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Everything the model can see in one call: instructions, files, documents, the conversation so far.</dd></div>
  <div><dt>Why</dt><dd>It is the hard boundary of what the model can know right now. Nothing outside it exists for this answer.</dd></div>
  <div><dt>Logic</dt><dd>Tokens are packed up to a limit; beyond it, material is dropped or summarised, and attention is never spread evenly.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Context · Context engineering · Compaction · RAG · Token</dd></div>
</dl>

<h2 id="prompt">2. The prompt</h2>

<p class="term-lead">The prompt is not a sentence you write; it is the whole input the model receives. These seven terms describe the layers of that input, from the standing instruction down to the example that fixes a format.</p>

<h3 class="term">Prompt<span class="lv lv1">L1</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>The instruction you give — in practice, everything sent with it: examples, files, tools, history.</dd></div>
  <div><dt>Why</dt><dd>People blame the model for a bad answer when the prompt only contained half the situation.</dd></div>
  <div><dt>Logic</dt><dd>Text in, continuation out. Whatever is absent from the prompt cannot influence the result.</dd></div>
  <div><dt>Links</dt><dd class="linklist">System prompt · Context · Few-shot · Prompt engineering</dd></div>
</dl>

<h3 class="term">System prompt<span class="lv lv1">L1</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>The standing instruction above the conversation that sets role, rules and boundaries.</dd></div>
  <div><dt>Why</dt><dd>It is the cheapest place to put a rule you want applied every single turn, rather than repeating it.</dd></div>
  <div><dt>Logic</dt><dd>Sent first, before user turns, so it colours everything after it. Most products let you edit it; few people do.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Prompt · Rules file · Hooks · Context engineering</dd></div>
</dl>

<h3 class="term">Prompt engineering<span class="lv lv1">L1</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>The craft of wording instructions so the model does what you meant.</dd></div>
  <div><dt>Why</dt><dd>It mattered enormously in 2023 and matters less now: the bottleneck moved from how you ask to what you supply.</dd></div>
  <div><dt>Logic</dt><dd>Iterate on phrasing against examples. Gains are real but local, and they do not transfer between tasks.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Context engineering · Few-shot · Chain of thought · Prompt</dd></div>
</dl>

<h3 class="term">Zero-shot<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Asking with no examples.</dd></div>
  <div><dt>Why</dt><dd>Fine for common tasks, unreliable for anything with a house style or an unusual output shape.</dd></div>
  <div><dt>Logic</dt><dd>The model falls back on the most common pattern in its training, which may not be yours.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Few-shot · Prompt · Fine-tuning</dd></div>
</dl>

<h3 class="term">Few-shot<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Two or three worked examples placed inside the prompt.</dd></div>
  <div><dt>Why</dt><dd>The cheapest quality upgrade available: one good input-output pair often beats a paragraph of adjectives.</dd></div>
  <div><dt>Logic</dt><dd>The model continues the pattern it sees. Examples teach format and judgement faster than instructions describe them.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Zero-shot · Prompt · Chain of thought · Fine-tuning</dd></div>
</dl>

<h3 class="term">Chain of thought<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Asking the model to reason step by step before giving the answer.</dd></div>
  <div><dt>Why</dt><dd>It helps with arithmetic, logic and multi-step edits — and mostly adds words when the model already reasons internally.</dd></div>
  <div><dt>Logic</dt><dd>Intermediate tokens become part of the context, so later steps can build on earlier ones.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Deep thinking · Few-shot · Prompt engineering</dd></div>
</dl>

<h3 class="term">Markdown<span class="lv lv1">L1</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>The plain-text formatting both you and the model read constantly — headings, lists, tables, code fences.</dd></div>
  <div><dt>Why</dt><dd>Structured input produces structured output. A pasted table stays a table; a wall of text stays a wall.</dd></div>
  <div><dt>Logic</dt><dd>Cheap markers that survive copy-paste and render as structure, which is why every agent writes in it.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Prompt · Rules file · Few-shot</dd></div>
</dl>

<h2 id="modes">3. The modes</h2>

<p class="term-lead">This is where the vocabulary grew fastest and where most confusion lives. The words here are not alternatives to each other — they sit on four levels, and most bad arguments come from treating a lower-level choice as if it were a higher-level one.</p>

<table class="seg-table">
<thead><tr><th>Level</th><th>The question it answers</th><th>Words that belong to it</th></tr></thead>
<tbody>
<tr><td><span class="en">1 · Model</span></td><td><span class="en">Can it do the job at all?</span></td><td><span class="en">ReAct · deep thinking · adaptive thinking · tool calling</span></td></tr>
<tr><td><span class="en">2 · Harness</span></td><td><span class="en">What surrounds the model?</span></td><td><span class="en">Harness engineering · MCP · skills · hooks · slash commands</span></td></tr>
<tr><td><span class="en">3 · Loop</span></td><td><span class="en">How does the work repeat?</span></td><td><span class="en">Agent loop · loop engineering · Ralph Wiggum loop · background agents</span></td></tr>
<tr><td><span class="en">4 · Team</span></td><td><span class="en">Who does the work?</span></td><td><span class="en">Subagents · agent teams · orchestration · A2A · ACP · BMAD</span></td></tr>
</tbody>
</table>

<h3 class="term">Vibe coding<span class="lv lv1">L1</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Karpathy's phrase from February 2025: describe what you want, accept the code, judge it by whether it runs.</dd></div>
  <div><dt>Why</dt><dd>It is a prototyping stance, not a delivery method. The name got stretched to cover production work it was never meant for.</dd></div>
  <div><dt>Logic</dt><dd>Prompt → code → run → look at it → adjust. The feedback loop is visual, so it only catches what you can see.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Agentic engineering · Prompt · Hallucination · Technical debt</dd></div>
</dl>

<h3 class="term">Agentic engineering<span class="lv lv1">L1</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>The 2026 correction, from Karpathy himself: same tools, but a spec, tests and evaluations decide whether the output is right.</dd></div>
  <div><dt>Why</dt><dd>It moves the standard from "looks right" to "passes the checks", which is the only difference that matters in production.</dd></div>
  <div><dt>Logic</dt><dd>Spec → agent work → deterministic tests → evals for the fuzzy parts → merge only on evidence.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Vibe coding · Harness engineering · Spec-driven development · Hooks</dd></div>
</dl>

<table class="seg-table">
<thead><tr><th></th><th>Vibe coding</th><th>Agentic engineering</th></tr></thead>
<tbody>
<tr><td><span class="en">You judge by</span></td><td><span class="en">Does it look right?</span></td><td><span class="en">Does it pass the checks?</span></td></tr>
<tr><td><span class="en">Context</span></td><td><span class="en">Whatever happens to be in the chat</span></td><td><span class="en">Rules file, chosen files, defined tools</span></td></tr>
<tr><td><span class="en">When it breaks</span></td><td><span class="en">You notice later</span></td><td><span class="en">A test or an eval fails</span></td></tr>
<tr><td><span class="en">Good for</span></td><td><span class="en">A prototype, a one-off script</span></td><td><span class="en">Anything someone depends on</span></td></tr>
</tbody>
</table>

<h3 class="term">Agentic coding<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Letting an agent read the repository, run commands, edit files and iterate — instead of pasting code into a chat.</dd></div>
  <div><dt>Why</dt><dd>The unit of work changes from a snippet to a task with a definition of done, which is why verification becomes unavoidable.</dd></div>
  <div><dt>Logic</dt><dd>Read → plan → edit → run → read output → repeat. The repository, not the chat, is the state.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Agent loop · Tool calling · Agentic engineering · Version control</dd></div>
</dl>

<h3 class="term">Harness engineering<span class="lv lv3">L3</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>The 2026 name for the layer around the model: rules, skills, sub-agents, hooks, tools, memory.</dd></div>
  <div><dt>Why</dt><dd>Its claim is that the model is now a commodity and the harness is the product — the same model in a tighter harness produces visibly better work.</dd></div>
  <div><dt>Logic</dt><dd>Constrain at four points: instruction, context, tool permission, runtime. Each layer narrows what the model may do.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Rules file · Agent skills · Hooks · MCP · Subagents · Agentic engineering</dd></div>
</dl>

<h3 class="term">Loop engineering<span class="lv lv3">L3</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Designing the cycle rather than the step: what starts it, what it may touch, how it verifies itself, when it must stop.</dd></div>
  <div><dt>Why</dt><dd>Closer to operations than prompting. The failure mode is not a bad answer but an agent looping confidently in the wrong direction.</dd></div>
  <div><dt>Logic</dt><dd>Trigger → attempt → check → decide: continue, escalate or stop. Every loop needs a budget and an exit.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Agent loop · Ralph Wiggum loop · Hooks · Background agents</dd></div>
</dl>

<h3 class="term">Multi-agent collaboration<span class="lv lv3">L3</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Several agents working on one problem, each with a role or a slice.</dd></div>
  <div><dt>Why</dt><dd>It buys parallelism and cleaner context, and it costs coordination — plus new surfaces where the agents can disagree.</dd></div>
  <div><dt>Logic</dt><dd>Split the task, hand out slices, merge results. Merge quality decides whether the parallelism was worth it.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Agent orchestration · Subagents · Agent teams · A2A</dd></div>
</dl>

<h3 class="term">Agent orchestration<span class="lv lv3">L3</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>The layer that decides who does what: splitting, dispatching, collecting, resolving conflicts.</dd></div>
  <div><dt>Why</dt><dd>It is where multi-agent systems actually fail — not in the models, but in the handoffs.</dd></div>
  <div><dt>Logic</dt><dd>Planner → queue → workers → aggregator. Usually a script plus a queue; the impressive name is optional.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Multi-agent collaboration · Subagents · Agent teams · BMAD</dd></div>
</dl>

<h3 class="term">Subagents<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>A helper agent with its own fresh context, spawned for one bounded job, returning only a conclusion.</dd></div>
  <div><dt>Why</dt><dd>Its real value is isolation: the mess of searching and reading stays out of the main thread.</dd></div>
  <div><dt>Logic</dt><dd>Main agent delegates with a narrow brief → subagent works in its own window → returns a short result.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Context engineering · Agent teams · Orchestration · Compaction</dd></div>
</dl>

<h3 class="term">Agent teams<span class="lv lv3">L3</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Three to five agents working in parallel on one project, with a lead splitting work and teammates messaging each other.</dd></div>
  <div><dt>Why</dt><dd>Good for broad mechanical change across modules; poor for anything that needs one coherent design decision.</dd></div>
  <div><dt>Logic</dt><dd>Lead decomposes → teammates claim tasks → messages coordinate → lead integrates and verifies.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Subagents · Orchestration · Multi-agent collaboration · Version control</dd></div>
</dl>

<h3 class="term">Self-improving agents<span class="lv lv3">L3</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Agents that distil a finished task into a reusable skill document and retrieve it next time — the pattern behind Hermes and similar 2026 projects.</dd></div>
  <div><dt>Why</dt><dd>Useful when you repeat the same kind of job; a way to accumulate your own mistakes when you do not.</dd></div>
  <div><dt>Logic</dt><dd>Task → reflection → written skill → retrieval on the next similar task → revision.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Agent skills · Rules file · Context engineering</dd></div>
</dl>

<h3 class="term">Background agents<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Work that runs without you watching: on a schedule, on a queue, or on a pull request.</dd></div>
  <div><dt>Why</dt><dd>Nobody was present when it happened, so the output has to be checkable after the fact.</dd></div>
  <div><dt>Logic</dt><dd>Trigger → run → produce a diff, report or comment → human or automated review.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Loop engineering · Hooks · Code review · Agentic engineering</dd></div>
</dl>

<h3 class="term">Personal agents<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>An agent with standing access to your own files, mail and calendar, rather than a blank chat.</dd></div>
  <div><dt>Why</dt><dd>Convenience purchased with permissions — the more it can reach, the more a wrong step costs.</dd></div>
  <div><dt>Logic</dt><dd>Persistent identity → scoped credentials → tools over personal data → audit trail.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Super-agents · Desktop agents · Hooks · MCP</dd></div>
</dl>

<h3 class="term">Super-agents<span class="lv lv3">L3</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>The marketing word for an agent given many tools and long-running autonomy.</dd></div>
  <div><dt>Why</dt><dd>Treat it as a claim, not a specification. The useful questions are always which tools, and what stops it.</dd></div>
  <div><dt>Logic</dt><dd>More tools → more capability and more risk; the limit has to come from the harness, not the model's goodwill.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Personal agents · Harness engineering · Hooks · MCP</dd></div>
</dl>

<h3 class="term">Agent loop<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>The core mechanism: the model calls a tool, reads the result, decides again.</dd></div>
  <div><dt>Why</dt><dd>Everything else in this section is built on this one cycle. It ends when no tool is called or a step limit is reached.</dd></div>
  <div><dt>Logic</dt><dd>Think → call → observe → think. The observation re-enters the context, which is why long loops drift.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Tool calling · Loop engineering · ReAct · Context window</dd></div>
</dl>

<figure class="article-figure">
  <img src="/assets/images/agent-loop.svg" alt="A loop from task to model to tool call to result, returning to the model, with a note that writes need a confirmation." width="900" height="374">
  <figcaption>The loop is the difference between a chat and an agent. The exit is not a decision you make — it is the model stopping, or a limit you set.</figcaption>
</figure>

<h3 class="term">Ralph Wiggum loop<span class="lv lv3">L3</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>A deliberately dumb pattern: write the checklist first, then let a fresh agent take one unfinished item per round, commit, and start again with clean context.</dd></div>
  <div><dt>Why</dt><dd>Progress lives in git rather than in a long conversation, which is exactly why it survives context limits.</dd></div>
  <div><dt>Logic</dt><dd>Checklist → pick one item → implement → test → commit → new window → repeat until empty.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Loop engineering · Agent loop · Version control · Spec-driven development</dd></div>
</dl>

<h3 class="term">ReAct<span class="lv lv3">L3</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Reason and act, interleaved: think about the next step, take it, observe, think again.</dd></div>
  <div><dt>Why</dt><dd>It is the pattern underneath most tool-using agents — named in 2022 and never renamed.</dd></div>
  <div><dt>Logic</dt><dd>Thought → action → observation, repeated. The trace is the audit log of why the agent did what it did.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Agent loop · Tool calling · Chain of thought</dd></div>
</dl>

<h3 class="term">Deep thinking<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Built-in reasoning before answering: the model works through steps internally, then replies.</dd></div>
  <div><dt>Why</dt><dd>Better on architecture, hard bugs and multi-step maths; slower and more expensive per answer.</dd></div>
  <div><dt>Logic</dt><dd>A budget of reasoning tokens is spent before the visible answer, and billed either way.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Adaptive thinking · Chain of thought · Temperature</dd></div>
</dl>

<h3 class="term">Adaptive thinking<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>The model decides how much reasoning a question deserves, instead of a manual on-off switch.</dd></div>
  <div><dt>Why</dt><dd>Simple questions answer at once; hard ones take the long path. Introduced across major models during 2026 and now mostly default.</dd></div>
  <div><dt>Logic</dt><dd>A difficulty estimate routes the request to a short or long reasoning path, with configurable effort levels.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Deep thinking · Temperature · Token</dd></div>
</dl>

<h3 class="term">Tool calling<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>The model emitting a structured request — tool name plus arguments — for the runtime to execute.</dd></div>
  <div><dt>Why</dt><dd>This is how an agent touches files, tests, databases and APIs. The model never runs anything; it only asks.</dd></div>
  <div><dt>Logic</dt><dd>Model returns JSON → runtime validates and executes → result returns as an observation.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Agent loop · MCP · Hooks · ReAct</dd></div>
</dl>

<h3 class="term">MCP<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>The Model Context Protocol: a standard way to expose tools and data to any compatible client.</dd></div>
  <div><dt>Why</dt><dd>One integration serves many agents, instead of every tool being rebuilt for every product.</dd></div>
  <div><dt>Logic</dt><dd>In 2026 the protocol moved to a stateless core and added a skills extension that loads instructions in stages — metadata first, full procedure on demand.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Tool calling · Agent skills · A2A · Super-agents</dd></div>
</dl>

<h3 class="term">Agent skills<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>A folder with a <code>SKILL.md</code> file: a procedure the agent loads only when a task matches.</dd></div>
  <div><dt>Why</dt><dd>Progressive disclosure — the instruction costs almost nothing until needed, unlike a rules file paid for on every call.</dd></div>
  <div><dt>Logic</dt><dd>Metadata is always visible → matching skill is loaded on demand → its scripts and references load last.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Harness engineering · Rules file · MCP · Self-improving agents</dd></div>
</dl>

<h3 class="term">Hooks<span class="lv lv3">L3</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Deterministic code that runs at fixed points — before a tool call, after an edit, before a commit.</dd></div>
  <div><dt>Why</dt><dd>Where a rule says "do not touch production", a hook makes it impossible. The cheapest reliability in the stack.</dd></div>
  <div><dt>Logic</dt><dd>Event → your script → allow, block or modify. Never asks the model for permission; it removes the option.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Harness engineering · Tool calling · Linter · Agentic engineering</dd></div>
</dl>

<h3 class="term">Slash commands<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Named shortcuts typed into the agent's prompt — <code>/review</code>, <code>/test</code>, <code>/commit</code> — that expand into a longer instruction.</dd></div>
  <div><dt>Why</dt><dd>A way to standardise the twenty prompts you actually reuse, instead of retyping them from memory.</dd></div>
  <div><dt>Logic</dt><dd>Name → stored template → inserted with arguments. Cheap, and it keeps team instructions identical.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Rules file · Agent skills · Hooks</dd></div>
</dl>

<h3 class="term">A2A<span class="lv lv3">L3</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Agent-to-Agent: a protocol for agents built by different vendors to discover each other and exchange tasks.</dd></div>
  <div><dt>Why</dt><dd>Enterprise plumbing rather than something you use directly — it matters when you buy agents from several suppliers.</dd></div>
  <div><dt>Logic</dt><dd>Agent card describes capabilities → task handoff → status and artefacts returned over HTTP.</dd></div>
  <div><dt>Links</dt><dd class="linklist">ACP · MCP · Multi-agent collaboration · Orchestration</dd></div>
</dl>

<h3 class="term">ACP<span class="lv lv3">L3</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Two things share the acronym: IBM's Agent Communication Protocol, and the Agent Client Protocol used by editors.</dd></div>
  <div><dt>Why</dt><dd>Both address the same gap as A2A from different directions, and neither is settled — expect the names to move.</dd></div>
  <div><dt>Logic</dt><dd>Communication protocol: REST-style messages between frameworks. Client protocol: an editor talking to any agent.</dd></div>
  <div><dt>Links</dt><dd class="linklist">A2A · MCP · Multi-agent collaboration</dd></div>
</dl>

<h3 class="term">BMAD<span class="lv lv3">L3</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>A role-based method — analyst, product manager, architect, developer, tester — where each role is an agent with its own instructions and artefacts.</dd></div>
  <div><dt>Why</dt><dd>It works because it forces the specification to exist before the code, which is the same insight as SDD with more ceremony.</dd></div>
  <div><dt>Logic</dt><dd>Role → artefact → handoff. Each document is the next agent's context, so quality is bounded by the documents.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Spec-driven development · Orchestration · Agent teams · Agentic engineering</dd></div>
</dl>

<h3 class="term">Browser use<span class="lv lv3">L3</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>An agent driving a real browser: clicking, typing, reading the page.</dd></div>
  <div><dt>Why</dt><dd>Good for sites with no API; fragile in the way all UI automation is fragile — one redesign breaks the script.</dd></div>
  <div><dt>Logic</dt><dd>Screenshot or DOM → locate element → act → verify the page changed as expected.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Computer use · Tool calling · Desktop agents</dd></div>
</dl>

<h3 class="term">Computer use<span class="lv lv3">L3</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>The same idea one level up: the agent sees the screen, moves the mouse and types.</dd></div>
  <div><dt>Why</dt><dd>It reaches any desktop application, which is also why it belongs in a sandbox rather than on your working machine.</dd></div>
  <div><dt>Logic</dt><dd>Screenshot → plan → input event → screenshot again. Slow by nature, because every step is a round trip.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Browser use · Desktop agents · Personal agents</dd></div>
</dl>

<h2 id="context">4. The context</h2>

<p class="term-lead">If the model is fixed and the harness is yours, the only variable left is what you put in front of it. This layer is the practical core of the whole vocabulary: it decides quality more than any prompt trick.</p>

<h3 class="term">Context<span class="lv lv1">L1</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Everything inside the window for this call. Not memory, not training.</dd></div>
  <div><dt>Why</dt><dd>If it is not here, it does not exist for this answer — the single most useful sentence in this glossary.</dd></div>
  <div><dt>Logic</dt><dd>Instructions, files, retrieved documents and history compete for the same budget and the same attention.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Context window · Context engineering · RAG · Rules file</dd></div>
</dl>

<figure class="article-figure">
  <img src="/assets/images/context-window.svg" alt="A context window containing rules, chosen files, retrieved documents and the conversation, with an unpasted conversion table sitting outside it." width="900" height="330">
  <figcaption>The window is the whole world for one call. A table you never pasted is not “forgotten” — it does not exist yet.</figcaption>
</figure>

<h3 class="term">Context engineering<span class="lv lv1">L1</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Filling the window with exactly the right information for the next step — Karpathy's definition, and the skill that replaced prompt engineering.</dd></div>
  <div><dt>Why</dt><dd>Quality tracks context quality more than wording. This is where the hours are actually spent.</dd></div>
  <div><dt>Logic</dt><dd>Four moves: write it down, select what matters, compress at boundaries, isolate the mess in a sub-agent.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Context · Compaction · Rules file · Subagents · Prompt engineering</dd></div>
</dl>

<h3 class="term">Compaction<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Summarising a long session so early decisions survive in short form.</dd></div>
  <div><dt>Why</dt><dd>Done at task boundaries, not when the window is full — by then the details you needed are already gone.</dd></div>
  <div><dt>Logic</dt><dd>History → summary → summary replaces history → work continues on the smaller base.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Context window · Context engineering · Subagents</dd></div>
</dl>

<h3 class="term">Rules file<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>A file of standing instructions read every session: build commands, boundaries, forbidden modules, what "done" means.</dd></div>
  <div><dt>Why</dt><dd>Keep it to what cannot be inferred from the code — every line is paid for on every call and competes for attention.</dd></div>
  <div><dt>Logic</dt><dd>Loaded automatically → shapes every response → costs tokens even when irrelevant.</dd></div>
  <div><dt>Links</dt><dd class="linklist">AGENTS.md · Token caching · Agent skills · Harness engineering</dd></div>
</dl>

<h3 class="term">AGENTS.md<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>The 2026 convention for that file: plain Markdown at the repository root, read by most coding agents.</dd></div>
  <div><dt>Why</dt><dd>No format to learn. The discipline is entirely in what you leave out.</dd></div>
  <div><dt>Logic</dt><dd>Repository layout and commands → boundaries → definition of done. Written for a new colleague, not for a machine.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Rules file · Context engineering · Spec-driven development</dd></div>
</dl>

<h3 class="term">Spec-driven development<span class="lv lv3">L3</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Writing the specification first and treating it as the source of truth the code must satisfy.</dd></div>
  <div><dt>Why</dt><dd>With agents it stops being bureaucracy: a vague plan produces vague code, and the spec is the only artefact you and the model can both be held to.</dd></div>
  <div><dt>Logic</dt><dd>Spec → tasks → implementation → tests that quote the spec. Change the spec first, then the code.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Agentic engineering · BMAD · Rules file · Ralph Wiggum loop</dd></div>
</dl>

<h3 class="term">RAG<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Retrieval-augmented generation: fetch relevant documents at question time and put them in the window.</dd></div>
  <div><dt>Why</dt><dd>Strong on prose and policy; weak on exact identifiers, where plain search still wins.</dd></div>
  <div><dt>Logic</dt><dd>Question → search → top passages → context → answer. Quality is bounded by retrieval, not by the model.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Embeddings · Vector database · Agentic RAG · Context</dd></div>
</dl>

<h3 class="term">Agentic RAG<span class="lv lv3">L3</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>RAG where the agent decides what to search, reformulates, and searches again if the first result is thin.</dd></div>
  <div><dt>Why</dt><dd>Better on multi-hop questions; harder to bound, because the loop can keep looking forever.</dd></div>
  <div><dt>Logic</dt><dd>Plan a query → search → judge sufficiency → refine or stop. Needs an explicit stopping rule.</dd></div>
  <div><dt>Links</dt><dd class="linklist">RAG · Agent loop · Loop engineering · Embeddings</dd></div>
</dl>

<h3 class="term">Vector database<span class="lv lv3">L3</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>A store that indexes embeddings and returns nearest neighbours.</dd></div>
  <div><dt>Why</dt><dd>Useful once you have thousands of chunks; before that, a folder and a search command are honest enough.</dd></div>
  <div><dt>Logic</dt><dd>Text → embedding → index → query vector → top-k results by distance.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Embeddings · RAG · Agentic RAG</dd></div>
</dl>

<h3 class="term">Embeddings<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Text turned into vectors so that similar meaning lands nearby.</dd></div>
  <div><dt>Why</dt><dd>This is why semantic search finds "returns policy" when you typed "refund rules" — and why it confidently returns something adjacent when you needed the exact one.</dd></div>
  <div><dt>Logic</dt><dd>Text → fixed-length vector → cosine distance. Meaning becomes geometry, and geometry has no notion of exact.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Vector database · RAG · Token</dd></div>
</dl>

<h2 id="output">5. The output</h2>

<p class="term-lead">Four words about what comes back, and what you can do about it. Three of them are often mistaken for controls over correctness; only one actually is, and it is not the one people reach for.</p>

<h3 class="term">Hallucination<span class="lv lv1">L1</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Fluent output with no basis in the input.</dd></div>
  <div><dt>Why</dt><dd>Not an intermittent bug: it is the same prediction mechanism working without enough to work from. The remedy is a better source or a check.</dd></div>
  <div><dt>Logic</dt><dd>Insufficient context + pressure to continue → the most plausible continuation wins, and plausible is not true.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Context · Temperature · Linter · Agentic engineering</dd></div>
</dl>

<h3 class="term">Temperature<span class="lv lv1">L1</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>The randomness dial on sampling.</dd></div>
  <div><dt>Why</dt><dd>Lower makes output repeatable; it does not make it correct. People keep turning it down hoping for truth.</dd></div>
  <div><dt>Logic</dt><dd>Reshapes the probability distribution before sampling: flat for variety, sharp for consistency.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Hallucination · Token · Deep thinking</dd></div>
</dl>

<h3 class="term">Streaming<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Sending the answer token by token as it is produced.</dd></div>
  <div><dt>Why</dt><dd>A latency trick, not a quality one — though the first line tells you quickly whether the direction is wrong.</dd></div>
  <div><dt>Logic</dt><dd>Generation and delivery interleave, so perceived wait drops even when total time does not.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Input and output tokens · Token · Hallucination</dd></div>
</dl>

<h3 class="term">System-1 models<span class="lv lv3">L3</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Small models that return a decision instead of prose: a probability, a category, a score.</dd></div>
  <div><dt>Why</dt><dd>Milliseconds and near-zero cost, which makes them the right tool for routing, triage and filtering before a larger model is called.</dd></div>
  <div><dt>Logic</dt><dd>Input → single forward pass → fixed-shape output. No generation, so no parsing failures and no long wait.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Distillation · Temperature · Agent orchestration</dd></div>
</dl>

<h2 id="tools">6. The tools</h2>

<p class="term-lead">The oldest words in the list, and the ones people skip. They matter again because agents work through these surfaces: a clean command line and a real editor are now part of the AI toolchain, not the backdrop to it.</p>

<h3 class="term">IDE<span class="lv lv1">L1</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>An integrated development environment: editor, debugger, terminal and project model in one window.</dd></div>
  <div><dt>Why</dt><dd>VS Code and its forks dominate, and the AI features now matter more than the editor itself.</dd></div>
  <div><dt>Logic</dt><dd>One process holds the project model, so completion, navigation and agents all read the same index.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Code editor · Code completion · Linter · CLI</dd></div>
</dl>

<h3 class="term">Code editor<span class="lv lv1">L1</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>The lighter half of an IDE: a window for editing text with syntax highlighting.</dd></div>
  <div><dt>Why</dt><dd>Many people now work inside an agent's chat pane and open the editor only to read a diff.</dd></div>
  <div><dt>Logic</dt><dd>Text buffer plus language awareness; everything else is a plugin. That is why agents can substitute for parts of it.</dd></div>
  <div><dt>Links</dt><dd class="linklist">IDE · Code completion · Code review</dd></div>
</dl>

<h3 class="term">CLI<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>The command line.</dd></div>
  <div><dt>Why</dt><dd>It matters again in 2026 because agents are good at it: reading output, running tests, chaining commands.</dd></div>
  <div><dt>Logic</dt><dd>Text in, text out, exit codes. A tool with a clean CLI is easier for an agent than one with a pretty UI.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Tool calling · Linter · Agentic coding</dd></div>
</dl>

<h3 class="term">No-code platforms<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Tools that build software from forms and blocks rather than code.</dd></div>
  <div><dt>Why</dt><dd>Still the fastest path for a fixed, well-understood shape; still a wall when you need something the platform did not anticipate.</dd></div>
  <div><dt>Logic</dt><dd>Configuration compiles to a fixed runtime. Flexibility is traded for speed, and the trade is hard to reverse.</dd></div>
  <div><dt>Links</dt><dd class="linklist">BaaS · Vibe coding · MVP</dd></div>
</dl>

<h3 class="term">Code completion<span class="lv lv1">L1</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Suggesting the next line as you type.</dd></div>
  <div><dt>Why</dt><dd>The oldest AI coding feature and the least discussed, because it quietly became normal.</dd></div>
  <div><dt>Logic</dt><dd>Local context → model → ranked suggestions. Fast enough to feel like typing, shallow enough to stay uncritical.</dd></div>
  <div><dt>Links</dt><dd class="linklist">IDE · Code editor · Token</dd></div>
</dl>

<h3 class="term">Code review<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Reading a change before it lands, for correctness and for intent.</dd></div>
  <div><dt>Why</dt><dd>With generated code the practice matters more, not less: the reviewer is often the only thing between a plausible diff and production.</dd></div>
  <div><dt>Logic</dt><dd>Diff → intent check → risk check → approve or send back. Agents can pre-review, but they share the blind spots of the code they wrote.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Version control · Linter · Agentic engineering · Hooks</dd></div>
</dl>

<h3 class="term">Linter<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>A tool that flags suspicious code by rule: unused variables, missing types, unreachable branches.</dd></div>
  <div><dt>Why</dt><dd>Deterministic, cheap, and the easiest quality gate to hand an agent, because the output is a list it can work through.</dd></div>
  <div><dt>Logic</dt><dd>Parse → rules → line-level findings. No model, no variance: the same code always produces the same complaints.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Hooks · Code review · Agentic engineering · CLI</dd></div>
</dl>

<h3 class="term">Debugging<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Finding why behaviour differs from expectation.</dd></div>
  <div><dt>Why</dt><dd>Agents are good at the mechanical half — stack traces, logs, bisecting — and weak at the half that needs to know what the system was supposed to do.</dd></div>
  <div><dt>Logic</dt><dd>Reproduce → narrow → inspect state → fix → prove with a test. The first step is the one agents skip.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Linter · Code review · Agentic coding</dd></div>
</dl>

<h3 class="term">Desktop agents<span class="lv lv3">L3</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Open-source agents that run on your own machine and act on it — files, browser, terminal, sometimes your chat apps.</dd></div>
  <div><dt>Why</dt><dd>OpenClaw is the best-known 2026 example. Powerful, and the reason "what permissions did I grant?" became a real question.</dd></div>
  <div><dt>Logic</dt><dd>Local runtime → tools over OS → messaging front end. The trust boundary is your own account.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Computer use · Personal agents · Hooks · MCP</dd></div>
</dl>

<h2 id="project">7. The project words</h2>

<p class="term-lead">None of these changed because of AI, and all of them changed meaning. Each was a safeguard against human shortcuts; with generated code the safeguards matter more and are easier to skip.</p>

<h3 class="term">MVP<span class="lv lv1">L1</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>The smallest version that tests whether anyone wants this.</dd></div>
  <div><dt>Why</dt><dd>With agents the temptation is to build the whole thing in an afternoon, which is exactly how MVPs stop being minimal.</dd></div>
  <div><dt>Logic</dt><dd>One hypothesis → the least software that tests it → a decision. Scope is a question, not a schedule.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Iteration · Vibe coding · No-code platforms</dd></div>
</dl>

<h3 class="term">Iteration<span class="lv lv1">L1</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>One pass of build, check, adjust.</dd></div>
  <div><dt>Why</dt><dd>Small iterations keep the context small and the failures visible — the unit that makes agent work manageable.</dd></div>
  <div><dt>Logic</dt><dd>Scope → change → verify → commit. Each pass should end in something you could ship or throw away.</dd></div>
  <div><dt>Links</dt><dd class="linklist">MVP · Agent loop · Version control · Refactoring</dd></div>
</dl>

<h3 class="term">Refactoring<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Changing structure without changing behaviour.</dd></div>
  <div><dt>Why</dt><dd>Agents are genuinely good at this, because the behaviour is defined by tests — which is also the condition for letting them near it.</dd></div>
  <div><dt>Logic</dt><dd>Tests first → mechanical change → tests still green → commit. No tests, no refactor.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Technical debt · Iteration · Code review</dd></div>
</dl>

<h3 class="term">Technical debt<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>The future cost of a shortcut taken now.</dd></div>
  <div><dt>Why</dt><dd>Generated code accrues it faster, because nobody remembers choosing the shortcut.</dd></div>
  <div><dt>Logic</dt><dd>Speed now → interest later: slower changes, more bugs, fewer people willing to touch the file.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Refactoring · Code review · Vibe coding</dd></div>
</dl>

<h3 class="term">Version control<span class="lv lv1">L1</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Git, in practice: every state recoverable, every change attributable.</dd></div>
  <div><dt>Why</dt><dd>For agent work it is not bookkeeping but the safety net — commit before the agent starts, and a bad afternoon costs one command.</dd></div>
  <div><dt>Logic</dt><dd>Snapshot → branch → diff → merge. Diffs are also how you review what an agent actually did.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Git worktree · Code review · Ralph Wiggum loop</dd></div>
</dl>

<h3 class="term">Git worktree<span class="lv lv3">L3</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>A second working directory attached to the same repository, on its own branch.</dd></div>
  <div><dt>Why</dt><dd>The cheap way to let an agent work in parallel without stepping on your uncommitted files.</dd></div>
  <div><dt>Logic</dt><dd>Same object store → separate checkout → no stashing, no copying the folder.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Version control · Agent teams · Iteration</dd></div>
</dl>

<h3 class="term">Deployment<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Moving code from your machine to where it runs.</dd></div>
  <div><dt>Why</dt><dd>The step where "it worked locally" stops being an argument.</dd></div>
  <div><dt>Logic</dt><dd>Build → environment → release → observe. Each stage adds a way for the code to be wrong that tests did not cover.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Version control · Background agents · Hooks</dd></div>
</dl>

<h3 class="term">GEO<span class="lv lv3">L3</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Generative engine optimisation: writing so that an AI search engine cites you, rather than so that a results page ranks you.</dd></div>
  <div><dt>Why</dt><dd>Same instinct as SEO, different surface — structure, specificity and named facts instead of keywords.</dd></div>
  <div><dt>Logic</dt><dd>Clear claims → citable statements → machine-readable structure → inclusion in generated answers.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Markdown · RAG · Hallucination</dd></div>
</dl>

<h2 id="stack">8. Front end, back end</h2>

<p class="term-lead">The words that never changed, kept here because every AI coding conversation lands on them eventually — and because "full stack" now means something slightly different than it did.</p>

<h3 class="term">Frontend<span class="lv lv1">L1</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>What runs in the browser: layout, interaction, state.</dd></div>
  <div><dt>Why</dt><dd>The part users judge, and the part agents are most confident about and most often wrong on details.</dd></div>
  <div><dt>Logic</dt><dd>Data → render → events → state change → render again. Errors are visible immediately, which helps.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Backend · API · Full stack</dd></div>
</dl>

<h3 class="term">Backend<span class="lv lv1">L1</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>What runs on the server: data, rules, authentication, integrations.</dd></div>
  <div><dt>Why</dt><dd>Where the business logic lives, and where a plausible-looking mistake costs the most.</dd></div>
  <div><dt>Logic</dt><dd>Request → validation → rule → data change → response. Failures here are quiet and expensive.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Frontend · API · Database · BaaS</dd></div>
</dl>

<h3 class="term">Full stack<span class="lv lv1">L1</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Both ends, plus the seam between them.</dd></div>
  <div><dt>Why</dt><dd>With agents it increasingly means being able to specify and verify both ends rather than typing either.</dd></div>
  <div><dt>Logic</dt><dd>One person owns the contract across the seam, so mismatches get caught before deployment.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Frontend · Backend · API</dd></div>
</dl>

<h3 class="term">API<span class="lv lv2">L2</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>A defined way for one program to call another: endpoints, inputs, outputs, errors.</dd></div>
  <div><dt>Why</dt><dd>It is the contract an agent reads when integrating, and the thing to paste into the window before asking for code.</dd></div>
  <div><dt>Logic</dt><dd>Request shape → auth → handler → response shape. Ambiguity in the shape is where generated code goes wrong.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Frontend · Backend · MCP · Tool calling</dd></div>
</dl>

<h3 class="term">Database<span class="lv lv1">L1</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Where state persists: tables, keys, constraints.</dd></div>
  <div><dt>Why</dt><dd>Most agent mistakes that matter are data mistakes — a wrong join, a duplicated row, a unit never converted.</dd></div>
  <div><dt>Logic</dt><dd>Schema → writes constrained by rules → reads shaped by joins. Constraints are the part agents cannot talk around.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Backend · API · BaaS · Version control</dd></div>
</dl>

<h3 class="term">BaaS<span class="lv lv3">L3</span></h3>
<dl class="term-grid">
  <div><dt>Definition</dt><dd>Backend as a service: hosted database, auth and storage behind an SDK.</dd></div>
  <div><dt>Why</dt><dd>A small project needs no server of its own — fast to start, and a dependency to plan for when you outgrow it.</dd></div>
  <div><dt>Logic</dt><dd>Client SDK → managed backend → row-level rules. Security moves from your code to the platform's policy language.</dd></div>
  <div><dt>Links</dt><dd class="linklist">Database · Backend · No-code platforms</dd></div>
</dl>

<h2>How to use a page like this</h2>

<div class="seg">
<p class="en">Eighty-two terms, / and the working set is smaller than it looks. // In my own week I use a rules file, / a few skills, / two or three tools per task, / and a check that fails loudly. // Everything else I look up when a page like this is open beside me. //</p>
</div>

<div class="seg">
<p class="en">The test of whether a term is yours / is not whether you can define it. // It is whether you can say what it connects to / and what changes when it is missing. // Token connects to cost and to the window. // Context connects to everything. // Hallucination connects to the check you did not build. //</p>
</div>

<div class="seg">
<p class="en">The vocabulary will be different next year. // The structure will hold: / a model you do not control, / a harness you do, / a loop that needs an exit, / and a check that can fail. //</p>
</div>
