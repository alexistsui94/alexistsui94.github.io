---
title: "A Delivery Project, Reviewed Honestly"
date: 2026-03-12
categories: [projects]
topic: erp
tags: [ERP, Implementation]
summary: "Not a framework — three specific things that went wrong on one ERP delivery, what they cost, and the four checks I now run before calling a stage finished."
---

<div class="seg">
<p class="en">This is not a methodology post. // It is one project, / with the parts / I would do differently. // Names and numbers are generalised, / but the shape of each problem / is exactly as it happened. //</p>
</div>

<div class="seg">
<p class="en">The client was a distributor / with five shops / and one warehouse. // Before the project / they ran on spreadsheets / and an old system / that only the warehouse team understood. //</p>
</div>

<div class="seg">
<p class="en">Six months, / five stages, / and one month after go-live / we were still fixing reports. // The system worked. // The rules were the problem. //</p>
</div>

<h2>What the stages actually looked like</h2>

<div class="seg">
<p class="en">The textbook version is clean: / requirements, / blueprint, / configuration, / testing, / go-live. // Here is the same list / with what actually happened. //</p>
</div>

<table class="seg-table">
<thead><tr><th>Stage</th><th>What it looked like</th><th>What it cost</th></tr></thead>
<tbody>
<tr><td><span class="en">Requirements</span></td><td><span class="en">Four workshops, / each ending with / a list of “we will confirm later”</span></td><td><span class="en">Three of those / came back in month five</span></td></tr>
<tr><td><span class="en">Blueprint</span></td><td><span class="en">A 40-page document / approved in a meeting / where two people read it</span></td><td><span class="en">Sign-off meant / less than we treated it</span></td></tr>
<tr><td><span class="en">Build and test</span></td><td><span class="en">Working, / with a shared issue list / that kept growing</span></td><td><span class="en">Two weeks lost / to one field meaning</span></td></tr>
<tr><td><span class="en">Go-live</span></td><td><span class="en">A weekend of imports / and three phone calls / after midnight</span></td><td><span class="en">Old documents / matched about 90%</span></td></tr>
<tr><td><span class="en">First month after</span></td><td><span class="en">Reports being rewritten / while people used them</span></td><td><span class="en">Trust, mostly</span></td></tr>
</tbody>
</table>

<div class="seg">
<p class="en">Three of those rows / are really the same mistake, / made at three different times. // So let me take them one by one. //</p>
</div>

<h2>1. “We need approval” is not a requirement</h2>

<div class="seg">
<p class="en">In the first workshop / the client said, / “when a purchase order is created, / it needs approval.” // Everyone nodded. // I wrote it down / exactly like that. //</p>
</div>

<div class="seg">
<p class="en">In month five / we found out what it meant. // Under 10,000 / one approver. // Over 10,000 / two. // Over 50,000 / three, / and the last one / was the finance director / who was often travelling. //</p>
</div>

<div class="seg">
<p class="en">Return orders / did not need approval at all. // And there was one customer / whose orders always went by email, / then got entered the next morning, / which nobody had mentioned / because “everyone knows that”. //</p>
</div>

<div class="seg">
<p class="en">None of this was hidden. // It was just normal, / and normal things / do not get said out loud / unless someone asks / the boring questions. // Who starts it. / Who approves. / At what amount. / What happens after a rejection. / What about old documents. //</p>
</div>

<div class="seg">
<p class="en">Now I ask those five questions / about every approval / before writing anything down. // It takes ten minutes / and it has never once / been a waste. //</p>
</div>

<h2>2. The demo promised something nobody built</h2>

<div class="seg">
<p class="en">In the sales demo / there was a slide saying / “automatic reconciliation”. // It was true in a narrow sense: / the system could export both sides / in one format. //</p>
</div>

<div class="seg">
<p class="en">The client heard “we click a button / and the difference is explained.” // That is not what the system does. // It shows you the difference / and waits for a human / to decide why. //</p>
</div>

<div class="seg">
<p class="en">Nobody lied. // A slide got compressed, / a phrase travelled from sales / to the client / to the contract / to the blueprint, / and each step lost a little. // By the time it reached me / it was a promise. //</p>
</div>

<div class="seg">
<p class="en">What I would do differently / is small and unglamorous: / every phrase like that / gets rewritten / as a sentence with a subject and a verb / before it enters the blueprint. // “Automatic reconciliation” becomes / “the system lists unmatched items / and the finance team marks the reason.” //</p>
</div>

<div class="seg">
<p class="en">If the sentence sounds disappointing, / that is information. // It means the promise / was doing work / the product cannot do. //</p>
</div>

<h2>3. The imports matched 90%, and 10% is a lot</h2>

<div class="seg">
<p class="en">We migrated a few thousand / old documents. // About 90% matched cleanly. // Everyone relaxed. //</p>
</div>

<div class="seg">
<p class="en">But 10% of a few thousand / is a few hundred, / and each one of those / is a document someone has to open, / compare by hand, / and fix. // At two minutes each, / that is a working week. // It landed on one person. //</p>
</div>

<div class="seg">
<p class="en">The cause was boring: / two systems used different item codes, / and the mapping table / had been maintained by hand / for years. // Some codes had been reused. / A few items had two codes. / One code pointed at a deleted item. //</p>
</div>

<div class="seg">
<p class="en">The lesson is not / “test your data earlier”. // Everyone says that. // The lesson is that / 90% is not a passing grade / when the remaining 10% / becomes manual work / for one person / during the busiest week of their year. //</p>
</div>

<h2>Four checks before I call a stage finished</h2>

<div class="seg">
<p class="en">I still use the same five stages. // What changed is the test / for whether one of them is done. //</p>
</div>

<ol class="seg-list">
<li><span class="en">Can the next person / start from a document, / without me explaining it in the corridor? //</span></li>
<li><span class="en">Is every “will confirm later” / written down / with a name / and a date? //</span></li>
<li><span class="en">Have I asked / who starts it, / who approves, / at what amount, / what happens after a rejection, / and what about old documents? //</span></li>
<li><span class="en">If only 90% works, / who does the other 10% / and in which week? //</span></li>
</ol>

<div class="seg">
<p class="en">The project did go live, / and it is still running. // That is the normal ending. // Most projects are not saved by a clever idea; / they are saved by somebody / asking the boring question / one week earlier. //</p>
</div>
