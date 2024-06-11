import numpy as np
import matplotlib.pyplot as plt


# Função para calcular precisão e revocação
def calculate_precision_recall(similarities, relevant_results, threshold):
    # Definir como relevantes as imagens com similaridade acima do limiar
    predicted_relevant = [1 if sim >= threshold else 0 for sim in similarities]

    true_positives = sum([1 for pr, rr in zip(predicted_relevant, relevant_results) if pr == rr == 1])
    false_positives = sum([1 for pr, rr in zip(predicted_relevant, relevant_results) if pr == 1 and rr == 0])
    false_negatives = sum([1 for pr, rr in zip(predicted_relevant, relevant_results) if pr == 0 and rr == 1])

    precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
    recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0

    return precision, recall


# Carregar as similaridades e os resultados esperados (ajuste conforme necessário)
similarities = [0.9, 0.85, 0.8, 0.75, 0.7, 0.65, 0.6, 0.55, 0.5, 0.45]
relevant_results = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0]  # Exemplo de resultados esperados

thresholds = np.linspace(0, 1, 50)
precisions = []
recalls = []

for threshold in thresholds:
    precision, recall = calculate_precision_recall(similarities, relevant_results, threshold)
    precisions.append(precision)
    recalls.append(recall)

# Plotar o gráfico de precisão vs. revocação
plt.figure()
plt.plot(recalls, precisions, marker='.')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision vs. Recall')
plt.show()
