import chainlit as cl
import dotenv

dotenv.load_dotenv()

@cl.on_message
async def on_message(message: cl.message):
    result = await Runner.run(nutrition_agent,message.content)
    await cl.Message(content= result.final_output).send()
    

