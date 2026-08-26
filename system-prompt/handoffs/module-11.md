# Handoff: Module 11 — Async & Concurrency

Build `11-async-concurrency/` in the course repo. Read `CONVENTIONS.md`
(same folder) and the master spec first. You own ONLY this folder.

Audience: completed modules 01–10 (may use type hints from here on —
annotate solutions lightly, don't make typing the point). Knows TS
async/await; the lesson should note "same keywords, but Python has no
implicit event loop — you start it with asyncio.run()".

## Test discipline (important)
- NO pytest-asyncio dependency. Sync test functions call
  `asyncio.run(...)` themselves.
- Determinism over timing: assert on EVENT LOGS (lists recording
  start/end order) rather than wall-clock durations. Where sleeps are
  needed use tiny ones (≤ 0.05s) and only ever assert generous upper
  bounds, never lower-bound races. Total module test runtime must stay
  under ~5 seconds.

## LESSON.md outline
1. Why this exists: waiting is not working — one thread can juggle many
   waits.
2. Sync vs async — REQUIRED sequence diagram: two coroutines
   interleaving at await points on one event loop.
3. Coroutines: `async def` returns a coroutine object; nothing runs
   until awaited/scheduled; `asyncio.run` starts the loop.
4. `gather` vs `create_task` — table + when each.
5. Timeouts and errors: `asyncio.wait_for`, TimeoutError,
   `gather(..., return_exceptions=True)`.
6. Async iteration: async generators, `async for`.
7. The GIL in 5 sentences — REQUIRED diagram: decision flowchart —
   I/O-bound + async-friendly libs → asyncio; I/O-bound + blocking libs
   → threads; CPU-bound → processes.
8. threads (ThreadPoolExecutor) and processes (one paragraph —
   ProcessPoolExecutor exists; details out of scope), plus
   `loop.run_in_executor` as the bridge.
9. Gotchas: forgetting await (coroutine never ran), blocking calls
   (time.sleep) inside async code, creating tasks without keeping
   references, mixing sync and async carelessly.
10. Try it now → exercises.

## Exercises (exactly 7)
- `ex01_first_coroutine.py` — `async def fetch_greeting(name)`
  (awaits asyncio.sleep(0)); `run_fetch(name)` sync wrapper using
  asyncio.run; a "forgot to await" fix-it (function returns the
  coroutine instead of its result — real bug, test exposes it).
- `ex02_gather.py` — `fetch_all(names, log)`: gather over a given
  `fake_fetch(name, delay, log)`; results keep input order while `log`
  shows interleaved start/end — tests assert both.
- `ex03_tasks.py` — `race(log)`: create_task two workers, prove both
  started before either finished (log order), await both;
  `first_done(coros)` using asyncio.wait FIRST_COMPLETED.
- `ex04_timeouts_errors.py` — `fetch_with_timeout(coro_factory,
  timeout)` returning fallback on TimeoutError; `gather_safe(coros)`
  with return_exceptions=True, splitting results/errors into two lists.
- `ex05_async_iterators.py` — async generator `ticker(count)` yielding
  0..count-1 with sleep(0); `collect(agen)` consuming via async for;
  `alimit(agen, n)` async version of islice.
- `ex06_threads.py` — `fetch_all_threaded(urls, fake_io, max_workers)`
  with ThreadPoolExecutor.map preserving order (fake_io is an injected
  blocking function using a tiny sleep + thread-safe log via lock —
  provide the lock pattern in the stub docstring).
- `ex07_choose_model.py` — knowledge check: `choose(scenario_key)`
  mapping described scenarios ("1000 HTTP calls", "resize 500 images",
  "3 calls to a blocking SDK"...) → "asyncio"/"threads"/"processes"
  (scenarios given as a dict of descriptions in the file); plus
  `run_blocking_in_executor(func)` bridge drill using
  loop.run_in_executor(None, func).

## Checkpoint (`checkpoint_11.py`)
Async download manager: `download_all(jobs, worker_count, limit_log)` —
an asyncio.Queue of jobs, N workers, a semaphore capping concurrent
"downloads" at 2 (each fake download records current-active count into
limit_log so tests assert max ≤ 2), one job raises → collected into an
errors list without killing the others; returns (results_dict, errors).
Deterministic: fake downloads take sleep(0)-ish steps.

## SUMMARY.md
Cheat-sheet: asyncio starter template, gather/create_task/wait_for
table, async-for template, executor bridge snippet, the
asyncio/threads/processes decision table. One mermaid mindmap.
Self-quiz: 7 questions, answers in `<details>`.

Finish with every "Definition of done" check from CONVENTIONS.md, and
confirm the whole module's tests run in a few seconds.
