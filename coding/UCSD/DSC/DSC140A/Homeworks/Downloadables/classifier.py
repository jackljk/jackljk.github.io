import numpy as np


def extract_features(words):
    # 26 letters + 26^2 bigrams + 26^3 trigrams
    n_features = 26 + 26 ** 2 + 26 ** 3
    features = np.zeros((len(words), n_features))
    
    for i, word in enumerate(words):
        for letter in word:
            index = ord(letter.lower()) - ord('a')
            if 0 <= index < 26:
                features[i, index] += 1
                
        for j in range(len(word) - 1):
            bigram_index = 26 + (ord(word[j].lower()) - ord('a')) * 26 + (ord(word[j+1].lower()) - ord('a'))
            if 0 <= bigram_index - 26 < 26 ** 2:
                features[i, bigram_index] += 1
                
        for k in range(len(word) - 2):
            trigram_index = 26 + 26 ** 2 + (ord(word[k].lower()) - ord('a')) * 26 ** 2 + (ord(word[k+1].lower()) - ord('a')) * 26 + (ord(word[k+2].lower()) - ord('a'))
            if 0 <= trigram_index - 26 - 26 ** 2 < 26 ** 3:
                features[i, trigram_index] += 1
    
    return features


def train_naive_bayes(features, labels):
    # Determine the number of classes and initialize the prior and likelihoods
    classes = np.unique(labels)  # Unique class labels
    n_classes = len(classes)
    n_features = features.shape[1]
    
    # Initializing probabilities
    class_prior = np.zeros(n_classes)
    feature_prob = np.zeros((n_classes, n_features))
    
    for i, cls in enumerate(classes):
        # Find indices where the class label equals the current class
        cls_indices = np.where(labels == cls)[0]
        
        # Calculate class prior probabilities
        class_prior[i] = len(cls_indices) / float(len(labels))
        
        # Subset features for the current class
        cls_features = features[cls_indices, :]
        
        # Calculate the probability of each feature being 1 in the current class
        # Using Laplace smoothing with alpha = 1
        feature_prob[i, :] = (np.sum(cls_features, axis=0) + 1) / (len(cls_indices) + 2)
    
    return class_prior, feature_prob, classes


def predict_naive_bayes(model, features):
    class_prior, feature_likelihood, classes = model
    log_prob = np.log(feature_likelihood)
    # Calculate the log posterior for each class
    log_posterior = np.dot(features, log_prob.T) + np.log(class_prior)
    # Return the class with the highest posterior probability
    return classes[np.argmax(log_posterior, axis=1)]


def classify(train_words, train_labels, test_words):
    train_features = extract_features(train_words)
    test_features = extract_features(test_words)

    model = train_naive_bayes(train_features, train_labels)
    predictions = predict_naive_bayes(model, test_features)
    return predictions