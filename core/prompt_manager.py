def create_prompt(question, context):
    return f"Вот выдержка из учебного материала:\n\n{context}\n\nОтветь на вопрос: {question}"