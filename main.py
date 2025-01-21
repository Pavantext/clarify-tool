from together import Together
import os

# Initialize Together AI client
api_key = os.getenv('TOGETHER_API_KEY') or "b83a813f6cbd23ab0095ee507943399a1f751256f12118976cdef8b4ceee9163"
client = Together(api_key=api_key)

def clarify_text(input_text: str, audience_level: str = "beginner") -> str:
    """
    Simplifies and explains content based on audience level.
    """
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3",
        messages=[
            {"role": "system", "content": f"""You are an educational assistant focused on making complex topics accessible for {audience_level} level learners.
            
            Format your response in the following structure:
            1. Simplified Explanation
               - Break down complex concepts
               - Use clear language
            
            2. Key Definitions
               - Define important terms
               - Use simple analogies
            
            3. Examples
               - Provide real-world examples
               - Include practical applications
            
            4. Visual Analogies
               - Use metaphors
               - Create mental images"""},
            {"role": "user", "content": input_text}
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content

def challenge_text(input_text: str, audience_level: str = "advanced") -> str:
    """
    Generates advanced analysis and critical thinking prompts.
    """
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3",
        messages=[
            {"role": "system", "content": f"""You are an advanced educational assistant creating content for {audience_level} level learners.
            
            Structure your response as follows:
            1. Critical Reflection Questions
               - Thought-provoking questions
               - Analysis prompts
            
            2. Advanced Concepts
               - Related theories
               - Complex connections
            
            3. Interdisciplinary Links
               - Connections to other fields
               - Cross-domain applications
            
            4. Counterarguments
               - Alternative perspectives
               - Potential criticisms
            
            5. Future Implications
               - Long-term impacts
               - Future challenges"""},
            {"role": "user", "content": input_text}
        ],
        temperature=0.9,
    )
    return response.choices[0].message.content

def devils_advocate(input_text: str) -> str:
    """
    Analyzes text and provides critical perspectives, challenges assumptions,
    and encourages evidence-based thinking.
    """
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3",
        messages=[
            {"role": "system", "content": """You are a Devil's Advocate assistant that helps educators explore alternative perspectives and challenge their views constructively.

            Structure your response as follows:
            1. Main Points & Assumptions Identified
               - Key arguments
               - Supporting points
               - Implicit assumptions

            2. Alternative Perspectives & Challenges
               - Different viewpoints
               - Potential counterarguments
               - Areas needing more exploration

            3. Evidence-Based Analysis
               - Suggestions for supporting evidence
               - Areas requiring additional data
               - Research questions to consider

            4. Bias Assessment
               - Potential cognitive biases
               - Perspective limitations
               - Bias reduction suggestions

            5. Adaptability Suggestions
               - Ways to refine arguments
               - Alternative approaches
               - Implementation considerations"""},
            {"role": "user", "content": input_text}
        ],
        temperature=0.8,
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    # Choose mode
    mode = input("Choose mode (1: clarify, 2: challenge, 3: devil's advocate): ").strip()
    
    input_text = input("Enter your text: ")
    
    if mode == "1":
        clarified_output = clarify_text(input_text)
        print("\nClarified Output:")
        print(clarified_output)
    elif mode == "2":
        challenged_output = challenge_text(input_text)
        print("\nChallenged Output:")
        print(challenged_output)
    elif mode == "3":
        devils_advocate_output = devils_advocate(input_text)
        print("\nDevil's Advocate Analysis:")
        print(devils_advocate_output)
    else:
        print("Invalid mode selected. Please enter 1 for 'clarify', 2 for 'challenge', or 3 for 'devil's advocate'.")