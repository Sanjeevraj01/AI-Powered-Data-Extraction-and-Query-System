import requests
from bs4 import BeautifulSoup


def extract_text_from_url(url: str) -> str:
    """
    Extract text content from a web page.

    Args:
        url (str): Website URL

    Returns:
        str: Extracted text content
    """

    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            )
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        # Remove unwanted elements
        for tag in soup([
            "script",
            "style",
            "noscript",
            "header",
            "footer",
            "nav"
        ]):
            tag.decompose()

        text = soup.get_text(
            separator=" ",
            strip=True
        )

        # Remove extra whitespace
        cleaned_text = " ".join(text.split())

        return cleaned_text

    except requests.exceptions.RequestException as e:
        raise Exception(
            f"Failed to fetch URL: {str(e)}"
        )

    except Exception as e:
        raise Exception(
            f"Error extracting text: {str(e)}"
        )