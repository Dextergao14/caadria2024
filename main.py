# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import text_crawler


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    url = "https://grasshopperdocs.com/addons/grasshopper-curve.html"
    text = text_crawler.get_webpage_text_without_header_footer(url)
    cleaned_content = text_crawler.clean_text(text)
    print(cleaned_content)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
