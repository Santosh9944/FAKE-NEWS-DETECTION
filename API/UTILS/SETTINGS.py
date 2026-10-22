import os

# BASE DIRECTORY OF THE PROJECT (WORKS BOTH LOCALLY AND ON RENDER)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# PATH TO SHARED TF-IDF VECTORIZER
TFIDF_PATH = os.path.join(BASE_DIR, "MODEL", "VECTORIZER", "TFIDF_VECTORIZER.pkl")

# DICTIONARY OF MODEL NAMES (USED IN DROPDOWN) MAPPED TO THEIR RESPECTIVE FILE PATHS
MODEL_PATHS = {
    "LOGISTIC":      os.path.join(BASE_DIR, "MODEL", "MODELS", "ML", "LOGISTIC_TFIDF.pkl"),
    "LSTM":          os.path.join(BASE_DIR, "MODEL", "MODELS", "DL", "LSTM_MODEL.h5"),
    "CNN":           os.path.join(BASE_DIR, "MODEL", "MODELS", "DL", "CNN_MODEL.h5"),
    "DNN":           os.path.join(BASE_DIR, "MODEL", "MODELS", "DL", "DNN_MODEL.h5"),
    "NAIVE_BAYES":   os.path.join(BASE_DIR, "MODEL", "MODELS", "ML", "NAIVE_BAYES_TFIDF.pkl"),
    "RANDOM_FOREST": os.path.join(BASE_DIR, "MODEL", "MODELS", "ML", "RANDOM_FOREST_TFIDF.pkl"),
}
