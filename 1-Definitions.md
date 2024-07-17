# 1. Definitions
## Zero-shot Prompting
This technique involves giving an AI model a task or query without any prior examples or context related to that specific task. The model relies solely on its pre-trained knowledge and general understanding to generate a response. This approach tests the model's ability to generalize from its training data to new, unseen tasks.

## Few-shot Prompting
In few-shot prompting, the AI model is provided with a small number of examples related to the task at hand. These examples serve as a guide, helping the model understand the desired output format and context. This method leverages the model’s ability to learn from minimal data to perform new tasks more accurately than zero-shot prompting.

## Chain-of-Thought (CoT) Prompting
This method involves encouraging the model to articulate its reasoning process step-by-step before arriving at a final answer. By generating intermediate reasoning steps, the model can better handle complex tasks that require logical thinking, multi-step problem solving, and detailed explanations, leading to more accurate and coherent responses.

## Self-Consistency
Self-consistency in AI models refers to generating multiple independent reasoning paths or solutions for a given problem and then selecting the most consistent answer from these paths. This approach helps in enhancing the reliability and accuracy of the model’s responses by cross-verifying different reasoning processes.

## Generate Knowledge Prompting
This strategy prompts the model to first produce relevant background knowledge or contextual information related to a query before attempting to answer it directly. By generating and leveraging this additional knowledge, the model can provide more informed and accurate responses, especially for complex or specialized queries.

## Prompt Chaining
Prompt chaining involves decomposing a complex task into a series of simpler, sequential tasks. Each step's output serves as the input for the next step in the chain. This structured approach helps the model handle intricate tasks more effectively by focusing on manageable subtasks, thereby improving the overall quality and coherence of the final output.

## Tree of Thoughts
This strategy involves exploring multiple reasoning paths or solutions in parallel, similar to branching out like a tree. Each branch represents a different line of thought or solution pathway. By evaluating and comparing these branches, the model can select the most promising or accurate path, enhancing decision-making and problem-solving capabilities.

## Retrieval Augmented Generation
This technique combines the generative capabilities of the model with information retrieved from external sources, such as databases or documents. By integrating relevant, up-to-date information with the model’s responses, retrieval augmented generation enhances the accuracy, relevance, and richness of the generated content, particularly for knowledge-intensive tasks.

## Directional Stimulus Prompting
In this approach, the prompt includes directional hints or cues that guide the model’s response in a specific direction. These stimuli can be explicit instructions, keywords, or contextual hints that influence the model’s output, helping to steer it towards a desired response or focus on particular aspects of the query.

## ReAct Prompting
ReAct prompting involves a dynamic interaction between reasoning and acting phases. The model alternates between thinking (reasoning about the problem) and taking actions (generating responses or performing tasks). This iterative process allows the model to refine its approach based on intermediate feedback, improving the effectiveness and adaptability of its solutions.

## Multimodal CoT Prompting
This method extends chain-of-thought prompting to tasks involving multiple types of data, such as text, images, and audio. By applying step-by-step reasoning across different modalities, the model can better integrate and process diverse information sources, leading to more comprehensive and accurate responses in multimodal tasks.