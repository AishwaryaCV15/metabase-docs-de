from pathlib import PurePosixPath
import requests
from bs4 import BeautifulSoup

# -------------------
#  Config
# -------------------
BASE_URL = "https://infomedia.gipmbh.de"      # e.g. "https://your-domain.atlassian.net/wiki"
USERNAME = ""      # Confluence username/email
PASSWORD = ""     
SPACE_KEY = "1002025" #Space Key for Kidicap Anwender Doku, check it in the site link once before running
PARENT_PAGE_ID = 591561883   # optional 


auth = (USERNAME, PASSWORD)
# -------------------
#  Fetch all pages
# -------------------
def get_all_pages():
    url = f"{BASE_URL}/rest/api/content"
    params = {"spaceKey": SPACE_KEY, "expand": "body.storage", "limit": 100}
    pages = []
    while url:
        r = requests.get(url, auth=auth, params=params)
        r.raise_for_status()
        data = r.json()
        pages.extend(data.get("results", []))
        if "_links" in data and "next" in data["_links"]:
            url = BASE_URL + data["_links"]["next"]
            params = None
        else:
            break
    print(f"Retrieved {len(pages)} pages from space {SPACE_KEY}")
    return pages


# -------------------
# Build page map
# -------------------
def build_page_map(pages):
    page_map = {}
    for p in pages:
        title = p["title"]
        page_map[title.lower()] = {
            "id": p["id"],
            "title": title,
            "html": p.get("body", {}).get("storage", {}).get("value", "")
        }
    return page_map


# -------------------
# Update page content
# -------------------
def update_page(page_id: str, title: str, html: str):
    url = f"{BASE_URL}/rest/api/content/{page_id}"
    get_r = requests.get(url, auth=auth, params={"expand": "version"})
    get_r.raise_for_status()
    page = get_r.json()
    current_version = page["version"]["number"]

    payload = {
        "id": page_id,
        "type": "page",
        "title": title,
        "space": {"key": SPACE_KEY},
        "version": {"number": current_version + 1},
        "body": {"storage": {"value": html, "representation": "storage"}},
    }

    r = requests.put(url, auth=auth, json=payload)
    r.raise_for_status()
    print(f"Updated page {title} (ID {page_id})")


# -------------------
# Fix links using BeautifulSoup
# -------------------
def fix_links():
    pages = get_all_pages()
    page_map = build_page_map(pages)

    for meta in page_map.values():
        html = meta["html"]
        page_id = meta["id"]
        title = meta["title"]

        soup = BeautifulSoup(html, "html.parser")
        changed = False

        # Find all <a> tags
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if href.endswith(".md"):
                target_title = PurePosixPath(href).stem.replace("-", " ").title()
                target_page = page_map.get(target_title.lower())
                if target_page:
                    confluence_link = soup.new_tag("ac:link")
                    ri_page = soup.new_tag("ri:page", **{"ri:content-title": target_page["title"]})
                    confluence_link.append(ri_page)
                    plain_text = soup.new_tag("ac:plain-text-link-body")
                    plain_text.string = a.text
                    confluence_link.append(plain_text)
                    a.replace_with(confluence_link)
                    changed = True
                else:
                    print(f"No page found for target '{href}' in '{title}'")

        if changed:
            update_page(page_id, title, str(soup))
        else:
            print(f"No link changes needed for '{title}'")


# -------------------
# Run
# -------------------
if __name__ == "__main__":
    fix_links()
