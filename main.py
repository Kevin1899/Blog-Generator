import streamlit as st
import openai

# (Replace with your actual OpenAI API key)
openai.api_key = "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"

def cute_messages(query):
    """Generates a blog post using OpenAI's GPT-3.5-turbo model,
    formatted in Markdown.

    Args:
        query (str): The topic for the blog post.

    Returns:
        str: The generated blog post in Markdown format.
    """

    system_msg = "You are a blogger."
    user_msg = "Write a blog for {}".format(query)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.7,
        messages=[{"role": "system", "content": system_msg}, {"role": "user", "content": user_msg}],
        max_tokens=1000,
        n=1,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    if "choices" in response and response["choices"] and "message" in response["choices"][0] and "content" in response["choices"][0]["message"]:
        return f"# Blog: {query}\n\n{response['choices'][0]['message']['content']}"  # Wrap in Markdown
    else:
        return "An error occurred while generating the blog post. Please try again later."

def main():
    st.title("Blog Post Generator with OpenAI")

    # Input field for the blog post topic
    query = st.text_input("Enter a topic for your blog post:")

    # Button to trigger the generation of the blog post
    if st.button("Generate Blog Post"):
        if query:
            blog_post = cute_messages(query)
            st.markdown(blog_post)
        else:
            st.error("Please enter a topic for your blog post.")

    # Safety instructions
    st.markdown(
        """**Important Safety Instructions:**

        * This tool uses OpenAI's GPT-3.5-turbo model, which can generate harmful or misleading content.
        * Always review the generated content carefully before using it.
        * Do not use this tool to generate content that promotes hate speech, violence, or other harmful activities.
        * Be aware of the potential biases and limitations of this model.
        * Use this tool responsibly and ethically.
        """
    )

if __name__ == "__main__":
    main()
