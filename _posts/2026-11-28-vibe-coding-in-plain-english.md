---
title: "Vibe Coding, Term by Term: The Whole Vocabulary, Translated"
date: 2026-11-28
categories: [tech]
topic: ai
tags: [AI, Vibe Coding, Agents, Glossary]
summary: "A faithful English rendering of a Chinese Vibe Coding glossary — eighty-two terms kept in the original order, with the source's analogies and figures intact, plus tables and diagrams for structure."
---

<div class="seg">
<p class="en">This is a translation, not an essay. // The source is Yu Pi's <a href="https://github.com/liyupi/ai-guide">Vibe Coding concept guide</a>, / a Chinese glossary of eighty-two terms / that has become the standard reference for people learning AI coding there. //</p>
</div>

<div class="seg">
<p class="en">I have kept the original order, / the original analogies, / and the original figures — / including the model names and prices, / which are as the source states them in 2026. // Where a table or a diagram makes the structure easier to hold, / I have added one. // The L1 to L3 grades are also mine; / the source does not grade its terms. //</p>
</div>

<div class="seg">
<p class="en">Read it as a dictionary, / or read it in order as a course. // The eight chapters build: / the model, / the prompt, / the modes, / the context, / the output, / the tools, / the project words, / and the stack underneath. //</p>
</div>

<p class="term-toc"><a href="#model">1 · The model</a> · <a href="#prompt">2 · The prompt</a> · <a href="#modes">3 · The modes</a> · <a href="#context">4 · The context</a> · <a href="#output">5 · The output</a> · <a href="#tools">6 · The tools</a> · <a href="#project">7 · The project words</a> · <a href="#stack">8 · Front end, back end</a></p>

<p class="level-key"><span class="lv lv1">L1</span>daily use<span class="lv lv2">L2</span>once you start building<span class="lv lv3">L3</span>specialist, still moving. The grades are a reading aid added here; the source does not grade its terms.</p>

<h2 id="model">1. The model</h2>

<h3 class="term">Artificial intelligence<span class="lv lv1">L1</span></h3>
<p>The technology that lets computers imitate human intelligence — in plain words, a machine that thinks, learns and solves problems the way a person does.</p>
<p>In vibe coding, AI is your programming assistant: you say what you want, and it drafts the approach, writes the code and fixes the bugs. The source's image is a programmer friend who is online twenty-four hours a day.</p>

<h3 class="term">Large language model<span class="lv lv1">L1</span></h3>
<p>An AI system that understands and generates human language. ChatGPT, Claude, Gemini and DeepSeek are all large language models.</p>
<p>Why “large”? Because the number of parameters is enormous — tens of billions, sometimes trillions. More parameters usually mean a smarter model, and a more expensive one to run. The source's analogy: a top student who has read an ocean of books and code, which is why it can write, explain and repair code for you.</p>
<p>Text models are not the only kind: there are vision models (Stable Diffusion), audio models (Whisper), and multimodal models that handle text, images and sound together (GPT-4o, Gemini). For AI coding, you mostly deal with the text ones.</p>

<h3 class="term">Token<span class="lv lv1">L1</span></h3>
<p>The basic unit of text a model processes — a “word piece”, the smallest thing the text is broken into.</p>
<p>It is the concept you cannot skip, because AI services bill by token: what you send and what comes back both consume them, and more tokens means more money. In English a token is roughly a word or part of one. Different models use different tokenisers, so the same passage can cost different amounts in different models.</p>
<table class="seg-table">
<thead><tr><th>What you send</th><th>Roughly</th></tr></thead>
<tbody>
<tr><td><span class="en"><code>Hello World</code></span></td><td><span class="en">about 2 tokens</span></td></tr>
<tr><td><span class="en">the same greeting in Chinese</span></td><td><span class="en">about 4 to 6 tokens</span></td></tr>
</tbody>
</table>
<p>Chinese-first models such as Qwen and DeepSeek optimise for the language, so one token covers about 1.5 to 1.8 Chinese characters — noticeably more efficient than the early English-first models. Most coding tools now show a running token count, so you can watch the cost while you work.</p>

<h3 class="term">Input and output tokens<span class="lv lv1">L1</span></h3>
<p>Billing separates what goes in from what comes out. Input tokens are your prompt, code and files; output tokens are the answer, the generated code and the tool calls.</p>
<p>Output is generally the more expensive half, because generating costs more compute than reading. In the source's example, Claude Sonnet 4 charges $3 per million input tokens and $15 per million output tokens — five times more for output.</p>
<p>The cheapest saving is still the simplest: write prompts that are clear enough to be understood in one pass, so you do not pay for the same explanation three times.</p>

<h3 class="term">Token caching<span class="lv lv2">L2</span></h3>
<p>A mechanism that saves real money. When you keep talking to the same model, much of the prompt repeats — the system instruction, the files you attached — and recomputing it every time is waste. Caching stores the intermediate result and reuses it when the same prefix appears again.</p>
<p>Cached tokens come in two kinds: writing the cache costs slightly more than normal input the first time, and reading it later can cost as little as one tenth of normal input.</p>
<p>The practical advice: keep the top of your context stable. If your rules file and reference files do not change between turns, you keep getting the discount — which is why one long conversation can be cheaper than three short ones.</p>

<h3 class="term">Model parameters<span class="lv lv2">L2</span></h3>
<p>The “knowledge points” a model learned during training, stored as numbers. If it read countless statements that the sky is blue, the association between sky and blue lives in the parameters. More parameters, more associations retained.</p>
<p>Parameter count drives both capability and running cost: a larger model is usually smarter and usually needs more GPU compute per request.</p>
<table class="seg-table">
<thead><tr><th>Model (as the source lists it)</th><th>Parameters</th><th>Note</th></tr></thead>
<tbody>
<tr><td><span class="en">DeepSeek V4.1 Flash</span></td><td><span class="en">552B</span></td><td><span class="en">MoE, natively multimodal</span></td></tr>
<tr><td><span class="en">GLM-5.4</span></td><td><span class="en">~750B</span></td><td><span class="en">Loop Transformer architecture</span></td></tr>
<tr><td><span class="en">Qwen4-Max</span></td><td><span class="en">2.4T</span></td><td><span class="en">MoE, 71–95B active per call</span></td></tr>
<tr><td><span class="en">Kimi K3.1 Pro</span></td><td><span class="en">2.8T</span></td><td><span class="en">MoE, 104B active</span></td></tr>
</tbody>
</table>
<p>The trend worth noticing: size and capability are no longer a straight line. The source points out that a 552B model can beat a 1.6T model of the same family, and that architectural changes such as looping a middle layer twice raise the ceiling without adding parameters. Vendors also ship several sizes of the same family, so you can trade cost against capability.</p>

<h3 class="term">Training and inference<span class="lv lv2">L2</span></h3>
<p>Training is how a model learns from large amounts of data. It takes enormous compute and time, and it is done by the AI companies — you almost never train a model yourself; you use a finished one.</p>
<p>Inference is using the trained model to answer and generate. Every chat with ChatGPT and every request to Cursor is inference.</p>
<p>The source's analogy: training is a student going to school and studying; inference is that student sitting an exam.</p>

<h3 class="term">Fine-tuning<span class="lv lv3">L3</span></h3>
<p>Continuing to train an existing model on domain-specific data so it performs better in one area — medical records to make a medical specialist, or your company's codebase to make it familiar with your style.</p>
<p>For ordinary users the cost is high and it is usually unnecessary; a ready-made model is enough. Platforms such as Alibaba Cloud Bailian and Volcano Engine offer fine-tuning as a service, which lowers the barrier.</p>

<h3 class="term">Distillation<span class="lv lv3">L3</span></h3>
<p>Compressing a large model's knowledge into a small one — knowledge distillation.</p>
<p>The source's image is a senior developer mentoring a junior: the senior does not just give the answer, but shares the reasoning. The junior learns the way of thinking and reaches similar decisions at a fraction of the cost.</p>
<p>The mechanism is the “soft label”. Shown a photo, a large model does not say only “dog”; it returns a distribution — dog 92%, cat 5%, wolf 3% — and the 5% carries real information about resemblance. A small model trained on those distributions learns the subtle relations between categories, which works far better than learning from right-or-wrong labels alone.</p>
<p>The payoff in the source: five to thirty times cheaper, about four times faster, and over 95% of the performance retained. DeepSeek-R1's distilled versions are the example — a 671B teacher, a 32B student, still strong. Distillation differs from fine-tuning in aim: fine-tuning makes a model more specialised; distillation makes it lighter and cheaper.</p>

<h3 class="term">Context window<span class="lv lv1">L1</span></h3>
<p>The maximum amount of content a model can “remember” at once, measured in tokens.</p>
<table class="seg-table">
<thead><tr><th>Model family (per the source)</th><th>Window</th></tr></thead>
<tbody>
<tr><td><span class="en">GPT-4o</span></td><td><span class="en">128K — an early model</span></td></tr>
<tr><td><span class="en">Claude 5.5 series</span></td><td><span class="en">1M</span></td></tr>
<tr><td><span class="en">GPT-6.2 series</span></td><td><span class="en">~1.05M</span></td></tr>
<tr><td><span class="en">Gemini 4 series</span></td><td><span class="en">1M, text, image, audio and video together</span></td></tr>
<tr><td><span class="en">DeepSeek V4.1 Flash / Qwen4-Max / Kimi K3.1</span></td><td><span class="en">1M; Qwen4-Max has no long-context surcharge</span></td></tr>
</tbody>
</table>
<p>A larger window means more code and more history in one conversation, which helps when the project is big or the task may not finish in a single pass.</p>
<p>The cost side matters too: everything you stuff in is billed on every request. Some models also price long requests higher — Claude once charged double beyond 200K tokens — so read the pricing page before assuming the window is free.</p>

<h2 id="prompt">2. The prompt</h2>

<h3 class="term">Prompt<span class="lv lv1">L1</span></h3>
<p>The instruction or question you give the AI — in coding, your requirement written in natural language.</p>
<p>Prompt quality decides output quality. A good one is specific, carries the necessary background, and states the output format you expect. The source's contrast: “make a website” is vague; “build an expense tracker in React with add, list and total, in blue” is a prompt.</p>
<p>Messages in a conversation have three roles: system (sets the AI's role and rules, invisible to the user), user (what you send), and assistant (what the AI replies).</p>

<h3 class="term">System prompt<span class="lv lv1">L1</span></h3>
<p>The instruction set before the conversation begins, defining the AI's role, behaviour and limits — for example, “you are a senior Java backend expert; answer with concise, clear code”.</p>
<p>It stays in force for the whole conversation, which makes it the main lever for customising behaviour. The source recalls the wave of “AI assistant” sites a few years ago: many were the same model underneath, differentiated only by their system prompts — translator, legal adviser, and so on.</p>

<h3 class="term">Prompt engineering<span class="lv lv1">L1</span></h3>
<p>The craft of designing and refining prompts so the AI understands your intent and produces what you expected.</p>
<p>It is one of the core skills of vibe coding: a good prompt engineer gets better code with fewer turns and fewer tokens.</p>

<h3 class="term">Zero-shot<span class="lv lv2">L2</span></h3>
<p>Giving the task with no examples at all — just a description, such as “translate this paragraph”. The model relies on what it already learned.</p>
<p>For simple tasks it is enough, and it saves tokens. For anything with a house style, it is a gamble.</p>

<h3 class="term">Few-shot<span class="lv lv2">L2</span></h3>
<p>Adding a few input-output examples so the model learns the format or style you want before it produces its own.</p>
<p>The source's example is a translation template: two filled pairs, then a third with only the left side, and the model completes it in the same shape. Examples make the requirement concrete, and the output more consistent.</p>

<h3 class="term">Chain of thought<span class="lv lv2">L2</span></h3>
<p>A prompting technique that asks the model to show its reasoning step by step instead of jumping to an answer. It is especially effective on multi-step arithmetic, code logic and system design.</p>
<p>Many reasoning models and coding tools now do this by themselves; you can also add “think step by step” to the prompt. For projects with complex business rules, several interacting modules, or a choice between technical approaches, it pays to let the model reason before it writes.</p>

<h3 class="term">Markdown<span class="lv lv1">L1</span></h3>
<p>A lightweight markup language: <code>#</code> for headings, <code>**bold**</code>, <code>-</code> for lists.</p>
<p>It matters in AI coding for three reasons: most answers come back in Markdown, project documents such as the README are written in it, and the rules files that define an agent's behaviour are Markdown too.</p>
<p>The deeper reason from the source: structure — heading levels, lists, code blocks — helps the model understand your intent more precisely, and trains your own structured thinking, which in turn makes your prompts better.</p>

<h2 id="modes">3. The modes</h2>

<p class="term-lead">The source's largest chapter, and the one where names are most easily confused. Its own framing is useful here: prompt engineering asks how to instruct, context engineering asks what to supply, and harness engineering asks how to keep the whole job reliable — each one containing the last.</p>

<h3 class="term">Vibe coding<span class="lv lv1">L1</span></h3>
<p>A concept Andrej Karpathy proposed in February 2025: you talk to the AI in natural language, describe what you want, test the result and steer the direction. You do not need to know syntax — only to say clearly what you mean.</p>
<p>So the point is not writing code but specifying a requirement. The clearer the description, the more reliable the result. The source's analogy is ordering takeaway: you say what you want, the kitchen cooks it; you do not need to cook, but you do need to know what you feel like eating.</p>

<h3 class="term">Agentic engineering<span class="lv lv1">L1</span></h3>
<p>Karpathy's follow-up concept, from February 2026 — effectively the disciplined version of vibe coding. Instead of one sentence and whatever comes back, you think the work through, write the plan, split the tasks, hand them over, then review the delivery and send it back if the quality is not there.</p>
<p>The source's image: in vibe coding you are a DJ, playing whatever feels right; in agentic engineering you are the site foreman, and process, quality and sign-off are yours. One follows feeling, the other follows procedure.</p>
<p>Neither replaces the other. Vibe coding shows you what is possible; agentic engineering turns that possibility into something usable. Small tools can stay on the first; company projects need the second.</p>

<table class="seg-table">
<thead><tr><th></th><th>Vibe coding</th><th>Agentic engineering</th></tr></thead>
<tbody>
<tr><td><span class="en">Stance</span></td><td><span class="en">Follow the feeling</span></td><td><span class="en">Follow the process</span></td></tr>
<tr><td><span class="en">Your role</span></td><td><span class="en">DJ</span></td><td><span class="en">Foreman</span></td></tr>
<tr><td><span class="en">Fails when</span></td><td><span class="en">The project gets big</span></td><td><span class="en">The process is skipped</span></td></tr>
</tbody>
</table>

<h3 class="term">Agentic coding<span class="lv lv2">L2</span></h3>
<p>Letting the AI work as an autonomous agent: plan the task, execute the operations, verify the result — rather than answering questions passively.</p>
<p>The distinction from agentic engineering is one of subject: agentic coding is about what the AI can do on its own; agentic engineering is the human method for managing it. In Cursor's agent mode, for instance, the AI reads several files, plans an approach, edits code, runs tests and fixes what fails.</p>

<h3 class="term">Harness engineering<span class="lv lv3">L3</span></h3>
<p>A 2026 paradigm whose core idea is <strong>human steers, agent executes</strong>. It does not optimise the model; it builds the constraints, feedback loops and workflow management around the agent so an unpredictable model runs steadily in a high-reliability environment.</p>
<p>The word is a horse harness — reins and saddle for a strong animal that does not always go where you point. The argument for it: the model is now a commodity, and the competitive part is the engineering system around it. The same model in different harnesses produces very different code, and the programmer's job shifts from writing code to designing the system that makes the AI write it reliably.</p>
<p>The source places it as the third step: prompt engineering asks how to instruct, context engineering asks what to supply, harness engineering asks how to get a whole job finished reliably. Its modules: context architecture, execution capability (tools and MCP), task orchestration (plan mode, parallel subagents), feedback (linters, tests, browser use), and architectural guardrails against entropy.</p>

<h3 class="term">Loop engineering<span class="lv lv3">L3</span></h3>
<p>A mid-2026 paradigm: design an automatic loop so the AI executes, verifies and repairs itself until the goal is met. Manual driving versus automatic — you set the destination and the safety rules, then it drives.</p>
<p>A workable loop needs three things: a clear goal with a stopping condition (“all tests pass” is a good one), a feedback closure that checks each round, and state kept outside the conversation — a <code>PROGRESS.md</code> — so a crash does not restart from zero. It sits on top of the previous three: the environment makes work reliable, the loop makes it repeat without you.</p>

<h3 class="term">Multi-agent collaboration<span class="lv lv3">L3</span></h3>
<p>Several agents dividing the work — one designs the architecture, one writes the front end, one the back end, one reviews — the way a software team would.</p>
<p>Its advantages are not only handling bigger projects but speed: work that took hours can finish in minutes when the parts run in parallel.</p>

<h3 class="term">Agent orchestration<span class="lv lv3">L3</span></h3>
<p>Coordinating several agents or tasks so they run in the right order and hand results over correctly.</p>
<p>If multi-agent collaboration asks which roles exist, orchestration asks who goes first, who follows, and how results are merged. The source's image is a conductor: the orchestrator decides who does what, when, what they tell each other, and how it all comes together.</p>

<h3 class="term">Subagents<span class="lv lv2">L2</span></h3>
<p>The main agent hands part of the work to independent sub-agents that run in parallel — a manager giving jobs to several staff at once.</p>
<p>The benefits: parallelism, a clean main context unpolluted by sub-task detail, and tighter focus per agent. In Claude Code the built-in Task tool spawns them automatically; you can also define custom ones as Markdown files under <code>.claude/agents/</code> with their own role, tool permissions and rules.</p>
<p>The limits: sub-agents have separate contexts and cannot share information directly, so tightly coupled work does not suit them, and running several at once costs more tokens — hiring more people is faster, but the payroll and the coordination cost go up too.</p>

<h3 class="term">Agent teams<span class="lv lv3">L3</span></h3>
<p>A 2026 pattern introduced by Claude Code: three to five independent agents form a team on one project, with a team lead splitting the work and teammates claiming tasks and messaging each other.</p>
<p>The source's image: you used to manage one intern; now you manage a small team, with front end, back end and testing running at once. Anthropic's own engineers ran sixteen agents together and produced a hundred thousand lines of Rust, compressing days into hours — at the cost of more tokens, so it is not the default choice.</p>
<p>In practice the agents need physical isolation to avoid conflicts: Git worktrees give each one its own directory and branch. Cursor's parallel agents mode does this automatically and merges with one click.</p>

<h3 class="term">Hermes Agent<span class="lv lv3">L3</span></h3>
<p>An open-source, self-improving agent released by Nous Research in February 2026. Its distinguishing feature is that it learns from the tasks it completes.</p>
<p>Ordinary agents start from zero each time. Hermes runs a closed learning loop: when a task finishes, it distils the solution into a reusable skill document; next time it retrieves similar documents first; and it keeps refining them with new practice. The source cites a 40% speed-up on similar tasks once skills accumulate.</p>
<p>It keeps three layers of memory — session, skill documents, and a persistent user profile — connects through Telegram, Slack, Discord and WeChat, supports over two hundred models, and is free and open source.</p>

<h3 class="term">Background agents<span class="lv lv2">L2</span></h3>
<p>Hand a task over and walk away: the agent runs in the cloud and notifies you when it is done, so you can close the laptop.</p>
<p>Typical jobs are fixing a batch of bugs, running a review pass, or finishing a whole feature module. The source's prediction is that this becomes like sending a message: you describe the work from your phone, go do something else, and come back to review.</p>

<h3 class="term">Personal agents<span class="lv lv2">L2</span></h3>
<p>A step beyond the background agent: not one task, but an assistant that stays with you long term.</p>
<p>The source lists four traits: a name and long-term memory that accumulates your preferences; its own cloud computer, so it does not occupy yours; authorised access to your mail, calendar and social accounts; and scheduled work that runs while you are offline and reports back.</p>
<p>In late 2026 the large vendors shipped these — Grok Bot, Meta's Muse, OpenAI's Dots. OpenClaw and Hermes are the same idea self-hosted: a bare shell you furnish yourself, versus a furnished flat whose rent is your data and memory sitting on someone else's cloud.</p>

<h3 class="term">Super-agents<span class="lv lv3">L3</span></h3>
<p>An architecture proposed and open-sourced by the DeepSeek Harness team in October 2026. The goal is to detach the agent from a single session, so that handling several tasks at once does not turn the human into a messenger between them.</p>
<p>If an ordinary agent is a contractor who can only do one job at a time, a super-agent is a working project team: a resident <strong>router</strong> receives messages from Feishu, GitHub and elsewhere, remembers the whole picture and assigns work; <strong>workers</strong> each keep their own context, run tasks concurrently and subscribe to follow-ups on their own tickets. Two-level event filtering, asynchronous full-duplex exchange, separated storage and compute (bring your own model), and a watchdog keep it running around the clock.</p>

<h3 class="term">Agent loop<span class="lv lv2">L2</span></h3>
<p>The core mechanism of any agent: perceive, think, act, observe, and repeat until the task is done or a termination condition is met.</p>
<p>Perception reads the environment — files, errors; thinking decides the next move; action executes it; observation checks what happened; the loop decides whether to continue.</p>
<p>The practical warning from the source: do not let the loop run too long. Most tools cap the number of iterations, and long loops both degrade and burn tokens — people have woken up to an exhausted quota because the agent was stuck circling. Claude Code's own implementation is a plain <code>while(true)</code>: compress the context, call the model, execute any requested tool, append the result, repeat.</p>

<figure class="article-figure">
  <img src="/assets/images/agent-loop.svg" alt="A loop from task to model to tool call to result, returning to the model, with a note that writes need a confirmation." width="900" height="374">
  <figcaption>The loop is the difference between a chat and an agent. The exit is not a decision you make — it is the model stopping, or a limit you set.</figcaption>
</figure>

<h3 class="term">Ralph Wiggum loop<span class="lv lv3">L3</span></h3>
<p>A 2026 pattern named after the Simpsons character who never gives up: put the AI in a loop and let it run until every checklist item in the requirements document is done.</p>
<p>The workflow: write a PRD that breaks the feature into checkable items; the agent picks an unfinished one; when it finishes, it commits and records progress; the next round starts with a completely fresh context; repeat until the list is empty.</p>
<p>Its cleverness is the clean context each round, with progress persisted in Git rather than a long conversation — which avoids the agent losing the plot, and lets it run unattended. The source's caution: set an iteration limit and a token budget, or it will loop and burn money.</p>

<h3 class="term">ReAct<span class="lv lv3">L3</span></h3>
<p>Reasoning and acting, alternating: think about the situation, act, look at the effect, then think again about the next step.</p>
<p>Traditional AI either thought without acting or acted without thinking. ReAct interleaves them — reason, act, observe, adjust — which is why it is one of the core techniques under modern coding agents.</p>

<h3 class="term">Deep thinking<span class="lv lv2">L2</span></h3>
<p>The model's built-in ability to reason internally before answering — also called extended thinking or thinking mode.</p>
<p>It differs from chain-of-thought prompting: CoT is a prompt technique that asks for visible reasoning, while deep thinking is a model capability that happens without being asked. In normal mode the answer comes straight out; with it on, the model analyses, weighs options and evaluates trade-offs first — the “thinking…” you sometimes see.</p>
<p>It suits architecture design, stubborn bugs and algorithm work. The cost is slower responses and more tokens, and most models and tools now let you switch it on or off.</p>

<h3 class="term">Adaptive thinking<span class="lv lv2">L2</span></h3>
<p>The smarter version of the above: the model judges for itself how much reasoning the question deserves.</p>
<p>The old manual switch had a problem — turn it on and simple questions crawl; turn it off and hard ones fail. Adaptive thinking answers easy questions instantly and routes hard ones into deep reasoning, keeping both quality and cost. Anthropic introduced it in Claude Opus 4.6 and refined it in 4.8, with effort levels developers can set.</p>

<h3 class="term">Tool use<span class="lv lv2">L2</span></h3>
<p>The technology that lets the AI use external tools. On its own a model only produces text; with tool use it can read and write files, search the web, run commands and scripts, call APIs, and query databases.</p>
<p>Four steps: recognise that a tool is needed, choose which one, call it with the right arguments, and fold the result back into the answer.</p>
<p>The model never executes anything itself — it emits “I want to call this tool with these arguments”, the runtime executes, and the result returns to the model. That is the difference between an assistant that tells you what to change and one that changes it.</p>

<h3 class="term">MCP<span class="lv lv2">L2</span></h3>
<p>The Model Context Protocol, an open standard released by Anthropic at the end of 2024 for connecting models safely to external data sources and tools.</p>
<p>The source's image is the USB port of the AI world: one shape that everything plugs into, instead of a custom cable per device. Developers write a connector once to the standard and every MCP-capable tool can use it — Claude Code, Cursor, Windsurf and most web agents support it.</p>
<p>What it buys in practice: a Figma MCP lets the model read a design and generate the page; a GitHub MCP lets it work with repositories and open pull requests; a database MCP lets it query real business data.</p>

<h3 class="term">Agent skills<span class="lv lv2">L2</span></h3>
<p>An open standard from Anthropic, released in October 2025, that lets an agent learn professional procedures and extend its capability in a specific domain.</p>
<p>A skill is a <strong>skill pack</strong>: carefully written instructions, scripts and resource files. The source's image is a new hire — install the document-processing skill and it knows how to make slides and handle spreadsheets; install the coding-standards skill and it writes to your company's conventions.</p>
<p>Concretely it is a folder containing a <code>SKILL.md</code> file, with instructions, code and references beside it. The key design is <strong>progressive disclosure</strong>: content loads only when a matching task appears, so it saves tokens and stays flexible.</p>

<h3 class="term">Hooks<span class="lv lv3">L3</span></h3>
<p>Automated triggers inside AI coding tools: when the AI finishes an action — generating code, committing, running a command — the hook runs a script or check you defined.</p>
<p>In Claude Code they can format code after generation, run tests after a file changes, judge whether a permission request is safe, or check conventions before a commit.</p>
<p>The source's caution: a badly configured hook can block the agent's normal workflow, so test it on a small scope before applying it to the whole project.</p>

<h3 class="term">Slash commands<span class="lv lv2">L2</span></h3>
<p>Shortcuts typed with <code>/</code> in the chat box to trigger common operations — the keyboard shortcuts for operating an AI.</p>
<p>Claude Code ships several: <code>/help</code> for available commands, <code>/compact</code> to compress the current context, <code>/config</code> for settings, <code>/skills</code> to list installed skills.</p>
<p>You can define your own to package a workflow — a <code>/commit-push-pr</code> that commits, pushes and opens a PR in one go, or a <code>/techdebt</code> that clears duplicated code at the end of a session. A custom command is just a Markdown file in <code>.cursor/commands/</code>; the filename becomes the command, and the files can live in Git for reuse across projects.</p>

<h3 class="term">A2A<span class="lv lv3">L3</span></h3>
<p>Agent-to-Agent: the protocol by which agents communicate and collaborate — the foundation of any multi-agent system.</p>
<p>Just as people need a shared language, agents need a standard way to exchange information, assign tasks and report results. Google launched it in 2025 and more than 150 companies have joined.</p>
<p>Do not confuse it with MCP: they are complementary. MCP connects an agent to tools; A2A connects agents to each other.</p>

<h3 class="term">ACP<span class="lv lv3">L3</span></h3>
<p>Two different things share this acronym. <strong>Agent Communication Protocol</strong>, from IBM Research, lets agents built on different frameworks and by different companies work together — like phones from different brands calling each other. It is built on lightweight HTTP REST, handles text, code, files and images, and does not care which language you write in.</p>
<p><strong>Agent Client Protocol</strong>, from JetBrains and Zed, solves something else entirely: letting any coding agent run inside any IDE. Before it, every agent needed a separate plugin per editor; now an agent implements ACP once and IDEA can host it — Claude Code in IDEA, Gemini CLI in Zed, no longer locked to one editor. JetBrains also runs an ACP agent registry for one-click installs.</p>
<p>ACP and A2A are independent: both address cross-framework collaboration, with different formats and different discovery mechanisms.</p>

<h3 class="term">BMAD<span class="lv lv3">L3</span></h3>
<p>The Breakthrough Method of Agile AI-Driven Development: a systematic framework for AI-agent development whose aim is to make a messy AI coding process structured and reusable.</p>
<p>It organises work through <strong>role-playing agents</strong> — an analyst who writes the project brief with market analysis and user profiles, a product manager who turns it into a PRD, an architect who designs the technical approach. Agents come in two kinds: simple, single-file and self-contained for focused jobs such as review or documentation; and expert, with cross-session memory and a resource folder for complex multi-step workflows.</p>
<p>Each agent has standard parts: persona (role, identity, communication style, principles), capability list, interaction menu, and optional key actions.</p>

<h3 class="term">Browser use<span class="lv lv3">L3</span></h3>
<p>The ability of an agent to drive a web browser on its own: browse, click, fill forms, extract data.</p>
<p>Typical uses are research across several sites, structured data collection, tedious form filling, and multi-step tasks that cross platforms. The best-known open-source project is Browser-Use, which drives browsers from Python with various models; Cursor and Claude Code also build the capability in for previewing and testing during development.</p>
<p>Its key advantage: the agent can use your existing session and logins, so it reaches sites with no public API — which widens automation considerably.</p>

<h3 class="term">Computer use<span class="lv lv3">L3</span></h3>
<p>Anthropic's capability, released in 2024, that lets Claude operate a whole desktop the way a person does — reading screenshots, moving the cursor, clicking, typing, running commands.</p>
<p>Unlike browser use, it reaches any desktop application. The mechanism is a continuous loop: capture the screen, decide the next step, send input, observe the result and adjust.</p>
<p>For safety it is normally run in a virtual machine or container rather than on your real computer. The source notes the direction of travel: on top of it, Anthropic shipped Claude Cowork in 2026, a desktop assistant that works directly with your files — tidying the downloads folder, pulling figures out of screenshots into a spreadsheet, preparing a brand report.</p>

<h2 id="context">4. The context</h2>

<h3 class="term">Context<span class="lv lv1">L1</span></h3>
<p>Everything the AI can refer to when answering: the history of the current conversation, the files you have open, the project's structure and configuration, and any reference material you supplied.</p>
<p>The richer and more relevant the context, the better the code fits your need. The source's analogy is handing work over to a new colleague — the more background you give, the faster they become useful. Cursor shows a token meter near the chat box; in Claude Code, <code>/context</code> reports what is currently occupying the window.</p>

<figure class="article-figure">
  <img src="/assets/images/context-window.svg" alt="A context window containing rules, chosen files, retrieved documents and the conversation, with an unpasted conversion table sitting outside it." width="900" height="330">
  <figcaption>The window is the whole world for one call. A table you never pasted is not “forgotten” — it does not exist yet.</figcaption>
</figure>

<h3 class="term">Context engineering<span class="lv lv1">L1</span></h3>
<p>Managing and optimising what goes into the context, with one goal: the AI should have exactly the right amount of information — not so little that it misunderstands, not so much that it drowns and the bill rises.</p>
<p>The practices: choose the most relevant files, supply the necessary background, define project conventions in a rules file, and clear irrelevant history at the right moment. It is an active research area, and the 2026 direction is from simple management toward a <strong>memory architecture</strong>: short-term (this conversation), long-term (accumulated across sessions), and external (vector databases, knowledge graphs).</p>
<p>The source's example is Claude Code's own three tiers: a <code>MEMORY.md</code> of hot data, loaded every time but capped at 200 lines and 25KB; topic files of warm data — coding preferences, project conventions — of which only the five most relevant load at the start of a conversation; and past conversations as cold data, searched with grep when needed. One detail worth copying: the memory stores people's preferences and judgements, never code facts, because code changes and a stale memory about where a function lives becomes a trap.</p>

<h3 class="term">Compaction<span class="lv lv2">L2</span></h3>
<p>Automatic summarising of earlier conversation when the context is about to overflow, so a long task can continue without the AI losing the thread.</p>
<p>The source's analogy is meeting minutes: after three hours you cannot record every sentence, but the decisions, the action items and the conclusions are kept. Compaction does the same to a conversation.</p>
<p>Claude Code implements it as a five-stage funnel: snip old tool results down to their structure, offload large outputs to cache, collapse the middle of the conversation into a summary, autocompact when a threshold is crossed, and finally react when the API returns a “prompt too long” error. Light cuts first, heavy ones only when needed.</p>

<h3 class="term">Rules file<span class="lv lv2">L2</span></h3>
<p>A configuration file in the project that tells the AI your conventions, stack and code style, so every generation already fits — no repeating yourself each session.</p>
<p>Formats differ by tool: Cursor moved from a single <code>.cursorrules</code> to <code>.cursor/rules/*.mdc</code>, Claude Code uses <code>CLAUDE.md</code>, GitHub Copilot uses <code>.github/copilot-instructions.md</code>. Cursor's <code>.mdc</code> files carry YAML frontmatter — description, globs, alwaysApply — and can be activated always, by file pattern, by explicit reference with <code>@</code>, or by the AI's own judgement of relevance.</p>
<p>The source's note: these file names and standards change with tool versions, so the official documentation wins.</p>

<h3 class="term">AGENTS.md<span class="lv lv2">L2</span></h3>
<p>An open file format for giving coding agents project instructions — a rules file, but cross-tool rather than tied to one product.</p>
<p>The distinction from a README: the README is written for people and explains what the project is; <code>AGENTS.md</code> is written for the AI and carries the technical detail it needs — build and start commands, how to run tests, style rules, project structure. Tens of thousands of open-source projects have adopted it, and tools such as Claude Code, Codex, Cursor and Copilot pick it up from the repository root automatically.</p>

<h3 class="term">Spec-driven development<span class="lv lv3">L3</span></h3>
<p>A methodology for the AI era: write an explicit specification first, treat it as the single source of truth, and make the code conform to it. The spec is a “project constitution” — requirements, design, interfaces — and the AI must follow its articles.</p>
<p>The argument for it: the quality of generated code depends on how clear the context is, far more than on prompt tricks. A clear spec beats any prompt wizardry.</p>
<p>The six steps in the source: constitution (principles, standards), specify (what and why), clarify (the AI asks structured questions about edge cases and error handling), plan (stack, architecture, data model, APIs), tasks (a dependency-ordered list), implement (the AI writes, the human verifies). It is the standard corporate process with the executor changed from a person to a model. GitHub's open-source Spec Kit, released in September 2025, walks you through it with slash commands.</p>

<h3 class="term">RAG<span class="lv lv2">L2</span></h3>
<p>Retrieval-augmented generation: retrieve from an external knowledge base first, then answer from what was retrieved, so the answer is grounded rather than remembered.</p>
<p>An ordinary model relies on what it learned in training, which may already be out of date. RAG lets it look at your documents, your codebase, your knowledge base at question time — particularly useful in company settings, where it can follow the style of code you already have.</p>
<p>In production the pattern has grown variants: multi-query retrieval, HyDE (generate a draft answer, then search with its vector), hybrid search (vectors plus keywords), reranking to filter noise, GraphRAG for multi-hop reasoning across documents, and agentic RAG. Different problems need different combinations.</p>

<h3 class="term">Agentic RAG<span class="lv lv3">L3</span></h3>
<p>The evolved form: the fixed retrieve-then-generate pipeline becomes a closed loop controlled by an agent.</p>
<p>The source's contrast is a librarian versus a researcher. A traditional RAG librarian fetches once from the shelf and hands back whatever was found, right or wrong. An agentic researcher thinks about where to look, judges whether what came back is relevant, searches again from another angle if it is not, checks several sources, and repeats until satisfied.</p>
<p>Its capabilities: multiple retrieval rounds, query rewriting, several data sources at once (vector store, API, web, SQL), and self-correction. Named patterns include CRAG (corrective, with a retrieval evaluator), Self-RAG (reflection during generation) and Adaptive RAG (choosing a strategy by question type). The cost is latency and several times the tokens, so it suits high-stakes, high-accuracy work — legal, medical, compliance. A simple single-source lookup does not need it.</p>

<h3 class="term">Vector database<span class="lv lv3">L3</span></h3>
<p>A database built to store and query vectors — arrays of numbers such as <code>[0.1, 0.5, 0.3, 0.8]</code> — where each number is a feature dimension. Text, images and code can all be turned into such arrays, and semantically similar content ends up with similar vectors.</p>
<p>Once your code or documents are stored this way, the AI finds semantically close material even when the words differ: search “user login” and it can return a function named <code>handleAuth</code>. The AI boom produced a large field of databases that support vector storage.</p>

<h3 class="term">Embeddings<span class="lv lv2">L2</span></h3>
<p>The process of turning text, code or other content into a numeric vector that captures its meaning. In vector space, similar meanings sit closer together — which is exactly why semantic search works.</p>
<p>You do not need the mathematics. It is enough to know that embeddings are the foundation under RAG and under semantic code search.</p>

<h2 id="output">5. The output</h2>

<h3 class="term">Hallucination<span class="lv lv1">L1</span></h3>
<p>Output that does not match reality: an API that does not exist, a function used the wrong way, a library invented outright, or a confident paragraph that is simply false.</p>
<p>It is inherent to models that generate by probability — sometimes they fill the gap with something made up. The source's mitigations are practical: ask the AI for documentation links and check them, verify against official docs yourself, try another model, start a new conversation and restate the problem, or use a documentation MCP such as Context7 to pull current technical references.</p>
<p>For people building AI applications, reducing hallucination is a central problem, and RAG is the most common answer: retrieve real data first, generate afterwards.</p>

<h3 class="term">Temperature<span class="lv lv1">L1</span></h3>
<p>The parameter controlling randomness, usually between 0 and 2, though ranges differ by model and tool.</p>
<p>Low (around 0.1) gives determined, conservative output — what you want for code. High (around 1.0) gives variety and invention — what you want for brainstorming names, copy, or product ideas.</p>
<p>In coding, keep it low for predictable, stable output; raise it deliberately when the task is to generate options rather than a correct answer.</p>

<h3 class="term">Streaming<span class="lv lv2">L2</span></h3>
<p>Showing the answer as it is generated, instead of waiting for the whole thing.</p>
<p>The source's image is live broadcast versus recorded video: you watch the output arrive, and if the direction is wrong you can stop it early and save the tokens. Most coding tools stream by default, and the underlying mechanism is usually Server-Sent Events, with the server pushing fragments to the client.</p>

<h3 class="term">System-1 models<span class="lv lv3">L3</span></h3>
<p>A class of models that do not generate text — they only decide. The name comes from <em>Thinking, Fast and Slow</em>: system one is fast intuition, system two is slow reasoning, and while a conventional model behaves like system two, a decision model is system one. The source's example is Jev, opened in September 2026.</p>
<p>Ask whether an email is urgent and it does not write an analysis; it returns JSON — yes, 95%. It handles three question shapes: yes or no with a probability, choose one of several with probabilities, or a score on your own scale. Because nothing is written word by word, it answers in milliseconds, costs far less, and the output format is fixed by construction, so it never fails to parse.</p>
<p>Its natural role is the intelligent <code>if</code> statement inside a program: ticket classification, content moderation, the quick decision at each step of an agent. Anything that needs prose or arithmetic still belongs to a conventional model.</p>

<h2 id="tools">6. The tools</h2>

<h3 class="term">IDE<span class="lv lv1">L1</span></h3>
<p>An integrated development environment: the all-in-one program for writing code, usually bundling an editor, a debugger, a terminal and a plugin marketplace.</p>
<p>VS Code is the most popular lightweight IDE — built by Microsoft and open source. Cursor and Windsurf are built on top of it, inheriting the interface and extending the AI side considerably.</p>

<h3 class="term">Code editor<span class="lv lv1">L1</span></h3>
<p>The tool for writing and changing code, with syntax highlighting, completion and error hints. Sublime Text and Vim are the familiar examples.</p>
<p>The difference from an IDE is weight: an editor is lighter and starts faster, good for quick edits to a single file; an IDE carries the debugger, terminal and version control, which suits professional work and large projects.</p>
<p>In the vibe coding era the editor absorbed AI: generate from a prompt, explain code, fix errors. Early Cursor was powerful, but at heart still an editor with AI added.</p>

<h3 class="term">CLI<span class="lv lv2">L2</span></h3>
<p>The command line interface — typing text commands in a small black window, as opposed to the GUI of icons, buttons and windows.</p>
<p>It is having a revival, and not because programmers like terminals. Models have read enormous amounts of code and shell commands, so reading a command and executing it is natural for them; driving a graphical interface is not — screenshots, element hunting, simulated clicks, slow and error-prone. The source cites a test where an AI finished tasks through a browser only 35.8% of the time, and close to 100% through a CLI.</p>
<p>That is why vendors have been open-sourcing CLIs for their own products — Google, Feishu, DingTalk, WeCom. Products used to be designed for human users only; now they need an interface for agents too. The prediction: two front ends per product, a GUI for people and a CLI for AI.</p>

<h3 class="term">No-code platforms<span class="lv lv2">L2</span></h3>
<p>Platforms that build applications without writing code. Low-code is the neighbour: a little code plus visual dragging, with more freedom.</p>
<p>In the AI era these platforms merged with models — Bolt.new, Lovable, v0.dev, Baidu Miaoda — and you describe the requirement in natural language while the platform generates a complete, online application.</p>
<p>They suit people with no programming background and anyone who needs a quick prototype. The weaknesses are equally clear: problems are hard to debug, deep customisation is difficult, and a project that grows hits a ceiling.</p>

<h3 class="term">Code completion<span class="lv lv1">L1</span></h3>
<p>The AI predicting what you are about to write from the surrounding code and offering it inline; you press Tab to accept.</p>
<p>GitHub Copilot started this in 2021. Within a few years the same technology moved from completing a few lines to developing a whole project, and many developers now skip line-by-line completion and let an agent write an entire feature in one pass.</p>

<h3 class="term">Code review<span class="lv lv2">L2</span></h3>
<p>Checking code for quality, finding problems and suggesting improvements — before merge rather than after launch, when fixes are far more expensive.</p>
<p>Traditionally a colleague or a senior did it. In vibe coding you can ask the AI: it points out potential bugs, security issues and performance problems, with suggested changes.</p>
<p>The source's warning is worth keeping: AI review does not fully replace a human review, especially for important production code.</p>

<h3 class="term">Linter<span class="lv lv2">L2</span></h3>
<p>A tool that automatically checks code for syntax errors, style problems and potential bugs. ESLint for the front end, Pylint for Python, golint for Go — a strict grammar teacher that keeps the code consistent.</p>
<p>In vibe coding it catches problems in generated code quickly, and most front-end scaffolds now wire ESLint in for you, so there is nothing to configure.</p>

<h3 class="term">Debugging<span class="lv lv2">L2</span></h3>
<p>The process of finding and fixing errors when behaviour does not match expectation: breakpoints and stepping, watching variables, reading error messages and stack traces, adding log output.</p>
<p>With an AI in the loop you can paste the error straight in and let it analyse the cause, propose a fix, or repair it on its own.</p>

<h3 class="term">OpenClaw<span class="lv lv3">L3</span></h3>
<p>The most conspicuous open-source AI project of 2026: it reached the top of GitHub's star history in a little over a hundred days, with more than 300,000 stars.</p>
<p>Think of it as a digital employee that can operate your computer — not a chat bot, but something that opens software, drives the browser, handles files and runs code. You can send it work from a chat app on your phone, and it completes the task on your machine.</p>
<p>Its features: real execution rather than advice, connections to WeChat, QQ, Feishu, Telegram and Discord, a skill ecosystem you extend by installing packs, support for Anthropic, OpenAI and Chinese models, and a fully open MIT licence with local deployment so the data stays yours.</p>
<p>The source's caution is proportionate to the power: OpenClaw's permissions are large, and it needs care in use.</p>

<h2 id="project">7. The project words</h2>

<h3 class="term">MVP<span class="lv lv1">L1</span></h3>
<p>The minimum viable product: the version with the fewest features that still meets the core need — something that runs and does the essential job.</p>
<p>Beginners tend to plan every feature at once, spend their time on the unnecessary ones, and abandon the project when it becomes too complex. The MVP reverses that: prove the core value with the least software, get feedback, then iterate. The source's example is an expense app whose first version records expenses and lists them, with everything else later.</p>

<h3 class="term">Iteration<span class="lv lv1">L1</span></h3>
<p>Splitting a large project into small cycles, each one finishing a part of the functionality.</p>
<p>A cycle runs plan → develop → test → release → feedback → improve. It suits vibe coding particularly well: let the AI implement the core, check it, then add the next piece. It is also one of the core practices of agile development — small steps, fast feedback, embrace change — which matches the rhythm of AI-assisted work.</p>

<h3 class="term">Refactoring<span class="lv lv2">L2</span></h3>
<p>Improving the structure and quality of code without changing what it does: extracting repeated code into a function, improving names, simplifying logic, splitting an over-long file.</p>
<p>An AI can do this for you, but in small steps, with tests after each one. The source's qualification is fair: for a quick throwaway tool, working code is enough; for a long-lived project, code quality decides how fast you can iterate later, so regular refactoring earns its time.</p>

<h3 class="term">Technical debt<span class="lv lv2">L2</span></h3>
<p>The temporary solutions taken to ship quickly, which will need time later to put right. The source's image is a credit card: convenient now, repaid with interest.</p>
<p>AI-generated code is not always the best solution, and accumulated debt makes a project progressively harder to maintain. Regular refactoring is the repayment plan.</p>

<h3 class="term">Version control<span class="lv lv1">L1</span></h3>
<p>The system that records the history of code changes, so you can trace each change, compare versions, and roll back.</p>
<p>Git is the standard, and it is worth keeping distinct from GitHub: Git runs on your computer, GitHub is the online platform that hosts and shares repositories.</p>
<p>In vibe coding this matters more than usual — the AI may generate broken code, and with version control the previous working state is always one step away.</p>

<h3 class="term">Git worktree<span class="lv lv3">L3</span></h3>
<p>A hidden Git feature that lets one repository have several independent working directories, each on a different branch.</p>
<p>Normally a repository has one working directory, so you can only work on one branch at a time and must stash changes to switch. A worktree is a clone of yourself: several branches in progress without interference.</p>
<p>It is not the same as copying the folder. A copy duplicates the whole <code>.git</code> directory and history, takes space and makes merging awkward; a worktree links to the same <code>.git</code> and shares the history.</p>
<p>Its best use in AI coding is parallel agents: three features become three worktrees, one agent each, merged at the end. Cursor's parallel agents mode creates and manages them for you. The practical warning: give different agents different files, or the merge produces conflicts you have to resolve by hand.</p>

<h3 class="term">Deployment<span class="lv lv2">L2</span></h3>
<p>Publishing a finished application to a server so people can reach it.</p>
<p>The original method — log into the server, upload an archive, run it yourself — is error-prone; platform deployment is a few clicks. Vercel suits front-end and full-stack apps, Netlify suits static and front-end sites, Railway and Render suit back-end services, and no-code platforms such as Bolt.new deploy in one button.</p>
<p>There is also an MCP route: with EdgeOne Pages MCP, you describe what you want and the AI packages and deploys the site without you logging into anything.</p>

<h3 class="term">GEO<span class="lv lv3">L3</span></h3>
<p>Generative engine optimisation — SEO for the AI era. SEO asks how to rank high in search results; GEO asks how to be quoted and recommended by ChatGPT, DeepSeek and similar assistants.</p>
<p>The source's image: SEO is grabbing the golden shelf in a supermarket; GEO is getting the shop assistant to recommend your product when a customer asks.</p>
<p>Its strategies: state the conclusion first, because extracts come from the opening; write in structure — heading levels, question-and-answer form, comparison tables; build authority with specific data and citable sources; publish on high-weight platforms; and keep the technical side open, with robots.txt allowing AI crawlers and server-side rendering so pages can be read. GEO does not replace SEO — good SEO helps GEO — and both are content work, not tricks.</p>

<h2 id="stack">8. Front end, back end</h2>

<h3 class="term">Frontend<span class="lv lv1">L1</span></h3>
<p>Everything the user sees and touches: the interface, buttons, forms, animation. Bluntly, whatever appears in the browser is the front end.</p>
<p>The stack: HTML for structure, CSS for layout and style, JavaScript for interaction, and frameworks such as React, Vue or Next.js.</p>
<p>It is the part AI generates best, because the result is visible and therefore easy to check and adjust. The source also offers a practical goal — use skills and carefully written prompts to remove the tell-tale “AI flavour” from a generated page.</p>

<h3 class="term">Backend<span class="lv lv1">L1</span></h3>
<p>The part users never see: business logic, data storage, authentication.</p>
<p>When you press “place order” on a shop, the front end sends the order to the back end, which checks stock, calculates the price, takes payment, creates the order, and returns the result to be displayed. The stack: Node.js, Python or Java; Express, FastAPI or Spring; MySQL, PostgreSQL or MongoDB.</p>
<p>It is harder than the front end — security, performance, data consistency — and the source's conclusion follows: AI-generated back-end code needs closer review.</p>

<h3 class="term">Full stack<span class="lv lv1">L1</span></h3>
<p>An application that includes both front end and back end, and a developer who can handle both.</p>
<p>In vibe coding, tools such as Cursor and Bolt.new can generate a full-stack application in one pass, writing both halves for you.</p>

<h3 class="term">API<span class="lv lv2">L2</span></h3>
<p>The interface through which programs talk to each other.</p>
<p>The source's analogy is a restaurant menu: it tells you what can be ordered, how to order, and what will arrive. You do not need to know the kitchen; you order from the menu. In web development the front end talks to the back end through an API to fetch data or submit actions.</p>

<h3 class="term">Database<span class="lv lv1">L1</span></h3>
<p>The system that stores and manages data: user records, content, settings.</p>
<p>Three common shapes: relational (MySQL, PostgreSQL) as tables; document (MongoDB) as JSON documents; key-value (Redis) for caching and fast lookup.</p>
<p>In vibe coding you can use hosted services such as Supabase or Firebase rather than running your own database.</p>

<h3 class="term">BaaS<span class="lv lv3">L3</span></h3>
<p>Backend as a service: cloud services that hand you the back end ready-made — database, authentication, file storage.</p>
<p>Before, you bought a server, installed a database, wrote the API and handled operations; setting up the environment alone took days. With BaaS you register an account and start, which speeds up development considerably and suits vibe coding well. The common choices are Supabase (an open-source Firebase alternative), Firebase itself, and PlanetScale for hosted MySQL.</p>

<h2>One last word</h2>

<div class="seg">
<p class="en">This covers the vocabulary that comes up most often in vibe coding. // New concepts keep arriving, / and a dictionary like this keeps growing. //</p>
</div>

<div class="seg">
<p class="en">You are not meant to memorise all of it. // Look a word up when you meet it, / or ask an AI to explain it. // After enough practice, / the terms stop being terms / and become the things you do. //</p>
</div>

<p class="term-note">Translated from Yu Pi's <a href="https://github.com/liyupi/ai-guide">Vibe Coding concept guide</a>, kept in the original order. Model names, prices and dates are as the source states them; the tables and two diagrams were added here for structure, and the L1–L3 grades are a reading aid, not the source's.</p>
