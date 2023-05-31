# Step 1: Load the data, and inspect it
import pandas as pd

df = pd.read_csv('fake_or_real_news.csv')
print(df.head())

# Step 2: Split the data into 70% training and 30% testing data
from sklearn.model_selection import train_test_split

X = df['text']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 3: Compute the bag-of-words on the training data
from sklearn.feature_extraction.text import CountVectorizer

count_vectorizer = CountVectorizer(stop_words='english')
count_train = count_vectorizer.fit_transform(X_train.values)

# Step 4: Use the same vocabular in the training data to compute the bag-of-words of the text in testing data
count_test = count_vectorizer.transform(X_test.values)

# Step 5: Train a Naive Bayes classifier on the training data
from sklearn.naive_bayes import MultinomialNB

nb_classifier = MultinomialNB()
nb_classifier.fit(count_train, y_train)

# Step 6: Test the accuracy of the fitted model and confusion matrix on the testing data
from sklearn.metrics import accuracy_score, confusion_matrix

y_pred = nb_classifier.predict(count_test)
accuracy = accuracy_score(y_test, y_pred)
confusion_mat = confusion_matrix(y_test, y_pred, labels=['FAKE', 'REAL'])

print('Accuracy:', accuracy)
print('Confusion Matrix:', confusion_mat)