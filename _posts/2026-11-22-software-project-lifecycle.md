---
title: "How a Software Project Actually Moves, Stage by Stage"
date: 2026-11-22
categories: [projects]
topic: erp
tags: [ERP, Delivery, Requirements]
summary: "The same six stages, but with what each one looks like on a real ERP project — the one-sentence requirement, the field that meant two things, and the report nobody printed the same way twice."
---

<div class="seg">
<p class="en">Every article about project delivery / has the same diagram. / Opportunity, / requirements, / solution, / build, / go-live, / operations. // The diagram is correct. // It is also useless / until you know what each box / looks like on a Tuesday. //</p>
</div>

<div class="seg">
<p class="en">So this is the same six stages, / with one concrete example each, / taken from ERP work. //</p>
</div>

<h2>The three-part view</h2>

<table class="seg-table">
<thead><tr><th>Stage</th><th>The question it answers</th><th>What you should be able to hand over</th></tr></thead>
<tbody>
<tr><td><span class="en">Before signing</span></td><td><span class="en">Is this worth doing, / and can we actually do it?</span></td><td><span class="en">A scope list, / a price, / and the parts / we are not promising</span></td></tr>
<tr><td><span class="en">Signing to go-live</span></td><td><span class="en">How exactly, / and how do we prove it works?</span></td><td><span class="en">Confirmed rules, / test results, / and a cutover plan</span></td></tr>
<tr><td><span class="en">After go-live</span></td><td><span class="en">Is anyone actually using it?</span></td><td><span class="en">Usage numbers, / a closed issue list, / and the next change</span></td></tr>
</tbody>
</table>

<div class="seg">
<p class="en">That is the whole structure. // What follows is what fills it. //</p>
</div>

<h2>1. Before signing: from one sentence to a price</h2>

<div class="seg">
<p class="en">The first version of a requirement / is usually one sentence. // On this project it was: / “we need to see stock.” // Six words, / and about four different meanings. //</p>
</div>

<div class="seg">
<p class="en">Stock where — / one warehouse, or all of them? // Does it include goods on the way? // Does it include stock already reserved / for someone else? // Can a shop see the main warehouse / or only its own shelf? //</p>
</div>

<div class="seg">
<p class="en">None of those questions / are technical. // All of them change the price. // “See stock” can be one screen / or three weeks / and an integration. //</p>
</div>

<div class="seg">
<p class="en">The other thing that happens here / is the quiet promise. // A demo shows something impressive, / the client remembers it, / and it never appears / in the scope list. // Six months later / someone finds it in a meeting minute / and asks why it is missing. //</p>
</div>

<div class="seg">
<p class="en">The fix is unglamorous. // Anything shown in a demo / gets written into the scope list, / marked as included, / extra, / or not available. // Three words next to a line / saves an argument later. //</p>
</div>

<h2>2. Delivery: turning words into rules</h2>

<div class="seg">
<p class="en">“We need approval” / is enough to sign a contract. // It is not enough to configure anything. // Who starts it, / who approves, / at what amount, / how many levels, / what happens after a rejection, / and what to do with documents / created before the rule existed. //</p>
</div>

<div class="seg">
<p class="en">The expensive one on this project / was a field. // “Available stock.” // Finance read it as / stock minus what is already sold. // The warehouse read it as / what is physically on the shelf, / including goods already promised. //</p>
</div>

<div class="seg">
<p class="en">Both were reasonable. // Both had been true / in the old spreadsheets, / in different columns, / maintained by different people. // We found out in testing, / two weeks before go-live, / when two reports / disagreed by a few hundred units. //</p>
</div>

<div class="seg">
<p class="en">The lesson was not / “define your fields”. // It was that / a word everyone uses daily / is the most dangerous word in the room, / because nobody thinks / it needs defining. //</p>
</div>

<div class="seg">
<p class="en">So now the blueprint has a page / that is only definitions. // Not the technical data dictionary — / a plain list: / this word, / what it means here, / and what it does not include. // It is the least interesting page / and the one that gets quoted / three months later. //</p>
</div>

<h2>3. Testing: the part that decides whether people trust it</h2>

<div class="seg">
<p class="en">A system that runs / is not a system people trust. // The difference is usually small: / a total that is off by two decimal places, / a printout that wraps onto a second page, / a search that is one second slower / than the old one. //</p>
</div>

<div class="seg">
<p class="en">On this project / the finance team ran three days of real documents / through the system, / then compared totals with the old one. // Two matched. // One was off by 0.02, / every time, / on the same kind of order. //</p>
</div>

<div class="seg">
<p class="en">It was a rounding rule. // Nobody would have written it down. // Someone would have found it / in month two, / and by then / every number in the system / would have been slightly suspect. //</p>
</div>

<div class="seg">
<p class="en">That is what UAT is really for. // Not proving the software works — / we can test that ourselves. // It is letting the people who own the numbers / find the thing / we would never have thought to check. //</p>
</div>

<h2>4. After go-live: the quiet failure</h2>

<div class="seg">
<p class="en">Go-live went fine. // Two weeks later / we looked at who was logging in. // Three people. // Out of about twenty / who were supposed to use it daily. //</p>
</div>

<div class="seg">
<p class="en">The reason was not resistance. // The picking list printed / in a different layout / from the old one, / and the warehouse staff / had a routine built around that layout / for eleven years. // They were not refusing the system. // They were printing from the system, / then retyping it / into an old template. //</p>
</div>

<div class="seg">
<p class="en">Nobody complains about that. // They just quietly do the work twice. // Which is why “is it live?” / is a much weaker question / than “who did what they used to do, / and why?” //</p>
</div>

<div class="seg">
<p class="en">We changed the layout. // It took half a day. // It would have taken ten minutes / if we had asked / before go-live. //</p>
</div>

<h2>Two things I would tell someone starting</h2>

<div class="seg">
<p class="en">First: the work is not / writing documents. // It is getting a specific person / to say a specific sentence / in front of other people, / so it cannot quietly change later. //</p>
</div>

<div class="seg">
<p class="en">Second: every stage ends / when the next person can move / without asking you anything. // Not when the file is finished. // When you are no longer needed. //</p>
</div>

<div class="seg">
<p class="en">That is a low bar / and most projects / do not reach it. // Which is why the same diagram / keeps getting drawn. //</p>
</div>
