'''
ÂŠī¸ 2021. Contact(Telegram): @hellodarklord
'''
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def languages():
	markup = InlineKeyboardMarkup()

	btn = InlineKeyboardButton("đēđŋ Uzbek", callback_data="uz")
	markup.add(btn)

	markup.row_width = 2
	markup.add(InlineKeyboardButton("đŦđ§ English", callback_data="en"),
	InlineKeyboardButton("đˇđē Russian", callback_data="ru"),
	InlineKeyboardButton("đĢđˇ French", callback_data="fr"),
	InlineKeyboardButton("đŠđĒ German", callback_data="de"),
	InlineKeyboardButton("đ¸đĻ Arabic", callback_data="ar"),
	InlineKeyboardButton("đŽđŗ Hindi", callback_data="hi")),
        InlinekeyboardButton("đŽđŗ Bengali", callback_data="be")),
	InlinekeyboardButton("đŽđŗ English", callback_data="en")),

        return markup

def settings():
	markup = InlineKeyboardMarkup()

	btn2 = InlineKeyboardButton("âī¸ Change language", callback_data='settings')
	markup.add(btn2)

	return markup

def result():
	markup = InlineKeyboardMarkup()

	btn1 = InlineKeyboardButton("đ§ Pronunciation", callback_data='pronunciation')
	btn2 = InlineKeyboardButton("âī¸ Settings", callback_data='settings')
	btn = InlineKeyboardButton(" â ", callback_data='delete')
	markup.add(btn1, btn2)
	markup.add(btn)

	return markup

def delete():
	markup = InlineKeyboardMarkup()

	btn = InlineKeyboardButton(" â ", callback_data='delete')
	markup.add(btn)

	return markup

def repo():
	markup = InlineKeyboardMarkup()

	btn = InlineKeyboardButton(" Github Repo ", url='https://github.com/coder2077/iTranslator-bot')
	btn1 = InlineKeyboardButton(" â ", callback_data='delete')
	markup.add(btn)
	markup.add(btn1)

	return markup


'''
ÂŠī¸ 2021. Contact(Telegram): @hellodarklord
'''

