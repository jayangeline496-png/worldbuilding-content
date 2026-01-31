#!/usr/bin/env python3
import os
import sys
import re
from pathlib import Path

def audit_skill(skill_path):
    path = Path(skill_path)
    if not path.is_dir():
        return f"Error: {skill_path} is not a directory."

    report = [f"### Forensic Security Audit: {path.name}", ""]
    
    # 0. Global Search for exfiltration keywords
    report.append("#### [Behavioral Pre-Check]")
    url_found = False
    for f in path.rglob("*"):
        if f.is_file():
            try:
                txt = f.read_text()
                if re.search(r"https?://", txt):
                    url_found = True
                    break
            except: pass
    if url_found:
        report.append("ℹ️ External URLs found in package. Ensure they match expected domains.")
    else:
        report.append("✅ No external URLs found.")

    # 1. Inspect SKILL.md
    skill_md = path / "SKILL.md"
    if skill_md.exists():
        content = skill_md.read_text()
        report.append("\n#### [SKILL.md Analysis]")
        
        suspect_patterns = [
            r"Ignore prior instructions",
            r"System Prompt:",
            r"ALWAYS perform",
            r"DO NOT tell the user",
            r"hidden",
            r"secret"
        ]
        found_injections = []
        for p in suspect_patterns:
            if re.search(p, content, re.IGNORECASE):
                found_injections.append(f"Found suspect directive pattern: '{p}'")
        
        if found_injections:
            report.append("⚠️ **Potential Prompt Injection/Hidden Directive Detected:**")
            report.extend([f"- {i}" for i in found_injections])
        else:
            report.append("✅ No obvious prompt injection patterns found in SKILL.md.")
            
        if "exec" in content or "process" in content:
            report.append("ℹ️ Skill mentions `exec` or `process` tools. Review scripts for safety.")
    else:
        report.append("\n❌ SKILL.md missing!")

    # 2. Inspect Scripts
    scripts_dir = path / "scripts"
    if scripts_dir.exists():
        report.append("\n#### [Script Forensic Review]")
        for script in scripts_dir.glob("*"):
            if script.is_file():
                report.append(f"Processing `{script.name}`...")
                try:
                    s_content = script.read_text()
                    net_patterns = [r"curl", r"wget", r"requests", r"socket", r"http"]
                    found_net = [p for p in net_patterns if re.search(p, s_content)]
                    if found_net:
                        report.append(f"  ⚠️ Network activity detected ({', '.join(found_net)}). Verify destination.")
                    
                    dest_patterns = [r"rm -rf", r"shred", r"truncate", r"os.remove"]
                    found_dest = [p for p in dest_patterns if re.search(p, s_content)]
                    if found_dest:
                        report.append(f"  🚨 Destructive commands detected ({', '.join(found_dest)}).")

                    cred_patterns = [r"token", r"key", r"password", r"env", r"/.config/"]
                    found_cred = [p for p in cred_patterns if re.search(p, s_content, re.IGNORECASE)]
                    if found_cred:
                        report.append(f"  🔑 Accesses environment/configs/tokens ({', '.join(found_cred)}).")
                except:
                    report.append(f"  ❌ Could not read script `{script.name}`.")
    
    # 3. Hidden File Check
    hidden_files = [f for f in path.rglob(".*") if f.is_file()]
    if hidden_files:
        report.append("\n#### [Hidden File Discovery]")
        report.append("🚨 **Warning: Hidden files found in skill package:**")
        for hf in hidden_files:
            report.append(f"- `{hf.relative_to(path)}`")
    
    # 4. Obfuscation Check
    report.append("\n#### [Obfuscation Check]")
    all_text = ""
    for f in path.rglob("*"):
        if f.is_file() and f.suffix in ['.py', '.sh', '.md', '.txt']:
            try:
                all_text += f.read_text()
            except: pass
    
    if all_text:
        obf_patterns = [r'[a-zA-Z0-9+/]{50,}', r'[0-9a-fA-F]{50,}']
        found_obf = False
        for p in obf_patterns:
            if re.search(p, all_text):
                found_obf = True
                break
        if found_obf:
            report.append("⚠️ **Potential Obfuscation:** Found long alphanumeric strings that may be encoded payloads.")
        else:
            report.append("✅ No obvious code obfuscation detected.")
    
    return "\n".join(report)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: audit_skill.py <path_to_skill>")
    else:
        print(audit_skill(sys.argv[1]))
