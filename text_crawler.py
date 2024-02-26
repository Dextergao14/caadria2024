import requests
from bs4 import BeautifulSoup


def get_webpage_text_without_header_footer(url):
    # obtaining page content
    response = requests.get(url)
    response.raise_for_status()

    # parsing content via beautifulsoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # locate and remove header
    header = soup.find('div', {'id': 'header'})
    if header:
        header.extract()

    # locate and remove footer
    footer = soup.find('div', {'id': 'footer'})
    if footer:
        footer.extract()

    # getting all content from the webpage
    return soup.get_text()


def clean_text(text):
    # remove empty lines
    lines = text.splitlines()
    cleaned_lines = [line.strip() for line in lines if line.strip()]

    # remove redundant info from header and footer
    start_idx = next((i for i, line in enumerate(cleaned_lines) if "Grasshopper Curve" in line), 0)
    end_idx = next((i for i, line in enumerate(cleaned_lines) if "Terms of Service" in line), len(cleaned_lines))

    cleaned_lines = cleaned_lines[start_idx:end_idx + 1]
    return "\n".join(cleaned_lines)


def extract_key_value_from_line(line):
    idx = line.find(')')
    if idx == -1:
        return None, None
    key = line[:idx + 1].strip()
    value = line[idx + 1:].strip()
    return key, value


def create_hashmap_from_text(text):
    lines = text.splitlines()
    hashmap = {}
    for line in lines:
        key, value = extract_key_value_from_line(line)
        if key and value:
            hashmap[key] = value

    return hashmap


def hashmap_to_txt(hashmap):
    st_idx = url.rfind('-', 0, -5) + 1
    with open(f'hashmap_text_{url[st_idx: -5]}.txt', 'w', encoding='utf-8') as file:
        for key, value in hashmap.items():
            file.write(f"{key} : {value}\n")


def write_to_file(text):
    st_idx = url.rfind('-', 0, -5) + 1
    with open(f'text_{url[st_idx: -5]}.txt', 'w', encoding='utf-8') as file:
        file.write(text)


if __name__ == "__main__":
    url = "https://grasshopperdocs.com/addons/grasshopper-transform.html"
    text = get_webpage_text_without_header_footer(url)
    cleaned_content = clean_text(text)
    write_to_file(cleaned_content)
    hashmap_to_txt(create_hashmap_from_text(cleaned_content))

    print(cleaned_content)
