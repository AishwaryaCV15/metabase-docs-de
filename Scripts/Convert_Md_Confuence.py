#!/usr/bin/env python3 
import os
import re
import requests
import pypandoc
from pathlib import Path
from requests.auth import HTTPBasicAuth

# === CONFIG ===
BASE_URL = "https://infomedia.gipmbh.de"
USERNAME = "chincholi" #Username in GIP or Network account name
PASSWORD = ""
SPACE_KEY = "1002025"  #check it from the Infomedia Header
PARENT_PAGE_ID = 591561883   # Optional: parent page ID for nesting
DOCS_DIR = Path.home() / "Documents/Metabase/docs-de"

auth = HTTPBasicAuth(USERNAME, PASSWORD)

# Cache {md_stem: page_id}
page_cache = {}



def md_to_confluence_html(md_path: Path) -> str:
    html = pypandoc.convert_file(
        str(md_path),
        "html5",
        format="markdown",
        extra_args=["--standalone"]
    )
    html = re.sub(r"(?is)^.*?<body[^>]*>", "", html)
    html = re.sub(r"(?is)</body>.*$", "", html)
    return html.strip()

def clean_html_for_confluence(html: str, img_map: dict) -> str:
    html = re.sub(r"(?s)^.*?<body.*?>", "", html)
    html = re.sub(r"</body>.*$", "", html)
    html = re.sub(r"</?(html|head|meta|link|section|script|style)[^>]*>", "", html)
    html = re.sub(r"<p([^>]*)>(\s*)</p>", r"<p\1>&nbsp;</p>", html)
    for md_img, full_path in img_map.items():
        confluence_img = (
            f'<ac:image>'
            f'<ri:attachment ri:filename="{full_path.name}" />'
            f'</ac:image>'
        )
        html = re.sub(
            rf'<img [^>]*src=["\']{re.escape(md_img)}["\'][^>]*>',
            confluence_img,
            html
        )
    return html

def upload_attachment(page_id: str, image_path: Path) -> str:
    """Upload image as attachment to Confluence page, update if it exists."""
    url = f"{BASE_URL}/rest/api/content/{page_id}/child/attachment"
    headers = {"X-Atlassian-Token": "nocheck"}
    
    # Check if attachment already exists
    r = requests.get(url, auth=auth, params={"filename": image_path.name})
    r.raise_for_status()
    results = r.json().get("results", [])
    
    with open(image_path, "rb") as f:
        files = {"file": (image_path.name, f, "image/png")}
        
        if results:
            # Attachment exists → update
            attach_id = results[0]["id"]
            update_url = f"{url}/{attach_id}/data"
            r = requests.post(update_url, auth=auth, headers=headers, files=files)
        else:
            # Create new attachment
            r = requests.post(url, auth=auth, headers=headers, files=files)
    
    r.raise_for_status()
    
    data = r.json()
    # Return download URL safely
    if "results" in data:
        return BASE_URL + data["results"][0]["_links"]["download"]
    elif "_links" in data:
        return BASE_URL + data["_links"]["download"]
    else:
        raise ValueError(f"Unexpected response from Confluence attachment API: {data}")


def get_or_create_page(title: str, parent_id: str, body_html: str) -> str:
    """Return page_id: reuse if exists under parent, else create."""
    cache_key = f"{parent_id}/{title}"

    if cache_key in page_cache:
        return page_cache[cache_key]["id"]

    url = f"{BASE_URL}/rest/api/content"
    params = {"title": title, "spaceKey": SPACE_KEY, "expand": "ancestors"}
    r = requests.get(url, auth=auth, params=params)
    r.raise_for_status()
    results = r.json().get("results", [])

    print(f"\n Checking for page '{title}' under parent {parent_id}")
    print(f"   Found {len(results)} candidates with same title in space.")

    existing_id = None
    for page in results:
        ancestors = [str(a["id"]) for a in page.get("ancestors", [])]
        print(f"   Candidate ID {page['id']} has ancestors: {ancestors}")

        if str(parent_id) in ancestors:
            existing_id = page["id"]
            break

    if existing_id:
        print(f" Reusing existing page '{title}' (ID {existing_id}) under parent {parent_id}")
        page_id = existing_id
    else:
        print(f" Creating new page '{title}' under parent {parent_id}")
        data = {
            "type": "page",
            "title": title,
            "ancestors": [{"id": parent_id}],
            "space": {"key": SPACE_KEY},
            "body": {
                "storage": {
                    "value": body_html,
                    "representation": "storage"
                }
            }
        }
        print(" Payload being sent:")
        import json
        print(json.dumps(data, indent=2)[:1000])

        r = requests.post(url, auth=auth, json=data)
        print("Response status:", r.status_code, r.text[:500])
        r.raise_for_status()
        page_id = r.json()["id"]

    #  Always store with full metadata, even if reused
    page_cache[cache_key] = {
        "id": page_id,
        "title": title,
        "html": body_html,
        "md_links": []   # default, will be updated by process_markdown
    }

    return page_id


def ensure_folder_page(folder: Path, parent_id: str) -> str:
    """Ensure a Confluence page exists for this folder and return its page_id."""
    title = folder.name.replace("-", " ").title()
    
    # Skip "images" folders (we don't want a page for them)
    if title.lower() == "images":
        return parent_id  # return parent_id, Markdown files inside will attach images

    # Cache key: folder relative path
    cache_key = str(folder.relative_to(DOCS_DIR))
    if cache_key in page_cache:
        return page_cache[cache_key]["id"]

    # Check for README.md / index.md for folder content
    readme = None
    for candidate in ["README.md", "readme.md", "index.md"]:
        cand_path = folder / candidate
        if cand_path.exists():
            readme = cand_path
            break

    # Default folder page content
    body_html = f"<h1>{title}</h1>"
    if readme:
        raw_html = md_to_confluence_html(readme)
        body_html = clean_html_for_confluence(raw_html, {})

    # Check if folder page already exists under the parent
    url = f"{BASE_URL}/rest/api/content"
    params = {"title": title, "spaceKey": SPACE_KEY, "expand": "ancestors"}
    r = requests.get(url, auth=auth, params=params)
    r.raise_for_status()
    results = r.json().get("results", [])

    existing_id = None
    for page in results:
        if any(str(a["id"]) == str(parent_id) for a in page.get("ancestors", [])):
            existing_id = page["id"]
            break

    if existing_id:
        print(f"Reusing existing folder page '{title}' under parent {parent_id} (ID {existing_id})")
        page_id = existing_id
    else:
        print(f"Creating folder page '{title}' under parent {parent_id}")
        data = {
            "type": "page",
            "title": title,
            "ancestors": [{"id": parent_id}],
            "space": {"key": SPACE_KEY},
            "body": {"storage": {"value": body_html, "representation": "storage"}}
        }
        r = requests.post(url, auth=auth, json=data)
        r.raise_for_status()
        page_id = r.json()["id"]

    # Cache page ID
    page_cache[cache_key] = {"id": page_id, "title": title}
    return page_id




def escape_angle_brackets(text: str) -> str:
    """
    Escapes angle-bracket placeholders like <Enter>, <Leertaste>, <account_identifier>
    but keeps real HTML tags (<p>, <h1>, <a>, etc.) intact.
    """
    return re.sub(
        r"<(?!/?[a-z][a-z0-9]*\b)([^>]+)>", 
        r"&lt;\1&gt;", 
        text, 
        flags=re.IGNORECASE
    )

def process_markdown(md_path: Path, parent_id: str):
    title = md_path.stem.replace("-", " ").title()
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    md_links = re.findall(r"\[([^\]]+)\]\(([^)]+)\.md\)", content)
    # Collect local image references
    img_matches = re.findall(r"!\[.*?\]\((.*?)\)", content)
    img_map = {}
    for img_path in img_matches:
        full_path = (md_path.parent / img_path).resolve()
        if full_path.exists():
            img_map[img_path] = full_path
        else:
            print(f"[WARNING] Missing image: {img_path} in {md_path}")

    # Convert MD → HTML
    raw_html = md_to_confluence_html(md_path)

    # Clean HTML for Confluence (attachments, links, etc.)
    cleaned_html = clean_html_for_confluence(raw_html, img_map)

    # Escape problematic <Placeholders> like <Enter>, <Leertaste>
    cleaned_html = escape_angle_brackets(cleaned_html)

    """
    Debug (optional):
    print("Title:", title)
    print("Parent ID:", parent_id)
    print("Body HTML preview:", cleaned_html[:200])
    """

    # Create or reuse page
    page_id = get_or_create_page(title, parent_id, cleaned_html)

    # Upload images to the Markdown page itself
    for _, full_path in img_map.items():
        upload_attachment(page_id, full_path)

    # Cache by folder-relative path to avoid collisions
    cache_key = str(md_path.relative_to(DOCS_DIR))
    page_cache[cache_key] = {
        "id": page_id,
        "html": cleaned_html,
        "md_links": md_links,
        "title": title
    }

def update_page(page_id: str, title: str, html: str, version: int = 2):
    url = f"{BASE_URL}/rest/api/content/{page_id}"
    payload = {
        "id": page_id,
        "type": "page",
        "title": title,
        "space": {"key": SPACE_KEY},
        "body": {"storage": {"value": html, "representation": "storage"}},
        "version": {"number": version}
    }
    r = requests.put(url, json=payload, auth=auth)
    r.raise_for_status()

def second_pass_fix_links():
    for cache_key, meta in page_cache.items():
        html = meta["html"]
        page_id = meta["id"]
        title = meta["title"]

        original_html = html  # keep copy for comparison

        for link_text, target_md in meta.get("md_links", []):
            target_stem = Path(target_md).stem
            # search in cache by relative path ending with target_stem
            target_page = next(
                (v for k, v in page_cache.items() if k.endswith(target_stem)),
                None
            )
            if target_page:
                confluence_link = (
                    f'<ac:link>'
                    f'<ri:page ri:content-title="{target_page["title"]}"/>'
                    f'<ac:plain-text-link-body><![CDATA[{link_text}]]></ac:plain-text-link-body>'
                    f'</ac:link>'
                )
                html = re.sub(
                    rf'\[{re.escape(link_text)}\]\(\.\/{re.escape(target_md)}\.md\)',
                    confluence_link,
                    html
                )

        #  only update if content changed
        if html != original_html:
            print(f"Updating page '{title}' with fixed links")
            update_page(page_id, title, html)
        else:
            print(f"No link changes for '{title}', skipping update")


def walk_docs():
    """Walk DOCS_DIR, create folder pages, upload Markdown files and images."""
    root_parent_id = PARENT_PAGE_ID

    # --- Step 1: Create/reuse folder pages ---
    """ for folder in sorted(DOCS_DIR.rglob("*")):
        if folder.is_dir():
            if folder.parent == DOCS_DIR:
                parent_id = root_parent_id
            else:
                parent_key = str(folder.parent.relative_to(DOCS_DIR))
                parent_id = page_cache.get(parent_key, {}).get("id", root_parent_id)
            ensure_folder_page(folder, parent_id) """
    for folder in sorted([f for f in DOCS_DIR.rglob("*") if f.is_dir()],
                        key=lambda x: len(x.relative_to(DOCS_DIR).parts)):
        if folder.name.lower() == "images":
            continue  # skip images folder

        # Determine parent page ID
        if folder.parent == DOCS_DIR:
            parent_id = PARENT_PAGE_ID
        else:
            parent_rel = str(folder.parent.relative_to(DOCS_DIR))
            parent_id = page_cache.get(parent_rel, {}).get("id")
            if not parent_id:
                raise ValueError(f"Parent page not found in cache for folder {folder}")

        ensure_folder_page(folder, parent_id)
    # --- Step 2: Upload Markdown files ---
    for md_file in DOCS_DIR.rglob("*.md"):
        # Skip README.md / index.md (already used for folder pages)
        if md_file.name.lower() in ["readme.md", "index.md"]:
            continue

        parent_key = str(md_file.parent.relative_to(DOCS_DIR))
        parent_id = page_cache.get(parent_key, {}).get("id", root_parent_id)
        process_markdown(md_file, parent_id)
   

    print("First pass upload complete. Fixing links...")
    second_pass_fix_links()

if __name__ == "__main__":
    walk_docs()
    print("Upload with links & images completed.")