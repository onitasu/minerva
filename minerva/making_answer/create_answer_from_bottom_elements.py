import openai
from minerva.making_answer.task_tree_element import TaskTreeElement


def create_answer_from_bottom_elements(openai_api_key: str, goal: str, tree_element_list: list[TaskTreeElement],
                                       processed_task_number: int):
    openai.api_key = openai_api_key

    # 保留
    system_input = ''''''
    assistant_prompt = ''''''
    user_prompt = ''''''

    messages = [
        {"role": "system", "content": system_input},
        {"role": "assistant", "content": assistant_prompt},
        {"role": "user", "content": user_prompt}
    ]

    response = openai.ChatCompletion.create(
        temperature=1,
        max_tokens=1000,
        model="gpt-3.5-turbo",
        messages=messages
    )

    ai_response = response['choices'][0]['message']['content']

    tree_element_list[processed_task_number].answer = ai_response
