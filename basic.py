from bs4 import BeautifulSoup

html = """
<html>
  <body>
    <div id="content">
      <h1>Hello, BeautifulSoup!</h1>
      <p>This is a sample HTML page.</p>
      <a href="https://example.com">Visit Example</a>
    </div>
  </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

# Accessing elements
h1_tag = soup.h1
paragraph = soup.p
link = soup.a

# Searching for elements
first_div = soup.find('div')
all_paragraphs = soup.find_all('p')

# Navigation
parent_div = link.parent

# Filtering
filtered_elements = soup.find_all(lambda tag: tag.name == 'p' and 'sample' in tag.text)

# Output formatting
formatted_html = soup.prettify()

# Printing results
print("Accessing Elements:")
print("h1_tag:", h1_tag)
print("paragraph:", paragraph)
print("link:", link)

print("\nSearching for Elements:")
print("first_div:", first_div)
print("all_paragraphs:", all_paragraphs)

print("\nNavigation:")
print("parent_div:", parent_div)

print("\nFiltering:")
print("filtered_elements:", filtered_elements)

print("\nOutput Formatting:")
print(formatted_html)


