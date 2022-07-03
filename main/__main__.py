from main import app
import pyrogram
from pyrogram import filters, idle
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from main.logo import generate_logo

START = """
**🔮 Hello There, You Can Use Me To Create Awesome Logos...**

➤ Click /help Or The Button Below To Know How To Use Me
➤ Developer - [(c) Ankit](https://xnkit.github.io/k)
"""

HELP = """
**🖼 How To Use Me ?**

**To Make Logo -** `/logo` Your Name
**To Make Square Logo - ** `/logosq` Your Name

**♻️ Example:** 
`/logo XnKiT `
`/logosq XnKiT`
"""

# Commands
@app.on_message(filters.command("start"))
async def start(bot, message):
  await message.",caption=START,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Help", callback_data="help_menu"), InlineKeyboardButton(text="мαℓιтнα мιнιяαηgα 🇱🇰", url="https://t.me/Malitha_Mihiranga"),InlineKeyboardButton(text="</ᴇᴘɪᴄ ʙᴏᴛs <s/ʟ>🇱🇰", url="https://t.me/EpicBotsSl")]]))

@app.on_message(filters.command("help"))
async def help(bot, message):
  await message.reply_photo("https://te.legra.ph/file/a13b6c99ebcd96c88fdd6.jpg",caption=HELP,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Back", callback_data="start_menu")]]))

@app.on_message(filters.command("logo") & filters.incoming & filters.text & ~filters.forwarded & (
  filters.group | filters.private))https://te.legra.ph/file/a13b6c99ebcd96c88fdd6.jpg
async def logo(bot, message):
  try:
    text = message.text.replace("logo","").replace("/","").replace("@XnKiTKuMaR","").strip().upper()
    
    if text == "":
      return await message.reply_text(HELP)

    x = await message.reply_text("`🔍 Generating Logo For You...`")  
    logo = await generate_logo(text)

    if "telegra.ph" not in logo:
      return await x.edit("`❌ Something Went Wrong...`\n\nReport This Error To @XnKiTKuMaR")
      
    if "error" in logo:
      return await x.edit(f"`❌ Something Went Wrong...`\n\nReport This Error To @XnKiTKuMaR \n\n`{logo}`")
      
    await x.edit("`🔄 Done Generated... Now Sending You`")

    logo_id = logo.replace("https://telegra.ph//file/","").replace(".jpg","").strip()
    await message.reply_photo(logo,caption="**🖼 Logo Generated By @XnKiTKuMaR**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Upload As File 📁", callback_data=f"flogo {logo_id}")]]))
    await x.delete()
  except FloodWait:
    pass
  except Exception as e:
    try:
      await x.delete()
    except:
      pass
    return await message.reply_text("`❌ Something Went Wrong...`\n\nReport This Error To @XnKiTKuMaR")

# Square Logo
@app.on_message(filters.command("logosq") & filters.incoming & filters.text & ~filters.forwarded & (
  filters.group | filters.private))
async def logo(bot, message):
  try:
    text = message.text.replace("logosq","").replace("/","").replace("@XnKiTKuMaR","").strip().upper()
      
    if text == "":
      return await message.reply_text(HELP)
  
    x = await message.reply_text("`🔍 Generating Logo For You...`")  
    logo = await generate_logo(text,True)
  
    if "telegra.ph" not in logo:
      return await x.edit("`❌ Something Went Wrong...`\n\nReport This Error To @XnKiTKuMaR")
        
    if "error" in logo:
      return await x.edit(f"`❌ Something Went Wrong...`\n\nReport This Error To @XnKiTKuMaR \n\n`{logo}`")
      
    await x.edit("`🔄 Done Generated... Now Sending You`")
    
    logo_id = logo.replace("https://telegra.ph//file/","").replace(".jpg","").strip()
    
    await message.reply_photo(logo,caption="**🖼 Logo Generated By @XnKiTKuMaR**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Upload As File 📁", callback_data=f"flogo {logo_id}")]]))
    await x.delete()
  except FloodWait:
    pass
  except Exception as e:
    try:
      await x.delete()
    except:
      pass
    return await message.reply_text("`❌ Something Went Wrong...`\n\nReport This Error To @XnKiTKuMaR")

# Callbacks
@app.on_callback_query(filters.regex("start_menu"))
async def start_menu(_,query):
  await query.answer()
  await query.message.edit(START,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Help", callback_data="help_menu"),InlineKeyboardButton(text="(c)XnKiT", url="https://xnkit.github.io/k"),InlineKeyboardButton(text="</ᴇᴘɪᴄ ʙᴏᴛs <s/ʟ>🇱🇰", url="https://t.me/EpicBotsSl")]]))

@app.on_callback_query(filters.regex("help_menu"))
async def help_menu(_,query):
  await query.answer()
  await query.message.edit(HELP,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Back", callback_data="start_menu")]]))

@app.on_callback_query(filters.regex("flogo"))
async def logo_doc(_,query):
  await query.answer()
  try:
    x = await query.message.reply_text("`🔄 Sending You The Logo As File`")
    await query.message.edit_reply_markup(reply_markup=None)
    link = "https://telegra.ph//file/" + query.data.replace("flogo","").strip() + ".jpg"
    await query.message.reply_document(link,caption="**🖼 Logo Generated By @XnKiTKuMaR**")
  except FloodWait:
    pass
  except Exception as e:
    try:
      return await x.edit(f"`❌ Something Went Wrong...`\n\nReport This Error To @XnKiTKuMaR \n\n`{str(e)}`")
    except:
      return
    
  return await x.delete()
  

if __name__ == "__main__":
  print("==================================")
  print("[INFO]: LOGO BOT STARTED SUCCESSFULLY")
  print("==========By ~(c) XnKiT=========")

  idle()
  print("[INFO]: LOGO MAKER BOT STOPPED")
