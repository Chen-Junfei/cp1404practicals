import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

def main():
    print("Welcome to the Wikipedia search tool!")

    title = input("Enter page title: ").strip()
    while title != "":
        try:
            page = wikipedia.page(title, autosuggest=False)
            print(f"\n{page.title}\n{page.summary}\n{page.url}")

        except DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options[:10],"...")

        except PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        title = input("Enter page title: ").strip()

    print("Thank you.")

main()