---
title: "Vibe Coding, Term by Term: The Whole Vocabulary in Order"
date: 2026-11-28
categories: [tech]
topic: ai
tags: [AI, Vibe Coding, Agents, Glossary]
summary: "Eighty-odd terms of AI coding, in the order they are usually taught — model, prompt, modes, context, output, tools, project words, front and back end. Definitions kept short, with the 2026 corrections where the common explanation has gone stale."
---

<div class="seg">
<p class="en">Every field grows a vocabulary / faster than it grows a practice. // AI coding is two years old / and already has eighty words for itself, / most of them borrowed, / several of them meaning something else by now. //</p>
</div>

<div class="seg">
<p class="en">What follows is the whole set, in the order it is usually taught: / the model, / the prompt, / the modes, / the context, / the output, / the tools, / the ordinary project words, / and the front-end words that never changed. // Where the field moved in 2026, I have said so. // Where a term is mostly fashion, I have said that too. //</p>
</div>

<div class="seg">
<p class="en">Definitions are short on purpose. // This is a page to look things up in, / not to read in one sitting. //</p>
</div>

<p class="term-toc"><a href="#model">1 · The model</a> · <a href="#prompt">2 · The prompt</a> · <a href="#modes">3 · The modes</a> · <a href="#context">4 · The context</a> · <a href="#output">5 · The output</a> · <a href="#tools">6 · The tools</a> · <a href="#project">7 · The project words</a> · <a href="#stack">8 · Front end, back end</a></p>

<p class="level-key"><span class="lv lv1">L1</span>daily use<span class="lv lv2">L2</span>once you start building<span class="lv lv3">L3</span>specialist, still moving. Grades are mine, not the dictionary's.</p>

<h2 id="model">1. The model</h2>

<h3 class="term">Artificial intelligence<span class="lv lv1">L1</span></h3>
<p>The umbrella term for systems that do tasks we associate with human judgement. In this list it is the least useful word, because it describes an ambition rather than a mechanism.</p>

<h3 class="term">Large language model<span class="lv lv1">L1</span></h3>
<p>A model trained to predict the next token across a very large body of text. Everything it does — answering, translating, writing code — is that prediction running in a loop. ChatGPT, Claude, Gemini and DeepSeek are all this.</p>

<h3 class="term">Token<span class="lv lv1">L1</span></h3>
<p>The unit a model reads and writes. Not a word: in English it averages about four characters, and the split ignores meaning. Names like <code>RetailToSaleOrder</code> arrive in pieces.</p>

<h3 class="term">Input and output tokens<span class="lv lv1">L1</span></h3>
<p>What you send is input; what comes back is output. They are priced separately, and output usually costs several times more. A long paste is cheap per call; a long answer is not.</p>

<h3 class="term">Token caching<span class="lv lv2">L2</span></h3>
<p>Providers keep a prefix of your prompt in memory so the next call does not pay full price to re-read it. Cached input is billed at a fraction of fresh input, and the cache expires after minutes. It rewards stable top-of-prompt material — rules, schemas, documentation — and punishes reshuffling it.</p>

<h3 class="term">Model parameters<span class="lv lv2">L2</span></h3>
<p>The weights learned in training, counted in billions. More parameters usually mean more capability and more cost, but the number says nothing about how well a model fits your task.</p>

<h3 class="term">Training and inference<span class="lv lv2">L2</span></h3>
<p>Training is the expensive process that produces the weights, done once by the provider. Inference is the cheap process of using them, done every time you press send.</p>

<h3 class="term">Fine-tuning<span class="lv lv3">L3</span></h3>
<p>Further training of a finished model on your own examples, so it learns a format, a tone or a narrow task. Useful when the shape of the answer matters more than the knowledge. It does not add facts reliably; for facts, put them in the context.</p>

<h3 class="term">Distillation<span class="lv lv3">L3</span></h3>
<p>Training a small model on the outputs of a large one, so it imitates the behaviour at a fraction of the cost. Most cheap models you use are somebody's distillation.</p>

<h3 class="term">Context window<span class="lv lv1">L1</span></h3>
<p>Everything the model can see in one call: instructions, files, documents, the conversation so far. In 2026 the common size is a few hundred thousand tokens, with a million on some frontier models. Large is not free — the whole window is re-sent, and attention is not spread evenly across it.</p>

<h2 id="prompt">2. The prompt</h2>

<h3 class="term">Prompt<span class="lv lv1">L1</span></h3>
<p>The instruction you give. In practice it is the whole input: instruction, examples, files, tools, and the conversation history that comes with it.</p>

<h3 class="term">System prompt<span class="lv lv1">L1</span></h3>
<p>The standing instruction that sits above the conversation and sets role, rules and boundaries. Written once, applied to every turn. Most products let you edit it; few people do, and that is usually a mistake.</p>

<h3 class="term">Prompt engineering<span class="lv lv1">L1</span></h3>
<p>The craft of wording instructions so the model does what you meant. It mattered enormously in 2023 and matters less now: with better models, the bottleneck moved from how you ask to what you supply. See context engineering.</p>

<h3 class="term">Zero-shot<span class="lv lv2">L2</span></h3>
<p>Asking with no examples. Fine for common tasks, unreliable for anything with a house style.</p>

<h3 class="term">Few-shot<span class="lv lv2">L2</span></h3>
<p>Giving two or three worked examples inside the prompt. The cheapest quality upgrade available: one good input-output pair often beats a paragraph of adjectives.</p>

<h3 class="term">Chain of thought<span class="lv lv2">L2</span></h3>
<p>Asking the model to reason step by step before answering. It helps with arithmetic, logic and multi-step edits. With reasoning models this is largely built in, so the explicit request mostly adds words.</p>

<h3 class="term">Markdown<span class="lv lv1">L1</span></h3>
<p>The plain-text formatting both you and the model read constantly — headings, lists, tables, code fences. Worth knowing well, because structured input produces structured output.</p>

<h2 id="modes">3. The modes</h2>

<p class="term-lead">This is where the vocabulary grew fastest, and where most of the confusion lives. The terms are not alternatives to each other; they describe different layers of the same workflow.</p>

<h3 class="term">Vibe coding<span class="lv lv1">L1</span></h3>
<p>Karpathy's phrase from February 2025: describe what you want, accept the code, judge it by whether it runs. Excellent for prototypes and one-off scripts. The name has been stretched to cover production work, which it was never meant to do.</p>

<h3 class="term">Agentic engineering<span class="lv lv1">L1</span></h3>
<p>The 2026 correction, from Karpathy himself. Same tools, different standard: the model may write the code, but a spec, tests and evaluations decide whether it is right. The difference is not the prompt; it is whether anything can fail.</p>

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
<p>The narrower practice: letting an agent read the repository, run commands, edit files and iterate, rather than pasting code into a chat. The unit of work becomes a task with a definition of done, not a snippet.</p>

<h3 class="term">Harness engineering<span class="lv lv3">L3</span></h3>
<p>The 2026 name for the layer around the model: rules, skills, sub-agents, hooks, tools, memory. The claim behind it is that the model is now a commodity and the harness is the product — the same model in a tighter harness produces visibly better work.</p>

<h3 class="term">Loop engineering<span class="lv lv3">L3</span></h3>
<p>Designing the cycle rather than the step: what starts it, what it may touch, how it verifies itself, when it must stop. Closer to operations than to prompting. The failure mode is an agent that loops confidently in the wrong direction.</p>

<h3 class="term">Multi-agent collaboration<span class="lv lv3">L3</span></h3>
<p>Several agents working on one problem, each with a role or a slice. Buys parallelism and cleaner context; costs coordination, and multiplies the surfaces where things can disagree.</p>

<h3 class="term">Agent orchestration<span class="lv lv3">L3</span></h3>
<p>The layer that decides who does what: splitting a task, handing it out, collecting results, resolving conflicts. In practice this is a script plus a queue; the impressive name is optional.</p>

<h3 class="term">Subagents<span class="lv lv2">L2</span></h3>
<p>A helper agent with its own fresh context, spawned for one bounded job — search the repository, review this diff, summarise this folder — and returning only a conclusion. Its real value is isolation: the mess stays out of the main thread.</p>

<h3 class="term">Agent teams<span class="lv lv3">L3</span></h3>
<p>Three to five agents working in parallel on the same project, with a lead that splits work and teammates that message each other. Good for broad mechanical changes across modules; poor for anything that needs one coherent design decision.</p>

<h3 class="term">Self-improving agents<span class="lv lv3">L3</span></h3>
<p>Agents that distil a finished task into a reusable skill document and retrieve it next time — the pattern behind Hermes and similar 2026 projects. Useful when you repeat the same kind of job; a way to accumulate your own mistakes when you do not.</p>

<h3 class="term">Background agents<span class="lv lv2">L2</span></h3>
<p>Work that runs without you watching: on a schedule, on a queue, or on a pull request. The output has to be checkable later, because nobody was there when it happened.</p>

<h3 class="term">Personal agents<span class="lv lv2">L2</span></h3>
<p>An agent with standing access to your own files, mail and calendar, rather than a blank chat. Convenience purchased with permissions.</p>

<h3 class="term">Super-agents<span class="lv lv3">L3</span></h3>
<p>The marketing word for an agent given many tools and long-running autonomy. Treat it as a claim, not a specification. The useful question is always which tools, and what stops it.</p>

<h3 class="term">Agent loop<span class="lv lv2">L2</span></h3>
<p>The core mechanism: the model calls a tool, reads the result, decides again. It ends when the model calls no more tools or a step limit is reached. Everything else in this section is built on this one cycle.</p>

<figure class="article-figure">
  <img src="/assets/images/agent-loop.svg" alt="A loop from task to model to tool call to result, returning to the model, with a note that writes need a confirmation." width="900" height="374">
  <figcaption>The loop is the difference between a chat and an agent. The exit is not a decision you make — it is the model stopping, or a limit you set.</figcaption>
</figure>

<h3 class="term">Ralph Wiggum loop<span class="lv lv3">L3</span></h3>
<p>A deliberately dumb pattern that works: write the checklist first, then let a fresh agent take one unfinished item per round, commit, and start again with clean context. Progress lives in git rather than in a long conversation, which is precisely why it survives 2026's context limits.</p>

<h3 class="term">ReAct<span class="lv lv3">L3</span></h3>
<p>Reason and act, interleaved: think about the next step, take it, observe, think again. The pattern underneath most tool-using agents, named in 2022 and never renamed.</p>

<h3 class="term">Deep thinking<span class="lv lv2">L2</span></h3>
<p>Built-in reasoning before answering — the model works through steps internally, then replies. Better on architecture, hard bugs and multi-step maths; slower and more expensive. Different from chain of thought, which is a prompting trick rather than a model capability.</p>

<h3 class="term">Adaptive thinking<span class="lv lv2">L2</span></h3>
<p>Letting the model decide how much reasoning a question deserves, instead of a manual on-off switch. Simple questions answer immediately; hard ones get the long path. Introduced across the major models during 2026 and now the default in most of them.</p>

<h3 class="term">Tool calling<span class="lv lv2">L2</span></h3>
<p>The model emitting a structured request — tool name plus arguments — for the runtime to execute. This is how an agent touches files, tests, databases and APIs. The model never runs anything itself; it only asks.</p>

<h3 class="term">MCP<span class="lv lv2">L2</span></h3>
<p>The Model Context Protocol: a standard way to expose tools and data to any compatible client, so one integration serves many agents. In 2026 the protocol moved to a stateless core and added a skills extension that loads instructions in stages — metadata first, full procedure on demand.</p>

<h3 class="term">Agent skills<span class="lv lv2">L2</span></h3>
<p>A folder with a <code>SKILL.md</code> file: a procedure the agent loads only when a task matches. The point is progressive disclosure — the instruction costs almost nothing until it is needed, unlike a rules file that is paid for on every call.</p>

<h3 class="term">Hooks<span class="lv lv3">L3</span></h3>
<p>Deterministic code that runs at fixed points — before a tool call, after an edit, before a commit. Where a rule says "do not touch production", a hook makes it impossible. The cheapest reliability in the whole stack.</p>

<h3 class="term">Slash commands<span class="lv lv2">L2</span></h3>
<p>Named shortcuts typed into the agent's prompt — <code>/review</code>, <code>/test</code>, <code>/commit</code> — that expand into a longer instruction. A way to standardise the twenty prompts you actually reuse.</p>

<h3 class="term">A2A<span class="lv lv3">L3</span></h3>
<p>Agent-to-Agent: a protocol for agents built by different vendors to discover each other and exchange tasks. Enterprise plumbing rather than something you use directly.</p>

<h3 class="term">ACP<span class="lv lv3">L3</span></h3>
<p>Two things share the acronym: IBM's Agent Communication Protocol for cross-framework agents, and the Agent Client Protocol used by editors. Both address the same gap as A2A from different directions; none of them is settled.</p>

<h3 class="term">BMAD<span class="lv lv3">L3</span></h3>
<p>A role-based method — analyst, product manager, architect, developer, tester — where each role is an agent with its own instructions and artefacts. It works because it forces the specification to exist before the code.</p>

<h3 class="term">Browser use<span class="lv lv3">L3</span></h3>
<p>An agent driving a real browser: clicking, typing, reading the page. Good for sites with no API. Fragile in the way all UI automation is fragile — one redesign breaks the script.</p>

<h3 class="term">Computer use<span class="lv lv3">L3</span></h3>
<p>The same idea one level up: the agent sees the screen, moves the mouse, types. It reaches any desktop application, which is also why it belongs in a sandbox, not on your working machine.</p>

<h2 id="context">4. The context</h2>

<h3 class="term">Context<span class="lv lv1">L1</span></h3>
<p>Everything inside the window for this call. Not memory, not training — just what is in front of the model right now. If it is not here, it does not exist for this answer.</p>

<figure class="article-figure">
  <img src="/assets/images/context-window.svg" alt="A context window containing rules, chosen files, retrieved documents and the conversation, with an unpasted conversion table sitting outside it." width="900" height="330">
  <figcaption>The window is the whole world for one call. A table you never pasted is not “forgotten” — it does not exist yet.</figcaption>
</figure>

<h3 class="term">Context engineering<span class="lv lv1">L1</span></h3>
<p>Filling the window with exactly the right information for the next step — Karpathy's definition, and the skill that replaced prompt engineering. Four moves: write it down, select what matters, compress at boundaries, isolate the mess in a sub-agent.</p>

<h3 class="term">Compaction<span class="lv lv2">L2</span></h3>
<p>Summarising a long session so the early decisions survive in short form. Done at task boundaries, not when the window is full; by then the details you needed are already gone.</p>

<h3 class="term">Rules file<span class="lv lv2">L2</span></h3>
<p>A file of standing instructions the agent reads every session: build commands, boundaries, forbidden modules, what "done" means. Keep it to what cannot be inferred from the code — every line is paid for on every call.</p>

<h3 class="term">AGENTS.md<span class="lv lv2">L2</span></h3>
<p>The 2026 convention for that file — a plain Markdown document at the repository root, read by most coding agents. No format to learn; the discipline is in what you leave out.</p>

<h3 class="term">Spec-driven development<span class="lv lv3">L3</span></h3>
<p>Writing the specification first and treating it as the source of truth the code must satisfy. With agents, this stops being bureaucracy: a vague plan produces vague code, and the spec is the only artefact both you and the model can be held to.</p>

<h3 class="term">RAG<span class="lv lv2">L2</span></h3>
<p>Retrieval-augmented generation: fetch relevant documents at question time and put them in the window. Strong on prose and policy; weak on exact identifiers, where plain search still wins.</p>

<h3 class="term">Agentic RAG<span class="lv lv3">L3</span></h3>
<p>RAG where the agent decides what to search, reformulates, and searches again if the first result is thin. Better on multi-hop questions; harder to bound, because the loop can keep looking forever.</p>

<h3 class="term">Vector database<span class="lv lv3">L3</span></h3>
<p>A store that indexes embeddings and returns nearest neighbours. Useful once you have thousands of chunks; before that, a folder and a search command are honest enough.</p>

<h3 class="term">Embeddings<span class="lv lv2">L2</span></h3>
<p>Text turned into vectors so that similar meaning lands nearby. This is why semantic search finds "returns policy" when you typed "refund rules" — and why it confidently returns something adjacent when you needed the exact one.</p>

<h2 id="output">5. The output</h2>

<h3 class="term">Hallucination<span class="lv lv1">L1</span></h3>
<p>Fluent output with no basis in the input. Not an intermittent bug: it is the same prediction mechanism working without enough to work from. The remedy is a better source or a check, never a stronger instruction.</p>

<h3 class="term">Temperature<span class="lv lv1">L1</span></h3>
<p>The randomness dial on sampling. Lower makes output repeatable; it does not make it correct. People keep turning it down hoping for truth, and keep being surprised.</p>

<h3 class="term">Streaming<span class="lv lv2">L2</span></h3>
<p>Sending the answer token by token as it is produced. A latency trick, not a quality one — though watching the first line arrive tells you quickly whether the direction is wrong.</p>

<h3 class="term">System-1 models<span class="lv lv3">L3</span></h3>
<p>Small models that return a decision instead of prose: a probability, a category, a score. Milliseconds and near-zero cost, which makes them the right tool for routing, triage and filtering before a larger model is called.</p>

<h2 id="tools">6. The tools</h2>

<h3 class="term">IDE<span class="lv lv1">L1</span></h3>
<p>An integrated development environment: editor, debugger, terminal and project model in one window. VS Code and its forks dominate; the AI features now matter more than the editor itself.</p>

<h3 class="term">Code editor<span class="lv lv1">L1</span></h3>
<p>The lighter half of an IDE — a window for editing text with syntax highlighting. Many people now work entirely inside an agent's chat pane and open the editor only to read a diff.</p>

<h3 class="term">CLI<span class="lv lv2">L2</span></h3>
<p>The command line. It matters again in 2026 because agents are good at it: reading output, running tests, chaining commands. A tool with a clean CLI is easier for an agent to use than one with a pretty UI.</p>

<h3 class="term">No-code platforms<span class="lv lv2">L2</span></h3>
<p>Tools that build software from forms and blocks rather than code. Still the fastest path for a fixed, well-understood shape; still a wall when you need something the platform did not anticipate.</p>

<h3 class="term">Code completion<span class="lv lv1">L1</span></h3>
<p>Suggesting the next line as you type. The oldest AI coding feature and the least discussed, because it quietly became normal.</p>

<h3 class="term">Code review<span class="lv lv2">L2</span></h3>
<p>Reading a change before it lands, for correctness and for intent. With generated code the practice matters more, not less — the reviewer is often the only thing standing between a plausible diff and production.</p>

<h3 class="term">Linter<span class="lv lv2">L2</span></h3>
<p>A tool that flags suspicious code by rule: unused variables, missing types, unreachable branches. Deterministic, cheap, and the easiest quality gate to hand an agent, because the output is a list it can work through.</p>

<h3 class="term">Debugging<span class="lv lv2">L2</span></h3>
<p>Finding why behaviour differs from expectation. Agents are good at the mechanical half — reading stack traces, adding logs, bisecting — and weak at the half that requires knowing what the system was supposed to do.</p>

<h3 class="term">Desktop agents<span class="lv lv3">L3</span></h3>
<p>Open-source agents that run on your own machine and act on it — files, browser, terminal, sometimes your chat apps. OpenClaw is the best-known 2026 example. Powerful, and the reason "what permissions did I grant?" became a real question.</p>

<h2 id="project">7. The project words</h2>

<h3 class="term">MVP<span class="lv lv1">L1</span></h3>
<p>The smallest version that tests whether anyone wants this. With agents the temptation is to build the full thing in an afternoon, which is exactly how MVPs stop being minimal.</p>

<h3 class="term">Iteration<span class="lv lv1">L1</span></h3>
<p>One pass of build, check, adjust. The unit that makes agent work manageable: small iterations keep the context small and the failures visible.</p>

<h3 class="term">Refactoring<span class="lv lv2">L2</span></h3>
<p>Changing structure without changing behaviour. Agents are genuinely good at this, because the behaviour is defined by tests — which is also the condition for letting them near it.</p>

<h3 class="term">Technical debt<span class="lv lv2">L2</span></h3>
<p>The future cost of a shortcut taken now. Generated code accrues it faster, because nobody remembers choosing the shortcut.</p>

<h3 class="term">Version control<span class="lv lv1">L1</span></h3>
<p>Git, in practice: every state recoverable, every change attributable. For agent work it is not bookkeeping but the safety net — commit before the agent starts, and a bad afternoon costs one command.</p>

<h3 class="term">Git worktree<span class="lv lv3">L3</span></h3>
<p>A second working directory attached to the same repository, on its own branch. The cheap way to let an agent work in parallel without stepping on your uncommitted files.</p>

<h3 class="term">Deployment<span class="lv lv2">L2</span></h3>
<p>Moving code from your machine to where it runs. The step where "it worked locally" stops being an argument.</p>

<h3 class="term">GEO<span class="lv lv3">L3</span></h3>
<p>Generative engine optimisation: writing so that an AI search engine cites you, rather than so that a results page ranks you. Same instinct as SEO, different surface — structure, specificity and named facts instead of keywords.</p>

<h2 id="stack">8. Front end, back end</h2>

<h3 class="term">Frontend<span class="lv lv1">L1</span></h3>
<p>What runs in the browser: layout, interaction, state. The part users judge, and the part agents are most confident about and most often wrong on details.</p>

<h3 class="term">Backend<span class="lv lv1">L1</span></h3>
<p>What runs on the server: data, rules, authentication, integrations. Where the business logic lives, and where a plausible-looking mistake costs the most.</p>

<h3 class="term">Full stack<span class="lv lv1">L1</span></h3>
<p>Both ends, plus the seam between them. With agents, "full stack" increasingly means being able to specify and verify both ends rather than typing either.</p>

<h3 class="term">API<span class="lv lv2">L2</span></h3>
<p>A defined way for one program to call another: endpoints, inputs, outputs, errors. The contract an agent reads when it integrates something, and the thing to paste into the window before asking for code.</p>

<h3 class="term">Database<span class="lv lv1">L1</span></h3>
<p>Where state persists: tables, keys, constraints. Most agent mistakes that matter are data mistakes — a wrong join, a duplicated row, a unit that was never converted.</p>

<h3 class="term">BaaS<span class="lv lv3">L3</span></h3>
<p>Backend as a service: hosted database, auth and storage behind an SDK, so a small project needs no server of its own. Fast to start, and a dependency to plan for when you outgrow it.</p>

<h2>What I actually keep</h2>

<div class="seg">
<p class="en">Eighty terms, / and the working set is smaller than it looks. // In my own week I use a rules file, / a few skills, / two or three tools per task, / and a check that fails loudly. // Everything else I look up when a page like this is open beside me. //</p>
</div>

<div class="seg">
<p class="en">The vocabulary will be different next year. // The habit will not: / put the right things in the window, / ask for something checkable, / and keep a way to prove it wrong. //</p>
</div>
