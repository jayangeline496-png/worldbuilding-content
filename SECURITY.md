# Security & Forensics

## New Skill Auditing
Before downloading or enabling a new skill, run the forensic audit script to check for prompt injections, hidden files, network exfiltration, or destructive behavior.

**Audit Script:** `scripts/audit_skill.py`

### Usage
```bash
python3 scripts/audit_skill.py skills/<skill-name>
```

### Checkpoints
1. **Behavioral Pre-Check:** Scans for external URLs and networking.
2. **SKILL.md Analysis:** Searches for directive injections (e.g., "Ignore prior instructions").
3. **Script Forensic Review:** Analyzes Python/Bash scripts for `curl`, `rm -rf`, or token access.
4. **Hidden File Discovery:** Finds `.dotfiles` that might contain backdoors.
5. **Obfuscation Check:** Detects Base64/Hex blobs that might hide payloads.

---

## Tooling Status

### Audited & Verified (Clean)
- **exa-search**: Deep research using Exa.
- **humanizer**: Writing style refinement for natural flow.
- **marketing-mode**: Persona shift for strategic marketing work.
- **tweet-writer**: Social media content generation. (Flagged 'secret' was just content filler).
- **deep-research**: Multi-step research workflows.
- **create-content**: High-level content ideation and planning.
- **last30days-lite**: Recent trending topic analysis.
- **byterover**: Knowledge mapping and context trees.
- **superdesign**: Modern UI/UX design and prototyping.
- **clawddocs**: Expert guidance on Clawdbot documentation.
- **second-brain**: Conversation-to-knowledge synthesis. (Flagged 'secret' was a warning NOT to include them).
- **self-improving-agent**: Error detection and autonomous skill patching.
- **reddit-scraper**: Specialized Reddit search and data extraction.
- **search-x**: Alternative X/Twitter search interface.
- **proactive-agent**: Autonomous background tasking. (Flagged 'secret' was a reference to security-audit script).
- **auto-updater**: Self-maintenance for the agent.
- **agent-browser**: Advanced browser-based research.
- **bird**: X/Twitter integration via CLI.
- **clawdhub**: Skill management and installation.
- **brave-search**: Direct Brave Search API integration.
- **reddit-read-only**: Anonymous Reddit research.

### Verified (Global Standard Library)
- bluebubbles, gemini, github, notion, skill-creator, slack, tmux, weather.
