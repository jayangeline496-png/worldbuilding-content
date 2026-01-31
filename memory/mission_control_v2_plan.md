# Mission Control App: V2 Blueprint

## Problem Statement
The current Streamlit app is a static viewer. It lacks interactivity (no drag-and-drop), doesn't reflect the true state of projects, and serves as a redundant interface for actions David already does elsewhere.

## Proposed Tech Stack
- **Frontend/Backend:** **Next.js** or **Remix** (React) for a truly interactive experience. 
- **Component Library:** **shadcn/ui** + **Tailwind CSS** (Forensic/Dark aesthetic).
- **Kanban Logic:** `@hello-pangea/dnd` (the maintained fork of `react-beautiful-dnd`) for smooth drag-and-drop.
- **Persistence:** GitHub-as-a-Database (saving a `tasks.json` or `db.sqlite` directly to the repo) so we don't need a separate DB server.
- **Hosting:** Vercel (Free Tier) - zero maintenance and lightning-fast.

## Feature Set

### 1. Interactive Kanban (The "Pulse")
- **Stages:**
  - `Backlog`: Ideas and future refactors.
  - `Active`: Currently being written/refactored.
  - `Review`: Ready for David's eyes or forensic edit.
  - `Finished`: Published and metrics tracked.
- **Interactivity:** Drag-and-drop between stages.
- **Assignment:** Owners (David vs. Jay). David owns the "Magic Shapes Language" refactor; Jay owns the "Mission Control App" rebuild.

### 2. Forensic Briefing Dashboard
- A dedicated view for the **Daily Strategic Briefing**. 
- No more clicking a button to "generate"—it's just there, pulled from the same data I push to Notion.

### 3. Integrated "Forensic Chat"
- A lightweight chat interface that talks directly to me (Clawdbot). 
- Avoids Discord's markdown/formatting limitations.

### 4. Task Management
- Quick-add modal for new tasks.
- Details: IP (Cosmere, Poppins, etc.), Priority, Owner, and a link to the GitHub draft.

---

## Action Plan
1. **Initialize Next.js Repo:** Scaffold the new app structure in `ender207/mission-control`.
2. **Design System:** Use `/superdesign` and `/frontend-design` to build the forensic dark-mode UI.
3. **Draft Kanban:** Implement a JSON-backed board.
4. **Deploy:** Setup Vercel so David can actually use it.
