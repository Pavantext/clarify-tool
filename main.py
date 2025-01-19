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

if __name__ == "__main__":
    # Choose mode
    mode = input("Choose mode: For 'clarify' press 1 or For 'challenge' press 2: ").strip()
    
    input_text = input("Enter your text: ")
    
    if mode == "1":
        clarified_output = clarify_text(input_text)
        print("\nClarified Output:")
        print(clarified_output)
    elif mode == "2":
        challenged_output = challenge_text(input_text)
        print("\nChallenged Output:")
        print(challenged_output)
    else:
        print("Invalid mode selected. Please enter 1 for 'clarify' or 2 for 'challenge'.")