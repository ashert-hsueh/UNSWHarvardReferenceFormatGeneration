import bibtexparser
from pylatexenc.latex2text import LatexNodes2Text


def parse_bibtex_from_text(bib_text: str):
    """
    receive BibTeX text and return the parsed entries
    """
    try:
        bib_database = bibtexparser.loads(bib_text)
        return bib_database.entries
    except Exception as e:
        print("Error:", e)
        return []


def latex_to_text(s: str) -> str:
    return LatexNodes2Text().latex_to_text(s)


def convert_to_harvard(entries):
    """
    receive the parsed entries and return the Harvard reference format text
    """
    harvard_text = ""
    print(entries)
    # author
    entry = entries[0]
    if "author" in entry:
        authors_clean = latex_to_text(entry["author"])
        for author in authors_clean.split(","):
            author_name = author.replace(" and", "").strip()
            author_name = author_name.strip().split(" ")
            result = ""
            if len(author_name) > 1:
                for i in range(len(author_name) - 1):
                    result += author_name[i][0].upper()
                harvard_text += result + ", "
            harvard_text += author_name[-1] + ", "
    # year
    harvard_text = harvard_text.strip(", ")
    harvard_text += f" {entry['year']}, "

    # title italic
    harvard_text += f"*{latex_to_text(entry['title'])}*, "

    # journal
    if "journal" in entry:
        harvard_text += f"{latex_to_text(entry['journal'])}, "

    if "volume" in entry:
        harvard_text += f"vol. {latex_to_text(entry['volume'])}, "
        if "number" in entry:
            harvard_text += f"no. {latex_to_text(entry['number'])}, "
            if "pages" in entry:
                harvard_text += f"pp. {latex_to_text(entry['pages'])}, "
    # DOI
    # URL
    # access time
    return harvard_text
