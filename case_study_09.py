# Case Study 34: Student Feedback Sentiment Scoring

student_feedback = input("Enter course feedback comment: ").lower()

positive_keywords = ["good", "great", "excellent", "clear", "helpful", "easy", "interesting", "nice", "well"]
negative_keywords = ["poor", "bad", "slow", "hard", "boring", "confusing", "difficult", "worst", "hate"]

positive_word_count = 0
negative_word_count = 0

for word in positive_keywords:
    if word in student_feedback:
        positive_word_count = positive_word_count + 1

for word in negative_keywords:
    if word in student_feedback:
        negative_word_count = negative_word_count + 1

net_sentiment_score = positive_word_count - negative_word_count

print("\n--- Feedback Sentiment Analysis ---")
print("Positive indicators found:", positive_word_count)
print("Negative indicators found:", negative_word_count)
print("Net sentiment score      :", net_sentiment_score)

if net_sentiment_score > 0:
    print("Classification           : POSITIVE FEEDBACK")
elif net_sentiment_score < 0:
    print("Classification           : NEGATIVE FEEDBACK")
else:
    print("Classification           : NEUTRAL FEEDBACK")
