# Task 1: Keyword Highlighter

# Write a program that searches through reviews list and looks for keywords such as 
# "good", "excellent", "bad", "poor", and "average". We want you to capitalize those
# keywords then print out each review. Print out each review with the keywords in 
# uppercase so they stand out.

# So for the first string in the reviews list, we want it to say: 
# "This product is really GOOD. I'm impressed with its quality."

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

keywords = ["good", "excellent", "bad", "Poor", "average"]

def product_review():
    for review in reviews:
        for key in keywords:
            review = review.replace(key.lower(), key.upper())
        print(review)
            

product_review()

#Task 2: Sentiment Tally

# Develop a function that tallies the number of positive and negative words in each 
# review.  The function should return the total count of positive and negative words.

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

count_p = 0
count_n = 0

for review in reviews:
    for word in review.split():
        word = word.replace(".", "").lower()
        if word in positive_words:
            count_p += 1
        elif word in negative_words:
            count_n += 1
print(f"""
The total count of positive words in reviews is {count_p} and the total count of negative words in reviews is {count_n}.""")

# Task 3: Review Summary

# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the 
# summary does not cut off in the middle of a word.

# Example: "This product is really good. I'm...",


def summarize_review(review):
    trimmed_review = review[:30]
    last_space = trimmed_review.rfind(' ')
    if last_space != -1:
        summary = trimmed_review[:last_space] + "…"
    else:
        summary = trimmed_review + "…"
    return summary

summaries = [summarize_review(review) for review in reviews]

print(summaries)

