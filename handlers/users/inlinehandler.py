
from aiogram import Bot, Dispatcher, types
from aiogram.utils import markdown
from loader import dp
from utils.memegen import memegen


@dp.inline_handler()
async def inline_query(query: types.InlineQuery):
    # Get the user's query
    search_term = query.query
    meme = memegen()
    # Generate a list of joke results based on the search term
    results = [
        types.InlineQueryResultArticle(
            id = str(meme['type']),
            title = str("this is random Joke"),
            hide_url=True,
            description = f"{meme['setup']} \n-{meme['punchline']}",
            input_message_content=types.InputTextMessageContent(
                message_text=f"{meme['setup']} \n-{meme['punchline']}"
            )
            
        )
    ]