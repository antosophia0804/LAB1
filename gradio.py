interface = gr.Interface(
    fn=summarize_text,
    inputs="text",
    outputs="text",
    title="Text Summarization with BART",
    description="Summarize text using the facebook/bart-large-cnn model.",
)

# Launch the Gradio app
interface.launch()

