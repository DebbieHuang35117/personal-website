from typing import List
from datasets import Features, Value, Sequence, Dataset
from ragas.metrics import context_recall, faithfulness
from ragas import evaluate
import pandas as pd

def compute_context_recall_score(context: List[List[str]], ground_truth: List[str], question: List[str]) -> pd.DataFrame:
    """
    Compute context recall scores for a given dataset.
    """
    
    data_samples = { 'contexts': context, 'ground_truth': ground_truth, 'question': question}
    dataset = Dataset.from_dict(data_samples)
    score = evaluate(dataset, metrics=[context_recall])
    df_score = score.to_pandas()
    
    return df_score

def compute_faithfulness_score(context: List[List[str]], answer: List[str], question: List[str]) -> pd.DataFrame:
    """
    Compute faithfulness scores for a given dataset.
    """
    
    data_samples = { 'contexts': context, 'answer': answer, 'question': question}
    dataset = Dataset.from_dict(data_samples)
    score = evaluate(dataset, metrics=[faithfulness])
    df_score = score.to_pandas()
    
    return df_score
'''
# Example usage
data = {
    'question': ['When was the first super bowl?', 'Who won the most super bowls?'],
    'answer': ['The first superbowl was held on Jan 15, 1967', 'The most super bowls have been won by The New England Patriots'],
    'contexts': [['The First AFL–NFL World Championship Game was an American football game played on January 15, 1967, at the Los Angeles Memorial Coliseum in Los Angeles,'], 
                 ['The Green Bay Packers...Green Bay, Wisconsin.','The Packers compete...Football Conference']],
    'ground_truth': ['The first superbowl was held on January 15, 1967', 'The New England Patriots have won the Super Bowl a record six times']
}

# Call the function
df_score = compute_context_recall_score(data['contexts'], data['ground_truth'], data['question'])

# Print the results
print(df_score)

df_score = compute_context_recall_score(data['contexts'], data['ground_truth'], [''])

# Print the results
print(df_score)

# Print the results
print(df_score)
'''
