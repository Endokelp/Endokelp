<div align="center">

<img src="assets/hero.svg" alt="ENDOKELP" width="888" />

**Anirudh Devireddy** &nbsp;·&nbsp; high school senior in Bellevue, WA

I put AI inside real systems: drinking-water rules, bird-safe glass, teen labor law, drone detection, classrooms. Most of it is public, with the numbers next to the code.

[endokelp.com](https://endokelp.com) &nbsp;·&nbsp; [endoblog.dev](https://endoblog.dev) &nbsp;·&nbsp; [venni.devireddy@gmail.com](mailto:venni.devireddy@gmail.com)

</div>

## One habit, applied to different domains

<div align="center">
<img src="assets/method-map.svg" width="888" alt="Map of nine projects around a center labeled systems thinking plus AI. Research: TTHM warning rules for drinking water, Hypnos for circadian health, a partner rotation study on multi-agent AI, and CSAwesome2 for CS education. Builds: Off the Clock for teen labor law, Gap check for bird-safe glass, Listening Post for drone detection, Vaidra for learning access, and Endoplexity for browser automation." />
</div>

Map the system, find the step where a model changes the outcome, then test it on data the model never saw.

## Research

<table>
  <tr>
    <td valign="top" width="30%">
      <b>Drinking-water TTHM warnings</b><br />
      Independent research, mentored by Prof. Gregory Korshin, University of Washington
    </td>
    <td valign="top">
      Total trihalomethanes (TTHM) are disinfection byproducts the EPA regulates. I analyzed 7,149 water systems and tested seasonal warning rules on held-out data. They caught 13.5% more exceedances than the EPA rule while sending 15.8% fewer alerts.
    </td>
  </tr>
  <tr>
    <td valign="top">
      <b>Does rotating partners change collusion?</b><br />
      Apart Research AI Collusion Sprint, October 2026
    </td>
    <td valign="top">
      LLM agents that verify each other's work end up accepting it, even when rejecting is the only compliant action (Shi, Zhang and Yang, 2026). I tested whether DeepSeek-V4-Flash agents accept less when every partner is a stranger. Fixed partners accepted 81%, strangers 73%: a drop of 8 points (nominal 95% interval +1 to +16). That met neither pre-registered call, so I report it as inconclusive. <a href="https://apartresearch.com/sprints/projects/rotating-verifier-partners-in-deepseekv4flash-an-inconclusive-8point-drop-in-acceptance-a5su">Read the report</a>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <b>Hypnos</b><br />
      Computational biology, 2nd place, Washington State Science Fair
    </td>
    <td valign="top">
      A reinforcement-learning model of the brain's circadian clock that plans light and caffeine for night-shift workers.
    </td>
  </tr>
  <tr>
    <td valign="top">
      <b>CSAwesome2</b><br />
      Research intern, University of Michigan School of Information
    </td>
    <td valign="top">
      Ongoing research on AI-assisted computer science learning inside the CSAwesome2 / Runestone Academy AP CS A curriculum: 10 adopted contributions, 65 exercises and 4 exams. <a href="https://github.com/Endokelp/CSAwesome2">Fork</a>
    </td>
  </tr>
</table>

## Built for competitions, 2026

<table>
  <tr>
    <td valign="top" width="42%">
      <a href="https://youtu.be/txb_xofC8QA"><img src="https://raw.githubusercontent.com/Endokelp/Off-The-Clock/main/.github/media/demo-intro.gif" alt="Off the Clock opening: the app name beside a phone showing the first question" /></a>
    </td>
    <td valign="top">
      <b><a href="https://github.com/Endokelp/Off-The-Clock">Off the Clock</a></b><br />
      <sub>RevenueCat Shipaton 2026</sub><br />
      An Android app that tells working teenagers what their employer owes them. Log a shift by hand or from a photo of the posted schedule. A rules engine built from Washington's minor labor law flags each violation, quotes the statute and adds up the unpaid time in dollars.<br /><br />
      Expo, TypeScript, RevenueCat. 55 tests. <a href="https://youtu.be/txb_xofC8QA">Watch the demo</a>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <a href="https://github.com/Endokelp/Bird_safe_OpenCV"><img src="https://raw.githubusercontent.com/Endokelp/Bird_safe_OpenCV/main/docs/media/demo-repair-pass.gif" alt="Phone screen recording: the page reports REPAIR with a 62.0 mm gap, then PASS at 40.0 mm after a dot is put back" /></a>
    </td>
    <td valign="top">
      <b><a href="https://github.com/Endokelp/Bird_safe_OpenCV">Bird-safe gap check</a></b><br />
      <sub>OpenCV AI Competition 2026</sub><br />
      Bird-safe window markings only work when no gap is wider than about 2 inches. Tape a printed calibration sheet to the glass, take one phone photo, and OpenCV 5 on AWS Lambda answers pass, repair here or retake. On a real window it measured 60.5 mm against 61 mm expected. 173 tests.<br /><br />
      <a href="https://iwny3i3fsawk2mlo3au4dcyrzi0cyepf.lambda-url.us-east-2.on.aws/">Try it live</a>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <a href="https://endokelp.github.io/listening-post/"><img src="https://raw.githubusercontent.com/Endokelp/listening-post/main/assets/demo.gif" alt="The Listening Post app showing a live spectrogram and four meters while it listens" /></a>
    </td>
    <td valign="top">
      <b><a href="https://github.com/Endokelp/listening-post">Listening Post</a></b><br />
      <sub>Congressional App Challenge 2026</sub><br />
      Acoustic drone detection that runs in a phone browser with no added hardware. Two seconds of sound become 53 numbers, a classifier scores them, and an alert needs 3 of the last 5 windows to agree. It flagged 80 to 94% of drone windows from labs it had heard and 0 to 7% from a lab it had not. The repo opens with that limit.<br /><br />
      <a href="https://endokelp.github.io/listening-post/">Open the app</a>
    </td>
  </tr>
</table>

## Products and open source

<table>
  <tr>
    <td align="center" valign="top" width="50%">
      <a href="https://github.com/Endokelp/Endoplexity">
        <img src="logos/endoplexity.png" width="48" height="48" alt="" /><br />
        <b>Endoplexity</b>
      </a><br />
      Browser agents on your own Claude or Cursor login. Open source, 156 tests.<br />
      <img src="https://img.shields.io/github/stars/Endokelp/Endoplexity?style=flat-square&color=8b5cf6&labelColor=15122f" alt="Endoplexity stars" />
    </td>
    <td align="center" valign="top" width="50%">
      <a href="https://vaidra.org">
        <img src="logos/vaidra.png" width="48" height="48" alt="" /><br />
        <b>Vaidra</b>
      </a><br />
      Free audiobooks and courses in regional Indian languages. A nonprofit with government school and NGO partners across 450+ schools and 60k+ students.
    </td>
  </tr>
  <tr>
    <td align="center" valign="top">
      <a href="https://fintell.app">
        <img src="logos/fintell.png" width="48" height="48" alt="" /><br />
        <b>FinTell</b>
      </a><br />
      Stock research
    </td>
    <td align="center" valign="top">
      <a href="https://forcelogic.io">
        <img src="logos/sitebot.svg" width="48" height="48" alt="" /><br />
        <b>SiteBot</b>
      </a><br />
      A chatbot that only answers from the client's own site
    </td>
  </tr>
  <tr>
    <td align="center" valign="top">
      <a href="https://github.com/Endokelp/NextStep">
        <img src="logos/nextstep.png" width="48" height="48" alt="" /><br />
        <b>NextStep</b>
      </a><br />
      Local-first career maps for high schoolers. No server, no account
    </td>
    <td align="center" valign="top">
      <a href="https://github.com/Endokelp/Only-Skill-You-Need">
        <img src="logos/onlyskill.png" width="48" height="48" alt="" /><br />
        <b>Only Skill You Need</b>
      </a><br />
      The first skill a beginner installs. It routes the rest.<br />
      <img src="https://img.shields.io/github/stars/Endokelp/Only-Skill-You-Need?style=flat-square&color=8b5cf6&labelColor=15122f" alt="Only Skill You Need stars" />
    </td>
  </tr>
  <tr>
    <td align="center" valign="top">
      <a href="https://github.com/Endokelp/Should-I-build">
        <img src="logos/shouldibuild.svg" width="48" height="48" alt="" /><br />
        <b>Should I Build?</b>
      </a><br />
      BUILD, PIVOT or STOP, with receipts
    </td>
    <td align="center" valign="top">
      <a href="https://github.com/Endokelp/DecisionCouncil">
        <img src="logos/decisioncouncil.svg" width="48" height="48" alt="" /><br />
        <b>DecisionCouncil</b>
      </a><br />
      A ranked verdict, with dissent, when the decision is expensive
    </td>
  </tr>
</table>

<div align="center">

In progress: **Pasupa** (in-sack crop-spoilage sensors) and **JARVIS**.<br />
Sites built for others: [Valuation AI](https://pricing-self-six.vercel.app/) · [LaCrosse Wagon](https://caraige.vercel.app) · [Interlake HI](https://www.interlakehi.org/) · [ihsAquatics](https://www.ihsaquatics.org/)

<br />

TypeScript · Python · Next.js · FastAPI · Supabase · OpenCV · Expo · AWS Lambda · Three.js

Open to internships, freelance, and education or nonprofit work.

</div>
