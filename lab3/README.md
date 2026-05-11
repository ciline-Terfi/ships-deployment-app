

Resource scrapped : the website :Books to Scrape We love being scraped!
url = "https://books.toscrape.com/"

his lab demonstrates how to turn "messy" internet text into "clean" numbers that an AI can understand. It follows a three-stage process.

-> Stage 1: The Scraper (Data Collection)

Websites are built for humans to read, not machines. Our script acts like an automated eye.

    The Goal: Visit a website and find specific "containers" (HTML tags) that hold product names and prices.

    The Tool: BeautifulSoup. It "parses" the website's code so we can pull out exactly what we need without the extra advertisements or menus.

-> Stage 2: The Cleaner (Regex)

When we scrape a price, it usually looks like text: "£52.35". A computer cannot calculate the average of a string that contains a "£" symbol.

    The Goal: Strip away everything that isn't a digit or a decimal point.

    The Tool: Regex (Regular Expressions). We use the pattern [^\d.] to find and delete anything that isn't a number.

    The Result: We turn the text "£52.35" into the number 52.35.

-> Stage 3: The Processor (AI-Readying)

Even with clean numbers, AI models have a hard time if the data isn't "balanced."

    Scaling: If one column is "Price" (up to 100) and another is "Rating" (up to 5), the AI might think the Price is 20x more important just because the numbers are bigger. We Scale them so they all live on the same small range (usually -1 to 1).

    Encoding: AI cannot understand "In Stock" vs. "Out of Stock." We Encode these into 1 and 0.
