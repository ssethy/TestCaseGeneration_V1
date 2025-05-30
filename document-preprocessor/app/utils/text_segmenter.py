import re
from typing import List, Dict

def segment_text(raw_text: str) -> List[Dict[str, str]]:
    """
    Improved segmentation: splits raw text into sections based on heading-like patterns.
    Returns a list of dictionaries with 'title' and 'content' keys.
    """
    sections = []
    current_title = "Introduction"
    current_content = []

    lines = raw_text.splitlines()

    # Improved heading detection
    section_header_pattern = re.compile(
        r"^(Section\s*\d+[:.-]?|[A-Z][^\n]{2,80}:|^\d+\.\s+.+)$", re.IGNORECASE
    )

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Match heading-like lines
        if section_header_pattern.match(line):
            # Save previous section
            if current_content:
                sections.append({
                    "title": current_title.strip(),
                    "content": "\n".join(current_content).strip()
                })
                current_content = []

            current_title = line
        else:
            current_content.append(line)

    # Save final section
    if current_content:
        sections.append({
            "title": current_title.strip(),
            "content": "\n".join(current_content).strip()
        })

    return sections
